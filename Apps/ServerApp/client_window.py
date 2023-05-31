# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client-window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import PySide2.QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Apps.ServerApp.Resources.ClientWindowIcons_rc


class Ui_ClientWindow(QMdiSubWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

    def setupUi(self, ClientWindow):
        if not ClientWindow.objectName():
            ClientWindow.setObjectName(u"ClientWindow")
        ClientWindow.resize(499, 353)
        ClientWindow.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint |
                                  Qt.WindowMinimizeButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/client-window-icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        ClientWindow.setWindowIcon(icon)
        ClientWindow.setStyleSheet(u"*{\n"
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
        self.gridLayoutWidget = QWidget(ClientWindow)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 241, 341))
        self.optionsLayout = QGridLayout(self.gridLayoutWidget)
        self.optionsLayout.setObjectName(u"optionsLayout")
        self.optionsLayout.setContentsMargins(0, 0, 0, 0)
        self.actionsLayout = QHBoxLayout()
        self.actionsLayout.setObjectName(u"actionsLayout")
        self.startConnectionButton = QPushButton(self.gridLayoutWidget)
        self.startConnectionButton.setObjectName(u"startConnectionButton")
        self.startConnectionButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/send-scenario-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startConnectionButton.setIcon(icon1)

        self.actionsLayout.addWidget(self.startConnectionButton)


        self.optionsLayout.addLayout(self.actionsLayout, 4, 1, 1, 2)

        self.clientPortEdit = QSpinBox(self.gridLayoutWidget)
        self.clientPortEdit.setObjectName(u"clientPortEdit")
        self.clientPortEdit.setAlignment(Qt.AlignCenter)
        self.clientPortEdit.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.clientPortEdit.setMinimum(0)
        self.clientPortEdit.setMaximum(65535)
        self.clientPortEdit.setValue(5551)

        self.optionsLayout.addWidget(self.clientPortEdit, 2, 2, 1, 1)

        self.clientIPEdit = QLineEdit(self.gridLayoutWidget)
        self.clientIPEdit.setObjectName(u"clientIPEdit")
        self.clientIPEdit.setAlignment(Qt.AlignCenter)
        self.clientIPEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.clientIPEdit.setClearButtonEnabled(False)

        self.optionsLayout.addWidget(self.clientIPEdit, 1, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.optionsLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.optionsLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.clientNameEdit = QLineEdit(self.gridLayoutWidget)
        self.clientNameEdit.setObjectName(u"clientNameEdit")

        self.optionsLayout.addWidget(self.clientNameEdit, 0, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.optionsLayout.addWidget(self.label, 0, 1, 1, 1)



        self.gridLayoutWidget_2 = QWidget(ClientWindow)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(260, 25, 231, 321))
        self.codeLayout = QGridLayout(self.gridLayoutWidget_2)
        self.codeLayout.setObjectName(u"codeLayout")
        self.codeLayout.setContentsMargins(0, 0, 0, 0)
        self.scenarioLabel = QLabel(self.gridLayoutWidget_2)
        self.scenarioLabel.setObjectName(u"scenarioLabel")
        self.scenarioLabel.setAlignment(Qt.AlignCenter)

        self.codeLayout.addWidget(self.scenarioLabel, 0, 0, 1, 0)

        self.codeEditor = QPlainTextEdit(self.gridLayoutWidget_2)
        self.codeEditor.setObjectName(u"codeEditor")

        self.codeLayout.addWidget(self.codeEditor, 1, 0, 1, 0)

        self.retranslateUi(ClientWindow)

        QMetaObject.connectSlotsByName(ClientWindow)
    # setupUi

    def retranslateUi(self, ClientWindow):
        ClientWindow.setWindowTitle(QCoreApplication.translate("ClientWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.startConnectionButton.setText(QCoreApplication.translate("ClientWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0441\u0446\u0435\u043d\u0430\u0440\u0438\u0439", None))
        self.clientIPEdit.setInputMask(QCoreApplication.translate("ClientWindow", u"000.000.000.000", None))
        self.label_2.setText(QCoreApplication.translate("ClientWindow", u"IP \u043a\u043b\u0438\u0435\u043d\u0442\u0430:", None))
        self.label_3.setText(QCoreApplication.translate("ClientWindow", u"\u041f\u043e\u0440\u0442 \u043a\u043b\u0438\u0435\u043d\u0442\u0430:", None))
        self.label.setText(QCoreApplication.translate("ClientWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442:", None))
        self.scenarioLabel.setText(QCoreApplication.translate("ClientWindow", u"\u0421\u0446\u0435\u043d\u0430\u0440\u0438\u0439:", None))
    # retranslateUi

