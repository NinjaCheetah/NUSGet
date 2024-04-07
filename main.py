import sys
import os
import libWiiPy

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QThread, Signal, Qt

from qt.py.ui_MainMenu import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.download_btn.clicked.connect(self.download_btn_pressed)

    def download_btn_pressed(self):
        title = libWiiPy.Title()

        tid = self.ui.tid_entry.text()
        version = int(self.ui.version_entry.text())

        title = libWiiPy.download_title(tid, version)

        file = open(tid + "-v" + str(version) + ".wad", "wb")
        file.write(title.dump_wad())
        file.close()
        self.ui.textBrowser.setMarkdown("## Done!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('breeze')

    window = MainWindow()
    window.setWindowTitle("NUSD-Py")
    window.show()

    sys.exit(app.exec())
