from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon

from appui.controllers.MainFormController import MainWindow

import sys
import os

import config
from ESIAPI import APIHelper

api = APIHelper(debug=config.DEBUG_MODE)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./assets")

    return os.path.join(base_path, relative_path)


def main():
    app = QApplication([])
    app.setApplicationName(config.APP_NAME)
    application = MainWindow()

    app_icon = QIcon()
    app_icon.addFile(resource_path("EveTradeMaster.svg"), QSize(), QIcon.Normal, QIcon.Off)
    application.setWindowIcon(app_icon)

    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
