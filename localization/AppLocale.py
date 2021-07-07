from localization.languages.en import STRINGS as EN_STRINGS
from localization.languages.ru import STRINGS as RU_STRINGS

import config


class AppLocale:
    __instance = None

    @staticmethod
    def get_instance(language_code='en'):
        if AppLocale.__instance is None:
            AppLocale(language_code=language_code)
        return AppLocale.__instance

    def __init__(self, language_code='en'):
        if AppLocale.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AppLocale.__instance = self

        self.language_code = language_code
        self.default_language = config.APP_LANGUAGE
        self.languages = {
            'en': EN_STRINGS,
            'ru': RU_STRINGS,
        }

        if language_code not in self.languages:
            self.language_code = self.default_language

    def get_string(self, string_name='test_message'):
        if string_name in self.languages[self.language_code]:
            return self.languages[self.language_code][string_name]
        elif string_name in self.languages[self.default_language]:
            return self.languages[self.default_language][string_name]
        else:
            if config.DEBUG_MODE:
                self.languages[self.default_language]['test_message']
            else:
                self.languages[self.default_language]['empty']