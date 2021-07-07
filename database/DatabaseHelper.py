"""
Класс для работы с БД
"""

from database.models import (
    GroupType,
    GameType,
    PricePrediction,
)
from ESIAPI import APIHelper

from peewee import SqliteDatabase

import peeweedbevolve
import config

api = APIHelper(debug=config.DEBUG_MODE)


class DatabaseHelper:

    @staticmethod
    def create_tables():

        print("creating tables")

        db = SqliteDatabase(
            config.DB_NAME
        )
        db.create_tables([GroupType, GameType, PricePrediction])
        # db.evolve()
        print("Finish")

    @staticmethod
    def get_type(type_id):

        try:
            game_type = GameType.get(GameType.id == type_id)
        except GameType.DoesNotExist:
            game_type_info = api.type_info(type_id)['content']
            game_type = GameType.create(
                id=type_id,
                name=game_type_info['name'],
                group=DatabaseHelper.get_group(game_type_info['group_id'])
            )

        return game_type

    @staticmethod
    def get_all_types():
        game_types = GameType.select()
        result = []
        for game_type in game_types:
            result.append(game_type)

        return result

    @staticmethod
    def get_all_default_types():
        game_types = GameType.select().where(GameType.in_default_predict == True)
        return game_types

    @staticmethod
    def get_group(group_id):

        try:
            group = GroupType.get(GroupType.id == group_id)
        except GroupType.DoesNotExist:
            group_info = api.group_info(group_id)['content']
            group = GroupType.create(
                id=group_id,
                name=group_info['name']
            )

        return group

    @staticmethod
    def delete_unsaved_predictions():
        unsaved = PricePrediction.select().where(PricePrediction.experiment_saved == 0)
        for predict in unsaved:
            predict.delete_instance()

    @staticmethod
    def get_predict(predict_id):
        return PricePrediction.get_by_id(predict_id)

    @staticmethod
    def create_predict(game_type, prediction_name, min_sell_price, max_buy_price,
                       marge_price, marge_percent,
                       recommended_sell, recommended_buy,
                       profit_per_one, experiment_cost, experiment_volume, experiment_profit):

        predict = PricePrediction.create(
            game_type=game_type,
            name=prediction_name,
            min_sell_price=min_sell_price,
            max_buy_price=max_buy_price,
            marge_price=marge_price,
            marge_percent=marge_percent,
            recommended_sell=recommended_sell,
            recommended_buy=recommended_buy,
            profit_per_one=profit_per_one,
            experiment_volume=experiment_volume,
            experiment_cost=experiment_cost,
            experiment_profit=experiment_profit,
            current_profit=experiment_profit
        )
        return predict
