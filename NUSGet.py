# "NUSGet.py", licensed under the MIT license
# Copyright 2024-2025 NinjaCheetah and Contributors

# Nuitka options. These determine compilation settings based on the current OS.
# nuitka-project-if: {OS} == "Darwin":
#    nuitka-project: --standalone
#    nuitka-project: --macos-create-app-bundle
#    nuitka-project: --macos-app-icon={MAIN_DIRECTORY}/resources/icon.png
# nuitka-project-if: {OS} == "Windows":
#    nuitka-project: --onefile
#    nuitka-project: --windows-icon-from-ico={MAIN_DIRECTORY}/resources/icon.png
#    nuitka-project: --windows-console-mode=disable
# nuitka-project-if: {OS} in ("Linux", "FreeBSD", "OpenBSD"):
#    nuitka-project: --onefile

# These are standard options that are needed on all platforms.
# nuitka-project: --plugin-enable=pyside6
# nuitka-project: --include-data-dir={MAIN_DIRECTORY}/data=data
# nuitka-project: --include-data-dir={MAIN_DIRECTORY}/resources=resources

import sys
import webbrowser
from importlib.metadata import version

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QListView
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Signal, QObject, QLibraryInfo, QTranslator, QLocale

from qt.py.ui_AboutDialog import AboutNUSGet
from qt.py.ui_MainMenu import Ui_MainWindow

from modules.core import *
from modules.tree import NUSGetTreeModel, TIDFilterProxyModel
from modules.download_batch import run_nus_download_batch
from modules.download_wii import run_nus_download_wii
from modules.download_dsi import run_nus_download_dsi

nusget_version = "1.4.0"

regions = {"World": ["41"], "USA/NTSC": ["45"], "Europe/PAL": ["50"], "Japan": ["4A"], "Korea": ["4B"], "China": ["43"],
           "Australia/NZ": ["55"]}


# Signals needed for the worker used for threading the downloads.
class WorkerSignals(QObject):
    result = Signal(object)
    progress = Signal(str)


