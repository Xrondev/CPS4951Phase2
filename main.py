from PySide6.QtWidgets import QMainWindow, QApplication, QSizePolicy
from qt_material import apply_stylesheet

from ui.dynamic_conversation import ConversationWidget
from ui.main_window import Ui_Form


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.conversation_widget = ConversationWidget()
        self.conversation_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # test: draw a border around the conversation widget
        # self.conversation_widget.setStyleSheet("border: 1px solid black;")
        self.gridLayout_2.addWidget(self.conversation_widget)

        self.pushButton_2.clicked.connect(self.add_conversation)
        self.pushButton.clicked.connect(self.conversation_widget.clear_conversation)

    def add_conversation(self):
        # get the text
        text = self.textEdit.toPlainText()
        # clear the text
        self.textEdit.clear()
        self.conversation_widget.add_message("user", text)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    apply_stylesheet(app, theme='light_blue.xml')
    window.show()
    app.exec()
