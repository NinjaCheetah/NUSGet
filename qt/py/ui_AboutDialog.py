# "qt/py/ui_AboutDialog.py", licensed under the MIT license
# Copyright 2024-2025 NinjaCheetah and Contributors
# Thanks Isla and Alex for making such a nice about dialog that I could then "borrow" :p

import os
import pathlib
import webbrowser

from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon

class AboutNUSGet(QDialog):
    def __init__(self, versions):
        super().__init__()
        self.setWindowTitle(self.tr("About NUSGet"))
        self.setFixedWidth(450)
        self.setFixedHeight(500)

        # Set background color to match main app
        self.setStyleSheet("""
        Credits {
            background-color: #222222;
            color: #ffffff;
        }
        QLabel {
            color: #ffffff;
        }
        QLabel[class="title"] {
            font-size: 20px;
            font-weight: bold;
            color: #ffffff;
        }
        QLabel[class="version"] {
            font-size: 13px;
            color: #aaaaaa;
        }
        QLabel[class="copyright"] {
            font-size: 12px;
            color: #888888;
        }
        QLabel[class="header"] {
            font-size: 14px;
            font-weight: bold;
            border-bottom: 1px solid #444444;
            padding-bottom: 4px;
            margin-top: 8px;
        }
        QPushButton {
            background-color: transparent;
            border: 1px solid rgba(70, 70, 70, 1);
            border-radius: 8px;
            padding: 8px 12px;
            margin: 4px 0px;
            font-size: 13px;
            font-weight: 500;
            color: #ffffff;
            text-align: center;
        }
        QPushButton:hover {
            background-color: rgba(60, 60, 60, 1);
            border-color: #4a86e8;
        }
        QPushButton:pressed {
            background-color: rgba(26, 115, 232, 0.15);
            border: 1px solid #1a73e8;
        }""")

        # Create main layout
        self.layout = QVBoxLayout()
        self.layout.setSpacing(4)
        self.layout.setContentsMargins(30, 20, 30, 20)

        # Logo
        logo_label = QLabel()
        icon = QIcon(str(pathlib.Path(os.path.dirname(__file__)).parents[1].joinpath("resources", "icon.png")))
        logo_pixmap = icon.pixmap(96, 96)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Title
        title_label = QLabel(self.tr("NUSGet"))
        title_label.setProperty("class", "title")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # NUSGet Version
        version_label = QLabel(self.tr("Version {nusget_version}").format(nusget_version=versions[0]))
        version_label.setProperty("class", "version")
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Library Versions
        libraries_label = QLabel(self.tr("Using libWiiPy {libwiipy_version} & libTWLPy {libtwlpy_version}")
                                         .format(libwiipy_version=versions[1], libtwlpy_version=versions[2]))
        libraries_label.setProperty("class", "version")
        libraries_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Copyright
        copyright_label = QLabel(self.tr("© 2024-2025 NinjaCheetah & Contributors"))
        copyright_label.setProperty("class", "copyright")
        copyright_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add header section
        self.layout.addWidget(logo_label)
        self.layout.addWidget(title_label)
        self.layout.addWidget(version_label)
        self.layout.addWidget(libraries_label)
        self.layout.addWidget(copyright_label)
        self.layout.addSpacing(15)

        # External links layout
        links_layout = QVBoxLayout()

        # GitHub button
        self.github_button = QPushButton(self.tr("View Project on GitHub"))
        self.github_button.clicked.connect(lambda: webbrowser.open("https://github.com/NinjaCheetah/NUSGet"))
        links_layout.addWidget(self.github_button)

        # Add the links layout to main layout
        self.layout.addLayout(links_layout)
        self.layout.addSpacing(15)

        # Add a horizontal line
        line = QLabel()
        line.setStyleSheet("background-color: #444444; height: 1px;")
        line.setFixedHeight(1)
        self.layout.addWidget(line)
        self.layout.addSpacing(10)

        # Team members header
        team_header = QLabel(self.tr("Translations"))
        team_header.setProperty("class", "header")
        self.layout.addWidget(team_header)
        self.layout.addSpacing(5)

        # Team members with roles
        self.people = {
            "rougets": QLabel(self.tr(
                "French (Français): <a href=https://github.com/rougets style='color: #4a86e8; text-decoration: none;'><b>rougets</b></a>")),
            "yeah-its-gloria": QLabel(self.tr(
                "German (Deutsch): <a href=https://github.com/yeah-its-gloria style='color: #4a86e8; text-decoration: none;'><b>yeah-its-gloria</b></a>")),
            "LNLenost": QLabel(self.tr(
                "Italian (Italiano): <a href=https://github.com/LNLenost style='color: #4a86e8; text-decoration: none;'><b>LNLenost</b></a>")),
            "DDinghoya": QLabel(self.tr(
                "Korean (\ud55c\uad6d\uc5b4): <a href=https://github.com/DDinghoya style='color: #4a86e8; text-decoration: none;'><b>DDinghoya</b></a>")),
            "rolfiee": QLabel(self.tr(
                "Norwegian (Norsk): <a href=https://github.com/rolfiee style='color: #4a86e8; text-decoration: none;'><b>rolfiee</b></a>")),
            "NotImplementedLife": QLabel(self.tr(
                "Romanian (Rom\u00e2n\u0103): <a href=https://github.com/NotImplementedLife style='color: #4a86e8; text-decoration: none;'><b>NotImplementedLife</b></a>")),
            "DarkMatterCore": QLabel(self.tr(
                "Spanish (Español): <a href=https://github.com/DarkMatterCore style='color: #4a86e8; text-decoration: none;'><b>DarkMatterCore</b></a>"))
        }

        # Add team members to layout
        for credit in self.people.values():
            credit.setOpenExternalLinks(True)
            credit.setContentsMargins(15, 0, 0, 0)
            self.layout.addWidget(credit)

        # Add spacer at the bottom
        self.layout.addStretch()

        self.setLayout(self.layout)
