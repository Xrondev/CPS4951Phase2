"""Main Entry Point for the GUI Application"""

import threading
from functools import partial

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QSizePolicy, QWidget
from qt_material import apply_stylesheet

from ui.dynamic_conversation import ConversationWidget
from ui.main_window import UiForm
from ui.settings_window import SettingsWindow
from utils.chat_session_maintainer import ChatSessionMaintainer


class MainWindow(QWidget, UiForm):
    """
    Main Window of the GUI Application
    """
    # Define a custom signal to update the conversation widget from another thread
    update_conversation_widget_signal = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        self.setting_window = SettingsWindow()
        self.setupUi(self)
        self.csm = ChatSessionMaintainer()

        self.conversation_widget = ConversationWidget()
        self.conversation_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # test: draw a border around the conversation widget
        # self.conversation_widget.setStyleSheet("border: 1px solid black;")
        self.gridLayout_2.addWidget(self.conversation_widget)

        self.pushButton_2.clicked.connect(self.add_conversation)
        self.pushButton.clicked.connect(self.conversation_widget.clear_conversation)
        self.pushButton_3.clicked.connect(self.open_settings_window)

    def add_conversation(self) -> None:
        """
        Add a conversation to the conversation widget
        :return: None
        """
        # get the text
        text = self.textEdit.toPlainText()
        # clear the text
        self.textEdit.clear()
        self.conversation_widget.add_message('user', text)
        print('sending text: ', text)

        # Use multithreading to run the chat() method in a separate thread
        thread_ = threading.Thread(target=partial(self.run_chat, text))
        thread_.start()

    def run_chat(self, text) -> None:
        """
        Run the Chatting function in a separate thread to avoid blocking the GUI
        :param text: The text input from the user
        :return: None
        """
        emotion_dict = self.videoWidget.result
        response = self.csm.chat(text, emotion_dict)
        # Update the GUI from the main thread using a signal
        self.update_conversation_widget_signal.emit(response)

    def update_conversation_widget(self, response) -> None:
        """
        Update the conversation widget with the response from the chatbot
        :param response: The text response from the GPT
        :return:None
        """
        self.conversation_widget.add_message('gpt', response)

    def open_settings_window(self) -> None:
        """
        Open the settings window
        :return: None
        """
        self.setting_window.show()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    apply_stylesheet(app, theme='light_blue.xml')
    window.update_conversation_widget_signal.connect(window.update_conversation_widget)
    window.show()
    app.exec()
