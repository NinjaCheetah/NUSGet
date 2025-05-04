# "qt/py/ui_AboutDialog.py", licensed under the MIT license
# Copyright 2024-2025 NinjaCheetah and Contributors

from PySide6.QtWidgets import QDialog
from qt.py.ui_AboutNUSGet import Ui_AboutNUSGet

class AboutNUSGet(QDialog):
    def __init__(self, version_str):
        super().__init__()
        self.ui = Ui_AboutNUSGet()
        self.ui.setupUi(self)

        self.ui.version_lbl.setText(version_str)
