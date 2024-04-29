# NUSGet.py, licensed under the MIT license
# Copyright 2024 NinjaCheetah

import sys
import os
import json
import pathlib

import libWiiPy

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTreeWidgetItem, QHeaderView, QStyle
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Signal, QObject

from qt.py.ui_MainMenu import Ui_MainWindow

regions = [["World", "World", "41"], ["USA", "USA/NTSC", "45"], ["JAP", "Japan", "4A"], ["EUR", "Europe/PAL", "50"],
           ["KOR", "Korea", "4B"]]


# Signals needed for the worker used for threading the downloads.
class WorkerSignals(QObject):
    result = Signal(int)
    progress = Signal(str)


# Worker class used to thread the downloads.
class Worker(QRunnable):
    def __init__(self, fn, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        # All possible errors *should* be caught by the code and will safely return specific error codes. In the
        # unlikely event that an unexpected error happens, it can only possibly be a ValueError, so handle that and
        # return code 1.
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
        # Basic intro text set to automatically show when the app loads. This may be changed in the future.
        self.ui.log_text_browser.setText("NUSGet v1.0\nDeveloped by NinjaCheetah\nPowered by libWiiPy\n\n"
                                         "Select a title from the list on the left, or enter a Title ID to begin.\n\n"
                                         "Titles marked with a checkmark are free and have a ticket available, and can"
                                         " be decrypted and packed into a WAD. Titles with an X do not have a ticket,"
                                         " and only their encrypted contents can be saved.")
        # Tree building code.
        tree = self.ui.title_tree
        self.tree_categories = []
        global regions
        # Iterate over each category in the database file.
        for key in wii_database:
            new_category = QTreeWidgetItem()
            new_category.setText(0, key)
            # Iterate over each title in the current category.
            for title in wii_database[key]:
                new_title = QTreeWidgetItem()
                new_title.setText(0, title["TID"] + " - " + title["Name"])
                # Build the list of regions and what versions are offered for each region.
                for region in title["Versions"]:
                    new_region = QTreeWidgetItem()
                    region_title = ""
                    # This part is probably done poorly and should be improved.
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
                # Set an indicator icon to show if a ticket is offered for this title or not.
                if title["Ticket"] is True:
                    new_title.setIcon(0, self.style().standardIcon(QStyle.StandardPixmap.SP_DialogApplyButton))
                else:
                    new_title.setIcon(0, self.style().standardIcon(QStyle.StandardPixmap.SP_DialogCancelButton))
                new_category.addChild(new_title)
            self.tree_categories.append(new_category)
        tree.insertTopLevelItems(0, self.tree_categories)
        # Connect the double click signal for handling when titles are selected.
        tree.itemDoubleClicked.connect(self.onItemClicked)

    @Slot(QTreeWidgetItem, int)
    def onItemClicked(self, item, col):
        if self.ui.download_btn.isEnabled() is True:
            global regions
            region_names = []
            for region in regions:
                region_names.append(region[1])
            # This is checking to make sure all category names, title names, and region names are not handled as
            # valid choices. item.parent().parent().parent().text(0) is terrifying, I know.
            if ((item.parent() is not None) and item.parent() not in self.tree_categories
                    and item.parent().parent() not in self.tree_categories):
                category = item.parent().parent().parent().text(0)
                for title in wii_database[category]:
                    # Check to see if the current title matches the selected one, and if it does, pass that info on.
                    if item.parent().parent().text(0) == (title["TID"] + " - " + title["Name"]):
                        selected_title = title
                        selected_version = item.text(0)
                        selected_region = item.parent().text(0)
                        self.load_title_data(selected_title, selected_version, selected_region)

    def update_log_text(self, new_text):
        # This function primarily exists to be the handler for the progress signal emitted by the worker thread.
        self.log_text += new_text + "\n"
        self.ui.log_text_browser.setText(self.log_text)
        # Always auto-scroll to the bottom of the log.
        scrollBar = self.ui.log_text_browser.verticalScrollBar()
        scrollBar.setValue(scrollBar.maximum())

    def load_title_data(self, selected_title, selected_version, selected_region=None):
        # Use the information passed from the double click callback to prepare a title for downloading.
        selected_version = selected_version[1:]
        # If the last two characters are "XX", then this title has multiple regions, and each region uses its own
        # two-digit code. Use the region info passed to load the correct code.
        if selected_title["TID"][-2:] == "XX":
            global regions
            region_code = ""
            # Similarly to previous region-related code, this can definitely be improved.
            for region in regions:
                if region[1] == selected_region:
                    region_code = region[2]
            tid = selected_title["TID"][:-2] + region_code
        else:
            tid = selected_title["TID"]
        # Load the TID and version into the entry boxes.
        self.ui.tid_entry.setText(tid)
        self.ui.version_entry.setText(selected_version)
        # Load the WAD name, assuming it exists. This shouldn't ever be able to fail as the database has a WAD name
        # for every single title, regardless of whether it can be packed or not.
        try:
            wad_name = selected_title["WAD Name"] + "-v" + selected_version + ".wad"
            self.ui.wad_file_entry.setText(wad_name)
        except KeyError:
            pass
        # Same idea for the danger string, however this only exists for certain titles and will frequently be an error.
        danger_text = ""
        try:
            danger_text = selected_title["Danger"]
        except KeyError:
            pass
        # Add warning text to the log if the selected title has no ticket.
        if selected_title["Ticket"] is False:
            danger_text = danger_text + ("Note: This Title does not have a Ticket available, so it cannot be "
                                         "packed into a WAD or decrypted.")
        # Print log info about the selected title and version.
        self.log_text = (tid + " - " + selected_title["Name"] + "\n" + "Version: " + selected_version + "\n\n" +
                         danger_text + "\n")
        self.ui.log_text_browser.setText(self.log_text)

    def download_btn_pressed(self):
        # Throw an error and make a message box appear if you haven't selected any options to output the title.
        if (self.ui.pack_wad_chkbox.isChecked() is False and self.ui.keep_enc_chkbox.isChecked() is False and
                self.ui.create_dec_chkbox.isChecked() is False):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Critical)
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
            msgBox.setWindowTitle("No Output Selected")
            msgBox.setText("You have not selected any format to output the data in!")
            msgBox.setInformativeText("Please select at least one option for how you would like the download to be "
                                      "saved.")
            msgBox.exec()
            return
        # Lock the UI prior to the download beginning to avoid spawning multiple threads or changing info part way in.
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
        # Create a new worker object to handle the download in a new thread.
        worker = Worker(self.run_nus_download)
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
            msg_box.setWindowTitle("Invalid Title ID")
            msg_box.setText("The Title ID you have entered is not in a valid format!")
            msg_box.setInformativeText("Title IDs must be 16 digit strings of numbers and letters. Please enter a "
                                       "correctly formatted Title ID, or select one from the menu on the left.")
            msg_box.exec()
        elif result == -2:
            msg_box.setWindowTitle("Title ID/Version Not Found")
            msg_box.setText("No title with the provided Title ID or version could be found!")
            msg_box.setInformativeText("Please make sure that you have entered a valid Title ID, or selected one from "
                                       " the title database, and that the provided version exists for the title you are"
                                       " attempting to download.")
            msg_box.exec()
        elif result == -3:
            msg_box.setWindowTitle("Content Decryption Failed")
            msg_box.setText("Content decryption was not successful! Decrypted contents could not be created.")
            msg_box.setInformativeText("Your TMD or Ticket may be damaged, or they may not correspond with the content "
                                       "being decrypted. If you have checked \"Use local files, if they exist\", try "
                                       "disabling that option before trying the download again to fix potential issues "
                                       "with local data.")
            msg_box.exec()
        elif result == 1:
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setWindowTitle("Ticket Not Available")
            msg_box.setText("No Ticket is Available for the Requested Title!")
            msg_box.setInformativeText(
                "A ticket could not be downloaded for the requested title, but you have selected "
                "\"Pack WAD\" or \"Create Decrypted Contents\". These options are not available "
                "for titles without a ticket. Only encrypted contents have been saved.")
            msg_box.exec()
        # Now that the thread has closed, unlock the UI to allow for the next download.
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
        # Actual NUS download function that runs in a separate thread.
        tid = self.ui.tid_entry.text()
        # Immediately knock out any invalidly formatted Title IDs.
        if len(tid) != 16:
            return -1
        # An error here is acceptable, because it may just mean the box is empty. Or the version string is nonsense.
        # Either way, just fall back on downloading the latest version of the title.
        try:
            version = int(self.ui.version_entry.text())
        except ValueError:
            version = None
        # Set variables for these two options so that their state can be compared against the user's choices later.
        pack_wad_enabled = self.ui.pack_wad_chkbox.isChecked()
        decrypt_contents_enabled = self.ui.create_dec_chkbox.isChecked()
        # Create a new libWiiPy Title.
        title = libWiiPy.Title()
        # Make a directory for this title if it doesn't exist.
        title_dir = pathlib.Path(os.path.join(out_folder, tid))
        if not title_dir.is_dir():
            title_dir.mkdir()
        # Announce the title being downloaded, and the version if applicable.
        if version is not None:
            progress_callback.emit("Downloading title " + tid + " v" + str(version) + ", please wait...")
        else:
            progress_callback.emit("Downloading title " + tid + " vLatest, please wait...")
        progress_callback.emit(" - Downloading and parsing TMD...")
        # Download a specific TMD version if a version was specified, otherwise just download the latest TMD.
        try:
            if version is not None:
                title.load_tmd(libWiiPy.download_tmd(tid, version))
            else:
                title.load_tmd(libWiiPy.download_tmd(tid))
                version = title.tmd.title_version
        # If libWiiPy returns an error, that means that either the TID or version doesn't exist, so return code -2.
        except ValueError:
            return -2
        # Make a directory for this version if it doesn't exist.
        version_dir = pathlib.Path(os.path.join(title_dir, str(version)))
        if not version_dir.is_dir():
            version_dir.mkdir()
        # Write out the TMD to a file.
        tmd_out = open(os.path.join(version_dir, "tmd." + str(version)), "wb")
        tmd_out.write(title.tmd.dump())
        tmd_out.close()
        # Use a local ticket, if one exists and "use local files" is enabled.
        if self.ui.use_local_chkbox.isChecked() is True and os.path.exists(os.path.join(version_dir, "tik")):
            progress_callback.emit(" - Parsing local copy of Ticket...")
            local_ticket = open(os.path.join(version_dir, "tik"), "rb")
            title.load_ticket(local_ticket.read())
        else:
            progress_callback.emit(" - Downloading and parsing Ticket...")
            try:
                title.load_ticket(libWiiPy.download_ticket(tid))
                ticket_out = open(os.path.join(version_dir, "tik"), "wb")
                ticket_out.write(title.ticket.dump())
                ticket_out.close()
            except ValueError:
                # If libWiiPy returns an error, then no ticket is available. Log this, and disable options requiring a
                # ticket so that they aren't attempted later.
                progress_callback.emit("  - No Ticket is available!")
                pack_wad_enabled = False
                decrypt_contents_enabled = False
        # Load the content records from the TMD, and begin iterating over the records.
        title.load_content_records()
        content_list = []
        for content in range(len(title.tmd.content_records)):
            # Generate the correct file name by converting the content ID into hex, minus the 0x, and then appending
            # that to the end of 000000. I refuse to believe there isn't a better way to do this here and in libWiiPy.
            content_id_hex = hex(title.tmd.content_records[content].content_id)[2:]
            if len(content_id_hex) < 2:
                content_id_hex = "0" + content_id_hex
            content_file_name = "000000" + content_id_hex
            # Check for a local copy of the current content if "use local files" is enabled, and use it.
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
                # If keep encrypted contents is on, write out each content after its downloaded.
                if self.ui.keep_enc_chkbox.isChecked() is True:
                    content_id_hex = hex(title.tmd.content_records[content].content_id)[2:]
                    if len(content_id_hex) < 2:
                        content_id_hex = "0" + content_id_hex
                    content_file_name = "000000" + content_id_hex
                    enc_content_out = open(os.path.join(version_dir, content_file_name), "wb")
                    enc_content_out.write(content_list[content])
                    enc_content_out.close()
        title.content.content_list = content_list
        # If decrypt local contents is still true, decrypt each content and write out the decrypted file.
        if decrypt_contents_enabled is True:
            try:
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
            except ValueError:
                # If libWiiPy throws an error during decryption, return code -3. This should only be possible if using
                # local encrypted contents that have been altered at present.
                return -3
        # If pack WAD is still true, pack the TMD, ticket, and contents all into a WAD.
        if pack_wad_enabled is True:
            # Get the WAD certificate chain, courtesy of libWiiPy.
            progress_callback.emit(" - Building certificate...")
            title.wad.set_cert_data(libWiiPy.download_cert())
            # Use a typed WAD name if there is one, and auto generate one based on the TID and version if there isn't.
            progress_callback.emit("Packing WAD...")
            if self.ui.wad_file_entry.text() != "":
                wad_file_name = self.ui.wad_file_entry.text()
                if wad_file_name[-4:] != ".wad":
                    wad_file_name = wad_file_name + ".wad"
            else:
                wad_file_name = tid + "-v" + str(version) + ".wad"
            # Have libWiiPy dump the WAD, and write that data out.
            file = open(os.path.join(version_dir, wad_file_name), "wb")
            file.write(title.dump_wad())
            file.close()
        progress_callback.emit("Download complete!")
        # This is where the variables come in. If the state of these variables doesn't match the user's choice by this
        # point, it means that they enabled decryption or WAD packing for a title that doesn't have a ticket. Return
        # code 1 so that a warning popup is shown informing them of this.
        if ((not pack_wad_enabled and self.ui.pack_wad_chkbox.isChecked()) or
                (not decrypt_contents_enabled and self.ui.create_dec_chkbox.isChecked())):
            return 1
        return 0

    def pack_wad_chkbox_toggled(self):
        # Simple function to catch when the WAD checkbox is toggled and enable/disable the file name entry box
        # accordingly.
        if self.ui.pack_wad_chkbox.isChecked() is True:
            self.ui.wad_file_entry.setEnabled(True)
        else:
            self.ui.wad_file_entry.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Load the database file, this will work for both the raw Python file and compiled standalone/onefile binaries.
    database_file = open(os.path.join(os.path.dirname(__file__), "data/wii-database.json"))
    wii_database = json.load(database_file)
    # If this is a compiled build, the path needs to be obtained differently than if it isn't. The use of an absolute
    # path here is for compatibility with macOS .app bundles, which require the use of absolute paths.
    try:
        # noinspection PyUnresolvedReferences
        out_folder = os.path.join(__compiled__.containing_dir, "titles")
    except NameError:
        out_folder = os.path.join(os.path.dirname(sys.argv[0]), "titles")
    # Create the titles directory if it doesn't exist. In the future, this directory will probably be elsewhere.
    if not os.path.isdir(out_folder):
        os.mkdir(out_folder)

    window = MainWindow()
    window.setWindowTitle("NUSGet")
    window.show()

    sys.exit(app.exec())
