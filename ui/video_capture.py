"""
Capture video from the camera and display it in a Widget.
"""

import cv2
import numpy
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QMessageBox, QSizePolicy, QVBoxLayout, QWidget
from deepface import DeepFace


class VideoWidget(QWidget):
    """
    Widget for displaying video from the camera.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize UI elements
        self.label = QLabel(self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        # Initialize video capture
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        # if no camera found
        if not self.cap.isOpened():
            QMessageBox.critical(self, "Error", "No Camera Found")

        # Create timer for updating video frames
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 / 60)  # 30 fps

        self.result_buffer = []
        self.result = {
            'angry': 0,
            'disgust': 0,
            'fear': 0,
            'happy': 0,
            'sad': 0,
            'surprise': 0,
            'neutral': 0
        }

    def update_frame(self) -> None:
        """
        Update the video frame in the UI

        :return: None
        """
        # Read video frame from the camera
        ret, frame = self.cap.read()
        if not ret:
            return

        # Convert the frame to an image compatible with QPixmap
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, _ = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Update the label with the new image
        self.label.setPixmap(QPixmap.fromImage(q_image))
        self.label.setScaledContents(True)
        try:
            res = DeepFace.analyze(numpy.array(frame), actions=['emotion'], silent=True,
                                   detector_backend='ssd')
            self.update_result(res[0]['emotion'])
        except ValueError:
            # Face not found
            pass
        except Exception as e:
            print(e)

    def update_result(self, emotion: dict) -> None:
        """
        Update the emotion result, using a buffer to smooth the result
        :param emotion: A dict containing the emotion result. For example:
        {'angry': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happy': 0.0, 'sad': 0.0,
         'surprise': 0.0, 'neutral': 0.0}
        :return: None
        """
        self.result_buffer.append(emotion)
        # Buffer size is 15
        if len(self.result_buffer) > 30:
            self.result_buffer.pop(0)
        for k, _ in self.result.items():
            for item in self.result_buffer:
                self.result[k] += item[k]
            self.result[k] /= len(self.result_buffer)
            self.result[k] = int(self.result[k])
        # print(self.result)

    def closeEvent(self, event):
        """
        Release video capture when the widget is closed. Currently not used
        :param event: When needed, this parameter will be passed to the super class.
        :return: None
        """
        # Release video capture when the widget is closed
        self.cap.release()
        self.timer.stop()
        super().closeEvent(event)
