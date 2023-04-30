"""
The graphical result display (bar chart)
"""
from PySide6 import QtCharts
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow


class GraphicalResult(QMainWindow):
    """
    Implement the dynamic bar chart
    """

    def __init__(self):
        super().__init__()

        # Create a dictionary containing emotion names and their initial values
        self.emotions = {
            'angry': 3,
            'disgust': 0,
            'fear': 16,
            'happy': 1,
            'sad': 33,
            'surprise': 1,
            'neutral': 46
        }

        # Set up the chart widget
        self.chart = QtCharts.QChart()
        self.chart.setTitle("Emotion likelihoods")
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        # Create a bar series and add it to the chart
        self.series = QtCharts.QBarSeries()
        for key, val in self.emotions.items():
            barset = QtCharts.QBarSet(key)
            barset.append(val)
            self.series.append(barset)
        self.chart.addSeries(self.series)

        # Set up the chart view
        self.view = QtCharts.QChartView(self.chart)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setMinimumSize(400, 200)
        self.setCentralWidget(self.view)

        # Set up the timer for updating the chart
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(500)  # 100 ms

    def update_chart(self) -> None:
        """
        Update the bar chart with new values
        :return: None
        """
        new_emotions = self.emotions
        for key, val in new_emotions.items():
            self.emotions[key] = val

        # Update the bar chart data with the new emotion values
        for i, emotion in enumerate(self.emotions.keys()):
            barset = self.series.barSets()[i]
            barset.replace(0, self.emotions[emotion])

        # Update the chart view
        self.chart.update()
