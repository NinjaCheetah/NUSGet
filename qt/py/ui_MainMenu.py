# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextBrowser,
    QTreeView, QVBoxLayout, QWidget)

from qt.py.ui_WrapCheckboxWidget import WrapCheckboxWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1010, 675)
        MainWindow.setMinimumSize(QSize(1010, 675))
        MainWindow.setMaximumSize(QSize(1010, 675))
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.action_about.setIcon(icon)
        self.action_about.setMenuRole(QAction.MenuRole.ApplicationSpecificRole)
        self.action_about_qt = QAction(MainWindow)
        self.action_about_qt.setObjectName(u"action_about_qt")
        self.action_about_qt.setIcon(icon)
        self.action_about_qt.setMenuRole(QAction.MenuRole.ApplicationSpecificRole)
        self.action_language_system = QAction(MainWindow)
        self.action_language_system.setObjectName(u"action_language_system")
        self.action_language_system.setCheckable(True)
        self.action_language_system.setChecked(False)
        self.action_language_english = QAction(MainWindow)
        self.action_language_english.setObjectName(u"action_language_english")
        self.action_language_english.setCheckable(True)
        self.action_language_spanish = QAction(MainWindow)
        self.action_language_spanish.setObjectName(u"action_language_spanish")
        self.action_language_spanish.setCheckable(True)
        self.action_language_german = QAction(MainWindow)
        self.action_language_german.setObjectName(u"action_language_german")
        self.action_language_german.setCheckable(True)
        self.action_language_french = QAction(MainWindow)
        self.action_language_french.setObjectName(u"action_language_french")
        self.action_language_french.setCheckable(True)
        self.action_language_italian = QAction(MainWindow)
        self.action_language_italian.setObjectName(u"action_language_italian")
        self.action_language_italian.setCheckable(True)
        self.action_language_norwegian = QAction(MainWindow)
        self.action_language_norwegian.setObjectName(u"action_language_norwegian")
        self.action_language_norwegian.setCheckable(True)
        self.action_language_romanian = QAction(MainWindow)
        self.action_language_romanian.setObjectName(u"action_language_romanian")
        self.action_language_romanian.setCheckable(True)
        self.action_language_korean = QAction(MainWindow)
        self.action_language_korean.setObjectName(u"action_language_korean")
        self.action_language_korean.setCheckable(True)
        self.action_theme_system = QAction(MainWindow)
        self.action_theme_system.setObjectName(u"action_theme_system")
        self.action_theme_system.setCheckable(True)
        self.action_theme_light = QAction(MainWindow)
        self.action_theme_light.setObjectName(u"action_theme_light")
        self.action_theme_light.setCheckable(True)
        self.action_theme_dark = QAction(MainWindow)
        self.action_theme_dark.setObjectName(u"action_theme_dark")
        self.action_theme_dark.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.vertical_layout_trees = QVBoxLayout()
        self.vertical_layout_trees.setObjectName(u"vertical_layout_trees")
        self.tree_filter_layout = QHBoxLayout()
        self.tree_filter_layout.setObjectName(u"tree_filter_layout")
        self.tree_filter_input = QLineEdit(self.centralwidget)
        self.tree_filter_input.setObjectName(u"tree_filter_input")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_filter_input.sizePolicy().hasHeightForWidth())
        self.tree_filter_input.setSizePolicy(sizePolicy)

        self.tree_filter_layout.addWidget(self.tree_filter_input)

        self.tree_filter_reset_btn = QPushButton(self.centralwidget)
        self.tree_filter_reset_btn.setObjectName(u"tree_filter_reset_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tree_filter_reset_btn.sizePolicy().hasHeightForWidth())
        self.tree_filter_reset_btn.setSizePolicy(sizePolicy1)

        self.tree_filter_layout.addWidget(self.tree_filter_reset_btn)


        self.vertical_layout_trees.addLayout(self.tree_filter_layout)

        self.platform_tabs = QTabWidget(self.centralwidget)
        self.platform_tabs.setObjectName(u"platform_tabs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.platform_tabs.sizePolicy().hasHeightForWidth())
        self.platform_tabs.setSizePolicy(sizePolicy2)
        self.platform_tabs.setMinimumSize(QSize(410, 0))
        self.platform_tabs.setMaximumSize(QSize(410, 16777215))
        self.wii_tab = QWidget()
        self.wii_tab.setObjectName(u"wii_tab")
        self.verticalLayout_2 = QVBoxLayout(self.wii_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.wii_title_tree = QTreeView(self.wii_tab)
        self.wii_title_tree.setObjectName(u"wii_title_tree")

        self.verticalLayout_2.addWidget(self.wii_title_tree)

        self.platform_tabs.addTab(self.wii_tab, "")
        self.vwii_tab = QWidget()
        self.vwii_tab.setObjectName(u"vwii_tab")
        self.verticalLayout_4 = QVBoxLayout(self.vwii_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.vwii_title_tree = QTreeView(self.vwii_tab)
        self.vwii_title_tree.setObjectName(u"vwii_title_tree")

        self.verticalLayout_4.addWidget(self.vwii_title_tree)

        self.platform_tabs.addTab(self.vwii_tab, "")
        self.dsi_tab = QWidget()
        self.dsi_tab.setObjectName(u"dsi_tab")
        self.verticalLayout = QVBoxLayout(self.dsi_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dsi_title_tree = QTreeView(self.dsi_tab)
        self.dsi_title_tree.setObjectName(u"dsi_title_tree")

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.download_btn.sizePolicy().hasHeightForWidth())
        self.download_btn.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.download_btn)

        self.script_btn = QPushButton(self.centralwidget)
        self.script_btn.setObjectName(u"script_btn")
        sizePolicy.setHeightForWidth(self.script_btn.sizePolicy().hasHeightForWidth())
        self.script_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.script_btn)


        self.vertical_layout_controls.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)

        self.verticalLayout_7.addWidget(self.label_3)

        self.pack_archive_checkbox = WrapCheckboxWidget(self.centralwidget)
        self.pack_archive_checkbox.setObjectName(u"pack_archive_checkbox")

        self.verticalLayout_7.addWidget(self.pack_archive_checkbox)

        self.archive_file_entry = QLineEdit(self.centralwidget)
        self.archive_file_entry.setObjectName(u"archive_file_entry")
        self.archive_file_entry.setEnabled(True)

        self.verticalLayout_7.addWidget(self.archive_file_entry)

        self.keep_enc_checkbox = WrapCheckboxWidget(self.centralwidget)
        self.keep_enc_checkbox.setObjectName(u"keep_enc_checkbox")

        self.verticalLayout_7.addWidget(self.keep_enc_checkbox)

        self.create_dec_checkbox = WrapCheckboxWidget(self.centralwidget)
        self.create_dec_checkbox.setObjectName(u"create_dec_checkbox")

        self.verticalLayout_7.addWidget(self.create_dec_checkbox)

        self.use_local_checkbox = WrapCheckboxWidget(self.centralwidget)
        self.use_local_checkbox.setObjectName(u"use_local_checkbox")

        self.verticalLayout_7.addWidget(self.use_local_checkbox)

        self.use_wiiu_nus_checkbox = WrapCheckboxWidget(self.centralwidget)
        self.use_wiiu_nus_checkbox.setObjectName(u"use_wiiu_nus_checkbox")

        self.verticalLayout_7.addWidget(self.use_wiiu_nus_checkbox)

        self.patch_ios_checkbox = WrapCheckboxWidget(self.centralwidget)
        self.patch_ios_checkbox.setObjectName(u"patch_ios_checkbox")
        self.patch_ios_checkbox.setEnabled(False)

        self.verticalLayout_7.addWidget(self.patch_ios_checkbox)

        self.verticalSpacer_2 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.horizontalSpacer = QSpacerItem(300, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.horizontalSpacer)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_8.addWidget(self.label_4)

        self.pack_vwii_mode_checkbox = WrapCheckboxWidget(self.centralwidget)
        self.pack_vwii_mode_checkbox.setObjectName(u"pack_vwii_mode_checkbox")
        self.pack_vwii_mode_checkbox.setEnabled(False)

        self.verticalLayout_8.addWidget(self.pack_vwii_mode_checkbox)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_8.addWidget(self.label_2)

        self.auto_update_checkbox = WrapCheckboxWidget(self.centralwidget)
        self.auto_update_checkbox.setObjectName(u"auto_update_checkbox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.auto_update_checkbox.sizePolicy().hasHeightForWidth())
        self.auto_update_checkbox.setSizePolicy(sizePolicy4)

        self.verticalLayout_8.addWidget(self.auto_update_checkbox)

        self.custom_out_dir_checkbox = WrapCheckboxWidget(self.centralwidget)
        self.custom_out_dir_checkbox.setObjectName(u"custom_out_dir_checkbox")

        self.verticalLayout_8.addWidget(self.custom_out_dir_checkbox)

        self.custom_out_dir_entry_row = QHBoxLayout()
        self.custom_out_dir_entry_row.setObjectName(u"custom_out_dir_entry_row")
        self.custom_out_dir_entry = QLineEdit(self.centralwidget)
        self.custom_out_dir_entry.setObjectName(u"custom_out_dir_entry")
        self.custom_out_dir_entry.setEnabled(False)

        self.custom_out_dir_entry_row.addWidget(self.custom_out_dir_entry)

        self.custom_out_dir_btn = QPushButton(self.centralwidget)
        self.custom_out_dir_btn.setObjectName(u"custom_out_dir_btn")
        self.custom_out_dir_btn.setEnabled(False)

        self.custom_out_dir_entry_row.addWidget(self.custom_out_dir_btn)


        self.verticalLayout_8.addLayout(self.custom_out_dir_entry_row)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(300, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)


        self.vertical_layout_controls.addLayout(self.horizontalLayout_5)

        self.log_text_browser = QTextBrowser(self.centralwidget)
        self.log_text_browser.setObjectName(u"log_text_browser")
        self.log_text_browser.setMinimumSize(QSize(0, 222))

        self.vertical_layout_controls.addWidget(self.log_text_browser)

        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMinimumSize(QSize(0, 25))
        self.progress_bar.setMaximumSize(QSize(16777215, 30))
        self.progress_bar.setValue(0)

        self.vertical_layout_controls.addWidget(self.progress_bar)


        self.horizontalLayout_3.addLayout(self.vertical_layout_controls)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1010, 21))
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_options = QMenu(self.menubar)
        self.menu_options.setObjectName(u"menu_options")
        self.menu_options_language = QMenu(self.menu_options)
        self.menu_options_language.setObjectName(u"menu_options_language")
        self.menu_options_theme = QMenu(self.menu_options)
        self.menu_options_theme.setObjectName(u"menu_options_theme")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_options.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_about_qt)
        self.menu_help.addSeparator()
        self.menu_options.addAction(self.menu_options_language.menuAction())
        self.menu_options.addAction(self.menu_options_theme.menuAction())
        self.menu_options_language.addAction(self.action_language_system)
        self.menu_options_language.addAction(self.action_language_english)
        self.menu_options_language.addAction(self.action_language_spanish)
        self.menu_options_language.addAction(self.action_language_german)
        self.menu_options_language.addAction(self.action_language_french)
        self.menu_options_language.addAction(self.action_language_italian)
        self.menu_options_language.addAction(self.action_language_norwegian)
        self.menu_options_language.addAction(self.action_language_romanian)
        self.menu_options_language.addAction(self.action_language_korean)
        self.menu_options_theme.addAction(self.action_theme_system)
        self.menu_options_theme.addAction(self.action_theme_light)
        self.menu_options_theme.addAction(self.action_theme_dark)

        self.retranslateUi(MainWindow)

        self.platform_tabs.setCurrentIndex(0)
        self.console_select_dropdown.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About NUSGet", None))
        self.action_about_qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.action_language_system.setText(QCoreApplication.translate("MainWindow", u"System (Default)", None))
        self.action_language_english.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.action_language_spanish.setText(QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.action_language_german.setText(QCoreApplication.translate("MainWindow", u"Deutsch", None))
        self.action_language_french.setText(QCoreApplication.translate("MainWindow", u"Fran\u00e7ais", None))
        self.action_language_italian.setText(QCoreApplication.translate("MainWindow", u"Italiano", None))
        self.action_language_norwegian.setText(QCoreApplication.translate("MainWindow", u"Norsk", None))
        self.action_language_romanian.setText(QCoreApplication.translate("MainWindow", u"Rom\u00e2n\u0103", None))
        self.action_language_korean.setText(QCoreApplication.translate("MainWindow", u"\ud55c\uad6d\uc5b4", None))
        self.action_theme_system.setText(QCoreApplication.translate("MainWindow", u"System (Default)", None))
        self.action_theme_light.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.action_theme_dark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.tree_filter_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.tree_filter_reset_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
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
        self.archive_file_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"vWii Title Settings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"App Settings", None))
        self.custom_out_dir_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output Path", None))
        self.custom_out_dir_btn.setText(QCoreApplication.translate("MainWindow", u"Select...", None))
        self.log_text_browser.setMarkdown("")
        self.log_text_browser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Sans Serif'; font-size:9pt;\"><br /></p></body></html>", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menu_options.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menu_options_language.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
        self.menu_options_theme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
    # retranslateUi

