from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QRectF, QPoint
from PySide6.QtGui import QPainter, QPen, QColor, QBrush, QFont, QFontMetrics

class RoundProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 0

    def setValue(self, value):
        self._value = value
        self.update()

    def value(self):
        return self._value

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen_width = 10

        painter.setBrush(QColor(220, 220, 220, 64))
        rect = QRectF(0, 0, self.width(), self.height())
        start_angle = 90 * 16
        span_angle = -360 * self._value * 16
        painter.setPen(Qt.NoPen)
        painter.drawPie(rect, start_angle, span_angle)

        # Draw the circular progress bar

        rect = QRectF(pen_width / 2, pen_width / 2, self.width() - pen_width, self.height() - pen_width)
        start_angle = 90 * 16
        span_angle = -360 * self._value * 16
        pen = QPen(QColor(255, 0, 0), pen_width)
        painter.setPen(pen)
        painter.drawArc(rect, start_angle, span_angle)

        # Draw the text
        font = painter.font()
        font.setPointSize(12)
        painter.setFont(font)
        painter.setPen(QColor(255, 0, 0))  # text color
        painter.drawText(rect, Qt.AlignCenter, str(int(self._value * 100))+'%')


class TempProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 0

    def setValue(self, value):
        self._value = value
        self.update()  #  trigger pentru paintEvent

    def value(self):
        return self._value

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen_width = 10

        painter.setBrush(QColor(220, 220, 220, 64))
        rect = QRectF(0, 0, self.width(), self.height())
        start_angle = 90 * 16
        span_angle = -360 * self._value * 16
        painter.setPen(Qt.NoPen)
        painter.drawPie(rect, start_angle, span_angle)

        # Draw the circular progress bar

        rect = QRectF(pen_width / 2, pen_width / 2, self.width() - pen_width, self.height() - pen_width)
        start_angle = 90 * 16
        span_angle = -360 * self._value * 16
        if(self._value <= 0.5):
            pen = QPen(QColor(0, 255, 255), pen_width)
        elif(self._value > 0.5 and self._value < 0.7):
            pen = QPen(QColor(255, 255, 0), pen_width)
        else:
            pen = QPen(QColor(255, 0, 0), pen_width)
        painter.setPen(pen)
        painter.drawArc(rect, start_angle, span_angle)

        # Draw the text
        font = painter.font()
        font.setPointSize(12)
        painter.setFont(font)
        if(self._value <= 0.5):
            painter.setPen(QColor(0, 255, 255))
        elif(self._value > 0.5 and self._value < 0.7):
            painter.setPen(QColor(255, 255, 0))
        else:
            painter.setPen(QColor(255, 0, 0))
        painter.drawText(rect, Qt.AlignCenter, str(int(self._value * 100))+'°C')


class CustomProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 0
        self._maximum = 100
        self.setMinimumSize(250, 20)

    def setValue(self, value):
        self._value = value
        self.update()

    def setMaximum(self, maximum):
        self._maximum = maximum

    def setMinimum(self, minimum):
        self._minimum = minimum

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the gray background
        full_rect = QRectF(0, 0, self.width(), self.height())
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(220, 220, 220, 64))
        painter.drawRoundedRect(full_rect, 10, 10)

        # Draw the progress
        width = self._value / self._maximum * self.width()
        rect = QRectF(0, 0, width, self.height())
        painter.setBrush(QColor(0, 200, 0))
        painter.drawRoundedRect(rect, 10, 10)

        font = painter.font()
        font.setPointSize(12)
        painter.setFont(font)
        painter.setPen(QColor(255, 255, 255))
        text = f"{self._value}/{self._maximum}"
        painter.drawText(full_rect, Qt.AlignCenter, text + " GB")

