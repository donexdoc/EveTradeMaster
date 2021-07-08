"""
Модели БД
"""
import datetime

from peewee import (
    Model,
    IntegerField,
    DateTimeField,
    FloatField,
    CharField,
    ForeignKeyField,
    DateField,
    BooleanField,
    PrimaryKeyField
)
from peewee import SqliteDatabase

import config


class BaseModel(Model):

    class Meta:
        database = SqliteDatabase(
            config.DB_NAME
        )


class GroupType(BaseModel):
    id = PrimaryKeyField()
    name = CharField(default="")


class GameType(BaseModel):
    id = PrimaryKeyField()
    name = CharField(default="")
    group = ForeignKeyField(GroupType, to_field="id", on_delete='CASCADE')
    in_default_predict = BooleanField(default=False)


class PricePrediction(BaseModel):
    id = PrimaryKeyField()
    name = CharField(default="New prediction")
    game_type = ForeignKeyField(GameType, to_field="id", on_delete='CASCADE')
    prediction_date = DateTimeField(default=datetime.datetime.now())
    min_sell_price = FloatField()
    max_buy_price = FloatField()
    marge_price = FloatField()
    marge_percent = FloatField()
    recommended_sell = FloatField()
    recommended_buy = FloatField()
    profit_per_one = FloatField()
    experiment_volume = FloatField()
    experiment_cost = FloatField()
    experiment_profit = FloatField()
    experiment_ended = BooleanField(default=False)
    experiment_saved = BooleanField(default=False)
    current_profit = FloatField()


