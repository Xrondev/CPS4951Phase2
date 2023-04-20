import threading
import time
from functools import partial

from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QApplication, QSizePolicy, QWidget, QGridLayout
from qt_material import apply_stylesheet
from ui.dynamic_conversation import ConversationWidget
from ui.main_window import Ui_Form
from utils.chat_session_maintainer import ChatSessionMaintainer


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.csm = ChatSessionMaintainer()

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
        self.conversation_widget.add_message('user', text)
        print('sending text: ', text)

        # Use multithreading to run the chat() method in a separate thread
        t = threading.Thread(target=partial(self.run_chat, text))
        t.start()

    def run_chat(self, text):
        emotion_dict = self.videoWidget.result
        response = self.csm.chat(text, emotion_dict)
        # Update the GUI from the main thread using a signal
        self.update_conversation_widget_signal.emit(response)

    def update_conversation_widget(self, response):
        self.conversation_widget.add_message('gpt', response)

    # Define a custom signal to update the conversation widget from another thread
    update_conversation_widget_signal = QtCore.Signal(str)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    apply_stylesheet(app, theme='dark_blue.xml')
    window.update_conversation_widget_signal.connect(window.update_conversation_widget)
    window.show()
    app.exec()
