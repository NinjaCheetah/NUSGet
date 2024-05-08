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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTextBrowser, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1010, 625)
        MainWindow.setMinimumSize(QSize(1010, 625))
        MainWindow.setMaximumSize(QSize(1010, 625))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.vertical_layout_trees = QVBoxLayout()
        self.vertical_layout_trees.setObjectName(u"vertical_layout_trees")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)

        self.vertical_layout_trees.addWidget(self.label_2)

        self.platform_tabs = QTabWidget(self.centralwidget)
        self.platform_tabs.setObjectName(u"platform_tabs")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.platform_tabs.sizePolicy().hasHeightForWidth())
        self.platform_tabs.setSizePolicy(sizePolicy)
        self.platform_tabs.setMinimumSize(QSize(410, 0))
        self.platform_tabs.setMaximumSize(QSize(410, 16777215))
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
        self.dsi_tab = QWidget()
        self.dsi_tab.setObjectName(u"dsi_tab")
        self.verticalLayout = QVBoxLayout(self.dsi_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dsi_title_tree = QTreeWidget(self.dsi_tab)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.dsi_title_tree.setHeaderItem(__qtreewidgetitem2)
        self.dsi_title_tree.setObjectName(u"dsi_title_tree")
        self.dsi_title_tree.setHeaderHidden(True)
        self.dsi_title_tree.header().setMinimumSectionSize(49)
        self.dsi_title_tree.header().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.dsi_title_tree)

        self.platform_tabs.addTab(self.dsi_tab, "")

        self.vertical_layout_trees.addWidget(self.platform_tabs)


        self.horizontalLayout_3.addLayout(self.vertical_layout_trees)

        self.vertical_layout_controls = QVBoxLayout()
        self.vertical_layout_controls.setObjectName(u"vertical_layout_controls")
        self.vertical_layout_controls.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontal_layout_title_entry = QHBoxLayout()
        self.horizontal_layout_title_entry.setObjectName(u"horizontal_layout_title_entry")
        self.tid_entry = QLineEdit(self.centralwidget)
        self.tid_entry.setObjectName(u"tid_entry")

        self.horizontal_layout_title_entry.addWidget(self.tid_entry)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontal_layout_title_entry.addWidget(self.label)

        self.version_entry = QLineEdit(self.centralwidget)
        self.version_entry.setObjectName(u"version_entry")
        self.version_entry.setMaximumSize(QSize(85, 16777215))

        self.horizontal_layout_title_entry.addWidget(self.version_entry)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontal_layout_title_entry.addWidget(self.label_5)

        self.console_select_dropdown = QComboBox(self.centralwidget)
        self.console_select_dropdown.setObjectName(u"console_select_dropdown")
        self.console_select_dropdown.setMinimumSize(QSize(85, 0))
        self.console_select_dropdown.setEditable(False)

        self.horizontal_layout_title_entry.addWidget(self.console_select_dropdown)


        self.vertical_layout_controls.addLayout(self.horizontal_layout_title_entry)

        self.download_btn = QPushButton(self.centralwidget)
        self.download_btn.setObjectName(u"download_btn")

        self.vertical_layout_controls.addWidget(self.download_btn)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_7.addWidget(self.label_3)

        self.pack_archive_chkbox = QCheckBox(self.centralwidget)
        self.pack_archive_chkbox.setObjectName(u"pack_archive_chkbox")

        self.verticalLayout_7.addWidget(self.pack_archive_chkbox)

        self.archive_file_entry = QLineEdit(self.centralwidget)
        self.archive_file_entry.setObjectName(u"archive_file_entry")
        self.archive_file_entry.setEnabled(False)

        self.verticalLayout_7.addWidget(self.archive_file_entry)

        self.keep_enc_chkbox = QCheckBox(self.centralwidget)
        self.keep_enc_chkbox.setObjectName(u"keep_enc_chkbox")
        self.keep_enc_chkbox.setChecked(True)

        self.verticalLayout_7.addWidget(self.keep_enc_chkbox)

        self.create_dec_chkbox = QCheckBox(self.centralwidget)
        self.create_dec_chkbox.setObjectName(u"create_dec_chkbox")

        self.verticalLayout_7.addWidget(self.create_dec_chkbox)

        self.use_local_chkbox = QCheckBox(self.centralwidget)
        self.use_local_chkbox.setObjectName(u"use_local_chkbox")
        self.use_local_chkbox.setEnabled(True)

        self.verticalLayout_7.addWidget(self.use_local_chkbox)

        self.use_wiiu_nus_chkbox = QCheckBox(self.centralwidget)
        self.use_wiiu_nus_chkbox.setObjectName(u"use_wiiu_nus_chkbox")
        self.use_wiiu_nus_chkbox.setChecked(True)

        self.verticalLayout_7.addWidget(self.use_wiiu_nus_chkbox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_8.addWidget(self.label_4)

        self.pack_vwii_mode_chkbox = QCheckBox(self.centralwidget)
        self.pack_vwii_mode_chkbox.setObjectName(u"pack_vwii_mode_chkbox")
        self.pack_vwii_mode_chkbox.setEnabled(False)

        self.verticalLayout_8.addWidget(self.pack_vwii_mode_chkbox)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)


        self.vertical_layout_controls.addLayout(self.horizontalLayout_5)

        self.log_text_browser = QTextBrowser(self.centralwidget)
        self.log_text_browser.setObjectName(u"log_text_browser")
        self.log_text_browser.setMinimumSize(QSize(0, 312))

        self.vertical_layout_controls.addWidget(self.log_text_browser)


        self.horizontalLayout_3.addLayout(self.vertical_layout_controls)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1010, 29))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.platform_tabs.setCurrentIndex(0)
        self.console_select_dropdown.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Available Titles", None))
        self.platform_tabs.setTabText(self.platform_tabs.indexOf(self.wii_tab), QCoreApplication.translate("MainWindow", u"Wii", None))
        self.platform_tabs.setTabText(self.platform_tabs.indexOf(self.vwii_tab), QCoreApplication.translate("MainWindow", u"vWii", None))
        self.platform_tabs.setTabText(self.platform_tabs.indexOf(self.dsi_tab), QCoreApplication.translate("MainWindow", u"DSi", None))
        self.tid_entry.setText("")
        self.tid_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title ID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.version_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Console:", None))
        self.console_select_dropdown.setCurrentText("")
        self.download_btn.setText(QCoreApplication.translate("MainWindow", u"Start Download", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"General Settings", None))
        self.pack_archive_chkbox.setText(QCoreApplication.translate("MainWindow", u"Pack installable archive (WAD/TAD)", None))
        self.archive_file_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.keep_enc_chkbox.setText(QCoreApplication.translate("MainWindow", u"Keep encrypted contents", None))
        self.create_dec_chkbox.setText(QCoreApplication.translate("MainWindow", u"Create decrypted contents (*.app)", None))
        self.use_local_chkbox.setText(QCoreApplication.translate("MainWindow", u"Use local files, if they exist", None))
        self.use_wiiu_nus_chkbox.setText(QCoreApplication.translate("MainWindow", u"Use the Wii U NUS (faster, only effects Wii/vWii)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"vWii Title Settings", None))
        self.pack_vwii_mode_chkbox.setText(QCoreApplication.translate("MainWindow", u"Pack for vWii mode instead of Wii U mode", None))
        self.log_text_browser.setMarkdown("")
        self.log_text_browser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

