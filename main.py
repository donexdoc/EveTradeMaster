from PySide2.QtWidgets import QApplication
from appui.controllers.MainFormController import MainWindow

import sys

import config
from ESIAPI import APIHelper

api = APIHelper(debug=config.DEBUG_MODE)


def main():
    app = QApplication([])
    app.setApplicationName(config.APP_NAME)
    application = MainWindow()

    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
