# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SavePredictWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogSavePredict(object):
    def setupUi(self, DialogSavePredict):
        if not DialogSavePredict.objectName():
            DialogSavePredict.setObjectName(u"DialogSavePredict")
        DialogSavePredict.resize(409, 325)
        self.verticalLayout = QVBoxLayout(DialogSavePredict)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.predictNameLabel = QLabel(DialogSavePredict)
        self.predictNameLabel.setObjectName(u"predictNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.predictNameLabel)

        self.predictNameLe = QLineEdit(DialogSavePredict)
        self.predictNameLe.setObjectName(u"predictNameLe")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.predictNameLe)

        self.predictTypeNameLabel = QLabel(DialogSavePredict)
        self.predictTypeNameLabel.setObjectName(u"predictTypeNameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.predictTypeNameLabel)

        self.predictTypeNameLb = QLabel(DialogSavePredict)
        self.predictTypeNameLb.setObjectName(u"predictTypeNameLb")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.predictTypeNameLb)

        self.predictTypeIdLabel = QLabel(DialogSavePredict)
        self.predictTypeIdLabel.setObjectName(u"predictTypeIdLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.predictTypeIdLabel)

        self.predictTypeIdLb = QLabel(DialogSavePredict)
        self.predictTypeIdLb.setObjectName(u"predictTypeIdLb")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.predictTypeIdLb)

        self.mergePercentLabel = QLabel(DialogSavePredict)
        self.mergePercentLabel.setObjectName(u"mergePercentLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.mergePercentLabel)

        self.profitPerOneLabel = QLabel(DialogSavePredict)
        self.profitPerOneLabel.setObjectName(u"profitPerOneLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.profitPerOneLabel)

        self.sellPriceRecommendedLabel = QLabel(DialogSavePredict)
        self.sellPriceRecommendedLabel.setObjectName(u"sellPriceRecommendedLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.sellPriceRecommendedLabel)

        self.sellPriceRecomendedLe = QLineEdit(DialogSavePredict)
        self.sellPriceRecomendedLe.setObjectName(u"sellPriceRecomendedLe")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.sellPriceRecomendedLe)

        self.buyPriceRecommendedLabel = QLabel(DialogSavePredict)
        self.buyPriceRecommendedLabel.setObjectName(u"buyPriceRecommendedLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.buyPriceRecommendedLabel)

        self.buyPriceRecomendedLe = QLineEdit(DialogSavePredict)
        self.buyPriceRecomendedLe.setObjectName(u"buyPriceRecomendedLe")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.buyPriceRecomendedLe)

        self.experimentVolumeLabel = QLabel(DialogSavePredict)
        self.experimentVolumeLabel.setObjectName(u"experimentVolumeLabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.experimentVolumeLabel)

        self.experimentVolumeLe = QLineEdit(DialogSavePredict)
        self.experimentVolumeLe.setObjectName(u"experimentVolumeLe")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.experimentVolumeLe)

        self.experimentCostLabel = QLabel(DialogSavePredict)
        self.experimentCostLabel.setObjectName(u"experimentCostLabel")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.experimentCostLabel)

        self.experimentCostLe = QLineEdit(DialogSavePredict)
        self.experimentCostLe.setObjectName(u"experimentCostLe")
        self.experimentCostLe.setReadOnly(True)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.experimentCostLe)

        self.experimentProfitLabel = QLabel(DialogSavePredict)
        self.experimentProfitLabel.setObjectName(u"experimentProfitLabel")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.experimentProfitLabel)

        self.experimentProfitLe = QLineEdit(DialogSavePredict)
        self.experimentProfitLe.setObjectName(u"experimentProfitLe")
        self.experimentProfitLe.setReadOnly(True)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.experimentProfitLe)

        self.mergePercentLb = QLabel(DialogSavePredict)
        self.mergePercentLb.setObjectName(u"mergePercentLb")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.mergePercentLb)

        self.profitPerOneLb = QLabel(DialogSavePredict)
        self.profitPerOneLb.setObjectName(u"profitPerOneLb")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.profitPerOneLb)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.savePredictionBtn = QPushButton(DialogSavePredict)
        self.savePredictionBtn.setObjectName(u"savePredictionBtn")

        self.verticalLayout.addWidget(self.savePredictionBtn)


        self.retranslateUi(DialogSavePredict)

        QMetaObject.connectSlotsByName(DialogSavePredict)
    # setupUi

    def retranslateUi(self, DialogSavePredict):
        DialogSavePredict.setWindowTitle(QCoreApplication.translate("DialogSavePredict", u"Save predict", None))
        self.predictNameLabel.setText(QCoreApplication.translate("DialogSavePredict", u"Predict name:", None))
        self.predictTypeNameLabel.setText(QCoreApplication.translate("DialogSavePredict", u"Predict type name:", None))
        self.predictTypeNameLb.setText(QCoreApplication.translate("DialogSavePredict", u"name", None))
        self.predictTypeIdLabel.setText(QCoreApplication.translate("DialogSavePredict", u"Predict type id:", None))
        self.predictTypeIdLb.setText(QCoreApplication.translate("DialogSavePredict", u"id", None))
        self.mergePercentLabel.setText(QCoreApplication.translate("DialogSavePredict", u"Marge percent:", None))
        self.profitPerOneLabel.setText(QCoreApplication.translate("DialogSavePredict", u"Profit per one:", None))
        self.sellPriceRecommendedLabel.setText(QCoreApplication.translate("DialogSavePredict", u"Sell price (recommended):", None))
        self.buyPriceRecommendedLabel.setText(QCoreApplication.translate("DialogSavePredict", u"Buy price (recommended):", None))
        self.experimentVolumeLabel.setText(QCoreApplication.translate("DialogSavePredict", u"Experiment volume:", None))
        self.experimentCostLabel.setText(QCoreApplication.translate("DialogSavePredict", u"Experiment cost:", None))
        self.experimentProfitLabel.setText(QCoreApplication.translate("DialogSavePredict", u"Expected profit:", None))
        self.mergePercentLb.setText(QCoreApplication.translate("DialogSavePredict", u"100", None))
        self.profitPerOneLb.setText(QCoreApplication.translate("DialogSavePredict", u"100", None))
        self.savePredictionBtn.setText(QCoreApplication.translate("DialogSavePredict", u"Save prediction", None))
    # retranslateUi

