import sys
from PySide2.QtWidgets import QDialog

from localization.AppLocale import AppLocale
from database.DatabaseHelper import DatabaseHelper
from appui.design.pyforms.AddTypesForm import Ui_DialogAddTypes


class AddTypeWindow(QDialog):
    """
    Форма для добавления новых игровых типов
    """

    def __init__(self, parent):
        super(AddTypeWindow, self).__init__(parent)

        self.ui = Ui_DialogAddTypes()
        self.ui.setupUi(self)
        self.parent = parent

        self.db_helper = DatabaseHelper()
        self.localization = AppLocale.get_instance(language_code='ru')

        self.parsed_types = []
        self.ui.checkAndAddBtn.clicked.connect(self.parse_types)

        self.load_localization()

    def load_localization(self):
        self.ui.checkAndAddBtn.setText(self.localization.get_string('checkAndAddBtn'))
        self.ui.addNewTypesAddedLabel.setText(self.localization.get_string('addNewTypesAddedLabel'))

    def parse_types(self):
        self.parsed_types = []
        game_types_input = self.ui.typesInputTe.text().split(',')
        db_types = self.db_helper.get_all_types()
        for input_type in game_types_input:
            if input_type not in db_types:
                try:
                    inputed_type = self.db_helper.get_type(int(input_type.strip()))
                    self.parsed_types.append(inputed_type)
                except Exception as e:
                    print(f"Parsing error on type: {input_type}\nwith error: {sys.exc_info()}")

        print(self.parsed_types)
        self.print_to_lv()
        self.parent.load_types()
        self.parent.types_table_load()

    def print_to_lv(self):
        lv_items = []
        for game_type in self.parsed_types:
            lv_items.append(f"{game_type.name} - {game_type.id}")
        self.ui.typesLw.addItems(lv_items)




