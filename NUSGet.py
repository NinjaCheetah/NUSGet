# "NUSGet.py", licensed under the MIT license
# Copyright 2024 NinjaCheetah

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

import os
import sys
import json
import pathlib
import platform
import webbrowser
from importlib.metadata import version

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTreeWidgetItem, QHeaderView, QStyle,
                               QStyleFactory, QFileDialog)
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Signal, QObject, QLibraryInfo, QTranslator, QLocale

from qt.py.ui_MainMenu import Ui_MainWindow

from modules.core import *
from modules.download_wii import run_nus_download_wii, run_nus_download_wii_batch
from modules.download_dsi import run_nus_download_dsi, run_nus_download_dsi_batch

nusget_version = "1.2.0"

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
        self.ui.pack_archive_chkbox.clicked.connect(self.pack_wad_chkbox_toggled)
        self.ui.tid_entry.textChanged.connect(self.tid_updated)
        # noinspection PyUnresolvedReferences
        self.ui.wii_title_tree.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        # noinspection PyUnresolvedReferences
        self.ui.vwii_title_tree.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        # noinspection PyUnresolvedReferences
        self.ui.dsi_title_tree.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Basic intro text set to automatically show when the app loads. This may be changed in the future.
        libwiipy_version = "v" + version("libWiiPy")
        libtwlpy_version = "v" + version("libTWLPy")
        self.log_text = (app.translate("MainWindow", "NUSGet v{nusget_version}\nDeveloped by NinjaCheetah\nPowered by libWiiPy "
                              "{libwiipy_version}\nDSi support provided by libTWLPy {libtwlpy_version}\n\n"
                              "Select a title from the list on the left, or enter a Title ID to begin.\n\n"
                              "Titles marked with a checkmark are free and have a ticket available, and can"
                              " be decrypted and/or packed into a WAD or TAD. Titles with an X do not have "
                              "a ticket, and only their encrypted contents can be saved.\n\nTitles will be "
                              "downloaded to a folder named \"NUSGet\" inside your downloads folder.")
                       .format(nusget_version=nusget_version, libwiipy_version=libwiipy_version,
                               libtwlpy_version=libtwlpy_version))
        self.ui.log_text_browser.setText(self.log_text)
        # Add console entries to dropdown and attach on change signal.
        self.ui.console_select_dropdown.addItem("Wii")
        self.ui.console_select_dropdown.addItem("vWii")
        self.ui.console_select_dropdown.addItem("DSi")
        self.ui.console_select_dropdown.currentIndexChanged.connect(self.selected_console_changed)
        # Title tree building code.
        wii_tree = self.ui.wii_title_tree
        vwii_tree = self.ui.vwii_title_tree
        dsi_tree = self.ui.dsi_title_tree
        self.trees = [[wii_tree, wii_database], [vwii_tree, vwii_database], [dsi_tree, dsi_database]]
        for tree in self.trees:
            self.tree_categories = []
            global regions
            # Iterate over each category in the database file.
            for key in tree[1]:
                new_category = QTreeWidgetItem()
                new_category.setText(0, key)
                # Iterate over each title in the current category.
                for title in tree[1][key]:
                    new_title = QTreeWidgetItem()
                    new_title.setText(0, title["TID"] + " - " + title["Name"])
                    # Build the list of regions and what versions are offered for each region.
                    for region in title["Versions"]:
                        new_region = QTreeWidgetItem()
                        new_region.setText(0, region)
                        for title_version in title["Versions"][region]:
                            new_version = QTreeWidgetItem()
                            new_version.setText(0, "v" + str(title_version))
                            new_region.addChild(new_version)
                        new_title.addChild(new_region)
                    # Set an indicator icon to show if a ticket is offered for this title or not.
                    if title["Ticket"] is True:
                        new_title.setIcon(0, self.style().standardIcon(QStyle.StandardPixmap.SP_DialogApplyButton))
                    else:
                        new_title.setIcon(0, self.style().standardIcon(QStyle.StandardPixmap.SP_DialogCancelButton))
                    new_category.addChild(new_title)
                self.tree_categories.append(new_category)
            tree[0].insertTopLevelItems(0, self.tree_categories)
            # Connect the double click signal for handling when titles are selected.
            tree[0].itemDoubleClicked.connect(self.onItemClicked)

        # Prevent resizing, Qt makes us look stupid here
        self.setFixedSize(self.size())

        # Do a quick check to see if there's a newer release available, and inform the user if there is.
        worker = Worker(check_nusget_updates, app, nusget_version)
        worker.signals.result.connect(self.prompt_for_update)
        worker.signals.progress.connect(self.update_log_text)
        self.threadpool.start(worker)

    @Slot(QTreeWidgetItem, int)
    def onItemClicked(self, item, col):
        if self.ui.download_btn.isEnabled() is True:
            # Check to make sure that this is a version and nothing higher. If you've doubled clicked on anything other
            # than a version, this returns an AttributeError and the click can be ignored.
            try:
                category = item.parent().parent().parent().text(0)
            except AttributeError:
                return
            tree = self.trees[self.ui.platform_tabs.currentIndex()]
            for title in tree[1][category]:
                # Check to see if the current title matches the selected one, and if it does, pass that info on.
                if item.parent().parent().text(0) == (title["TID"] + " - " + title["Name"]):
                    self.ui.console_select_dropdown.setCurrentIndex(self.ui.platform_tabs.currentIndex())
                    try:
                        danger_text = title["Danger"]
                    except KeyError:
                        danger_text = ""
                    selected_title = SelectedTitle(title["TID"], title["Name"], title["Archive Name"], item.text(0)[1:],
                                                   title["Ticket"], item.parent().text(0), category,
                                                   self.ui.console_select_dropdown.currentText(), danger_text)
                    self.load_title_data(selected_title)

    def tid_updated(self):
        tid = self.ui.tid_entry.text()
        if len(tid) == 16:
            if tid[:8] == "00000001" and int(tid[-2:], 16) > 2:
                self.ui.patch_ios_chkbox.setEnabled(True)
                return
        self.ui.patch_ios_chkbox.setEnabled(False)

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
            msg_box.setText(app.translate("MainWindow", "There's a newer version of NUSGet available!"))
            msg_box.setInformativeText(app.translate("MainWindow", "You're currently running v{nusget_version}, "
                                                   "but v{new_version} is available on GitHub. Would you like to view"
                                                   " the latest version?"
                                                    .format(nusget_version=nusget_version, new_version=new_version)))
            ret = msg_box.exec()
            if ret == QMessageBox.StandardButton.Yes:
                webbrowser.open("https://github.com/NinjaCheetah/NUSGet/releases/latest")

    def load_title_data(self, selected_title: SelectedTitle):
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
        self.ui.version_entry.setText(selected_title.version)
        # Load the WAD name, assuming it exists. This shouldn't ever be able to fail as the database has a WAD name
        # for every single title, regardless of whether it can be packed or not.
        try:
            archive_name = f"{selected_title.archive_name}"
            if selected_title.category != "System" and selected_title.category != "IOS":
                archive_name += f"-{str(bytes.fromhex(tid).decode())[-4:]}"
            archive_name += f"-v{selected_title.version}"
            if selected_title.region != "World":
                archive_name += f"-{selected_title.region.split('/')[0]}"
            if self.ui.console_select_dropdown.currentText() == "DSi":
                archive_name += ".tad"
            elif self.ui.console_select_dropdown.currentText() == "vWii":
                if selected_title.category.find("System") != -1 or selected_title.category == "IOS":
                    archive_name += "-vWii"
                archive_name += ".wad"
            else:
                if selected_title.category.find("System") != -1 or selected_title.category == "IOS":
                    archive_name += "-Wii"
                archive_name += ".wad"
            self.ui.archive_file_entry.setText(archive_name)
        except KeyError:
            pass
        danger_text = selected_title.danger
        # Add warning text to the log if the selected title has no ticket.
        if selected_title.ticket is False:
            danger_text = danger_text + ("Note: This Title does not have a Ticket available, so it cannot be decrypted"
                                         " or packed into a WAD/TAD.")
        # Print log info about the selected title and version.
        self.log_text = f"{tid} - {selected_title.name}\nVersion: {selected_title.version}\n\n{danger_text}\n"
        self.ui.log_text_browser.setText(self.log_text)

    def lock_ui_for_download(self):
        # Lock the UI prior to the download beginning to avoid spawning multiple threads or changing info part way in.
        # Also resets the log.
        self.ui.tid_entry.setEnabled(False)
        self.ui.version_entry.setEnabled(False)
        self.ui.download_btn.setEnabled(False)
        self.ui.script_btn.setEnabled(False)
        self.ui.pack_archive_chkbox.setEnabled(False)
        self.ui.keep_enc_chkbox.setEnabled(False)
        self.ui.create_dec_chkbox.setEnabled(False)
        self.ui.use_local_chkbox.setEnabled(False)
        self.ui.use_wiiu_nus_chkbox.setEnabled(False)
        self.ui.pack_vwii_mode_chkbox.setEnabled(False)
        self.ui.archive_file_entry.setEnabled(False)
        self.ui.console_select_dropdown.setEnabled(False)
        self.log_text = ""
        self.ui.log_text_browser.setText(self.log_text)

    def download_btn_pressed(self):
        # Throw an error and make a message box appear if you haven't selected any options to output the title.
        if (self.ui.pack_archive_chkbox.isChecked() is False and self.ui.keep_enc_chkbox.isChecked() is False and
                self.ui.create_dec_chkbox.isChecked() is False):
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
        
        self.lock_ui_for_download()

        # Create a new worker object to handle the download in a new thread.
        if self.ui.console_select_dropdown.currentText() == "DSi":
            worker = Worker(run_nus_download_dsi, out_folder, self.ui.tid_entry.text(),
                            self.ui.version_entry.text(), self.ui.pack_archive_chkbox.isChecked(),
                            self.ui.keep_enc_chkbox.isChecked(), self.ui.create_dec_chkbox.isChecked(),
                            self.ui.use_local_chkbox.isChecked(), self.ui.archive_file_entry.text())
        else:
            worker = Worker(run_nus_download_wii, out_folder, self.ui.tid_entry.text(),
                            self.ui.version_entry.text(), self.ui.pack_archive_chkbox.isChecked(),
                            self.ui.keep_enc_chkbox.isChecked(), self.ui.create_dec_chkbox.isChecked(),
                            self.ui.use_wiiu_nus_chkbox.isChecked(), self.ui.use_local_chkbox.isChecked(),
                            self.ui.pack_vwii_mode_chkbox.isChecked(), self.ui.patch_ios_chkbox.isChecked(),
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
            title_text = app.translate("MainWindow", "The Title ID you have entered is not in a valid format!")
            body_text = app.translate("MainWindow", "Title IDs must be 16 digit strings of numbers and letters. Please enter a correctly "
                                "formatted Title ID, or select one from the menu on the left.")
        elif result == -2:
            window_title = app.translate("MainWindow", "Title ID/Version Not Found")
            title_text = app.translate("MainWindow", "No title with the provided Title ID or version could be found!")
            body_text = app.translate("MainWindow", "Please make sure that you have entered a valid Title ID, or selected one from the "
                                "title database, and that the provided version exists for the title you are attempting to download.")
        elif result == -3:
            window_title = app.translate("MainWindow", "Content Decryption Failed")
            title_text = app.translate("MainWindow", "Content decryption was not successful! Decrypted contents could not be created.")
            body_text = app.translate("MainWindow", "Your TMD or Ticket may be damaged, or they may not correspond with the content being "
                                "decrypted. If you have checked \"Use local files, if they exist\", try disabling that "
                                "option before trying the download again to fix potential issues with local data.")
        elif result == 1:
            msg_box.setIcon(QMessageBox.Icon.Warning)
            window_title = app.translate("MainWindow", "Ticket Not Available")
            title_text = app.translate("MainWindow", "No Ticket is Available for the Requested Title!")
            body_text = app.translate("MainWindow", "A ticket could not be downloaded for the requested title, but you have selected \"Pack"
                                " installable archive\" or \"Create decrypted contents\". These options are not "
                                "available for titles without a ticket. Only encrypted contents have been saved.")
        else:
            window_title = app.translate("MainWindow", "Unknown Error")
            title_text = app.translate("MainWindow", "An Unknown Error has Occurred!")
            body_text = app.translate("MainWindow", "Please try again. If this issue persists, please open a new issue on GitHub detailing"
                                " what you were trying to do when this error occurred.")
        if result != 0:
            msg_box.setWindowTitle(window_title)
            msg_box.setText(title_text)
            msg_box.setInformativeText(body_text)
            msg_box.exec()
        # Now that the thread has closed, unlock the UI to allow for the next download.
        self.ui.tid_entry.setEnabled(True)
        self.ui.version_entry.setEnabled(True)
        self.ui.download_btn.setEnabled(True)
        self.ui.script_btn.setEnabled(True)
        self.ui.pack_archive_chkbox.setEnabled(True)
        self.ui.keep_enc_chkbox.setEnabled(True)
        self.ui.create_dec_chkbox.setEnabled(True)
        self.ui.use_local_chkbox.setEnabled(True)
        self.ui.use_wiiu_nus_chkbox.setEnabled(True)
        self.ui.console_select_dropdown.setEnabled(True)
        if self.ui.pack_archive_chkbox.isChecked() is True:
            self.ui.archive_file_entry.setEnabled(True)
        # Call the dropdown callback because this will automagically handle setting console-specific settings based
        # on the currently selected console, and saves on duplicate code.
        self.selected_console_changed()

    def pack_wad_chkbox_toggled(self):
        # Simple function to catch when the WAD/TAD checkbox is toggled and enable/disable the file name entry box
        # accordingly.
        if self.ui.pack_archive_chkbox.isChecked() is True:
            self.ui.archive_file_entry.setEnabled(True)
        else:
            self.ui.archive_file_entry.setEnabled(False)

    def selected_console_changed(self):
        # Callback function to enable or disable console-specific settings based on the selected console.
        if self.ui.console_select_dropdown.currentText() == "vWii":
            self.ui.pack_vwii_mode_chkbox.setEnabled(True)
        elif self.ui.console_select_dropdown.currentText() == "Wii":
            self.ui.pack_vwii_mode_chkbox.setEnabled(False)
        elif self.ui.console_select_dropdown.currentText() == "DSi":
            self.ui.pack_vwii_mode_chkbox.setEnabled(False)

    def script_btn_pressed(self):
        file_name = QFileDialog.getOpenFileName(self, caption=app.translate("MainWindow", "Open NUS script"), filter=app.translate("MainWindow", "NUS Scripts (*.nus *.txt)"), options=QFileDialog.Option.ReadOnly)
        if len(file_name[0]) == 0:
            return

        try:
            file = open(file_name[0], "r")
        except:
            QMessageBox.critical(self, app.translate("MainWindow", "Script Failure"), app.translate("MainWindow", "Failed to open the script."), buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.Ok)
            return
        
        content = file.readlines()

        # Decoding NUS Scripts
        # NUS Scripts are plaintext UTF-8 files that list a title per line, terminated with newlines.
        # Every title is its u64 TID, a space and its u16 version, *both* written in hexadecimal.
        # NUS itself expects versions as decimal notation, so they need to be decoded first, but TIDs are always written in hexadecimal notation.

        titles = []

        for index, title in enumerate(content):
            decoded = title.replace("\n", "").split(" ", 1)
            if len(decoded[0]) != 16:
                QMessageBox.critical(self, app.translate("MainWindow", "Script Failure"), app.translate("MainWindow", "The TID for title #%n is not valid.", "", index+1), buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.Ok)
                return
            elif len(decoded[1]) != 4:
                QMessageBox.critical(self, app.translate("MainWindow", "Script Failure"), app.translate("MainWindow", "The version for title #%n is not valid.", "", index+1), buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.Ok)
                return
            
            tid = decoded[0]

            try:
                version = int(decoded[1], 16)
            except:
                QMessageBox.critical(self, app.translate("MainWindow", "Script Failure"), app.translate("MainWindow", "The version for title #%n is not valid.", "", index+1), buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.Ok)
                return

            title = None
            for category in self.trees[self.ui.platform_tabs.currentIndex()][1]:
                for title_ in self.trees[self.ui.platform_tabs.currentIndex()][1][category]:
                    # The last two digits are either identifying the title type (e.g IOS slot, BC type, etc) or a region code; in case of the latter, skip the region here to match it
                    if not ((title_["TID"][-2:] == "XX" and title_["TID"][:-2] == tid[:-2]) or title_["TID"] == tid):
                        continue

                    found_ver = False
                    for region in title_["Versions"]:
                        for db_version in title_["Versions"][region]:
                            if db_version == version:
                                found_ver = True
                                break

                    if not found_ver:
                        QMessageBox.critical(self, app.translate("MainWindow", "Script Failure"), app.translate("MainWindow", "The version for title #%n could not be discovered in the database.", "", index+1), buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.Ok)
                        return

                    title = title_
                    break
            
            if title == None:
                QMessageBox.critical(self, app.translate("MainWindow", "Script Failure"), app.translate("MainWindow", "Title #%n could not be discovered in the database.", "", index+1), buttons=QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.Ok)
                return

            titles.append((title["TID"], str(version), title["Archive Name"]))

        self.lock_ui_for_download()

        self.update_log_text(f"Found {len(titles)} titles, starting batch download.")

        if self.ui.console_select_dropdown.currentText() == "DSi":
            worker = Worker(run_nus_download_dsi_batch, out_folder, titles, self.ui.pack_archive_chkbox.isChecked(),
                            self.ui.keep_enc_chkbox.isChecked(), self.ui.create_dec_chkbox.isChecked(),
                            self.ui.use_local_chkbox.isChecked(), self.ui.archive_file_entry.text())
        else:
            worker = Worker(run_nus_download_wii_batch, out_folder, titles, self.ui.pack_archive_chkbox.isChecked(),
                            self.ui.keep_enc_chkbox.isChecked(), self.ui.create_dec_chkbox.isChecked(),
                            self.ui.use_wiiu_nus_chkbox.isChecked(), self.ui.use_local_chkbox.isChecked(),
                            self.ui.pack_vwii_mode_chkbox.isChecked(), self.ui.patch_ios_chkbox.isChecked())

        worker.signals.result.connect(self.check_download_result)
        worker.signals.progress.connect(self.update_log_text)
        self.threadpool.start(worker)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Load the database files, this will work for both the raw Python file and compiled standalone/onefile binaries.
    database_file = open(os.path.join(os.path.dirname(__file__), "data/wii-database.json"))
    wii_database = json.load(database_file)
    database_file = open(os.path.join(os.path.dirname(__file__), "data/vwii-database.json"))
    vwii_database = json.load(database_file)
    database_file = open(os.path.join(os.path.dirname(__file__), "data/dsi-database.json"))
    dsi_database = json.load(database_file)
    # Load the user's Downloads directory, which of course requires different steps on Windows vs macOS/Linux.
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = pathlib.Path(winreg.QueryValueEx(key, downloads_guid)[0])
    else:
        location = pathlib.Path(os.path.expanduser('~')).joinpath('Downloads')
    # Build the path by combining the path to the Downloads photo with "NUSGet".
    out_folder = location.joinpath("NUSGet")
    # Create the "NUSGet" directory if it doesn't exist. In the future, this will be user-customizable, but this works
    # for now, and avoids the issues from when it used to use a directory next to the binary (mostly on macOS).
    if not out_folder.is_dir():
        out_folder.mkdir()

    # Load the system plugins directory on Linux for system styles, if it exists. Try using Breeze if available, because
    # it looks nice, but fallback on kvantum if it isn't, since kvantum is likely to exist. If all else fails, fusion.
    if platform.system() == "Linux":
        if os.path.isdir("/usr/lib/qt6/plugins"):
            app.addLibraryPath("/usr/lib/qt6/plugins")
            if "Breeze" in QStyleFactory.keys():
                app.setStyle("Breeze")
            elif "kvantum" in QStyleFactory.keys():
                app.setStyle("kvantum")

    # Load qtbase translations, and then apps-specific translations.
    path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    translator = QTranslator(app)
    if translator.load(QLocale.system(), 'qtbase', '_', path):
        app.installTranslator(translator)
    translator = QTranslator(app)
    path = os.path.join(os.path.dirname(__file__), "resources/translations")
    if translator.load(QLocale.system(), 'nusget', '_', path):
        app.installTranslator(translator)

    window = MainWindow()
    window.setWindowTitle("NUSGet")
    window.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "resources/icon.png")))
    window.show()

    sys.exit(app.exec())
