import sys
import os
import json
import pathlib

import libWiiPy

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTreeWidgetItem, QHeaderView
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Signal, QObject

from qt.py.ui_MainMenu import Ui_MainWindow

regions = [["USA", "USA/NTSC", "45"], ["JAP", "Japan", "4A"], ["EUR", "Europe/PAL", "50"], ["KOR", "Korea", "4B"]]


class WorkerSignals(QObject):
    result = Signal(int)
    progress = Signal(str)


class Worker(QRunnable):
    def __init__(self, fn, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        try:
            result = self.fn(**self.kwargs)
        except ValueError:
            self.signals.result.emit(1)
        else:
            self.signals.result.emit(result)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.log_text = ""
        self.threadpool = QThreadPool()
        self.ui.download_btn.clicked.connect(self.download_btn_pressed)
        self.ui.pack_wad_chkbox.clicked.connect(self.pack_wad_chkbox_toggled)
        # noinspection PyUnresolvedReferences
        self.ui.title_tree.header().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.ui.log_text_browser.setText("NUSD-Py v1.0\nDeveloped by NinjaCheetah\nPowered by libWiiPy\n\n"
                                         "Select a title from the list on the left, or enter a Title ID to begin.")

        tree = self.ui.title_tree
        self.tree_categories = []

        global regions
        for key in wii_database:
            new_category = QTreeWidgetItem()
            new_category.setText(0, key)
            for title in wii_database[key]:
                new_title = QTreeWidgetItem()
                new_title.setText(0, title["TID"] + " - " + title["Name"])

                for region in title["Versions"]:
                    new_region = QTreeWidgetItem()
                    region_title = ""
                    if region == "World":
                        region_title = "World"
                    else:
                        for entry in regions:
                            if entry[0] == region:
                                region_title = entry[1]
                    new_region.setText(0, region_title)
                    for version in title["Versions"][region]:
                        new_version = QTreeWidgetItem()
                        new_version.setText(0, "v" + str(version))
                        new_region.addChild(new_version)
                    new_title.addChild(new_region)
                new_category.addChild(new_title)
            self.tree_categories.append(new_category)

        tree.insertTopLevelItems(0, self.tree_categories)
        tree.itemDoubleClicked.connect(self.onItemClicked)

    @Slot(QTreeWidgetItem, int)
    def onItemClicked(self, item, col):
        if self.ui.download_btn.isEnabled() is True:
            global regions
            region_names = []
            for region in regions:
                region_names.append(region[1])
            if (item.parent() is not None and item.parent() not in self.tree_categories
                    and item.parent().parent() not in self.tree_categories):
                category = item.parent().parent().parent().text(0)
                for title in wii_database[category]:
                    if item.parent().parent().text(0) == (title["TID"] + " - " + title["Name"]):
                        selected_title = title
                        selected_version = item.text(0)
                        selected_region = item.parent().text(0)
                        self.load_title_data(selected_title, selected_version, selected_region)

    def update_log_text(self, new_text):
        self.log_text += new_text + "\n"
        self.ui.log_text_browser.setText(self.log_text)
        # Always auto-scroll to the bottom of the log.
        scrollBar = self.ui.log_text_browser.verticalScrollBar()
        scrollBar.setValue(scrollBar.maximum())

    def load_title_data(self, selected_title, selected_version, selected_region=None):
        selected_version = selected_version[1:]
        if selected_title["TID"][-2:] == "XX":
            global regions
            region_code = ""
            for region in regions:
                if region[1] == selected_region:
                    region_code = region[2]
            tid = selected_title["TID"][:-2] + region_code
        else:
            tid = selected_title["TID"]
        self.ui.tid_entry.setText(tid)
        self.ui.version_entry.setText(selected_version)
        wad_name = selected_title["WAD Name"] + "-v" + selected_version + ".wad"
        self.ui.wad_file_entry.setText(wad_name)
        danger_text = ""
        try:
            danger_text = selected_title["Danger"]
        except KeyError:
            pass
        if selected_title["Ticket"] is False:
            danger_text = danger_text + ("\n\nNote: This Title does not have a Ticket available, so it cannot be "
                                         "packed into a WAD or decrypted.")
        self.log_text = (tid + " - " + selected_title["Name"] + "\n" + "Version: " + selected_version + "\n\n" +
                         danger_text + "\n")
        self.ui.log_text_browser.setText(self.log_text)

    def download_btn_pressed(self):
        self.ui.tid_entry.setEnabled(False)
        self.ui.version_entry.setEnabled(False)
        self.ui.download_btn.setEnabled(False)
        self.ui.pack_wad_chkbox.setEnabled(False)
        self.ui.keep_enc_chkbox.setEnabled(False)
        self.ui.create_dec_chkbox.setEnabled(False)
        self.ui.use_local_chkbox.setEnabled(False)
        self.ui.wad_file_entry.setEnabled(False)
        self.log_text = ""
        self.ui.log_text_browser.setText(self.log_text)

        worker = Worker(self.run_nus_download)
        worker.signals.result.connect(self.check_download_result)
        worker.signals.progress.connect(self.update_log_text)

        self.threadpool.start(worker)

    def check_download_result(self, result):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Icon.Critical)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
        if result == -1:
            msgBox.setWindowTitle("Invalid Title ID")
            msgBox.setText("The Title ID you have entered is not in a valid format!")
            msgBox.setInformativeText("Title IDs must be 16 digit strings of numbers and letters. Please enter a "
                                      "correctly formatted Title ID, or select one from the menu on the left.")
            msgBox.exec()
        elif result == -2:
            msgBox.setWindowTitle("Title ID/Version Not Found")
            msgBox.setText("No title with the provided Title ID or version could be found!")
            msgBox.setInformativeText("Please make sure that you have entered a valid Title ID or selected one from the"
                                      " title database, and that the provided version exists for the title you are"
                                      " attempting to download.")
            msgBox.exec()
        elif result == 1:
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setWindowTitle("Ticket Not Available")
            msgBox.setText("No Ticket is Available for the Requested Title!")
            msgBox.setInformativeText("A ticket could not be downloaded for the requested title, but you have selected "
                                      "\"Pack WAD\" or \"Create Decrypted Contents\". These options are not available "
                                      "for titles without a ticket. Only encrypted contents have been saved.")
            msgBox.exec()
        self.ui.tid_entry.setEnabled(True)
        self.ui.version_entry.setEnabled(True)
        self.ui.download_btn.setEnabled(True)
        self.ui.pack_wad_chkbox.setEnabled(True)
        self.ui.keep_enc_chkbox.setEnabled(True)
        self.ui.create_dec_chkbox.setEnabled(True)
        self.ui.use_local_chkbox.setEnabled(True)
        if self.ui.pack_wad_chkbox.isChecked() is True:
            self.ui.wad_file_entry.setEnabled(True)

    def run_nus_download(self, progress_callback):
        tid = self.ui.tid_entry.text()
        if tid == "":
            return -1
        try:
            version = int(self.ui.version_entry.text())
        except ValueError:
            version = None

        pack_wad_enabled = self.ui.pack_wad_chkbox.isChecked()
        decrypt_contents_enabled = self.ui.create_dec_chkbox.isChecked()

        title = libWiiPy.Title()

        title_dir = pathlib.Path(os.path.join(out_folder, tid))
        if not title_dir.is_dir():
            title_dir.mkdir()

        if version is not None:
            progress_callback.emit("Downloading title " + tid + " v" + str(version) + ", please wait...")
        else:
            progress_callback.emit("Downloading title " + tid + " vLatest, please wait...")

        progress_callback.emit(" - Downloading and parsing TMD...")
        try:
            if version is not None:
                title.load_tmd(libWiiPy.download_tmd(tid, version))
            else:
                title.load_tmd(libWiiPy.download_tmd(tid))
                version = title.tmd.title_version
        except ValueError:
            return -2

        version_dir = pathlib.Path(os.path.join(title_dir, str(version)))
        if not version_dir.is_dir():
            version_dir.mkdir()

        tmd_out = open(os.path.join(version_dir, "tmd." + str(version)), "wb")
        tmd_out.write(title.tmd.dump())
        tmd_out.close()

        progress_callback.emit(" - Downloading and parsing Ticket...")
        try:
            title.load_ticket(libWiiPy.download_ticket(tid))
            ticket_out = open(os.path.join(version_dir, "tik"), "wb")
            ticket_out.write(title.ticket.dump())
            ticket_out.close()
        except ValueError:
            progress_callback.emit("  - No Ticket is available!")
            pack_wad_enabled = False
            decrypt_contents_enabled = False

        title.load_content_records()
        content_list = []
        for content in range(len(title.tmd.content_records)):
            content_id_hex = hex(title.tmd.content_records[content].content_id)[2:]
            if len(content_id_hex) < 2:
                content_id_hex = "0" + content_id_hex
            content_file_name = "000000" + content_id_hex
            if self.ui.use_local_chkbox.isChecked() is True and os.path.exists(os.path.join(version_dir,
                                                                                            content_file_name)):
                progress_callback.emit(" - Using local copy of content " + str(content + 1) + " of " +
                                       str(len(title.tmd.content_records)))
                local_file = open(os.path.join(version_dir, content_file_name), "rb")
                content_list.append(local_file.read())
            else:
                progress_callback.emit(" - Downloading content " + str(content + 1) + " of " +
                                       str(len(title.tmd.content_records)) + " (" +
                                       str(title.tmd.content_records[content].content_size) + " bytes)...")
                content_list.append(libWiiPy.download_content(tid, title.tmd.content_records[content].content_id))
                progress_callback.emit("  - Done!")
                if self.ui.keep_enc_chkbox.isChecked() is True:
                    content_id_hex = hex(title.tmd.content_records[content].content_id)[2:]
                    if len(content_id_hex) < 2:
                        content_id_hex = "0" + content_id_hex
                    content_file_name = "000000" + content_id_hex
                    enc_content_out = open(os.path.join(version_dir, content_file_name), "wb")
                    enc_content_out.write(content_list[content])
                    enc_content_out.close()
        title.content.content_list = content_list

        if decrypt_contents_enabled is True:
            for content in range(len(title.tmd.content_records)):
                progress_callback.emit(" - Decrypting content " + str(content + 1) + " of " +
                                       str(len(title.tmd.content_records)) + "...")
                dec_content = title.get_content_by_index(content)
                content_id_hex = hex(title.tmd.content_records[content].content_id)[2:]
                if len(content_id_hex) < 2:
                    content_id_hex = "0" + content_id_hex
                content_file_name = "000000" + content_id_hex + ".app"
                dec_content_out = open(os.path.join(version_dir, content_file_name), "wb")
                dec_content_out.write(dec_content)
                dec_content_out.close()

        if pack_wad_enabled is True:
            progress_callback.emit(" - Building certificate...")
            title.wad.set_cert_data(libWiiPy.download_cert())

            progress_callback.emit("Packing WAD...")
            if self.ui.wad_file_entry.text() != "":
                wad_file_name = self.ui.wad_file_entry.text()
                if wad_file_name[-4:] != ".wad":
                    wad_file_name = wad_file_name + ".wad"
            else:
                wad_file_name = tid + "-v" + str(version) + ".wad"
            file = open(os.path.join(version_dir, wad_file_name), "wb")
            file.write(title.dump_wad())
            file.close()

        progress_callback.emit("Download complete!")
        if ((not pack_wad_enabled and self.ui.pack_wad_chkbox.isChecked()) or
                (not decrypt_contents_enabled and self.ui.create_dec_chkbox.isChecked())):
            return 1
        return 0

    def pack_wad_chkbox_toggled(self):
        if self.ui.pack_wad_chkbox.isChecked() is True:
            self.ui.wad_file_entry.setEnabled(True)
        else:
            self.ui.wad_file_entry.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    wii_database = json.load(open("wii-database.json", "r"))

    out_folder = pathlib.Path("titles")
    if not out_folder.is_dir():
        out_folder.mkdir()

    window = MainWindow()
    window.setWindowTitle("NUSD-Py")
    window.show()

    sys.exit(app.exec())