# Worker class used to thread the downloads.
class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        # All possible errors *should* be caught by the code and will safely return specific error codes. In the
        # unlikely event that an unexpected error happens, it can only possibly be a ValueError, so handle that and
        # return code 1.
        try:
            result = self.fn(*self.args, **self.kwargs)
        except ValueError:
            self.signals.result.emit(1)
        else:
            self.signals.result.emit(result)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()
        self.ui.download_btn.clicked.connect(self.download_btn_pressed)
        self.ui.script_btn.clicked.connect(self.script_btn_pressed)
        self.ui.custom_out_dir_btn.clicked.connect(self.choose_output_dir)
        # About and About Qt Buttons
        self.ui.actionAbout.triggered.connect(self.about_nusget)
        self.ui.actionAbout_Qt.triggered.connect(lambda: QMessageBox.aboutQt(self))
        self.ui.pack_archive_checkbox.toggled.connect(
            lambda: connect_is_enabled_to_checkbox([self.ui.archive_file_entry], self.ui.pack_archive_checkbox))
        self.ui.custom_out_dir_checkbox.toggled.connect(
            lambda: connect_is_enabled_to_checkbox([self.ui.custom_out_dir_entry, self.ui.custom_out_dir_btn],
                                                   self.ui.custom_out_dir_checkbox))
        # Load auto-update settings, and initialize them if they don't exist.
        try:
            self.ui.auto_update_checkbox.setChecked(config_data["auto_update"])
        except KeyError:
            update_setting(config_data, "auto_update", self.ui.auto_update_checkbox.isChecked())
        self.ui.auto_update_checkbox.toggled.connect(
            lambda: update_setting(config_data, "auto_update", self.ui.auto_update_checkbox.isChecked()))
        # Load custom output directory if one is saved and it is valid. Only enable the checkbox to actually use the
        # custom dir if "use_out_path" is set to true.
        try:
            out_dir = pathlib.Path(config_data["out_path"])
            if out_dir.exists() and out_dir.is_dir():
                self.ui.custom_out_dir_entry.setText(str(out_dir))
                if config_data["use_out_path"]:
                    self.ui.custom_out_dir_checkbox.setChecked(True)
        except KeyError:
            pass
        # Register this callback after the previous check to avoid an extra config write.
        self.ui.custom_out_dir_checkbox.toggled.connect(
            lambda: update_setting(config_data, "use_out_path", self.ui.custom_out_dir_checkbox.isChecked()))
        self.ui.tid_entry.textChanged.connect(self.tid_updated)
        self.ui.custom_out_dir_entry.textChanged.connect(self.custom_output_dir_changed)
        # Basic intro text set to automatically show when the app loads. This may be changed in the future.
        self.log_text = app.translate("MainWindow", "Select a title from the list on the left, or enter a "
                              "Title ID to begin.\n\nTitles marked with a checkmark are free and have a ticket "
                              "available, and can be decrypted and/or packed into a WAD or TAD. Titles with an X do not"
                              " have a ticket, and only their encrypted contents can be saved.\n\nBy default, titles "
                              "will be downloaded to a folder named \"NUSGet Downloads\" inside your downloads folder.")
        self.ui.log_text_browser.setText(self.log_text)
        # Add console entries to dropdown and attach on change signal.
        self.ui.console_select_dropdown.addItems(["Wii", "vWii", "DSi"])
        list_view = QListView()
        list_view.setMouseTracking(True)
        self.ui.console_select_dropdown.setView(list_view)
        dropdown_delegate = ComboBoxItemDelegate()
        self.ui.console_select_dropdown.setItemDelegate(dropdown_delegate)
        self.ui.console_select_dropdown.currentIndexChanged.connect(self.selected_console_changed)
        # Fix the annoying background on the help menu items.
        self.ui.menuHelp.setWindowFlags(self.ui.menuHelp.windowFlags() | Qt.FramelessWindowHint)
        self.ui.menuHelp.setWindowFlags(self.ui.menuHelp.windowFlags() | Qt.NoDropShadowWindowHint)
        self.ui.menuHelp.setAttribute(Qt.WA_TranslucentBackground)
        # Title tree loading code. Now powered by Models:tm:
        wii_model = NUSGetTreeModel(wii_database, root_name="Wii Titles")
        vwii_model = NUSGetTreeModel(vwii_database, root_name="vWii Titles")
        dsi_model = NUSGetTreeModel(dsi_database, root_name="DSi Titles")
        self.tree_models = [wii_model, vwii_model, dsi_model]
        self.trees = [self.ui.wii_title_tree, self.ui.vwii_title_tree, self.ui.dsi_title_tree]
        # Build proxy models required for searching
        self.proxy_models = [TIDFilterProxyModel(self.ui.wii_title_tree), TIDFilterProxyModel(self.ui.vwii_title_tree),
                             TIDFilterProxyModel(self.ui.dsi_title_tree)]
        for model in range(len(self.proxy_models)):
            self.proxy_models[model].setSourceModel(self.tree_models[model])
            self.proxy_models[model].setFilterKeyColumn(0)
        self.ui.tree_filter_input.textChanged.connect(lambda: self.filter_text_updated(self.ui.platform_tabs.currentIndex()))
        self.ui.tree_filter_reset_btn.clicked.connect(lambda: self.ui.tree_filter_input.setText(""))
        for tree in range(len(self.trees)):
            self.trees[tree].setModel(self.proxy_models[tree])
            self.trees[tree].doubleClicked.connect(self.title_double_clicked)
            self.trees[tree].expanded.connect(lambda: self.resize_tree(self.ui.platform_tabs.currentIndex()))
            self.trees[tree].collapsed.connect(lambda: self.resize_tree(self.ui.platform_tabs.currentIndex()))
            # This stylesheet patch allows me to add the correct padding above the scrollbar so that it doesn't overlap
            # the QTreeView's header.
            self.trees[tree].setStyleSheet(self.trees[tree].styleSheet() + f"""
                QTreeView QScrollBar::sub-line:vertical {{
                    border: 0;
                    background: #2b2b2b;
                    height: {self.trees[tree].header().sizeHint().height()}px;
                }}""")
        # Prevent resizing.
        self.setFixedSize(self.size())
        # These connections allow for clicking the checkbox labels to toggle the checkboxes, if they're enabled. This is
        # required because checkboxes can't word wrap, so regular labels must be used in their place.
        self.ui.pack_archive_checkbox.label.setText(app.translate("MainWindow", "Pack installable archive (WAD/TAD)"))
        self.ui.pack_archive_checkbox.setChecked(True)
        self.ui.keep_enc_checkbox.label.setText(app.translate("MainWindow", "Keep encrypted contents"))
        self.ui.keep_enc_checkbox.setChecked(True)
        self.ui.create_dec_checkbox.label.setText(app.translate("MainWindow", "Create decrypted contents (*.app)"))
        self.ui.use_local_checkbox.label.setText(app.translate("MainWindow", "Use local files, if they exist"))
        self.ui.use_wiiu_nus_checkbox.label.setText(app.translate("MainWindow", "Use the Wii U NUS (faster, only affects Wii/vWii)"))
        self.ui.use_wiiu_nus_checkbox.setChecked(True)
        self.ui.patch_ios_checkbox.label.setText(app.translate("MainWindow", "Apply patches to IOS (Applies to WADs only)"))
        self.ui.pack_vwii_mode_checkbox.label.setText(app.translate("MainWindow", "Re-encrypt title using the Wii Common Key"))
        self.ui.auto_update_checkbox.label.setText(app.translate("MainWindow", "Check for updates on startup"))
        self.ui.custom_out_dir_checkbox.label.setText(app.translate("MainWindow", "Use a custom download directory"))
        try:
            auto_update = config_data["auto_update"]
        except KeyError:
            auto_update = True
            config_data["auto_update"] = True
            save_config(config_data)
        if auto_update:
            # Do a quick check to see if there's a newer release available if auto-updates are enabled.
            worker = Worker(check_nusget_updates, app, nusget_version)
            worker.signals.result.connect(self.prompt_for_update)
            worker.signals.progress.connect(self.update_log_text)
            self.threadpool.start(worker)

    def title_double_clicked(self, index):
        if self.ui.download_btn.isEnabled() is True:
            # Need to map the proxy index to the source index because we're using a proxy model for searching. If we
            # don't, this for some reason isn't handled by PySide and causes a segfault.
            source_index = self.proxy_models[self.ui.platform_tabs.currentIndex()].mapToSource(index)
            title = source_index.internalPointer().metadata
            if title is not None:
                self.ui.console_select_dropdown.setCurrentIndex(self.ui.platform_tabs.currentIndex())
                selected_title = TitleData(title.tid, title.name, title.version, title.ticket,
                                           title.region, title.category, title.danger)
                self.load_title_data(selected_title)

    def filter_text_updated(self, target: int):
        text = self.ui.tree_filter_input.text()
        if text != "":
            self.trees[target].expandToDepth(0)
        else:
            self.trees[target].collapseAll()
        self.proxy_models[target].setFilterRegularExpression(text)
        self.trees[target].resizeColumnToContents(0)

    def resize_tree(self, target: int):
        text = self.ui.tree_filter_input.text()
        if text == "":
            tree = self.trees[target]
            tree.resizeColumnToContents(0)

    def tid_updated(self):
        tid = self.ui.tid_entry.text()
        if len(tid) == 16:
            if tid[:8] == "00000001" and int(tid[-2:], 16) > 2:
                self.ui.patch_ios_checkbox.setEnabled(True)
                return
        self.ui.patch_ios_checkbox.setEnabled(False)

    def update_log_text(self, new_text):
        # This method primarily exists to be the handler for the progress signal emitted by the worker thread.
        self.log_text += new_text + "\n"
        self.ui.log_text_browser.setText(self.log_text)
        # Always auto-scroll to the bottom of the log.
        scroll_bar = self.ui.log_text_browser.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())

    def prompt_for_update(self, new_version):
        # This method is designed to display a message box informing the user that a new NUSGet version is available.
        if new_version is not None:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg_box.setDefaultButton(QMessageBox.StandardButton.Yes)
            msg_box.setWindowTitle(app.translate("MainWindow", "NUSGet Update Available"))
            msg_box.setText(app.translate("MainWindow", "<b>There's a newer version of NUSGet available!</b>"))
            msg_box.setInformativeText(app.translate("MainWindow", "You're currently running v{nusget_version}, "
                                                   "but v{new_version} is available on GitHub. Would you like to view"
                                                   " the latest version?"
                                                    .format(nusget_version=nusget_version, new_version=new_version)))
            ret = msg_box.exec()
            if ret == QMessageBox.StandardButton.Yes:
                webbrowser.open("https://github.com/NinjaCheetah/NUSGet/releases/latest")

    def load_title_data(self, selected_title: TitleData):
        # Use the information passed from the double click callback to prepare a title for downloading.
        # If the last two characters are "XX", then this title has multiple regions, and each region uses its own
        # two-digit code. Use the region info passed to load the correct code.
        if selected_title.tid[-2:] == "XX":
            global regions
            region_code = regions[selected_title.region][0]
            tid = selected_title.tid[:-2] + region_code
        else:
            tid = selected_title.tid
        # Load the TID and version into the entry boxes.
        self.ui.tid_entry.setText(tid)
        self.ui.version_entry.setText(str(selected_title.version))
        # Create the WAD name by deriving it from the title name (basically just replace " " with "-").
        archive_name = selected_title.name.replace(" ", "-")
        if selected_title.category not in ["System", "IOS"]:
            archive_name += f"-{str(bytes.fromhex(tid).decode())[-4:]}"
        archive_name += f"-v{selected_title.version}"
        if selected_title.region != "World":
            archive_name += f"-{selected_title.region.split('/')[0]}"
        if self.ui.console_select_dropdown.currentText() == "DSi":
            archive_name += ".tad"
        else:
            if self.ui.console_select_dropdown.currentText() == "vWii":
                if selected_title.category.find("System") != -1 or selected_title.category == "IOS":
                    archive_name += "-vWii"
            else:
                if selected_title.category.find("System") != -1 or selected_title.category == "IOS":
                    archive_name += "-Wii"
            archive_name += ".wad"
        self.ui.archive_file_entry.setText(archive_name)
        danger_text = selected_title.danger
        # Add warning text to the log if the selected title has no ticket.
        if selected_title.ticket is False:
            danger_text = danger_text + ("Note: This Title does not have a Ticket available, so it cannot be decrypted"
                                         " or packed into a WAD/TAD.")
        # Print log info about the selected title and version.
        self.log_text = f"{tid} - {selected_title.name}\nVersion: {selected_title.version}\n\n{danger_text}\n"
        self.ui.log_text_browser.setText(self.log_text)

    def lock_ui(self):
        # Lock the UI prior to the download beginning to avoid spawning multiple threads or changing info part way in.
        # Also resets the log.
        self.ui.tid_entry.setEnabled(False)
        self.ui.version_entry.setEnabled(False)
        self.ui.download_btn.setEnabled(False)
        self.ui.script_btn.setEnabled(False)
        self.ui.pack_archive_checkbox.setEnabled(False)
        self.ui.keep_enc_checkbox.setEnabled(False)
        self.ui.create_dec_checkbox.setEnabled(False)
        self.ui.use_local_checkbox.setEnabled(False)
        self.ui.patch_ios_checkbox.setEnabled(False)
        self.ui.use_wiiu_nus_checkbox.setEnabled(False)
        self.ui.pack_vwii_mode_checkbox.setEnabled(False)
        self.ui.archive_file_entry.setEnabled(False)
        self.ui.console_select_dropdown.setEnabled(False)
        self.ui.auto_update_checkbox.setEnabled(False)
        self.ui.custom_out_dir_checkbox.setEnabled(False)
        self.ui.custom_out_dir_entry.setEnabled(False)
        self.ui.custom_out_dir_btn.setEnabled(False)
        self.log_text = ""
        self.ui.log_text_browser.setText(self.log_text)

    def unlock_ui(self):
        # Unlock the UI again after the current download finishes.
        self.ui.tid_entry.setEnabled(True)
        self.ui.version_entry.setEnabled(True)
        self.ui.download_btn.setEnabled(True)
        self.ui.script_btn.setEnabled(True)
        self.ui.pack_archive_checkbox.setEnabled(True)
        self.ui.keep_enc_checkbox.setEnabled(True)
        self.ui.create_dec_checkbox.setEnabled(True)
        self.ui.use_local_checkbox.setEnabled(True)
        self.ui.patch_ios_checkbox.setEnabled(True)
        self.ui.use_wiiu_nus_checkbox.setEnabled(True)
        self.ui.console_select_dropdown.setEnabled(True)
        if self.ui.pack_archive_checkbox.isChecked() is True:
            self.ui.archive_file_entry.setEnabled(True)
        self.ui.auto_update_checkbox.setEnabled(True)
        self.ui.custom_out_dir_checkbox.setEnabled(True)
        if self.ui.custom_out_dir_checkbox.isChecked() is True:
            self.ui.custom_out_dir_entry.setEnabled(True)
            self.ui.custom_out_dir_btn.setEnabled(True)

    def download_btn_pressed(self):
        # Throw an error and make a message box appear if you haven't selected any options to output the title.
        if (self.ui.pack_archive_checkbox.isChecked() is False and self.ui.keep_enc_checkbox.isChecked() is False and
                self.ui.create_dec_checkbox.isChecked() is False):
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg_box.setWindowTitle(app.translate("MainWindow", "No Output Selected"))
            msg_box.setText(app.translate("MainWindow", "You have not selected any format to output the data in!"))
            msg_box.setInformativeText(app.translate("MainWindow", "Please select at least one option for how you would "
                                                       "like the download to be saved."))
            msg_box.exec()
            return
        self.lock_ui()
        # Check for a custom output directory, and ensure that it's valid. If it is, then use that.
        if self.ui.custom_out_dir_checkbox.isChecked() and self.ui.custom_out_dir_entry.text() != "":
            out_path = pathlib.Path(self.ui.custom_out_dir_entry.text())
            if not out_path.exists() or not out_path.is_dir():
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Critical)
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
                msg_box.setWindowTitle(app.translate("MainWindow", "Invalid Download Directory"))
                msg_box.setText(app.translate("MainWindow", "The specified download directory does not exist!"))
                msg_box.setInformativeText(app.translate("MainWindow",
                                                         "Please make sure the specified download directory exists,"
                                                         " and that you have permission to access it."))
                msg_box.exec()
                return
        else:
            out_path = out_folder
        # Create a new worker object to handle the download in a new thread.
        if self.ui.console_select_dropdown.currentText() == "DSi":
            worker = Worker(run_nus_download_dsi, out_path, self.ui.tid_entry.text(),
                            self.ui.version_entry.text(), self.ui.pack_archive_checkbox.isChecked(),
                            self.ui.keep_enc_checkbox.isChecked(), self.ui.create_dec_checkbox.isChecked(),
                            self.ui.use_local_checkbox.isChecked(), self.ui.archive_file_entry.text())
        else:
            worker = Worker(run_nus_download_wii, out_path, self.ui.tid_entry.text(),
                            self.ui.version_entry.text(), self.ui.pack_archive_checkbox.isChecked(),
                            self.ui.keep_enc_checkbox.isChecked(), self.ui.create_dec_checkbox.isChecked(),
                            self.ui.use_wiiu_nus_checkbox.isChecked(), self.ui.use_local_checkbox.isChecked(),
                            self.ui.pack_vwii_mode_checkbox.isChecked(), self.ui.patch_ios_checkbox.isChecked(),
                            self.ui.archive_file_entry.text())
        worker.signals.result.connect(self.check_download_result)
        worker.signals.progress.connect(self.update_log_text)
        self.threadpool.start(worker)

    def check_download_result(self, result):
        # Handle all possible error codes returned from the download thread.
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
        if result == -1:
            window_title = app.translate("MainWindow", "Invalid Title ID")
            title_text = app.translate("MainWindow", "<b>The Title ID you have entered is not in a valid format!</b>")
            body_text = app.translate("MainWindow", "Title IDs must be 16 digit strings of numbers and letters. Please enter a correctly "
                                "formatted Title ID, or select one from the menu on the left.")
        elif result == -2:
            window_title = app.translate("MainWindow", "Title ID/Version Not Found")
            title_text = app.translate("MainWindow", "<b>No title with the provided Title ID or version could be found!</b>")
            body_text = app.translate("MainWindow", "Please make sure that you have entered a valid Title ID, or selected one from the "
                                "title database, and that the provided version exists for the title you are attempting to download.")
        elif result == -3:
            window_title = app.translate("MainWindow", "Content Decryption Failed")
            title_text = app.translate("MainWindow", "<b>Content decryption was not successful! Decrypted contents could not be created.</b>")
            body_text = app.translate("MainWindow", "Your TMD or Ticket may be damaged, or they may not correspond with the content being "
                                "decrypted. If you have checked \"Use local files, if they exist\", try disabling that "
                                "option before trying the download again to fix potential issues with local data.")
        elif result == 1:
            msg_box.setIcon(QMessageBox.Icon.Warning)
            window_title = app.translate("MainWindow", "Ticket Not Available")
            title_text = app.translate("MainWindow", "<b>No Ticket is Available for the Requested Title!</b>")
            body_text = app.translate("MainWindow", "A ticket could not be downloaded for the requested title, but you have selected \"Pack"
                                " installable archive\" or \"Create decrypted contents\". These options are not "
                                "available for titles without a ticket. Only encrypted contents have been saved.")
        else:
            window_title = app.translate("MainWindow", "Unknown Error")
            title_text = app.translate("MainWindow", "<b>An Unknown Error has Occurred!</b>")
            body_text = app.translate("MainWindow", "Please try again. If this issue persists, please open a new issue on GitHub detailing"
                                " what you were trying to do when this error occurred.")
        if result != 0:
            msg_box.setWindowTitle(window_title)
            msg_box.setText(title_text)
            msg_box.setInformativeText(body_text)
            msg_box.exec()
        self.unlock_ui()
        # Call the dropdown callback because this will automagically handle setting console-specific settings based
        # on the currently selected console, and saves on duplicate code.
        self.selected_console_changed()

    def check_batch_result(self, result: BatchResults):
        if result.code != 0:
            msg_box = QMessageBox()
            if result.failed_titles:
                msg_box.setIcon(QMessageBox.Icon.Critical)
            else:
                msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg_box.setWindowTitle(app.translate("MainWindow", "Script Issues Occurred"))
            msg_box.setText(app.translate("MainWindow", "<b>Some issues occurred while running the download script.</b>"))
            msg_box.setInformativeText(
                app.translate("MainWindow", "Check the log for more details about what issues were encountered."))
            msg_box.exec()
            self.log_text = ""
            if result.failed_titles:
                self.update_log_text(app.translate("MainWindow",
                                                   "The following titles could not be downloaded due to an error. "
                                                   "Please ensure that the Title ID and version listed in the script "
                                                   "are valid."))
                for title in result.failed_titles:
                    self.update_log_text(f"   - {title}")
            if result.warning_titles:
                if result.failed_titles:
                    self.update_log_text("")
                self.update_log_text(app.translate("MainWindow",
                                                   "You enabled \"Create decrypted contents\" or \"Pack installable "
                                                   "archive\", but the following titles in the script do not have "
                                                   "tickets available. If enabled, encrypted contents were still "
                                                   "downloaded."))
                for title in result.warning_titles:
                    self.update_log_text(f"   - {title}")
        self.unlock_ui()

    def selected_console_changed(self):
        # Callback function to enable or disable console-specific settings based on the selected console.
        if self.ui.console_select_dropdown.currentText() == "vWii":
            self.ui.pack_vwii_mode_checkbox.setEnabled(True)
        elif self.ui.console_select_dropdown.currentText() == "Wii":
            self.ui.pack_vwii_mode_checkbox.setEnabled(False)
        elif self.ui.console_select_dropdown.currentText() == "DSi":
            self.ui.pack_vwii_mode_checkbox.setEnabled(False)

    def script_btn_pressed(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg_box.setWindowTitle(app.translate("MainWindow", "Script Download Failed"))
        file_name = QFileDialog.getOpenFileName(self, caption=app.translate("MainWindow", "Open NUS Script"),
                                                filter=app.translate("MainWindow", "NUS Scripts (*.nus *.json)"),
                                                options=QFileDialog.Option.ReadOnly)
        # The old plaintext script format is no longer supported in NUSGet v1.3.0 and later. This script parsing code
        # is for the new JSON script format, which is much easier to use and is cleaner.
        if len(file_name[0]) == 0:
            return
        try:
            with open(file_name[0]) as script_file:
                script_data = json.load(script_file)
        except json.JSONDecodeError as e:
            msg_box.setText(app.translate("MainWindow", "<b>An error occurred while parsing the script file!</b>"))
            msg_box.setInformativeText(app.translate("MainWindow", f"Error encountered at line {e.lineno}, column {e.colno}. Please double-check the script and try again."))
            msg_box.exec()
            return
        # Build a list of the titles we need to download.
        titles = []
        for title in script_data:
            try:
                tid = title["Title ID"]
            except KeyError:
                msg_box.setText(app.translate("MainWindow", "<b>An error occurred while parsing Title IDs!</b>"))
                msg_box.setInformativeText(app.translate("MainWindow", f"The title at index {script_data.index(title)} does not have a Title ID!"))
                msg_box.exec()
                return
            # No version key is acceptable, just treat it as latest.
            try:
                title_version = int(title["Version"])
            except KeyError:
                title_version = -1
            # If no console was specified, assume Wii.
            try:
                console = title["Console"]
            except KeyError:
                console = "Wii"
            # Look up the title, and load the archive name for it if one can be found.
            archive_name = ""
            if console == "vWii":
                target_database = vwii_database
            elif console == "DSi":
                target_database = dsi_database
            else:
                target_database = wii_database
            for category in target_database:
                for t in target_database[category]:
                    if t["TID"][-2:] == "XX":
                        for r in regions:
                            if f"{t['TID'][:-2]}{regions[r][0]}" == tid:
                                try:
                                    archive_name = t["Name"].replace(" ", "-")
                                    break
                                except KeyError:
                                    archive_name = ""
                                    break
                    else:
                        if t["TID"] == tid:
                            try:
                                archive_name = t["Name"].replace(" ", "-")
                                break
                            except KeyError:
                                archive_name = ""
                                break
            titles.append(BatchTitleData(tid, title_version, console, archive_name))
        self.lock_ui()
        worker = Worker(run_nus_download_batch, out_folder, titles, self.ui.pack_archive_checkbox.isChecked(),
                        self.ui.keep_enc_checkbox.isChecked(), self.ui.create_dec_checkbox.isChecked(),
                        self.ui.use_wiiu_nus_checkbox.isChecked(), self.ui.use_local_checkbox.isChecked(),
                        self.ui.pack_vwii_mode_checkbox.isChecked(), self.ui.patch_ios_checkbox.isChecked())
        worker.signals.result.connect(self.check_batch_result)
        worker.signals.progress.connect(self.update_log_text)
        self.threadpool.start(worker)

    def choose_output_dir(self):
        # Use this handy convenience method to prompt the user to select a directory. Then we just need to validate
        # that the directory does indeed exist and is a directory, and we can save it as the output directory.
        selected_dir = QFileDialog.getExistingDirectory(self, app.translate("MainWindow", "Open Directory"),
                    "", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if selected_dir == "":
            return
        out_path = pathlib.Path(selected_dir)
        if not out_path.exists() or not out_path.is_dir():
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg_box.setWindowTitle(app.translate("MainWindow", "Invalid Download Directory"))
            msg_box.setText(app.translate("MainWindow", "<b>The specified download directory does not exist!</b>"))
            msg_box.setInformativeText(app.translate("MainWindow",
                                                     "Please make sure the download directory you want to use exists, and "
                                                     "that you have permission to access it."))
            msg_box.exec()
            return
        self.ui.custom_out_dir_entry.setText(str(out_path))
        config_data["out_path"] = str(out_path.absolute())
        save_config(config_data)

    def custom_output_dir_changed(self):
        # Callback method for when the custom output dir is changed manually. Check if the current path exists, and
        # save it if it does.
        if self.ui.custom_out_dir_entry.text() == "":
            config_data["out_path"] = ""
            save_config(config_data)
            return
        out_path = pathlib.Path(self.ui.custom_out_dir_entry.text())
        if out_path.exists() and out_path.is_dir():
            config_data["out_path"] = str(out_path.absolute())
            save_config(config_data)

    def about_nusget(self):
        about_box = AboutNUSGet([nusget_version, version("libWiiPy"), version("libTWLPy")])
        about_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Load the database files, this will work for both the raw Python file and compiled standalone/onefile binaries.
    database_file = open(os.path.join(os.path.dirname(__file__), "data", "wii-database.json"))
    wii_database = json.load(database_file)
    database_file = open(os.path.join(os.path.dirname(__file__), "data", "vwii-database.json"))
    vwii_database = json.load(database_file)
    database_file = open(os.path.join(os.path.dirname(__file__), "data", "dsi-database.json"))
    dsi_database = json.load(database_file)
    # Load the user's Downloads directory, which of course requires different steps on Windows vs macOS/Linux.
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = pathlib.Path(winreg.QueryValueEx(key, downloads_guid)[0])
    else:
        # Silence a false linter warning about redeclaration, since this is actually only ever assigned once.
        # noinspection PyRedeclaration
        location = pathlib.Path(os.path.expanduser('~')).joinpath('Downloads')
    # Build the path by combining the path to the Downloads photo with "NUSGet".
    out_folder = location.joinpath("NUSGet Downloads")
    # Create the "NUSGet Downloads" directory if it doesn't exist. In the future, this will be user-customizable, but
    # this works for now, and avoids using a directory next to the binary (mostly an issue on macOS/Linux).
    if not out_folder.is_dir():
        out_folder.mkdir()

    # Load the config path and then the configuration data, if it exists. If not, then we should initialize it and write
    # it out.
    config_file = get_config_file()
    if config_file.exists():
        config_data: dict = json.load(open(config_file))
    else:
        config_data: dict = {"auto_update": True}
        save_config(config_data)

    # This is essentially obsolete now with the addition of the custom stylesheet, but I'm keeping it just in case.
    # # Load the system plugins directory on Linux for system styles, if it exists. Try using Breeze if available, because
    # # it looks nice, but fallback on kvantum if it isn't, since kvantum is likely to exist. If all else fails, fusion.
    # if platform.system() == "Linux":
    #     if os.path.isdir("/usr/lib/qt6/plugins"):
    #         import subprocess
    #         try:
    #             # This CANNOT be the best way to get the system Qt version, but it's what I came up with for now.
    #             result = subprocess.run(['/usr/lib/qt6/bin/qtdiag'], stdout=subprocess.PIPE)
    #             result_str = result.stdout.decode("utf-8").split("\n")[0]
    #             sys_qt_ver = result_str.split(" ")[1].split(".")
    #             pyside_qt_ver = version("PySide6").split(".")
    #             if sys_qt_ver[0:2] == pyside_qt_ver[0:2]:
    #                 app.addLibraryPath("/usr/lib/qt6/plugins")
    #             if "Breeze" in QStyleFactory.keys():
    #                 app.setStyle("Breeze")
    #             elif "kvantum" in QStyleFactory.keys():
    #                 app.setStyle("kvantum")
    #         except Exception as e:
    #             print(e)

    # Load Fusion because that's objectively the best base theme, and then load the fancy stylesheet on top to make
    # NUSGet look nice and pretty.
    app.setStyle("fusion")
    stylesheet = open(os.path.join(os.path.dirname(__file__), "resources", "style.qss")).read()
    image_path_prefix = pathlib.Path(os.path.join(os.path.dirname(__file__), "resources")).resolve().as_posix()
    stylesheet = stylesheet.replace("{IMAGE_PREFIX}", image_path_prefix)
    app.setStyleSheet(stylesheet)

    # Load base Qt translations, and then app-specific translations.
    path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    translator = QTranslator(app)
    if translator.load(QLocale.system(), 'qtbase', '_', path):
        app.installTranslator(translator)
    translator = QTranslator(app)
    path = os.path.join(os.path.dirname(__file__), "resources", "translations")
    if translator.load(QLocale.system(), 'nusget', '_', path):
        app.installTranslator(translator)

    window = MainWindow()
    window.setWindowTitle("NUSGet")
    app.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "resources", "icon.png")))
    window.show()

    sys.exit(app.exec())
