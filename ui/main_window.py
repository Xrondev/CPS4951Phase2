# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, QTimer)
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QPushButton, QSizePolicy,
                               QTextEdit, QVBoxLayout)

from ui.graphical_result import GraphicalResult
from ui.video_capture import VideoWidget


class UiForm:
    def setupUi(self, form):
        if not form.objectName():
            form.setObjectName("Form")
        form.setStyleSheet("font: 16pt \"\u5f97\u610f\u9ed1\";")
        self.gridLayout_4 = QGridLayout(form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.videoWidget = VideoWidget()
        self.verticalLayout_4.addWidget(self.videoWidget)

        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.line_2 = QFrame(form)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.graphical_result = GraphicalResult()
        self.verticalLayout_2.addWidget(self.graphical_result)

        self.label = QLabel(form)
        self.label.setObjectName("label")
        self.label.setMinimumSize(QSize(0, 100))

        self.timer = QTimer(self.verticalLayout_2)
        self.timer.timeout.connect(self.update_result)
        self.timer.start(1000 / 30)

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton_3 = QPushButton(form)
        self.pushButton_3.setObjectName("pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.line_3 = QFrame(form)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QPushButton(form)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 1, 0, 1, 1)

        # self.progressBar = QProgressBar(Form)
        # self.progressBar.setObjectName("progressBar")
        # sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        # self.progressBar.setSizePolicy(sizePolicy)
        # self.progressBar.setValue(0)
        #
        # self.gridLayout_3.addWidget(self.progressBar, 2, 0, 1, 2)

        self.textEdit = QTextEdit(form)
        self.textEdit.setObjectName("textEdit")
        size_policy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy1.setHorizontalStretch(0)
        size_policy1.setVerticalStretch(0)
        size_policy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(size_policy1)

        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 2)

        self.pushButton_2 = QPushButton(form)
        self.pushButton_2.setObjectName("pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 3, 1, 1)

        self.line_4 = QFrame(form)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 0, 2, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(3, 1)

        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(form)

        QMetaObject.connectSlotsByName(form)
        form.resize(1530, 900)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "FER Chatting!", None))
        self.label.setText(
            QCoreApplication.translate("Form",
                                       "<html><head/><body><p align=\"center\">"
                                       "Result Here</p></body></html>",
                                       None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", "Settings", None))
        self.pushButton.setText(QCoreApplication.translate("Form", "Reset Conversation", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", "Send", None))

    # retranslateUi

    def update_result(self):
        """
        Update result label and the graphical result
        """
        result = self.videoWidget.result
        self.graphical_result.emotions = result
        result = str(result)
        import re
        result = re.sub(r"[{}']", '', result)
        self.label.setText(
            QCoreApplication.translate("Form",
                                       f"<html><head/><body><p align=\"center\">"
                                       f"{result}</p></body></html>",
                                       None))
