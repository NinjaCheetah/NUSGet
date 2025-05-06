from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QCheckBox, QHBoxLayout, QLabel, QWidget, QSizePolicy, QLayout

class WrapCheckboxWidget(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)

        self.checkbox = QCheckBox("")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkbox.sizePolicy().hasHeightForWidth())
        self.checkbox.setSizePolicy(sizePolicy1)

        self.label = QLabel(text)
        self.label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label.setWordWrap(True)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSizeConstraint(QLayout.SetMinimumSize)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.label)

        # Connect signals so that clicking the label still changes the state of the checkbox.
        def toggle_checkbox(event):
            if self.checkbox.isEnabled() and event.button() == Qt.LeftButton:
                self.checkbox.toggle()
        self.label.mousePressEvent = toggle_checkbox

        # Bind checkbox stuff for easier access.
        self.toggled = self.checkbox.toggled

    def isChecked(self):
        return self.checkbox.isChecked()

    def setChecked(self, checked):
        self.checkbox.setChecked(checked)

    def setEnabled(self, enabled):
        super().setEnabled(enabled)
        self.checkbox.setEnabled(enabled)
        self.label.setEnabled(enabled)
