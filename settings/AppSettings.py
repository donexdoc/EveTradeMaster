import os
import json

from patterns.Singleton import Singleton
import config


class AppSettings(metaclass=Singleton):

    def __init__(self):

        self.setting_file = config.SETTING_NAME
        self.settings = []

        self.__load_settings()

    def __setup_new_setting(function):
        def wrapper(self, *args, **kwargs):
            function(self, *args, **kwargs)
            self.__save_settings_file()
        return wrapper

    def __get_default_setting_value(self, setting_name):
        return self.__get_default_settings_dict()[setting_name]

    @__setup_new_setting
    def __setup_default_setting_value(self, setting_name):
        self.settings[setting_name] = self.__get_default_setting_value(setting_name)

    def __check_setting(setting_name):
        def decorator(function):
            def wrapper(self):
                if setting_name not in self.settings:
                    self.__setup_default_setting_value(setting_name)
                return function(self)
            return wrapper
        return decorator

    @__check_setting(setting_name='LANGUAGE')
    def get_app_language(self):
        return self.settings['LANGUAGE']

    @__check_setting('DEFAULT_SYSTEM_ID')
    def get_default_system(self):
        return self.settings['DEFAULT_SYSTEM_ID']

    @__check_setting('DEFAULT_REGION_ID')
    def get_default_region(self):
        return self.settings['DEFAULT_REGION_ID']

    @__check_setting('GOOD_MARGE_PERCENTAGE')
    def get_good_marge(self):
        return self.settings['GOOD_MARGE_PERCENTAGE']

    @__check_setting('BAD_MARGE_PERCENTAGE')
    def get_bad_marge(self):
        return self.settings['BAD_MARGE_PERCENTAGE']

    @__check_setting('EXPERIMENT_AMOUNT')
    def get_experiment_amount(self):
        return self.settings['EXPERIMENT_AMOUNT']

    @__check_setting('PRICE_DUMPING_SELL')
    def get_dumping_sell(self):
        return self.settings['PRICE_DUMPING_SELL']

    @__check_setting('PRICE_DUMPING_BUY')
    def get_dumping_buy(self):
        return self.settings['PRICE_DUMPING_BUY']

    @__check_setting('DEFAULT_TAX')
    def get_default_tax(self):
        return self.settings['DEFAULT_TAX']

    @__check_setting('BROKER_TAX')
    def get_broker_tax(self):
        return self.settings['BROKER_TAX']

    @__check_setting('DATABASE_MODELS_VERSION')
    def get_db_version(self):
        return self.settings['DATABASE_MODELS_VERSION']

    @__check_setting('APP_VERSION')
    def get_app_version(self):
        return self.settings['APP_VERSION']

    @__setup_new_setting
    def set_app_language(self, new_language):
        self.settings['LANGUAGE'] = new_language

    @__setup_new_setting
    def set_default_system(self, new_default_system):
        self.settings['DEFAULT_SYSTEM_ID'] = new_default_system

    @__setup_new_setting
    def set_default_region(self, new_default_region):
        self.settings['DEFAULT_REGION_ID'] = new_default_region

    @__setup_new_setting
    def set_good_marge(self, new_good_marge):
        self.settings['GOOD_MARGE_PERCENTAGE'] = new_good_marge

    @__setup_new_setting
    def set_bad_marge(self, new_bad_marge):
        self.settings['BAD_MARGE_PERCENTAGE'] = new_bad_marge

    @__setup_new_setting
    def set_experiment_amount(self, new_experiment_amount):
        self.settings['EXPERIMENT_AMOUNT'] = new_experiment_amount

    @__setup_new_setting
    def set_dumping_sell(self, new_dumping_sell):
        self.settings['PRICE_DUMPING_SELL'] = new_dumping_sell

    @__setup_new_setting
    def set_dumping_buy(self, new_dumping_buy):
        self.settings['PRICE_DUMPING_BUY'] = new_dumping_buy

    @__setup_new_setting
    def set_default_tax(self, new_default_tax):
        self.settings['DEFAULT_TAX'] = new_default_tax

    @__setup_new_setting
    def set_broker_tax(self, new_broker_tax):
        self.settings['BROKER_TAX'] = new_broker_tax

    @__setup_new_setting
    def set_language(self, lang_name):
        self.settings['LANGUAGE'] = lang_name

    @__setup_new_setting
    def set_db_version(self, new_db_version):
        self.settings['DATABASE_MODELS_VERSION'] = new_db_version

    @__setup_new_setting
    def set_app_version(self, new_app_version):
        self.settings['APP_VERSION'] = new_app_version

    def update_app_version(self):
        self.set_app_version(self.__get_default_setting_value('APP_VERSION'))

    def update_db_version(self):
        self.set_db_version_version(self.__get_default_setting_value('DATABASE_MODELS_VERSION'))

    def __load_settings(self):
        if os.path.isfile(self.setting_file):
            try:
                with open(self.setting_file, 'r') as reading_file:
                    self.settings = json.loads(reading_file.read())

            except Exception as e:
                return self.__create_default_file()
        else:
            return self.__create_default_file()

    def __get_default_settings_dict(self):
       return {
            'DEFAULT_SYSTEM_ID': config.DEFAULT_SYSTEM_ID,
            'DEFAULT_REGION_ID': config.DEFAULT_REGION_ID,
            'GOOD_MARGE_PERCENTAGE': config.GOOD_MARGE_PERCENTAGE,
            'BAD_MARGE_PERCENTAGE': config.BAD_MARGE_PERCENTAGE,
            'EXPERIMENT_AMOUNT': config.EXPERIMENT_AMOUNT,
            'PRICE_DUMPING_SELL': config.PRICE_DUMPING_SELL,
            'PRICE_DUMPING_BUY': config.PRICE_DUMPING_BUY,
            'DEFAULT_TAX': config.DEFAULT_TAX,
            'BROKER_TAX': config.BROKER_TAX,
            'LANGUAGE': config.APP_LANGUAGE,
            'DATABASE_MODELS_VERSION': config.DATABASE_MODELS_VERSION,
            'APP_VERSION': config.APP_VERSION,
        }

    def __set_default_settings(self):
        self.settings = json.dumps(self.__get_default_settings_dict())

    def __create_default_file(self):
        self.__set_default_settings()
        return self.__save_settings_file()

    def __save_settings_file(self):

        save_file = open(self.setting_file, 'w+')
        save_file.write(self.settings)
        save_file.close()

        return self.__load_settings()
