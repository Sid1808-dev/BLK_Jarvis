import time

from PySide6 import QtCore
from PySide6.QtCore import Qt, QRect, QTimer, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QIcon, QMovie
import sys


class WidgetThread(QThread):
    widget_closed = Signal()

    def run(self):
        app = QApplication([])
        window = Window()
        window.show()
        app.exec_()
        self.widget_closed.emit()


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        self.setGeometry(1400, 700, 80, 80)

        # self.setWindowOpacity(0)
        self.setWindowTitle("BLK-JARVIS")

        label = QLabel(self)
        movie = QMovie("C:\\Users\\ss956\\Downloads\\ai_3.gif")
        label.setMovie(movie)
        movie.start()

        # # Create a QTimer
        # self.timer = QTimer(self)
        # timeout_in_seconds = 5  # Set your desired timeout in seconds
        # self.timer.timeout.connect(self.close_application)
        # self.timer.start(timeout_in_seconds * 1000)  # Convert seconds to milliseconds

    def close_application(self):
        # Clean up any resources or perform necessary actions before exiting
        # ...

        # Exit the application
        QApplication.quit()


def show_widget():
    app = QApplication([])
    window = Window()
    window.show()
    # time.sleep(5)

    # app.exec()
    # window.close()

    sys.exit(app.exec())


show_widget()
