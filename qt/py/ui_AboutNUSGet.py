# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutNUSGet.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLayout, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_AboutNUSGet(object):
    def setupUi(self, AboutNUSGet):
        if not AboutNUSGet.objectName():
            AboutNUSGet.setObjectName(u"AboutNUSGet")
        AboutNUSGet.resize(400, 300)
        self.verticalLayout = QVBoxLayout(AboutNUSGet)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.outer_layout = QHBoxLayout()
        self.outer_layout.setObjectName(u"outer_layout")
        self.icon_layout = QVBoxLayout()
        self.icon_layout.setObjectName(u"icon_layout")
        self.icon_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.icon_lbl = QLabel(AboutNUSGet)
        icon = QIcon("resources/icon.png")
        pixmap = icon.pixmap(QSize(75, 75))
        self.icon_lbl.setPixmap(pixmap)
        self.icon_lbl.setObjectName(u"icon_lbl")
        self.icon_lbl.setMaximumSize(QSize(75, 75))

        self.icon_layout.addWidget(self.icon_lbl)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.icon_layout.addItem(self.verticalSpacer)


        self.outer_layout.addLayout(self.icon_layout)

        self.details_layout = QVBoxLayout()
        self.details_layout.setObjectName(u"details_layout")
        self.about_title_lbl = QLabel(AboutNUSGet)
        self.about_title_lbl.setObjectName(u"about_title_lbl")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.about_title_lbl.setFont(font)

        self.details_layout.addWidget(self.about_title_lbl)

        self.version_lbl = QLabel(AboutNUSGet)
        self.version_lbl.setObjectName(u"version_lbl")
        font1 = QFont()
        font1.setBold(True)
        self.version_lbl.setFont(font1)

        self.details_layout.addWidget(self.version_lbl)

        self.detail_text_lbl = QLabel(AboutNUSGet)
        self.detail_text_lbl.setObjectName(u"detail_text_lbl")
        self.detail_text_lbl.setWordWrap(True)

        self.details_layout.addWidget(self.detail_text_lbl)

        self.textBrowser = QTextBrowser(AboutNUSGet)
        self.textBrowser.setObjectName(u"textBrowser")

        self.details_layout.addWidget(self.textBrowser)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.details_layout.addItem(self.verticalSpacer_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.details_layout.addItem(self.horizontalSpacer)


        self.outer_layout.addLayout(self.details_layout)


        self.verticalLayout.addLayout(self.outer_layout)

        self.buttonBox = QDialogButtonBox(AboutNUSGet)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AboutNUSGet)
        self.buttonBox.accepted.connect(AboutNUSGet.accept)
        self.buttonBox.rejected.connect(AboutNUSGet.reject)

        QMetaObject.connectSlotsByName(AboutNUSGet)
    # setupUi

    def retranslateUi(self, AboutNUSGet):
        AboutNUSGet.setWindowTitle(QCoreApplication.translate("AboutNUSGet", u"Dialog", None))
        self.icon_lbl.setText("")
        self.about_title_lbl.setText(QCoreApplication.translate("AboutNUSGet", u"About NUSGet", None))
        self.version_lbl.setText(QCoreApplication.translate("AboutNUSGet", u"Placeholder Version String", None))
        self.detail_text_lbl.setText(QCoreApplication.translate("AboutNUSGet", u"Copyright (c) 2024-2025 NinjaCheetah & Contributors", None))
        self.textBrowser.setHtml(QCoreApplication.translate("AboutNUSGet", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Translations</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">German (Deutsch): <a href=\"https://github.com/yeah-its-gloria\"><span style=\" text-decoration: underline; color:#3586ff;\">yeah-its-gloria</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; mar"
                        "gin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Italian (Italiano): <a href=\"https://github.com/LNLenost\"><span style=\" text-decoration: underline; color:#3586ff;\">LNLenost</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Korean (\ud55c\uad6d\uc5b4): <a href=\"https://github.com/DDinghoya\"><span style=\" text-decoration: underline; color:#3586ff;\">DDinghoya</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Norwegian (Norsk): <a href=\"https://github.com/rolfiee\"><span style=\" text-decoration: underline; color:#3586ff;\">rolfiee</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Romanian (Rom\u00e2n\u0103): <a href=\"https://github.com/NotImplementedLife\"><span style=\" text-decoration: underline; color:#3586ff;\">"
                        "NotImplementedLife</span></a></p></body></html>", None))
    # retranslateUi

