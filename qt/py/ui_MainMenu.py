# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
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
        self.vertical_layout_controls.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.download_btn = QPushButton(self.centralwidget)
        self.download_btn.setObjectName(u"download_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.download_btn.sizePolicy().hasHeightForWidth())
        self.download_btn.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.download_btn)

        self.script_btn = QPushButton(self.centralwidget)
        self.script_btn.setObjectName(u"script_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.script_btn.sizePolicy().hasHeightForWidth())
        self.script_btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.script_btn)


        self.vertical_layout_controls.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_7.addWidget(self.label_3)

        self.pack_archive_row = QHBoxLayout()
        self.pack_archive_row.setSpacing(10)
        self.pack_archive_row.setObjectName(u"pack_archive_row")
        self.pack_archive_chkbox = QCheckBox(self.centralwidget)
        self.pack_archive_chkbox.setObjectName(u"pack_archive_chkbox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pack_archive_chkbox.sizePolicy().hasHeightForWidth())
        self.pack_archive_chkbox.setSizePolicy(sizePolicy3)
        self.pack_archive_chkbox.setText(u"")

        self.pack_archive_row.addWidget(self.pack_archive_chkbox)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setWordWrap(True)

        self.pack_archive_row.addWidget(self.label_7)


        self.verticalLayout_7.addLayout(self.pack_archive_row)

        self.archive_file_entry = QLineEdit(self.centralwidget)
        self.archive_file_entry.setObjectName(u"archive_file_entry")
        self.archive_file_entry.setEnabled(False)

        self.verticalLayout_7.addWidget(self.archive_file_entry)

        self.keep_enc_row = QHBoxLayout()
        self.keep_enc_row.setSpacing(10)
        self.keep_enc_row.setObjectName(u"keep_enc_row")
        self.keep_enc_chkbox = QCheckBox(self.centralwidget)
        self.keep_enc_chkbox.setObjectName(u"keep_enc_chkbox")
        sizePolicy3.setHeightForWidth(self.keep_enc_chkbox.sizePolicy().hasHeightForWidth())
        self.keep_enc_chkbox.setSizePolicy(sizePolicy3)
        self.keep_enc_chkbox.setText(u"")
        self.keep_enc_chkbox.setChecked(True)

        self.keep_enc_row.addWidget(self.keep_enc_chkbox)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setWordWrap(True)

        self.keep_enc_row.addWidget(self.label_6)


        self.verticalLayout_7.addLayout(self.keep_enc_row)

        self.create_dec_row = QHBoxLayout()
        self.create_dec_row.setSpacing(10)
        self.create_dec_row.setObjectName(u"create_dec_row")
        self.create_dec_chkbox = QCheckBox(self.centralwidget)
        self.create_dec_chkbox.setObjectName(u"create_dec_chkbox")
        sizePolicy3.setHeightForWidth(self.create_dec_chkbox.sizePolicy().hasHeightForWidth())
        self.create_dec_chkbox.setSizePolicy(sizePolicy3)
        self.create_dec_chkbox.setText(u"")

        self.create_dec_row.addWidget(self.create_dec_chkbox)

        self.create_dec_chkbox_lbl = QLabel(self.centralwidget)
        self.create_dec_chkbox_lbl.setObjectName(u"create_dec_chkbox_lbl")
        sizePolicy4.setHeightForWidth(self.create_dec_chkbox_lbl.sizePolicy().hasHeightForWidth())
        self.create_dec_chkbox_lbl.setSizePolicy(sizePolicy4)
        self.create_dec_chkbox_lbl.setWordWrap(True)

        self.create_dec_row.addWidget(self.create_dec_chkbox_lbl)


        self.verticalLayout_7.addLayout(self.create_dec_row)

        self.use_local_row = QHBoxLayout()
        self.use_local_row.setSpacing(10)
        self.use_local_row.setObjectName(u"use_local_row")
        self.use_local_chkbox = QCheckBox(self.centralwidget)
        self.use_local_chkbox.setObjectName(u"use_local_chkbox")
        self.use_local_chkbox.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.use_local_chkbox.sizePolicy().hasHeightForWidth())
        self.use_local_chkbox.setSizePolicy(sizePolicy3)
        self.use_local_chkbox.setText(u"")

        self.use_local_row.addWidget(self.use_local_chkbox)

        self.use_local_chkbox_lbl = QLabel(self.centralwidget)
        self.use_local_chkbox_lbl.setObjectName(u"use_local_chkbox_lbl")
        sizePolicy4.setHeightForWidth(self.use_local_chkbox_lbl.sizePolicy().hasHeightForWidth())
        self.use_local_chkbox_lbl.setSizePolicy(sizePolicy4)
        self.use_local_chkbox_lbl.setWordWrap(True)

        self.use_local_row.addWidget(self.use_local_chkbox_lbl)


        self.verticalLayout_7.addLayout(self.use_local_row)

        self.use_wiiu_nus_row = QHBoxLayout()
        self.use_wiiu_nus_row.setSpacing(10)
        self.use_wiiu_nus_row.setObjectName(u"use_wiiu_nus_row")
        self.use_wiiu_nus_row.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.use_wiiu_nus_chkbox = QCheckBox(self.centralwidget)
        self.use_wiiu_nus_chkbox.setObjectName(u"use_wiiu_nus_chkbox")
        sizePolicy.setHeightForWidth(self.use_wiiu_nus_chkbox.sizePolicy().hasHeightForWidth())
        self.use_wiiu_nus_chkbox.setSizePolicy(sizePolicy)
        self.use_wiiu_nus_chkbox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.use_wiiu_nus_chkbox.setText(u"")
        self.use_wiiu_nus_chkbox.setChecked(True)

        self.use_wiiu_nus_row.addWidget(self.use_wiiu_nus_chkbox)

        self.use_wiiu_nus_chkbox_lbl = QLabel(self.centralwidget)
        self.use_wiiu_nus_chkbox_lbl.setObjectName(u"use_wiiu_nus_chkbox_lbl")
        sizePolicy4.setHeightForWidth(self.use_wiiu_nus_chkbox_lbl.sizePolicy().hasHeightForWidth())
        self.use_wiiu_nus_chkbox_lbl.setSizePolicy(sizePolicy4)
        self.use_wiiu_nus_chkbox_lbl.setWordWrap(True)

        self.use_wiiu_nus_row.addWidget(self.use_wiiu_nus_chkbox_lbl)


        self.verticalLayout_7.addLayout(self.use_wiiu_nus_row)

        self.patch_ios_row = QHBoxLayout()
        self.patch_ios_row.setSpacing(10)
        self.patch_ios_row.setObjectName(u"patch_ios_row")
        self.patch_ios_chkbox = QCheckBox(self.centralwidget)
        self.patch_ios_chkbox.setObjectName(u"patch_ios_chkbox")
        self.patch_ios_chkbox.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.patch_ios_chkbox.sizePolicy().hasHeightForWidth())
        self.patch_ios_chkbox.setSizePolicy(sizePolicy3)
        self.patch_ios_chkbox.setText(u"")

        self.patch_ios_row.addWidget(self.patch_ios_chkbox)

        self.patch_ios_lbl = QLabel(self.centralwidget)
        self.patch_ios_lbl.setObjectName(u"patch_ios_lbl")
        self.patch_ios_lbl.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.patch_ios_lbl.sizePolicy().hasHeightForWidth())
        self.patch_ios_lbl.setSizePolicy(sizePolicy4)
        self.patch_ios_lbl.setWordWrap(True)

        self.patch_ios_row.addWidget(self.patch_ios_lbl)


        self.verticalLayout_7.addLayout(self.patch_ios_row)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.horizontalSpacer)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_8.addWidget(self.label_4)

        self.pack_vwii_mode_row = QHBoxLayout()
        self.pack_vwii_mode_row.setObjectName(u"pack_vwii_mode_row")
        self.pack_vwii_mode_chkbox = QCheckBox(self.centralwidget)
        self.pack_vwii_mode_chkbox.setObjectName(u"pack_vwii_mode_chkbox")
        self.pack_vwii_mode_chkbox.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.pack_vwii_mode_chkbox.sizePolicy().hasHeightForWidth())
        self.pack_vwii_mode_chkbox.setSizePolicy(sizePolicy3)
        self.pack_vwii_mode_chkbox.setText(u"")

        self.pack_vwii_mode_row.addWidget(self.pack_vwii_mode_chkbox)

        self.pack_vwii_mode_lbl = QLabel(self.centralwidget)
        self.pack_vwii_mode_lbl.setObjectName(u"pack_vwii_mode_lbl")
        self.pack_vwii_mode_lbl.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pack_vwii_mode_lbl.sizePolicy().hasHeightForWidth())
        self.pack_vwii_mode_lbl.setSizePolicy(sizePolicy5)
        self.pack_vwii_mode_lbl.setWordWrap(True)

        self.pack_vwii_mode_row.addWidget(self.pack_vwii_mode_lbl)


        self.verticalLayout_8.addLayout(self.pack_vwii_mode_row)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)


        self.vertical_layout_controls.addLayout(self.horizontalLayout_5)

        self.log_text_browser = QTextBrowser(self.centralwidget)
        self.log_text_browser.setObjectName(u"log_text_browser")
        self.log_text_browser.setMinimumSize(QSize(0, 247))

        self.vertical_layout_controls.addWidget(self.log_text_browser)


        self.horizontalLayout_3.addLayout(self.vertical_layout_controls)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1010, 30))
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
        self.script_btn.setText(QCoreApplication.translate("MainWindow", u"Run Script", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"General Settings", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Pack installable archive (WAD/TAD)", None))
        self.archive_file_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Keep encrypted contents", None))
        self.create_dec_chkbox_lbl.setText(QCoreApplication.translate("MainWindow", u"Create decrypted contents (*.app)", None))
        self.use_local_chkbox_lbl.setText(QCoreApplication.translate("MainWindow", u"Use local files, if they exist", None))
        self.use_wiiu_nus_chkbox_lbl.setText(QCoreApplication.translate("MainWindow", u"Use the Wii U NUS (faster, only effects Wii/vWii)", None))
        self.patch_ios_lbl.setText(QCoreApplication.translate("MainWindow", u"Apply patches to IOS (Applies to WADs only)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"vWii Title Settings", None))
        self.pack_vwii_mode_lbl.setText(QCoreApplication.translate("MainWindow", u"Re-encrypt title using the Wii Common Key", None))
        self.log_text_browser.setMarkdown("")
        self.log_text_browser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p></body></html>", None))
    # retranslateUi

