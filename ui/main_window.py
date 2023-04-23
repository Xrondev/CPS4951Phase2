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

from ui.video_capture import VideoWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1514, 1098)
        Form.setStyleSheet(u"font: 16pt \"\u5f97\u610f\u9ed1\";")
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.videoWidget = VideoWidget()
        self.verticalLayout_4.addWidget(self.videoWidget)

        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 200))

        self.timer = QTimer(self.verticalLayout_2)
        self.timer.timeout.connect(self.update_result)
        self.timer.start(1000 / 30)

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 1, 0, 1, 1)

        # self.progressBar = QProgressBar(Form)
        # self.progressBar.setObjectName(u"progressBar")
        # sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        # self.progressBar.setSizePolicy(sizePolicy)
        # self.progressBar.setValue(0)
        #
        # self.gridLayout_3.addWidget(self.progressBar, 2, 0, 1, 2)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 2)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 3, 1, 1)

        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 0, 2, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(3, 1)

        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"FER Chatting!", None))
        self.label.setText(
            QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Result Here</p></body></html>",
                                       None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Reset Conversation", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Send", None))

    # retranslateUi

    def update_result(self):
        result = self.videoWidget.result
        self.label.setText(
            QCoreApplication.translate("Form", f"<html><head/><body><p align=\"center\">{result}</p></body></html>",
                                       None))
