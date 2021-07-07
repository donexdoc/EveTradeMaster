from PySide2.QtWidgets import QDialog

from localization.AppLocale import AppLocale
from appui.design.pyforms.SavePredictionForm import Ui_DialogSavePredict


class SavePredictWindow(QDialog):
    """
    Форма для добавления новых игровых типов
    """

    def __init__(self, parent, predict):
        super(SavePredictWindow, self).__init__(parent)

        self.ui = Ui_DialogSavePredict()
        self.ui.setupUi(self)

        self.localization = parent.localization

        # from parent
        self.parent = parent
        self.predict = predict

        # UI interact setup
        self.ui.savePredictionBtn.clicked.connect(self.save_prediction)
        self.ui.sellPriceRecomendedLe.textChanged.connect(self.values_edit)
        self.ui.buyPriceRecomendedLe.textChanged.connect(self.values_edit)
        self.ui.experimentVolumeLe.textChanged.connect(self.values_edit)

        # form load
        self.load_localization()
        self.setup_predict()

    def values_edit(self):
        try:
            sell = float(self.ui.sellPriceRecomendedLe.text())
            buy = float(self.ui.buyPriceRecomendedLe.text())
            volume = float(self.ui.experimentVolumeLe.text())

            # рекомендуемая цена, выставляемая в маркете
            recommended_sell = sell - self.parent.app_settings.get_setting('PRICE_DUMPING_SELL')
            recommended_buy = buy + self.parent.app_settings.get_setting('PRICE_DUMPING_BUY')

            # расчет цены рекомендуемой продажи
            recommended_sell_percent = sell / 100.0
            recommended_sell_tax = recommended_sell_percent * self.parent.app_settings.get_setting('DEFAULT_TAX') + \
                                   recommended_sell_percent * self.parent.app_settings.get_setting('BROKER_TAX')
            # итоговая цена рекомендуемой цены продажи
            recommended_sell_amount = recommended_sell + recommended_sell_tax

            # расчет цены рекомендуемой покупки
            recommended_buy_percent = recommended_buy / 100.0
            recommended_buy_tax = recommended_buy_percent * self.parent.app_settings.get_setting('BROKER_TAX')

            # итоговая цена рекомендуемой цены покупки
            recommended_buy_amount = recommended_buy + recommended_buy_tax

            # ожидаемый профит от одной штуки
            expected_profit_per_one = recommended_sell_amount - recommended_buy_amount

            self.ui.experimentCostLe.setText(str(volume * buy))
            self.ui.experimentProfitLe.setText(str(volume * expected_profit_per_one))
        except Exception as e:
            print('Experiment cost or profit calculating error')

    def save_prediction(self):
        try:
            self.predict.name = str(self.ui.predictNameLe.text())
            self.predict.recommended_sell = float(self.ui.sellPriceRecomendedLe.text())
            self.predict.recommended_buy = float(self.ui.buyPriceRecomendedLe.text())
            self.predict.experiment_volume = float(self.ui.experimentVolumeLe.text())
            self.predict.experiment_cost = float(self.ui.experimentCostLe.text())
            self.predict.experiment_profit = float(self.ui.experimentProfitLe.text())
            self.predict.experiment_saved = True
            self.predict.save()
            self.close()
        except Exception as e:
            print("Prediction saving error")

    def setup_predict(self):
        self.ui.predictNameLe.setText(self.predict.name)
        self.ui.predictTypeNameLb.setText(self.predict.game_type.name)
        self.ui.predictTypeIdLb.setText(str(self.predict.game_type.id))
        self.ui.mergePercentLb.setText(str(self.predict.marge_percent))
        self.ui.profitPerOneLb.setText(str(self.predict.profit_per_one))
        self.ui.sellPriceRecomendedLe.setText(str(self.predict.recommended_sell))
        self.ui.buyPriceRecomendedLe.setText(str(self.predict.recommended_buy))
        self.ui.experimentVolumeLe.setText(str(self.predict.experiment_volume))
        self.ui.experimentCostLe.setText(str(self.predict.experiment_cost))
        self.ui.experimentProfitLe.setText(str(self.predict.experiment_profit))

    def load_localization(self):
        self.ui.predictNameLabel.setText(self.localization.get_string('predictNameLabel'))
        self.ui.predictTypeNameLabel.setText(self.localization.get_string('predictTypeNameLabel'))
        self.ui.predictTypeIdLabel.setText(self.localization.get_string('predictTypeIdLabel'))
        self.ui.mergePercentLabel.setText(self.localization.get_string('mergePercentLabel'))
        self.ui.profitPerOneLabel.setText(self.localization.get_string('profitPerOneLabel'))
        self.ui.sellPriceRecommendedLabel.setText(self.localization.get_string('sellPriceRecommendedLabel'))
        self.ui.buyPriceRecommendedLabel.setText(self.localization.get_string('buyPriceRecommendedLabel'))
        self.ui.experimentVolumeLabel.setText(self.localization.get_string('experimentVolumeLabel'))
        self.ui.experimentCostLabel.setText(self.localization.get_string('experimentCostLabel'))
        self.ui.experimentProfitLabel.setText(self.localization.get_string('experimentProfitLabel'))
        self.ui.savePredictionBtn.setText(self.localization.get_string('savePredictionBtn'))
