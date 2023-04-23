from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QGroupBox, QPushButton, QLineEdit

from utils.configuration import Configuration


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.editor = {
            'prompt': QTextEdit(),
        }

        self.setWindowTitle('Settings')
        self.config = Configuration()
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.config_dict = self.config.get_all()
        self.modified_config = self.config_dict.copy()

        for sec in self.config_dict.keys():
            self.verticalLayout.addWidget(self.setting_group(sec, self.config_dict[sec]))

        self.confirm_button = QPushButton('Confirm')
        self.confirm_button.clicked.connect(self.confirm)
        self.verticalLayout.addWidget(self.confirm_button)
        self.setLayout(self.verticalLayout)

    def confirm(self):
        print(self.modified_config)
        self.config.read_dict(self.modified_config)
        self.close()

    def setting_group(self, sec, keys: dict):
        group_box = QGroupBox()
        group_box.setTitle(str(sec))
        group_box.setMinimumWidth(500)
        layout = QVBoxLayout(group_box)
        for k in keys:
            label = QLabel(k)
            text_input = self.editor.get(k, QLineEdit())
            text_input.setText(keys[k])
            text_input.textChanged.connect(lambda text, key=k: self.modified_config[sec].update({key: text}))
            layout.addWidget(label)
            layout.addWidget(text_input)

        return group_box
