# комиссия брокера
BROKER_TAX = 5.0

# налог с продажи
DEFAULT_TAX = 5.0

# демпинг
PRICE_DUMPING_SELL = 1.0
PRICE_DUMPING_BUY = 1.0

# информация по приложению
DATABASE_MODELS_VERSION = '1.0'
APP_VERSION = '0.2.1'

# стоимость эксперимента
EXPERIMENT_AMOUNT = 100000000

# проценты маржи
GOOD_MARGE_PERCENTAGE = 20.0
BAD_MARGE_PERCENTAGE = 5.0

# Jitia ID
DEFAULT_SYSTEM_ID = 30000142

# The Forge ID
DEFAULT_REGION_ID = 10000002

DB_NAME = "app.db"
SETTING_NAME = "settings.json"

APP_NAME = "EVE Trade Master"
APP_LANGUAGE = "en"

TABLE_PREDICT_HEADERS = [
    'Type',
    'name',
    'group',
    'min sell',
    'max buy',
    'marge',
    'marge percent',
    'recommended sell',
    'recommended buy',
    'profit per one',
    'experiment volume',
    'experiment cost',
    'experiment profit',
 ]

TABLE_TYPES_HEADERS = [
    'id',
    'name',
    'group',
    'in default predict',
]

# Debug variables
DEBUG_MODE = True
test_default_predict_line = "4310, 16240, 16242, 32880, 28668, 439"