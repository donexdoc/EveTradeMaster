import sys
import os

from patterns.Singleton import Singleton


class Resources(metaclass=Singleton):

    def __init__(self):
        print("Resources init complete")

        self.abs_path = os.path.abspath("./assets")

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except BaseException as e:
            base_path = self.abs_path

        return os.path.join(base_path, relative_path)
