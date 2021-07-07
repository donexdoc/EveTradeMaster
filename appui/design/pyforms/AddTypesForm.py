# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddTypesWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogAddTypes(object):
    def setupUi(self, DialogAddTypes):
        if not DialogAddTypes.objectName():
            DialogAddTypes.setObjectName(u"DialogAddTypes")
        DialogAddTypes.resize(400, 284)
        self.verticalLayout = QVBoxLayout(DialogAddTypes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.typesInputTe = QLineEdit(DialogAddTypes)
        self.typesInputTe.setObjectName(u"typesInputTe")

        self.horizontalLayout.addWidget(self.typesInputTe)

        self.checkAndAddBtn = QPushButton(DialogAddTypes)
        self.checkAndAddBtn.setObjectName(u"checkAndAddBtn")

        self.horizontalLayout.addWidget(self.checkAndAddBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.addNewTypesAddedLabel = QLabel(DialogAddTypes)
        self.addNewTypesAddedLabel.setObjectName(u"addNewTypesAddedLabel")

        self.verticalLayout_2.addWidget(self.addNewTypesAddedLabel)

        self.typesLw = QListWidget(DialogAddTypes)
        self.typesLw.setObjectName(u"typesLw")

        self.verticalLayout_2.addWidget(self.typesLw)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(DialogAddTypes)

        QMetaObject.connectSlotsByName(DialogAddTypes)
    # setupUi

    def retranslateUi(self, DialogAddTypes):
        DialogAddTypes.setWindowTitle(QCoreApplication.translate("DialogAddTypes", u"Add new types", None))
        self.typesInputTe.setPlaceholderText(QCoreApplication.translate("DialogAddTypes", u"4, 6, 1337", None))
        self.checkAndAddBtn.setText(QCoreApplication.translate("DialogAddTypes", u"Add types in list", None))
        self.addNewTypesAddedLabel.setText(QCoreApplication.translate("DialogAddTypes", u"New types added:", None))
    # retranslateUi

