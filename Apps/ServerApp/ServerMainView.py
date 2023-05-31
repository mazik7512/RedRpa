# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'server.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Apps.ServerApp.Resources.ServerIcons_rc


class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 702)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/app-icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	font: 75 10pt \"Gadugi\";\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"	border: 1px solid black;\n"
"	box-shadow: 0 0 5px 0 black;\n"
"	height: 20px;\n"
"	margin-left: 5px;\n"
"	color: white;\n"
"	background-color: black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #9ACD32;\n"
"}")
        self.loadScenarioButton = QAction(MainWindow)
        self.loadScenarioButton.setObjectName(u"loadScenarioButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/open-file-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loadScenarioButton.setIcon(icon1)
        self.saveScenarioButton = QAction(MainWindow)
        self.saveScenarioButton.setObjectName(u"saveScenarioButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/save-file-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveScenarioButton.setIcon(icon2)
        self.exitButton = QAction(MainWindow)
        self.exitButton.setObjectName(u"exitButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/exit-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon3)
        self.addClientButton = QAction(MainWindow)
        self.addClientButton.setObjectName(u"addClientButton")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/add-client-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addClientButton.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 881, 551))
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        self.horizontalLayoutWidget_3 = QWidget(self.mainTab)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 10, 881, 511))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.clientsArea = QMdiArea(self.horizontalLayoutWidget_3)
        self.clientsArea.setObjectName(u"clientsArea")

        self.horizontalLayout_4.addWidget(self.clientsArea)

        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/main-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.mainTab, icon5, "")
        self.infoTab = QWidget()
        self.infoTab.setObjectName(u"infoTab")
        self.horizontalLayoutWidget_2 = QWidget(self.infoTab)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 10, 861, 501))
        self.verticalLayout = QVBoxLayout(self.horizontalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.nameInfoLabel = QLabel(self.horizontalLayoutWidget_2)
        self.nameInfoLabel.setObjectName(u"nameInfoLabel")
        self.nameInfoLabel.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 20px;")
        self.nameInfoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.nameInfoLabel)

        self.versionInfoLabel = QLabel(self.horizontalLayoutWidget_2)
        self.versionInfoLabel.setObjectName(u"versionInfoLabel")
        self.versionInfoLabel.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 20px;")
        self.versionInfoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.versionInfoLabel)

        self.hashInfoLabel = QLabel(self.horizontalLayoutWidget_2)
        self.hashInfoLabel.setObjectName(u"hashInfoLabel")
        self.hashInfoLabel.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 20px;")
        self.hashInfoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.hashInfoLabel)

        self.licenseInfoLabel = QLabel(self.horizontalLayoutWidget_2)
        self.licenseInfoLabel.setObjectName(u"licenseInfoLabel")
        self.licenseInfoLabel.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 20px;")
        self.licenseInfoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.licenseInfoLabel)

        self.additionalInfoLabel = QLabel(self.horizontalLayoutWidget_2)
        self.additionalInfoLabel.setObjectName(u"additionalInfoLabel")
        self.additionalInfoLabel.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius: 20px;")
        self.additionalInfoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.additionalInfoLabel)
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/info-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.infoTab, icon7, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 998, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"background-image: url(:/icons/Icons/file-icon.png);")
        self.menu.setTearOffEnabled(False)
        self.menu.setSeparatorsCollapsible(False)
        self.menu.setToolTipsVisible(False)
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dataWidget = QDockWidget(MainWindow)
        self.dataWidget.setObjectName(u"dataWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataWidget.sizePolicy().hasHeightForWidth())
        self.dataWidget.setSizePolicy(sizePolicy)
        self.dataWidget.setMinimumSize(QSize(82, 100))
        font = QFont()
        font.setFamily(u"Gadugi")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.dataWidget.setFont(font)
        self.dataWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.dataWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dataWidget.setAllowedAreas(Qt.BottomDockWidgetArea|Qt.TopDockWidgetArea)
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.verticalLayoutWidget_2 = QWidget(self.dockWidgetContents_4)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 30, 231, 561))
        self.windowsListLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.windowsListLayout.setObjectName(u"windowsListLayout")
        self.windowsListLayout.setContentsMargins(0, 0, 0, 0)
        self.windowsListViewLabel = QLabel(self.verticalLayoutWidget_2)
        self.windowsListViewLabel.setObjectName(u"windowsListViewLabel")
        self.windowsListViewLabel.setAlignment(Qt.AlignCenter)

        self.windowsListLayout.addWidget(self.windowsListViewLabel)

        self.windowsListView = QTreeWidget(self.verticalLayoutWidget_2)
        self.windowsListView.setObjectName(u"windowsListView")

        self.windowsListLayout.addWidget(self.windowsListView)

        self.refreshWindowsListButton = QPushButton(self.verticalLayoutWidget_2)
        self.refreshWindowsListButton.setObjectName(u"refreshWindowsListButton")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshWindowsListButton.setIcon(icon8)

        self.windowsListLayout.addWidget(self.refreshWindowsListButton)

        self.verticalLayoutWidget_3 = QWidget(self.dockWidgetContents_4)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(250, 30, 741, 561))
        self.codeLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.codeLayout.setObjectName(u"codeLayout")
        self.codeLayout.setContentsMargins(0, 0, 0, 0)
        self.scenarioLabel = QLabel(self.verticalLayoutWidget_3)
        self.scenarioLabel.setObjectName(u"scenarioLabel")
        self.scenarioLabel.setAlignment(Qt.AlignCenter)

        self.codeLayout.addWidget(self.scenarioLabel)

        self.codeEditor = QPlainTextEdit(self.verticalLayoutWidget_3)
        self.codeEditor.setObjectName(u"codeEditor")

        self.codeLayout.addWidget(self.codeEditor)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.statusHeaderLabel = QLabel(self.verticalLayoutWidget_3)
        self.statusHeaderLabel.setObjectName(u"statusHeaderLabel")
        self.statusHeaderLabel.setStyleSheet(u"background-color: #BDB76B;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 10px;")
        self.statusHeaderLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.statusHeaderLabel)

        self.currentStatusLabel = QLabel(self.verticalLayoutWidget_3)
        self.currentStatusLabel.setObjectName(u"currentStatusLabel")
        self.currentStatusLabel.setStyleSheet(u"background-color: #87CEEB;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 10px;")
        self.currentStatusLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.currentStatusLabel)

        self.startScenarioButton = QPushButton(self.verticalLayoutWidget_3)
        self.startScenarioButton.setObjectName(u"startScenarioButton")
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/start-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startScenarioButton.setIcon(icon9)

        self.horizontalLayout_2.addWidget(self.startScenarioButton)


        self.codeLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayoutWidget = QWidget(self.dockWidgetContents_4)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 0, 981, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.showBottomButton = QPushButton(self.horizontalLayoutWidget)
        self.showBottomButton.setObjectName(u"showBottomButton")
        self.showBottomButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.showBottomButton.setStyleSheet(u"#showBottomButton{\n"
"	background-color: white;\n"
"	color: black;\n"
"\n"
"}\n"
"\n"
"#showBottomButton:hover{\n"
"	background-color: #B0E0E6;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/show-icon-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showBottomButton.setIcon(icon10)

        self.horizontalLayout_3.addWidget(self.showBottomButton)

        self.dataWidget.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dataWidget)
        self.infoDataWidget = QDockWidget(MainWindow)
        self.infoDataWidget.setObjectName(u"infoDataWidget")
        self.infoDataWidget.setMinimumSize(QSize(110, 40))
        self.infoDataWidget.setMaximumSize(QSize(300, 524287))
        self.infoDataWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.infoDataWidget.setStyleSheet(u"")
        self.infoDataWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.infoDataWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_6 = QWidget()
        self.dockWidgetContents_6.setObjectName(u"dockWidgetContents_6")
        self.verticalLayoutWidget = QWidget(self.dockWidgetContents_6)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 281, 531))
        self.infoLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.infoLayout.setObjectName(u"infoLayout")
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.showButton = QPushButton(self.verticalLayoutWidget)
        self.showButton.setObjectName(u"showButton")
        self.showButton.setMinimumSize(QSize(95, 0))
        self.showButton.setMaximumSize(QSize(95, 16777215))
        self.showButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.showButton.setStyleSheet(u"#showButton{\n"
"	background-color: white;\n"
"	color: black;\n"
"\n"
"}\n"
"\n"
"#showButton:hover{\n"
"	background-color: #B0E0E6;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/show-hide-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showButton.setIcon(icon11)

        self.infoLayout.addWidget(self.showButton)

        self.infoErrosTabWidget = QTabWidget(self.verticalLayoutWidget)
        self.infoErrosTabWidget.setObjectName(u"infoErrosTabWidget")
        self.infoErrosTabWidget.setTabShape(QTabWidget.Rounded)
        self.infoInfoTab = QWidget()
        self.infoInfoTab.setObjectName(u"infoInfoTab")
        self.verticalLayoutWidget_4 = QWidget(self.infoInfoTab)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 0, 271, 471))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.infoView = QListWidget(self.verticalLayoutWidget_4)
        self.infoView.setObjectName(u"infoView")

        self.verticalLayout_2.addWidget(self.infoView)

        self.infoErrosTabWidget.addTab(self.infoInfoTab, "")
        self.infoErrorsTab = QWidget()
        self.infoErrorsTab.setObjectName(u"infoErrorsTab")
        self.verticalLayoutWidget_5 = QWidget(self.infoErrorsTab)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 0, 271, 481))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.errorsView = QListWidget(self.verticalLayoutWidget_5)
        self.errorsView.setObjectName(u"errorsView")

        self.verticalLayout_3.addWidget(self.errorsView)

        self.infoErrosTabWidget.addTab(self.infoErrorsTab, "")

        self.infoLayout.addWidget(self.infoErrosTabWidget)

        self.infoDataWidget.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.infoDataWidget)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.loadScenarioButton)
        self.menu.addAction(self.saveScenarioButton)
        self.menu.addSeparator()
        self.menu.addAction(self.exitButton)
        self.menu_2.addAction(self.addClientButton)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.infoErrosTabWidget.setCurrentIndex(0)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RedRPA - \u0441\u0435\u0440\u0432\u0435\u0440", None))
        self.loadScenarioButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u0446\u0435\u043d\u0430\u0440\u0438\u0439", None))
        self.saveScenarioButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0446\u0435\u043d\u0430\u0440\u0438\u0439", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.addClientButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.nameInfoLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>📡 RedRPA - \u0441\u0435\u0440\u0432\u0435\u0440</p></body></html>", None))
        self.versionInfoLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>💡 \u0412\u0435\u0440\u0441\u0438\u044f 1.0 &quot;Asuka&quot;</p></body></html>", None))
        self.hashInfoLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>🔐 \u0425\u044d\u0448 {}</p></body></html>", None))
        self.licenseInfoLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u00a9\u00ae Boost Software License - Version 1.0 - August 17th, 2003</span></p></body></html>", None))
        self.additionalInfoLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>📜  \u0420\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0441\u0435\u0440\u0432\u0435\u0440\u043d\u043e\u0433\u043e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u0444\u0440\u0435\u0439\u043c\u0432\u043e\u0440\u043a\u0430 RedRPA. \u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u0430 Boost Software License 1.0.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infoTab), QCoreApplication.translate("MainWindow", u"Инфо", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"📁 \u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"🎲 \u041e\u043f\u0446\u0438\u0438", None))
        self.dataWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e", None))
        self.windowsListViewLabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u043a\u043e\u043d:", None))
        self.refreshWindowsListButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u043e\u043a\u043e\u043d", None))
        self.scenarioLabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0446\u0435\u043d\u0430\u0440\u0438\u0439:", None))
        self.statusHeaderLabel.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0441\u0442\u0430\u0442\u0443\u0441:", None))
        self.currentStatusLabel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0436\u0438\u0434\u0430\u043d\u0438\u0435...", None))
        self.startScenarioButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0441\u0446\u0435\u043d\u0430\u0440\u0438\u0439", None))
        self.showBottomButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.infoDataWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.showButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.infoErrosTabWidget.setTabText(self.infoErrosTabWidget.indexOf(self.infoInfoTab), QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.infoErrosTabWidget.setTabText(self.infoErrosTabWidget.indexOf(self.infoErrorsTab), QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0438", None))
    # retranslateUi

