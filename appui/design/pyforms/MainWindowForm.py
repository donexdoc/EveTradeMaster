# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1068, 577)
        MainWindow.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.newPredictionsTab = QWidget()
        self.newPredictionsTab.setObjectName(u"newPredictionsTab")
        self.verticalLayout_3 = QVBoxLayout(self.newPredictionsTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.inputIdsLe = QLineEdit(self.newPredictionsTab)
        self.inputIdsLe.setObjectName(u"inputIdsLe")

        self.horizontalLayout_3.addWidget(self.inputIdsLe)

        self.newPredictionBtn = QPushButton(self.newPredictionsTab)
        self.newPredictionBtn.setObjectName(u"newPredictionBtn")

        self.horizontalLayout_3.addWidget(self.newPredictionBtn)

        self.defaultPredictionBtn = QPushButton(self.newPredictionsTab)
        self.defaultPredictionBtn.setObjectName(u"defaultPredictionBtn")

        self.horizontalLayout_3.addWidget(self.defaultPredictionBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.unsavedPredictionsTw = QTableWidget(self.newPredictionsTab)
        if (self.unsavedPredictionsTw.columnCount() < 13):
            self.unsavedPredictionsTw.setColumnCount(13)
        if (self.unsavedPredictionsTw.rowCount() < 1):
            self.unsavedPredictionsTw.setRowCount(1)
        self.unsavedPredictionsTw.setObjectName(u"unsavedPredictionsTw")
        self.unsavedPredictionsTw.setTextElideMode(Qt.ElideLeft)
        self.unsavedPredictionsTw.setRowCount(1)
        self.unsavedPredictionsTw.setColumnCount(13)

        self.verticalLayout_3.addWidget(self.unsavedPredictionsTw)

        self.tabWidget.addTab(self.newPredictionsTab, "")
        self.savedPredictionsTab = QWidget()
        self.savedPredictionsTab.setObjectName(u"savedPredictionsTab")
        self.verticalLayout_5 = QVBoxLayout(self.savedPredictionsTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.savedPredictsFilterLabel = QLabel(self.savedPredictionsTab)
        self.savedPredictsFilterLabel.setObjectName(u"savedPredictsFilterLabel")

        self.horizontalLayout_2.addWidget(self.savedPredictsFilterLabel)

        self.savedPredictionsFilterCmbb = QComboBox(self.savedPredictionsTab)
        self.savedPredictionsFilterCmbb.setObjectName(u"savedPredictionsFilterCmbb")
        self.savedPredictionsFilterCmbb.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.savedPredictionsFilterCmbb)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.savedPredictionsTw = QTableWidget(self.savedPredictionsTab)
        if (self.savedPredictionsTw.columnCount() < 13):
            self.savedPredictionsTw.setColumnCount(13)
        if (self.savedPredictionsTw.rowCount() < 1):
            self.savedPredictionsTw.setRowCount(1)
        self.savedPredictionsTw.setObjectName(u"savedPredictionsTw")
        self.savedPredictionsTw.setRowCount(1)
        self.savedPredictionsTw.setColumnCount(13)

        self.verticalLayout_4.addWidget(self.savedPredictionsTw)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.savedPredictionsTab, "")
        self.typesInDBTab = QWidget()
        self.typesInDBTab.setObjectName(u"typesInDBTab")
        self.verticalLayout_6 = QVBoxLayout(self.typesInDBTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.savedItemsFilterLabel = QLabel(self.typesInDBTab)
        self.savedItemsFilterLabel.setObjectName(u"savedItemsFilterLabel")

        self.horizontalLayout.addWidget(self.savedItemsFilterLabel)

        self.typesFIlterCmbb = QComboBox(self.typesInDBTab)
        self.typesFIlterCmbb.setObjectName(u"typesFIlterCmbb")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typesFIlterCmbb.sizePolicy().hasHeightForWidth())
        self.typesFIlterCmbb.setSizePolicy(sizePolicy)
        self.typesFIlterCmbb.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.typesFIlterCmbb)

        self.addTypesBtn = QPushButton(self.typesInDBTab)
        self.addTypesBtn.setObjectName(u"addTypesBtn")

        self.horizontalLayout.addWidget(self.addTypesBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.savedTypesTw = QTableWidget(self.typesInDBTab)
        self.savedTypesTw.setObjectName(u"savedTypesTw")

        self.verticalLayout_6.addWidget(self.savedTypesTw)

        self.tabWidget.addTab(self.typesInDBTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1068, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EveTradeMaster", None))
        self.inputIdsLe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"4, 6, 1337", None))
        self.newPredictionBtn.setText(QCoreApplication.translate("MainWindow", u"Prediction from line", None))
        self.defaultPredictionBtn.setText(QCoreApplication.translate("MainWindow", u"Prediction from default", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.newPredictionsTab), QCoreApplication.translate("MainWindow", u"New predictions", None))
        self.savedPredictsFilterLabel.setText(QCoreApplication.translate("MainWindow", u"Sort by: ", None))
        self.savedPredictionsFilterCmbb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FIlter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.savedPredictionsTab), QCoreApplication.translate("MainWindow", u"Saved predictions", None))
        self.savedItemsFilterLabel.setText(QCoreApplication.translate("MainWindow", u"Sort by: ", None))
        self.typesFIlterCmbb.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.addTypesBtn.setText(QCoreApplication.translate("MainWindow", u"Add more types", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.typesInDBTab), QCoreApplication.translate("MainWindow", u"Types in db", None))
    # retranslateUi

