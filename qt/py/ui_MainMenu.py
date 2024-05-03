# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QTabWidget, QTextBrowser,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 625)
        MainWindow.setMinimumSize(QSize(610, 625))
        MainWindow.setMaximumSize(QSize(610, 625))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.platform_tabs = QTabWidget(self.centralwidget)
        self.platform_tabs.setObjectName(u"platform_tabs")
        self.wii_tab = QWidget()
        self.wii_tab.setObjectName(u"wii_tab")
        self.verticalLayout_2 = QVBoxLayout(self.wii_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.wii_title_tree = QTreeWidget(self.wii_tab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.wii_title_tree.setHeaderItem(__qtreewidgetitem)
        self.wii_title_tree.setObjectName(u"wii_title_tree")
        self.wii_title_tree.setColumnCount(1)
        self.wii_title_tree.header().setVisible(False)
        self.wii_title_tree.header().setMinimumSectionSize(49)
        self.wii_title_tree.header().setDefaultSectionSize(100)
        self.wii_title_tree.header().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.wii_title_tree)

        self.platform_tabs.addTab(self.wii_tab, "")
        self.vwii_tab = QWidget()
        self.vwii_tab.setObjectName(u"vwii_tab")
        self.verticalLayout_4 = QVBoxLayout(self.vwii_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.vwii_title_tree = QTreeWidget(self.vwii_tab)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.vwii_title_tree.setHeaderItem(__qtreewidgetitem1)
        self.vwii_title_tree.setObjectName(u"vwii_title_tree")
        self.vwii_title_tree.setColumnCount(1)
        self.vwii_title_tree.header().setVisible(False)
        self.vwii_title_tree.header().setMinimumSectionSize(49)
        self.vwii_title_tree.header().setDefaultSectionSize(100)
        self.vwii_title_tree.header().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.vwii_title_tree)

        self.platform_tabs.addTab(self.vwii_tab, "")

        self.verticalLayout.addWidget(self.platform_tabs)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tid_entry = QLineEdit(self.centralwidget)
        self.tid_entry.setObjectName(u"tid_entry")

        self.horizontalLayout_2.addWidget(self.tid_entry)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.version_entry = QLineEdit(self.centralwidget)
        self.version_entry.setObjectName(u"version_entry")
        self.version_entry.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_2.addWidget(self.version_entry)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.download_btn = QPushButton(self.centralwidget)
        self.download_btn.setObjectName(u"download_btn")

        self.verticalLayout_3.addWidget(self.download_btn)

        self.log_text_browser = QTextBrowser(self.centralwidget)
        self.log_text_browser.setObjectName(u"log_text_browser")

        self.verticalLayout_3.addWidget(self.log_text_browser)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pack_wad_chkbox = QCheckBox(self.centralwidget)
        self.pack_wad_chkbox.setObjectName(u"pack_wad_chkbox")

        self.horizontalLayout_4.addWidget(self.pack_wad_chkbox)

        self.wad_file_entry = QLineEdit(self.centralwidget)
        self.wad_file_entry.setObjectName(u"wad_file_entry")
        self.wad_file_entry.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.wad_file_entry)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.keep_enc_chkbox = QCheckBox(self.centralwidget)
        self.keep_enc_chkbox.setObjectName(u"keep_enc_chkbox")
        self.keep_enc_chkbox.setChecked(True)

        self.verticalLayout_3.addWidget(self.keep_enc_chkbox)

        self.create_dec_chkbox = QCheckBox(self.centralwidget)
        self.create_dec_chkbox.setObjectName(u"create_dec_chkbox")

        self.verticalLayout_3.addWidget(self.create_dec_chkbox)

        self.use_local_chkbox = QCheckBox(self.centralwidget)
        self.use_local_chkbox.setObjectName(u"use_local_chkbox")
        self.use_local_chkbox.setEnabled(True)

        self.verticalLayout_3.addWidget(self.use_local_chkbox)

        self.use_wiiu_nus_chkbox = QCheckBox(self.centralwidget)
        self.use_wiiu_nus_chkbox.setObjectName(u"use_wiiu_nus_chkbox")
        self.use_wiiu_nus_chkbox.setChecked(True)

        self.verticalLayout_3.addWidget(self.use_wiiu_nus_chkbox)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 610, 30))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.platform_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Available Titles", None))
        self.platform_tabs.setTabText(self.platform_tabs.indexOf(self.wii_tab), QCoreApplication.translate("MainWindow", u"Wii", None))
        self.platform_tabs.setTabText(self.platform_tabs.indexOf(self.vwii_tab), QCoreApplication.translate("MainWindow", u"vWii", None))
        self.tid_entry.setText("")
        self.tid_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title ID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.version_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.download_btn.setText(QCoreApplication.translate("MainWindow", u"Start NUS Download!", None))
        self.log_text_browser.setMarkdown("")
        self.log_text_browser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p></body></html>", None))
        self.pack_wad_chkbox.setText(QCoreApplication.translate("MainWindow", u"Pack WAD", None))
        self.wad_file_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.keep_enc_chkbox.setText(QCoreApplication.translate("MainWindow", u"Keep encrypted contents", None))
        self.create_dec_chkbox.setText(QCoreApplication.translate("MainWindow", u"Create decrypted contents (*.app)", None))
        self.use_local_chkbox.setText(QCoreApplication.translate("MainWindow", u"Use local files, if they exist", None))
        self.use_wiiu_nus_chkbox.setText(QCoreApplication.translate("MainWindow", u"Use the Wii U NUS (faster)", None))
    # retranslateUi

