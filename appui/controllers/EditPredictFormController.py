from PySide2.QtWidgets import QDialog

from appui.design.pyforms.EditPredictionForm import Ui_DialogEditPredict


class EditPredictWindow(QDialog):
    """
    Форма для добавления новых игровых типов
    """

    def __init__(self, parent, predict):
        super(EditPredictWindow, self).__init__(parent)

        self.ui = Ui_DialogEditPredict()
        self.ui.setupUi(self)

        self.localization = parent.localization

        # from parent
        self.parent = parent
        self.predict = predict

        # UI interact setup
        self.ui.brokerSellChangeLe.textChanged.connect(self.calculate_broker_sell_tax)
        self.ui.brokerBuyChangeLe.textChanged.connect(self.calculate_broker_buy_tax)
        self.ui.savePredictBtn.clicked.connect(self.save_prediction)
        self.ui.completePredictBtn.clicked.connect(self.complete_prediction)
        self.ui.deletePredictBtn.clicked.connect(self.delete_prediction)
        # form load
        self.load_localization()
        self.setup_predict()

    def calculate_broker_buy_tax(self):

        try:
            if len(str(self.ui.brokerBuyChangeLe.text())) > 0:
                broker_buy_tax = float(self.ui.brokerBuyChangeLe.text())

                self.ui.expectedProfitTe.setText(str(self.predict.experiment_profit - broker_buy_tax))
                self.ui.brokerSellChangeLe.setEnabled(False)
            else:
                self.ui.brokerSellChangeLe.setEnabled(True)
        except Exception as e:
            print("calculating broker buy tax error")

    def calculate_broker_sell_tax(self):
        try:
            if len(str(self.ui.brokerSellChangeLe.text())) > 0:
                broker_sell_tax = float(self.ui.brokerSellChangeLe.text())
                self.ui.expectedProfitTe.setText(str(self.predict.experiment_profit - broker_sell_tax))

                self.ui.brokerBuyChangeLe.setEnabled(False)
            else:
                self.ui.brokerBuyChangeLe.setEnabled(True)
        except Exception as e:
            print("calculating broker sell tax error")

    def save_prediction(self):
        try:
            self.predict.name = str(self.ui.predictNameLe.text())

            self.calculate_broker_buy_tax()
            self.calculate_broker_sell_tax()

            self.predict.experiment_profit = float(self.ui.expectedProfitTe.text())
            self.predict.save()
            self.close()
        except Exception as e:
            print("Prediction saving error")

    def complete_prediction(self):
        try:
            self.predict.name = str(self.ui.predictNameLe.text())
            self.calculate_broker_buy_tax()
            self.calculate_broker_sell_tax()
            self.predict.experiment_profit = float(self.ui.expectedProfitTe.text())
            self.predict.experiment_ended = True

            self.predict.save()
            self.close()
        except Exception as e:
            print("Prediction complete error")

    def delete_prediction(self):
        self.predict.delete_instance()
        self.close()

    def setup_predict(self):
        self.ui.predictNameLe.setText(self.predict.name)
        self.ui.expectedProfitTe.setText(str(self.predict.experiment_profit))

    def load_localization(self):
        self.ui.editPredictNameLabel.setText(self.localization.get_string('editPredictNameLabel'))
        self.ui.brokerBuyPriceLabel.setText(self.localization.get_string('brokerBuyPriceLabel'))
        self.ui.brokerSellPriceLabel.setText(self.localization.get_string('brokerSellPriceLabel'))
        self.ui.expectedProfitLabel.setText(self.localization.get_string('expectedProfitLabel'))
        self.ui.deletePredictBtn.setText(self.localization.get_string('deletePredictBtn'))
        self.ui.completePredictBtn.setText(self.localization.get_string('completePredictBtn'))
        self.ui.savePredictBtn.setText(self.localization.get_string('savePredictBtn'))
