import os
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip
from PySide6 import QtCore
from PySide6.QtCore import QEvent
from PySide6 import QtGui
from ui_App import *




class MainApp(QMainWindow):
    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def toggle_menu(self):

        if self.ui.label_4.sizePolicy().horizontalPolicy() == QSizePolicy.Policy.Preferred:
            start_w = 150
            end_w = 0
            self.ui.label_4.setSizePolicy(self.ui.label_4.sizePolicy().Policy.Ignored, self.ui.label_4.sizePolicy().Policy.Preferred)
            self.ui.label_5.setSizePolicy(self.ui.label_5.sizePolicy().Policy.Ignored, self.ui.label_5.sizePolicy().Policy.Preferred)
            self.ui.label_6.setSizePolicy(self.ui.label_6.sizePolicy().Policy.Ignored, self.ui.label_6.sizePolicy().Policy.Preferred)
            self.ui.label_7.setSizePolicy(self.ui.label_7.sizePolicy().Policy.Ignored, self.ui.label_7.sizePolicy().Policy.Preferred)
            self.ui.label_8.setSizePolicy(self.ui.label_8.sizePolicy().Policy.Ignored, self.ui.label_8.sizePolicy().Policy.Preferred)
            self.ui.label_9.setSizePolicy(self.ui.label_9.sizePolicy().Policy.Ignored, self.ui.label_9.sizePolicy().Policy.Preferred)
            self.ui.label_10.setSizePolicy(self.ui.label_10.sizePolicy().Policy.Ignored, self.ui.label_10.sizePolicy().Policy.Preferred)

        else:
            start_w = 0
            end_w = 150
            self.ui.label_8.setSizePolicy(self.ui.label_8.sizePolicy().Policy.Preferred, self.ui.label_8.sizePolicy().Policy.Preferred)
            self.ui.label_6.setSizePolicy(self.ui.label_6.sizePolicy().Policy.Preferred, self.ui.label_6.sizePolicy().Policy.Preferred)
            self.ui.label_4.setSizePolicy(self.ui.label_4.sizePolicy().Policy.Preferred, self.ui.label_4.sizePolicy().Policy.Preferred)
            self.ui.label_5.setSizePolicy(self.ui.label_5.sizePolicy().Policy.Preferred, self.ui.label_5.sizePolicy().Policy.Preferred)
            self.ui.label_7.setSizePolicy(self.ui.label_7.sizePolicy().Policy.Preferred, self.ui.label_7.sizePolicy().Policy.Preferred)
            self.ui.label_9.setSizePolicy(self.ui.label_9.sizePolicy().Policy.Preferred, self.ui.label_9.sizePolicy().Policy.Preferred)
            self.ui.label_10.setSizePolicy(self.ui.label_10.sizePolicy().Policy.Preferred, self.ui.label_10.sizePolicy().Policy.Preferred)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            child = self.childAt(event.position().toPoint())
            if child.objectName()  == "header_frame" or child.objectName() == "label_2":
                self.m_mousePressPosition = event.globalPosition()
                return True
            else:
                self.m_mousePressPosition = None
                return False

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.m_mousePressPosition is not None:
            if self.isMaximized():
                self.showNormal()
            self.move(self.pos() + event.globalPosition().toPoint() - self.m_mousePressPosition.toPoint())
            self.m_mousePressPosition = event.globalPosition()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        # shadow effect
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(60)
        self.shadow.setXOffset(50)
        self.shadow.setYOffset(20)
        self.shadow.setColor(QtGui.QColor(0, 92, 157, 50))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.setWindowIcon(QtGui.QIcon("icons/icons8-speedometer-78.png"))
        self.setWindowTitle("Performance Monitor")

        self.ui.pushButton_2.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton_3.clicked.connect(lambda: self.close())
        self.ui.pushButton.clicked.connect(lambda: self.toggle_maximize())
        self.ui.pushButton_4.clicked.connect(lambda: self.toggle_menu())

        self.ui.header_frame.mouseMoveEvent = self.mouseMoveEvent

        QSizeGrip(self.ui.size_grip)


        # Navigate between pages using buttons
        self.ui.pushButton_12.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.GPU))
        self.ui.pushButton_9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.System))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.RAM))
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Disk))
        self.ui.pushButton_10.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Network))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.CPU))
        self.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    sys.exit(app.exec())

