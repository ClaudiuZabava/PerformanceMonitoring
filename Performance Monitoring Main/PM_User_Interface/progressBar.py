from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QRectF, QPoint
from PySide6.QtGui import QPainter, QPen, QColor, QBrush

class RoundProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 0

    def setValue(self, value):
        self._value = value
        self.update()  # this will trigger the paintEvent

    def value(self):
        return self._value

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen_width = 10

        painter.setBrush(QColor(220, 220, 220, 64))
        rect = QRectF(0, 0, self.width(), self.height())
        start_angle = 90 * 16  # angles are specified in 1/16th of a degree
        span_angle = -360 * self._value * 16
        painter.setPen(Qt.NoPen)
        painter.drawPie(rect, start_angle, span_angle)

        # Draw the circular progress bar

        rect = QRectF(pen_width / 2, pen_width / 2, self.width() - pen_width, self.height() - pen_width)
        start_angle = 90 * 16  # angles are specified in 1/16th of a degree
        span_angle = -360 * self._value * 16
        pen = QPen(QColor(255, 0, 0), pen_width)
        painter.setPen(pen)
        painter.drawArc(rect, start_angle, span_angle)

        # Draw the text
        font = painter.font()
        font.setPointSize(12)  # adjust the size as needed
        painter.setFont(font)
        painter.setPen(QColor(255, 0, 0))  # text color
        painter.drawText(rect, Qt.AlignCenter, str(int(self._value * 100))+'%')