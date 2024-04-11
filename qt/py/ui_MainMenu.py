# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 605)
        MainWindow.setMinimumSize(QSize(610, 605))
        MainWindow.setMaximumSize(QSize(800, 605))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_tree = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.title_tree.setHeaderItem(__qtreewidgetitem)
        self.title_tree.setObjectName(u"title_tree")
        self.title_tree.setColumnCount(1)
        self.title_tree.header().setVisible(False)

        self.horizontalLayout_3.addWidget(self.title_tree)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.show_titles_btn = QPushButton(self.centralwidget)
        self.show_titles_btn.setObjectName(u"show_titles_btn")

        self.horizontalLayout.addWidget(self.show_titles_btn)

        self.show_more_btn = QPushButton(self.centralwidget)
        self.show_more_btn.setObjectName(u"show_more_btn")

        self.horizontalLayout.addWidget(self.show_more_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

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
        self.use_local_chkbox.setEnabled(False)

        self.verticalLayout_3.addWidget(self.use_local_chkbox)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 610, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.show_titles_btn.setText(QCoreApplication.translate("MainWindow", u"Titles", None))
        self.show_more_btn.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.tid_entry.setText("")
        self.tid_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title ID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"v", None))
        self.version_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.download_btn.setText(QCoreApplication.translate("MainWindow", u"Start NUS Download!", None))
        self.log_text_browser.setMarkdown("")
        self.pack_wad_chkbox.setText(QCoreApplication.translate("MainWindow", u"Pack WAD", None))
        self.wad_file_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.keep_enc_chkbox.setText(QCoreApplication.translate("MainWindow", u"Keep Enc. Contents", None))
        self.create_dec_chkbox.setText(QCoreApplication.translate("MainWindow", u"Create Decrypted Contents (*.app)", None))
        self.use_local_chkbox.setText(QCoreApplication.translate("MainWindow", u"Use Local Files If They Exist", None))
    # retranslateUi

