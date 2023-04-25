# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Apps.ClientApp.Resources.Icons_rc


class Ui_MainWindow(object):

    def __init__(self, main_window):
        self.setupUi(main_window)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(977, 662)
        icon = QIcon()
        icon.addFile(u":/TabIcons/icons/app-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	font: 75 10pt \"Gadugi\";\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"	box-shadow: 0 0 5px 0 black;\n"
"	height: 20px;\n"
"	margin-left: 5px;\n"
"	color: white;\n"
"	background-color: black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: green;\n"
"}")
        self.openScenarioMenuOption = QAction(MainWindow)
        self.openScenarioMenuOption.setObjectName(u"openScenarioMenuOption")
        icon1 = QIcon()
        icon1.addFile(u":/TabIcons/icons/open-file-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openScenarioMenuOption.setIcon(icon1)
        self.openScenarioMenuOption.setShortcutContext(Qt.ApplicationShortcut)
        self.exitMenuOption = QAction(MainWindow)
        self.exitMenuOption.setObjectName(u"exitMenuOption")
        icon2 = QIcon()
        icon2.addFile(u":/TabIcons/icons/exit-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitMenuOption.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 971, 631))
        self.MainLayout = QGridLayout(self.gridLayoutWidget)
        self.MainLayout.setObjectName(u"MainLayout")
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainTabWidget = QTabWidget(self.gridLayoutWidget)
        self.MainTabWidget.setObjectName(u"MainTabWidget")
        self.MainTabWidget.setStyleSheet(u"")
        self.MainTabWidget.setTabPosition(QTabWidget.West)
        self.MainTabWidget.setTabShape(QTabWidget.Triangular)
        self.MainTabWidget.setElideMode(Qt.ElideNone)
        self.MainTab = QWidget()
        self.MainTab.setObjectName(u"MainTab")
        self.MainTab.setStyleSheet(u"#MainTab{\n"
"		\n"
"	\n"
"	background-color: white;\n"
"}")
        self.gridLayoutWidget_2 = QWidget(self.MainTab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 941, 501))
        self.horizontalLayout = QHBoxLayout(self.gridLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(10, 10, 0, 0)
        self.windowsListGroupBox = QGroupBox(self.gridLayoutWidget_2)
        self.windowsListGroupBox.setObjectName(u"windowsListGroupBox")
        self.windowsListGroupBox.setStyleSheet(u"	border-radius: 15px;\n"
"	color: white;\n"
"	background-color: black;\n"
"	transition: background-color 0.3s linear;")
        self.windowsListGroupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayoutWidget_3 = QWidget(self.windowsListGroupBox)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 20, 291, 461))
        self.windowsListLayout = QGridLayout(self.gridLayoutWidget_3)
        self.windowsListLayout.setObjectName(u"windowsListLayout")
        self.windowsListLayout.setContentsMargins(0, 0, 0, 0)
        self.windowsListView = QTreeView(self.gridLayoutWidget_3)
        self.windowsListView.setObjectName(u"windowsListView")
        self.windowsListView.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.windowsListView.setFrameShape(QFrame.StyledPanel)
        self.windowsListView.setFrameShadow(QFrame.Sunken)
        self.windowsListView.setAnimated(True)

        self.windowsListLayout.addWidget(self.windowsListView, 0, 0, 1, 1)

        self.refreshWindowsListButton = QPushButton(self.gridLayoutWidget_3)
        self.refreshWindowsListButton.setObjectName(u"refreshWindowsListButton")
        self.refreshWindowsListButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshWindowsListButton.setStyleSheet(u"#refreshWindowsListButton{\n"
"	background-color: green;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#refreshWindowsListButton:hover{\n"
"	background-color: white;\n"
"	color: black;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/TabIcons/icons/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshWindowsListButton.setIcon(icon3)

        self.windowsListLayout.addWidget(self.refreshWindowsListButton, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.windowsListGroupBox)

        self.scenarioGroupBox = QGroupBox(self.gridLayoutWidget_2)
        self.scenarioGroupBox.setObjectName(u"scenarioGroupBox")
        self.scenarioGroupBox.setStyleSheet(u"\n"
"	border-radius: 15px;\n"
"	color: white;\n"
"	background-color: black;\n"
"	transition: background-color 0.3s linear;\n"
"font: 75 10pt \"Gadugi\";")
        self.scenarioGroupBox.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget_4 = QWidget(self.scenarioGroupBox)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 20, 601, 461))
        self.scenarioLayout = QGridLayout(self.gridLayoutWidget_4)
        self.scenarioLayout.setObjectName(u"scenarioLayout")
        self.scenarioLayout.setContentsMargins(0, 0, 0, 0)
        self.scenarioEditor = QPlainTextEdit(self.gridLayoutWidget_4)
        self.scenarioEditor.setObjectName(u"scenarioEditor")
        self.scenarioEditor.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.scenarioLayout.addWidget(self.scenarioEditor, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.scenarioGroupBox)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayoutWidget = QWidget(self.MainTab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 509, 941, 101))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.optionsGroupBox = QGroupBox(self.horizontalLayoutWidget)
        self.optionsGroupBox.setObjectName(u"optionsGroupBox")
        self.optionsGroupBox.setStyleSheet(u"#optionsGroupBox{\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"}")
        self.optionsGroupBox.setAlignment(Qt.AlignCenter)
        self.optionsGroupBox.setFlat(False)
        self.horizontalLayoutWidget_2 = QWidget(self.optionsGroupBox)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(9, 20, 921, 71))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.startListenButton = QPushButton(self.horizontalLayoutWidget_2)
        self.startListenButton.setObjectName(u"startListenButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startListenButton.sizePolicy().hasHeightForWidth())
        self.startListenButton.setSizePolicy(sizePolicy)
        self.startListenButton.setMinimumSize(QSize(150, 30))
        self.startListenButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/TabIcons/icons/start-listen-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startListenButton.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.startListenButton)

        self.stopListenButton = QPushButton(self.horizontalLayoutWidget_2)
        self.stopListenButton.setObjectName(u"stopListenButton")
        sizePolicy.setHeightForWidth(self.stopListenButton.sizePolicy().hasHeightForWidth())
        self.stopListenButton.setSizePolicy(sizePolicy)
        self.stopListenButton.setMinimumSize(QSize(100, 30))
        self.stopListenButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/TabIcons/icons/stop-listen-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopListenButton.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.stopListenButton)

        self.horizontalSpacer_3 = QSpacerItem(300, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.currentStatusLabel = QLabel(self.horizontalLayoutWidget_2)
        self.currentStatusLabel.setObjectName(u"currentStatusLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.currentStatusLabel.sizePolicy().hasHeightForWidth())
        self.currentStatusLabel.setSizePolicy(sizePolicy1)
        self.currentStatusLabel.setMinimumSize(QSize(130, 50))
        self.currentStatusLabel.setStyleSheet(u"#currentStatusLabel{\n"
"	background-color: black;\n"
"	color: white;\n"
"}")
        self.currentStatusLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.currentStatusLabel)

        self.currentStatus = QLabel(self.horizontalLayoutWidget_2)
        self.currentStatus.setObjectName(u"currentStatus")
        sizePolicy1.setHeightForWidth(self.currentStatus.sizePolicy().hasHeightForWidth())
        self.currentStatus.setSizePolicy(sizePolicy1)
        self.currentStatus.setMinimumSize(QSize(110, 50))
        self.currentStatus.setStyleSheet(u"#currentStatus{\n"
"	background-color: red;\n"
"	color: white;\n"
"}")
        self.currentStatus.setScaledContents(False)
        self.currentStatus.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.currentStatus)

        self.horizontalSpacer = QSpacerItem(300, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.startScenarionButton = QPushButton(self.horizontalLayoutWidget_2)
        self.startScenarionButton.setObjectName(u"startScenarionButton")
        sizePolicy.setHeightForWidth(self.startScenarionButton.sizePolicy().hasHeightForWidth())
        self.startScenarionButton.setSizePolicy(sizePolicy)
        self.startScenarionButton.setMinimumSize(QSize(150, 30))
        self.startScenarionButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/TabIcons/icons/compile-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startScenarionButton.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.startScenarionButton)

        self.scenarioConstructorButton = QPushButton(self.horizontalLayoutWidget_2)
        self.scenarioConstructorButton.setObjectName(u"scenarioConstructorButton")
        sizePolicy.setHeightForWidth(self.scenarioConstructorButton.sizePolicy().hasHeightForWidth())
        self.scenarioConstructorButton.setSizePolicy(sizePolicy)
        self.scenarioConstructorButton.setMinimumSize(QSize(180, 30))
        self.scenarioConstructorButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/TabIcons/icons/scenario-constructor-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scenarioConstructorButton.setIcon(icon7)
        self.scenarioConstructorButton.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.scenarioConstructorButton)


        self.horizontalLayout_2.addWidget(self.optionsGroupBox)

        icon8 = QIcon()
        icon8.addFile(u":/TabIcons/icons/main-tab-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MainTabWidget.addTab(self.MainTab, icon8, "")
        self.SettingsTab = QWidget()
        self.SettingsTab.setObjectName(u"SettingsTab")
        self.gridLayoutWidget_5 = QWidget(self.SettingsTab)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 0, 931, 611))
        self.verticalLayout = QVBoxLayout(self.gridLayoutWidget_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.infoGroupBox = QGroupBox(self.gridLayoutWidget_5)
        self.infoGroupBox.setObjectName(u"infoGroupBox")
        self.infoGroupBox.setStyleSheet(u"#infoGroupBox{\n"
"	background-color: white;\n"
"\n"
"}")
        self.verticalLayoutWidget = QWidget(self.infoGroupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 996, 171))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.infoProgramNameLabel = QLabel(self.verticalLayoutWidget)
        self.infoProgramNameLabel.setObjectName(u"infoProgramNameLabel")
        self.infoProgramNameLabel.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.infoProgramNameLabel)

        self.infoProgramVersionLabel = QLabel(self.verticalLayoutWidget)
        self.infoProgramVersionLabel.setObjectName(u"infoProgramVersionLabel")
        self.infoProgramVersionLabel.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.infoProgramVersionLabel)

        self.infoProgramHashLabel = QLabel(self.verticalLayoutWidget)
        self.infoProgramHashLabel.setObjectName(u"infoProgramHashLabel")
        self.infoProgramHashLabel.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.infoProgramHashLabel)

        self.infoProgramLicenseLabel = QLabel(self.verticalLayoutWidget)
        self.infoProgramLicenseLabel.setObjectName(u"infoProgramLicenseLabel")
        self.infoProgramLicenseLabel.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.infoProgramLicenseLabel)

        self.infoProgramAdditionalData = QLabel(self.verticalLayoutWidget)
        self.infoProgramAdditionalData.setObjectName(u"infoProgramAdditionalData")
        self.infoProgramAdditionalData.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 10px;")

        self.verticalLayout_2.addWidget(self.infoProgramAdditionalData)


        self.verticalLayout.addWidget(self.infoGroupBox)

        self.settingsGroupBox = QGroupBox(self.gridLayoutWidget_5)
        self.settingsGroupBox.setObjectName(u"settingsGroupBox")
        self.gridLayoutWidget_6 = QWidget(self.settingsGroupBox)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 20, 911, 381))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.hostComboBox = QComboBox(self.gridLayoutWidget_6)
        self.hostComboBox.setObjectName(u"hostComboBox")

        self.gridLayout.addWidget(self.hostComboBox, 1, 1, 1, 1)

        self.portNumberLabel = QLabel(self.gridLayoutWidget_6)
        self.portNumberLabel.setObjectName(u"portNumberLabel")

        self.gridLayout.addWidget(self.portNumberLabel, 0, 0, 1, 1)

        self.hostLabel = QLabel(self.gridLayoutWidget_6)
        self.hostLabel.setObjectName(u"hostLabel")

        self.gridLayout.addWidget(self.hostLabel, 1, 0, 1, 1)

        self.portNumberSpinBox = QSpinBox(self.gridLayoutWidget_6)
        self.portNumberSpinBox.setObjectName(u"portNumberSpinBox")
        self.portNumberSpinBox.setAlignment(Qt.AlignCenter)
        self.portNumberSpinBox.setMaximum(65535)
        self.portNumberSpinBox.setValue(5551)

        self.gridLayout.addWidget(self.portNumberSpinBox, 0, 1, 1, 1)

        self.refreshHostsButton = QPushButton(self.gridLayoutWidget_6)
        self.refreshHostsButton.setObjectName(u"refreshHostsButton")
        self.refreshHostsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshHostsButton.setStyleSheet(u"#refreshHostsButton{\n"
"	background-color: green;\n"
"	font-size: 14px;\n"
"	border: 1px solid green;\n"
"}\n"
"\n"
"#refreshHostsButton:hover{\n"
"	background-color: black;\n"
"	color: white;\n"
"}")
        self.refreshHostsButton.setIcon(icon3)

        self.gridLayout.addWidget(self.refreshHostsButton, 1, 2, 1, 1)

        self.refreshPortButton = QPushButton(self.gridLayoutWidget_6)
        self.refreshPortButton.setObjectName(u"refreshPortButton")
        self.refreshPortButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshPortButton.setStyleSheet(u"#refreshPortButton{\n"
"	background-color: green;\n"
"	font-size: 14px;\n"
"	border: 1px solid green;\n"
"}\n"
"\n"
"#refreshPortButton:hover{\n"
"	background-color: black;\n"
"	color: white;\n"
"}")
        self.refreshPortButton.setIcon(icon3)

        self.gridLayout.addWidget(self.refreshPortButton, 0, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout.addWidget(self.settingsGroupBox)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        icon9 = QIcon()
        icon9.addFile(u":/TabIcons/icons/settings-tab-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MainTabWidget.addTab(self.SettingsTab, icon9, "")

        self.MainLayout.addWidget(self.MainTabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 977, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setTearOffEnabled(False)
        self.menu.setSeparatorsCollapsible(False)
        self.menu.setToolTipsVisible(True)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setBaseSize(QSize(500, 20))
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.openScenarioMenuOption)
        self.menu.addSeparator()
        self.menu.addAction(self.exitMenuOption)

        self.retranslateUi(MainWindow)

        self.MainTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RedRPA-клиент", None))
        self.openScenarioMenuOption.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u0446\u0435\u043d\u0430\u0440\u0438\u0439", None))
        self.exitMenuOption.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.windowsListGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u043a\u043e\u043d", None))
        self.refreshWindowsListButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u043e\u043a\u043e\u043d", None))
        self.scenarioGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0446\u0435\u043d\u0430\u0440\u0438\u0439", None))
        self.optionsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0446\u0438\u0438", None))
        self.startListenButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0436\u0438\u0434\u0430\u0442\u044c \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.stopListenButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043f", None))
        self.currentStatusLabel.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0435\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435:", None))
        self.currentStatus.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0430\u043a\u0442\u0438\u0432\u043d\u043e", None))
        self.startScenarionButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a \u0441\u0446\u0435\u043d\u0430\u0440\u0438\u044f", None))
        self.scenarioConstructorButton.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u043e\u0440 \u0441\u0446\u0435\u043d\u0430\u0440\u0438\u0435\u0432", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.MainTab), QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.infoGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.infoProgramNameLabel.setText(QCoreApplication.translate("MainWindow",
                                                                     u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">🖥 RedRPA-\u043a\u043b\u0438\u0435\u043d\u0442</span></p></body></html>",
                                                                     None))
        self.infoProgramVersionLabel.setText(QCoreApplication.translate("MainWindow",
                                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">🛠 \u0412\u0435\u0440\u0441\u0438\u044f: &quot;Rey&quot; 1.0</span></p></body></html>",
                                                                        None))
        self.infoProgramHashLabel.setText(QCoreApplication.translate("MainWindow",
                                                                     u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">⚙️ \u0425\u044d\u0448: {}</span></p></body></html>",
                                                                     None))
        self.infoProgramLicenseLabel.setText(QCoreApplication.translate("MainWindow",
                                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">©® Boost Software License - Version 1.0 - August 17th, 2003</span></p></body></html>",
                                                                        None))
        self.infoProgramAdditionalData.setText(QCoreApplication.translate("MainWindow",
                                                                          u"<html><head/><body><p align=\"center\">ℹ \u0420\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0441\u043a\u043e\u0433\u043e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u0444\u0440\u0435\u0439\u043c\u0432\u043e\u0440\u043a\u0430 RedRPA. \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u0430 Boost Software License 1.0.</p></body></html>",
                                                                          None))
        self.settingsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.portNumberLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043f\u043e\u0440\u0442\u0430:", None))
        self.hostLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043b\u0443\u0448\u0438\u0432\u0430\u0435\u043c\u044b\u0439 \u0430\u0434\u0440\u0435\u0441:", None))
        self.refreshHostsButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.refreshPortButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.SettingsTab), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
    # retranslateUi

