from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PySide2.QtCore import Qt

from settings.AppSettings import AppSettings
from localization.AppLocale import AppLocale
from appui.design.pyforms.MainWindowForm import Ui_MainWindow
from appui.controllers.AddTypeFormController import AddTypeWindow
from appui.controllers.SavePredictFormController import SavePredictWindow
from appui.controllers.EditPredictFormController import EditPredictWindow
from ESIAPI import APIHelper
from database.DatabaseHelper import DatabaseHelper
from database.models import (
    PricePrediction,
    GameType
)

import config
import sys
import threading


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Инициализация пользовательского интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Настройка элементов
        if config.DEBUG_MODE:
            self.ui.inputIdsLe.setText(config.test_default_predict_line)

        # API + DB + localization + settings
        self.api_helper = APIHelper(debug=config.DEBUG_MODE)
        self.db_helper = DatabaseHelper()
        self.db_helper.create_tables()
        self.app_settings = AppSettings()
        self.localization = AppLocale.get_instance(language_code=self.app_settings.get_setting('LANGUAGE'))

        # локальные переменные
        self.predictions = []
        self.game_types = []
        self.saved_predictions = []
        self.tables_titles = config.TABLE_PREDICT_HEADERS
        self.types_tables_titles = config.TABLE_TYPES_HEADERS

        # инициализируем функции интерактивных элементов
        self.ui.newPredictionBtn.clicked.connect(self.create_new_prediction)
        self.ui.unsavedPredictionsTw.doubleClicked.connect(self.save_prediction)
        self.ui.savedPredictionsTw.doubleClicked.connect(self.edit_prediction)
        self.ui.savedTypesTw.doubleClicked.connect(self.type_default_predict_change)
        self.ui.addTypesBtn.clicked.connect(self.add_more_types)
        self.ui.defaultPredictionBtn.clicked.connect(self.prediction_from_default)

        # переводим форму
        self.load_localization()
        # загружаем данные из БД
        self.load_types()
        self.load_saved_predictions()

        # выводим информацию
        self.unsaved_table_load()
        self.saved_table_load()
        self.types_table_load()

    def load_localization(self):
        self.ui.newPredictionBtn.setText(self.localization.get_string('newPredictionBtn'))
        self.ui.defaultPredictionBtn.setText(self.localization.get_string('defaultPredictionBtn'))
        self.ui.savedPredictsFilterLabel.setText(self.localization.get_string('savedPredictsFilterLabel'))
        self.ui.savedPredictionsFilterCmbb.setPlaceholderText(self.localization.get_string('savedPredictionsFilterCmbb'))
        self.ui.savedItemsFilterLabel.setText(self.localization.get_string('savedItemsFilterLabel'))
        self.ui.typesFIlterCmbb.setPlaceholderText(self.localization.get_string('typesFIlterCmbb'))
        self.ui.addTypesBtn.setText(self.localization.get_string('addTypesBtn'))
        self.ui.newPredictionBtn.setText(self.localization.get_string('newPredictionBtn'))
        self.ui.newPredictionBtn.setText(self.localization.get_string('newPredictionBtn'))

        self.tables_titles = [
            self.localization.get_string('tableType'),
            self.localization.get_string('tablePredictName'),
            self.localization.get_string('tableName'),
            self.localization.get_string('tableGroup'),
            self.localization.get_string('tableMinSell'),
            self.localization.get_string('tableMaxBuy'),
            self.localization.get_string('tableMarge'),
            self.localization.get_string('tableMargePercent'),
            self.localization.get_string('tableRecommendedSell'),
            self.localization.get_string('tableRecommendedBuy'),
            self.localization.get_string('tableProfitPerOne'),
            self.localization.get_string('tableExperimentVolume'),
            self.localization.get_string('tableExperimentCost'),
            self.localization.get_string('tableExperimentProfit'),
        ]
        self.types_tables_titles = [
            self.localization.get_string('typesTableId'),
            self.localization.get_string('typesTableName'),
            self.localization.get_string('typesTableGroup'),
            self.localization.get_string('typesTableInDefault'),
        ]

    def edit_prediction(self, item):
        selected_prediction = self.saved_predictions[item.row()]

        dialog_edit = EditPredictWindow(self, selected_prediction)
        dialog_edit.setModal(True)
        dialog_edit.setWindowTitle(self.localization.get_string('editPredictFormTitle'))
        dialog_edit.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        dialog_edit.exec_()

        self.load_saved_predictions()
        self.saved_table_load()

    def save_prediction(self, item):
        selected_prediction = self.predictions[item.row()]

        dialog_add = SavePredictWindow(self, selected_prediction)
        dialog_add.setModal(True)
        dialog_add.setWindowTitle(self.localization.get_string('savePredictFormTitle'))
        dialog_add.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        dialog_add.exec_()

        # selected_prediction.experiment_saved = True
        # selected_prediction.save()

        self.load_saved_predictions()
        self.saved_table_load()

    def prediction_from_default(self):
        self.db_helper.delete_unsaved_predictions()
        default_prediction_types = self.db_helper.get_all_default_types()
        print(default_prediction_types)
        self.prediction(default_prediction_types)

    def type_default_predict_change(self, item):
        edited_game_type = self.game_types[item.row()]

        if item.column() == 3:
            edited_game_type.in_default_predict = not edited_game_type.in_default_predict
            edited_game_type.save()
            self.types_table_load()

    def types_table_load(self):

        self.ui.savedTypesTw.setRowCount(0)

        self.ui.savedTypesTw.setColumnCount(len(self.types_tables_titles))
        self.ui.savedTypesTw.setHorizontalHeaderLabels(self.types_tables_titles)

        for type_index, game_type in enumerate(self.game_types):
            self.ui.savedTypesTw.insertRow(type_index)

            cols = [
                QTableWidgetItem(str(game_type.id)),
                QTableWidgetItem(game_type.name),
                QTableWidgetItem(game_type.group.name),
                QTableWidgetItem(str(game_type.in_default_predict)),
            ]

            for column_index, column in enumerate(cols):
                column.setTextAlignment(Qt.AlignHCenter)
                column.setFlags(column.flags() ^ Qt.ItemIsEditable)
                if game_type.in_default_predict:
                    column.setBackgroundColor("#6BCA5C")
                self.ui.savedTypesTw.setItem(type_index, column_index, column)

        self.ui.savedTypesTw.resizeColumnsToContents()
        self.ui.savedTypesTw.resizeRowsToContents()

    def saved_table_load(self):

        self.ui.savedPredictionsTw.setRowCount(0)

        self.ui.savedPredictionsTw.setColumnCount(len(self.tables_titles))
        self.ui.savedPredictionsTw.setHorizontalHeaderLabels(self.tables_titles)

        for predict_index, predict in enumerate(self.saved_predictions):
            self.ui.savedPredictionsTw.insertRow(predict_index)
            cols = [
                QTableWidgetItem(str(predict.game_type.id)),
                QTableWidgetItem(predict.name),
                QTableWidgetItem(predict.game_type.name),
                QTableWidgetItem(predict.game_type.group.name),
                QTableWidgetItem(str(predict.min_sell_price)),
                QTableWidgetItem(str(predict.max_buy_price)),
                QTableWidgetItem(str(predict.marge_price)),
                QTableWidgetItem(str(predict.marge_percent)),
                QTableWidgetItem(str(predict.recommended_sell)),
                QTableWidgetItem(str(predict.recommended_buy)),
                QTableWidgetItem(str(predict.profit_per_one)),
                QTableWidgetItem(str(predict.experiment_volume)),
                QTableWidgetItem(str(predict.experiment_cost)),
                QTableWidgetItem(str(predict.experiment_profit)),
            ]
            for column_index, column in enumerate(cols):
                column.setTextAlignment(Qt.AlignHCenter)
                column.setFlags(column.flags() ^ Qt.ItemIsEditable)
                if predict.marge_percent >= self.app_settings.get_setting('GOOD_MARGE_PERCENTAGE'):
                    column.setBackgroundColor("#6BCA5C")
                if predict.marge_percent <= self.app_settings.get_setting('BAD_MARGE_PERCENTAGE'):
                    column.setBackgroundColor("#C17D0F")

                if predict.experiment_ended:
                    column.setBackgroundColor("#E1E1E1")

                self.ui.savedPredictionsTw.setItem(predict_index, column_index, column)
        self.ui.savedPredictionsTw.resizeColumnsToContents()
        self.ui.savedPredictionsTw.resizeRowsToContents()

    def unsaved_table_load(self):
        self.ui.unsavedPredictionsTw.setRowCount(0)

        self.ui.unsavedPredictionsTw.setColumnCount(len(self.tables_titles))
        self.ui.unsavedPredictionsTw.setHorizontalHeaderLabels(self.tables_titles)
        for predict_index, predict in enumerate(self.predictions):
            self.ui.unsavedPredictionsTw.insertRow(predict_index)

            cols = [
                QTableWidgetItem(str(predict.game_type.id)),
                QTableWidgetItem(predict.name),
                QTableWidgetItem(predict.game_type.name),
                QTableWidgetItem(predict.game_type.group.name),
                QTableWidgetItem(str(predict.min_sell_price)),
                QTableWidgetItem(str(predict.max_buy_price)),
                QTableWidgetItem(str(predict.marge_price)),
                QTableWidgetItem(str(predict.marge_percent)),
                QTableWidgetItem(str(predict.recommended_sell)),
                QTableWidgetItem(str(predict.recommended_buy)),
                QTableWidgetItem(str(predict.profit_per_one)),
                QTableWidgetItem(str(predict.experiment_volume)),
                QTableWidgetItem(str(predict.experiment_cost)),
                QTableWidgetItem(str(predict.experiment_profit)),
            ]
            for column_index, column in enumerate(cols):
                column.setTextAlignment(Qt.AlignHCenter)
                column.setFlags(column.flags() ^ Qt.ItemIsEditable)
                if predict.marge_percent >= self.app_settings.get_setting('GOOD_MARGE_PERCENTAGE'):
                    column.setBackgroundColor("#6BCA5C")
                if predict.marge_percent <= self.app_settings.get_setting('BAD_MARGE_PERCENTAGE'):
                    column.setBackgroundColor("#C17D0F")
                self.ui.unsavedPredictionsTw.setItem(predict_index, column_index, column)

        self.ui.unsavedPredictionsTw.resizeColumnsToContents()
        self.ui.unsavedPredictionsTw.resizeRowsToContents()

    def create_new_prediction(self):
        self.db_helper.delete_unsaved_predictions()

        game_types_input = self.ui.inputIdsLe.text().split(',')
        game_types = []

        if self.api_helper.api_status():
            for input_type in game_types_input:
                try:
                    inputed_type = self.db_helper.get_type(int(input_type.strip()))
                    game_types.append(inputed_type)
                except Exception as e:
                    print(f"Parsing error on type: {input_type}\nwith error: {sys.exc_info()}")

            # print(game_types)
            self.prediction(game_types)
        else:
            self.show_connect_error()

        self.load_types()
        self.types_table_load()

    def show_connect_error(self):
        esi_connect_error_mb = QMessageBox()

        esi_connect_error_mb.question(
            self,
            self.localization.get_string('connectErrorTitle'),
            self.localization.get_string('connectErrorMessage'),
            esi_connect_error_mb.Ok
        )

    def prediction(self, game_types):
        self.predictions = []
        predict_threads = []

        for game_type in game_types:
            new_predict = threading.Thread(target=self.add_prediction, args=(game_type,))
            new_predict.start()
            predict_threads.append(new_predict)

        for thread in predict_threads:
            thread.join()

        self.predictions.sort(key=lambda x: x.experiment_profit, reverse=True)
        self.unsaved_table_load()

    def add_prediction(self, game_type):
        prices = self.api_helper.item_pricing_info(
            game_type.id,
            [self.app_settings.get_setting('DEFAULT_REGION_ID')],
            [self.app_settings.get_setting('DEFAULT_SYSTEM_ID')]
        )

        # расчет маржи по штуке и процента маржи
        marge_pricing = prices['min_sell'] - prices['max_buy']
        marge_by_percent = prices['min_sell'] / 100.0
        try:
            marge_percentage = marge_pricing / marge_by_percent
        except Exception as e:
            marge_percentage = 0

        # рекомендуемая цена, выставляемая в маркете
        recommended_sell = prices['min_sell'] - self.app_settings.get_setting('PRICE_DUMPING_SELL')
        recommended_buy = prices['max_buy'] + self.app_settings.get_setting('PRICE_DUMPING_BUY')

        # расчет цены рекомендуемой продажи
        recommended_sell_percent = prices['min_sell'] / 100.0
        recommended_sell_tax = recommended_sell_percent * self.app_settings.get_setting('DEFAULT_TAX') + \
                               recommended_sell_percent * self.app_settings.get_setting('BROKER_TAX')
        # итоговая цена рекомендуемой цены продажи
        recommended_sell_amount = recommended_sell + recommended_sell_tax

        # расчет цены рекомендуемой покупки
        recommended_buy_percent = recommended_buy / 100.0
        recommended_buy_tax = recommended_buy_percent * self.app_settings.get_setting('BROKER_TAX')

        # итоговая цена рекомендуемой цены покупки
        recommended_buy_amount = recommended_buy + recommended_buy_tax

        # ожидаемый профит от одной штуки
        expected_profit_per_one = recommended_sell_amount - recommended_buy_amount

        # стоимость эксперимента
        # кол-во позиций по цене, подходящей для покупки исходя из цены покупки
        experiment_volume = int(self.app_settings.get_setting('EXPERIMENT_AMOUNT') / recommended_buy_amount)
        # цена эксперимента
        expected_experiment_cost = experiment_volume * recommended_buy_amount
        # ожидаемый финальный профит за эксперимент
        expected_experiment_profit = experiment_volume * expected_profit_per_one

        prediction = PricePrediction.create(
            name=game_type.name,
            game_type=game_type,
            min_sell_price=prices['min_sell'],
            max_buy_price=prices['max_buy'],
            marge_price=marge_pricing,
            marge_percent=marge_percentage,
            recommended_sell=recommended_sell,
            recommended_buy=recommended_buy,
            profit_per_one=expected_profit_per_one,
            experiment_volume=experiment_volume,
            experiment_cost=expected_experiment_cost,
            experiment_profit=expected_experiment_profit,
            current_profit=expected_experiment_profit
        )
        self.predictions.append(prediction)

    def load_types(self):
        self.game_types = list(GameType.select())

    def load_saved_predictions(self):
        self.saved_predictions = list(PricePrediction.select().where(PricePrediction.experiment_saved == True))

    def add_more_types(self):
        dialog_add = AddTypeWindow(self)
        dialog_add.setModal(True)
        dialog_add.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        dialog_add.exec_()
