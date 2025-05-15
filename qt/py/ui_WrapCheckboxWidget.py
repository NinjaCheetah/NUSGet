from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCheckBox, QHBoxLayout, QLabel, QWidget, QSizePolicy, QLayout

class WrapCheckboxWidget(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        self.checkbox = QCheckBox("")
        size_policy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.checkbox.sizePolicy().hasHeightForWidth())
        self.checkbox.setSizePolicy(size_policy)

        self.label = QLabel(text)
        self.label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label.setWordWrap(True)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.label.setContentsMargins(0, 0, 0, 0)

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
