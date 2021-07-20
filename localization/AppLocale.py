from localization.languages.en import STRINGS as EN_STRINGS
from localization.languages.ru import STRINGS as RU_STRINGS

from patterns.Singleton import Singleton
import config


class AppLocale(metaclass=Singleton):

    def __init__(self, language_code='en'):

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