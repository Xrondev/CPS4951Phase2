import cv2
from PySide6.QtCore import QThread, Signal, QTimer
from PySide6.QtGui import QImage, QPixmap, Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy, QVBoxLayout


class VideoWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize UI elements
        self.label = QLabel(self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        # Initialize video capture
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Create timer for updating video frames
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000/30)  # 30 fps

    def update_frame(self):
        # Read video frame from the camera
        ret, frame = self.cap.read()
        if not ret:
            return

        # Convert the frame to an image compatible with QPixmap
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Update the label with the new image
        self.label.setPixmap(QPixmap.fromImage(q_image))
        self.label.setScaledContents(True)

    def closeEvent(self, event):
        # Release video capture when the widget is closed
        self.cap.release()
        self.timer.stop()
        super().closeEvent(event)