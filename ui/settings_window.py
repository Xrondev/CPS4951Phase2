"""
Create the setting window for user to change the config file in a more convenient way
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QGroupBox,\
    QPushButton, QLineEdit
from utils.configuration import Configuration


class SettingsWindow(QWidget):
    """
    This window is used to display the settings of the program, and allow the user to change them.
    """
    def __init__(self):
        super().__init__()

        self.editor = {
            'prompt': QTextEdit(),
        }

        self.setWindowTitle('Settings')
        self.config = Configuration()
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setObjectName("verticalLayout")

        self.config_dict = self.config.get_all()
        self.modified_config = self.config_dict.copy()

        for sec, pair in self.config_dict.items():
            self.vertical_layout.addWidget(self.setting_group(sec, pair))

        self.confirm_button = QPushButton('Confirm')
        self.confirm_button.clicked.connect(self.confirm)
        self.vertical_layout.addWidget(self.confirm_button)
        self.setLayout(self.vertical_layout)

    def confirm(self) -> None:
        """
        Confirm the changes and save the config file, then close the window
        """
        print(self.modified_config)
        self.config.read_dict_save(self.modified_config)
        self.close()

    def setting_group(self, sec, keys: dict) -> QGroupBox:
        """
        Dynamically create a group box for each section in the config file and change the text input
        type according to the type of the value
        :param sec: The section name from the config file. (e.g. 'model')
        :param keys: The key-value pairs in the section. (e.g. {'model': 'gpt-3.5-turbo'})
        :return: A QGroupBox object
        """
        group_box = QGroupBox()
        group_box.setTitle(str(sec))
        group_box.setMinimumWidth(500)
        layout = QVBoxLayout(group_box)
        for k in keys:
            label = QLabel(k)
            text_input = self.editor.get(k, QLineEdit())
            text_input.setText(keys[k])
            text_input.textChanged.connect(
                lambda text, key=k: self.modified_config[sec].update({key: text}))
            layout.addWidget(label)
            layout.addWidget(text_input)

        return group_box
