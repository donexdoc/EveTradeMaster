from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon

from appui.controllers.MainFormController import MainWindow
from resources.Resources import Resources

import sys

import config


def main():
    resource_manager = Resources()

    app = QApplication([])
    app.setApplicationName(config.APP_NAME)
    application = MainWindow()

    app_icon = QIcon()
    app_icon.addFile(resource_manager.resource_path("EveTradeMaster.svg"), QSize(), QIcon.Normal, QIcon.Off)
    application.setWindowIcon(app_icon)

    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
