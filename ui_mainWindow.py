# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(mainWindow)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(mainWindow)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(320, 0))

        self.verticalLayout.addWidget(self.lineEdit)

        self.modelTypesTreeViewer = QTreeView(mainWindow)
        self.modelTypesTreeViewer.setObjectName(u"modelTypesTreeViewer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.modelTypesTreeViewer.sizePolicy().hasHeightForWidth())
        self.modelTypesTreeViewer.setSizePolicy(sizePolicy2)
        self.modelTypesTreeViewer.setMinimumSize(QSize(320, 0))
        self.modelTypesTreeViewer.header().setVisible(False)

        self.verticalLayout.addWidget(self.modelTypesTreeViewer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.textBrowser = QTextBrowser(mainWindow)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)


        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Form", None))
    # retranslateUi

