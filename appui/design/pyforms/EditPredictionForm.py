# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditPredictionWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogEditPredict(object):
    def setupUi(self, DialogEditPredict):
        if not DialogEditPredict.objectName():
            DialogEditPredict.setObjectName(u"DialogEditPredict")
        DialogEditPredict.resize(477, 174)
        self.verticalLayout = QVBoxLayout(DialogEditPredict)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.editPredictNameLabel = QLabel(DialogEditPredict)
        self.editPredictNameLabel.setObjectName(u"editPredictNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.editPredictNameLabel)

        self.predictNameLe = QLineEdit(DialogEditPredict)
        self.predictNameLe.setObjectName(u"predictNameLe")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.predictNameLe)

        self.brokerBuyPriceLabel = QLabel(DialogEditPredict)
        self.brokerBuyPriceLabel.setObjectName(u"brokerBuyPriceLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.brokerBuyPriceLabel)

        self.brokerBuyChangeLe = QLineEdit(DialogEditPredict)
        self.brokerBuyChangeLe.setObjectName(u"brokerBuyChangeLe")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.brokerBuyChangeLe)

        self.brokerSellPriceLabel = QLabel(DialogEditPredict)
        self.brokerSellPriceLabel.setObjectName(u"brokerSellPriceLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.brokerSellPriceLabel)

        self.brokerSellChangeLe = QLineEdit(DialogEditPredict)
        self.brokerSellChangeLe.setObjectName(u"brokerSellChangeLe")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.brokerSellChangeLe)

        self.expectedProfitLabel = QLabel(DialogEditPredict)
        self.expectedProfitLabel.setObjectName(u"expectedProfitLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.expectedProfitLabel)

        self.expectedProfitTe = QLineEdit(DialogEditPredict)
        self.expectedProfitTe.setObjectName(u"expectedProfitTe")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.expectedProfitTe)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.deletePredictBtn = QPushButton(DialogEditPredict)
        self.deletePredictBtn.setObjectName(u"deletePredictBtn")

        self.horizontalLayout.addWidget(self.deletePredictBtn)

        self.completePredictBtn = QPushButton(DialogEditPredict)
        self.completePredictBtn.setObjectName(u"completePredictBtn")

        self.horizontalLayout.addWidget(self.completePredictBtn)

        self.savePredictBtn = QPushButton(DialogEditPredict)
        self.savePredictBtn.setObjectName(u"savePredictBtn")

        self.horizontalLayout.addWidget(self.savePredictBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.predictNameLe, self.brokerBuyChangeLe)
        QWidget.setTabOrder(self.brokerBuyChangeLe, self.brokerSellChangeLe)
        QWidget.setTabOrder(self.brokerSellChangeLe, self.expectedProfitTe)
        QWidget.setTabOrder(self.expectedProfitTe, self.savePredictBtn)
        QWidget.setTabOrder(self.savePredictBtn, self.completePredictBtn)
        QWidget.setTabOrder(self.completePredictBtn, self.deletePredictBtn)

        self.retranslateUi(DialogEditPredict)

        QMetaObject.connectSlotsByName(DialogEditPredict)
    # setupUi

    def retranslateUi(self, DialogEditPredict):
        DialogEditPredict.setWindowTitle(QCoreApplication.translate("DialogEditPredict", u"Edit prediction", None))
        self.editPredictNameLabel.setText(QCoreApplication.translate("DialogEditPredict", u"Predict name:", None))
        self.brokerBuyPriceLabel.setText(QCoreApplication.translate("DialogEditPredict", u"Broker buy price (after order change):", None))
        self.brokerSellPriceLabel.setText(QCoreApplication.translate("DialogEditPredict", u"Broker sell price (after order change):", None))
        self.expectedProfitLabel.setText(QCoreApplication.translate("DialogEditPredict", u"Expected profit:", None))
        self.deletePredictBtn.setText(QCoreApplication.translate("DialogEditPredict", u"Delete predict", None))
        self.completePredictBtn.setText(QCoreApplication.translate("DialogEditPredict", u"Complete Predict", None))
        self.savePredictBtn.setText(QCoreApplication.translate("DialogEditPredict", u"Save predict", None))
    # retranslateUi

