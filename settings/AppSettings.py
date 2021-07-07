import os
import json

import config


class AppSettings:
    __instance = None

    @staticmethod
    def get_instance():
        if AppSettings.__instance is None:
            AppSettings()
        return AppSettings.__instance

    def __init__(self):
        if AppSettings.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AppSettings.__instance = self

        self.setting_file = config.SETTING_NAME
        self.settings = json.dumps({})

        self.__load_settings()

    def __load_settings(self):
        if os.path.isfile(self.setting_file):
            try:
                sf = open(self.setting_file)
                self.settings = json.loads(sf.read())
                print(self.settings)
                sf.close()
            except Exception as e:
                self.__create_default_file()
                print("Setting file reading error")
        else:
            return self.__create_default_file()

    def get_setting(self, setting_name):
        return self.settings[setting_name]

    def __set_default_settings(self):
        self.settings = json.dumps(
            {
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
            }
        )

    def __create_default_file(self):
        self.__set_default_settings()
        return self.__save_settings_file()

    def __save_settings_file(self):

        sf = open(self.setting_file, 'w+')
        sf.write(self.settings)
        sf.close()
        return self.__load_settings()
