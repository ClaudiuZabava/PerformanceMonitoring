# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AppuqAuOQ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(851, 661)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.header_frame.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left = QFrame(self.header_frame)
        self.header_left.setObjectName(u"header_left")
        font = QFont()
        font.setPointSize(20)
        self.header_left.setFont(font)
        self.header_left.setFrameShape(QFrame.StyledPanel)
        self.header_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.header_left)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font1 = QFont()
        font1.setFamilies([u"Segoe MDL2 Assets"])
        font1.setPointSize(15)
        self.pushButton_4.setFont(font1)
        icon = QIcon()
        icon.addFile(u"icons/icons8-menu-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(36, 36))
        self.pushButton_4.setFlat(False)

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.horizontalLayout.addWidget(self.header_left, 0, Qt.AlignLeft)

        self.header_center = QFrame(self.header_frame)
        self.header_center.setObjectName(u"header_center")
        self.header_center.setFrameShape(QFrame.StyledPanel)
        self.header_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.header_center)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Black"])
        self.label.setFont(font2)
        self.label.setPixmap(QPixmap(u"icons/icons8-speedometer-78.png"))

        self.horizontalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.header_center)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(20)
        self.label_2.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_center)

        self.header_right = QFrame(self.header_frame)
        self.header_right.setObjectName(u"header_right")
        self.header_right.setFrameShape(QFrame.StyledPanel)
        self.header_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.pushButton_2 = QPushButton(self.header_right)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u"icons/icons8-minimize-window-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(24, 24))
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.header_right)
        self.pushButton.setObjectName(u"pushButton")
        icon2 = QIcon()
        icon2.addFile(u"icons/icons8-maximize-window-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(24, 24))
        self.pushButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.header_right)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        icon3.addFile(u"icons/icons8-close-window-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(24, 24))
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout.addWidget(self.header_right, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.main_body_frame.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_frame = QFrame(self.main_body_frame)
        self.left_frame.setObjectName(u"left_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_frame.sizePolicy().hasHeightForWidth())
        self.left_frame.setSizePolicy(sizePolicy1)
        self.left_frame.setMaximumSize(QSize(200, 16777215))
        self.left_frame.setBaseSize(QSize(0, 0))
        self.left_frame.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.left_frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.left_frame)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy2)
        icon4 = QIcon()
        icon4.addFile(u"icons/icons8-cd-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_8, 5, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setMargin(5)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy2.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy2)
        icon5 = QIcon()
        icon5.addFile(u"icons/icons8-signal-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon5)
        self.pushButton_10.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_10, 6, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy2.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy2)
        icon6 = QIcon()
        icon6.addFile(u"icons/icons8-settings-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon6)
        self.pushButton_11.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_11, 9, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)
        icon7 = QIcon()
        icon7.addFile(u"icons/icons8-memory-slot-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)
        icon8 = QIcon()
        icon8.addFile(u"icons/icons8-electronics-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy2.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy2)
        icon9 = QIcon()
        icon9.addFile(u"icons/icons8-video-card-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon9)
        self.pushButton_12.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_12, 2, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy2.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy2)
        icon10 = QIcon()
        icon10.addFile(u"icons/icons8-laptop-settings-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon10)
        self.pushButton_9.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_9, 3, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setMargin(5)

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMargin(5)

        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setMargin(5)

        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setMargin(5)

        self.gridLayout.addWidget(self.label_9, 6, 1, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setMargin(5)

        self.gridLayout.addWidget(self.label_10, 9, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.left_frame)

        self.center_frame = QFrame(self.main_body_frame)
        self.center_frame.setObjectName(u"center_frame")
        self.center_frame.setFrameShape(QFrame.StyledPanel)
        self.center_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.center_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.center_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.CPU = QWidget()
        self.CPU.setObjectName(u"CPU")
        self.verticalLayout_4 = QVBoxLayout(self.CPU)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cpu_info = QFrame(self.CPU)
        self.cpu_info.setObjectName(u"cpu_info")
        self.gridLayout_2 = QGridLayout(self.cpu_info)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_15 = QLabel(self.cpu_info)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 4, 0, 1, 1)

        self.label_20 = QLabel(self.cpu_info)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 5, 0, 1, 1)

        self.label_18 = QLabel(self.cpu_info)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 3, 2, 1, 1)

        self.label_21 = QLabel(self.cpu_info)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 5, 2, 1, 1)

        self.label_14 = QLabel(self.cpu_info)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 3, 0, 1, 1)

        self.label_13 = QLabel(self.cpu_info)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_12 = QLabel(self.cpu_info)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_16 = QLabel(self.cpu_info)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 1, 2, 1, 1)

        self.label_17 = QLabel(self.cpu_info)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 2, 2, 1, 1)

        self.label_19 = QLabel(self.cpu_info)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 4, 2, 1, 1)

        self.label_11 = QLabel(self.cpu_info)
        self.label_11.setObjectName(u"label_11")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_11.setFont(font4)

        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignTop)

        self.widget_10 = QWidget(self.cpu_info)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.widget_10, 1, 3, 3, 1)


        self.verticalLayout_4.addWidget(self.cpu_info)

        self.stackedWidget.addWidget(self.CPU)
        self.GPU = QWidget()
        self.GPU.setObjectName(u"GPU")
        self.verticalLayout_5 = QVBoxLayout(self.GPU)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gpu_info = QFrame(self.GPU)
        self.gpu_info.setObjectName(u"gpu_info")
        self.gpu_info.setFrameShape(QFrame.StyledPanel)
        self.gpu_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.gpu_info)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_22 = QLabel(self.gpu_info)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font4)

        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1, Qt.AlignTop)

        self.label_23 = QLabel(self.gpu_info)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 1, 0, 1, 1)

        self.label_26 = QLabel(self.gpu_info)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_3.addWidget(self.label_26, 1, 1, 1, 1)

        self.label_24 = QLabel(self.gpu_info)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_3.addWidget(self.label_24, 2, 0, 1, 1)

        self.label_27 = QLabel(self.gpu_info)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 2, 1, 1, 1)

        self.label_25 = QLabel(self.gpu_info)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_3.addWidget(self.label_25, 3, 0, 1, 1)

        self.label_28 = QLabel(self.gpu_info)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_3.addWidget(self.label_28, 3, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.gpu_info)

        self.gpu_usage = QFrame(self.GPU)
        self.gpu_usage.setObjectName(u"gpu_usage")
        self.gpu_usage.setFrameShape(QFrame.StyledPanel)
        self.gpu_usage.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.gpu_usage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_29 = QLabel(self.gpu_usage)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font4)

        self.gridLayout_4.addWidget(self.label_29, 0, 0, 1, 1, Qt.AlignTop)

        self.label_30 = QLabel(self.gpu_usage)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_4.addWidget(self.label_30, 1, 0, 1, 1)

        self.label_32 = QLabel(self.gpu_usage)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_4.addWidget(self.label_32, 3, 0, 1, 1)

        self.label_31 = QLabel(self.gpu_usage)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_4.addWidget(self.label_31, 2, 0, 1, 1)

        self.widget_gpu_util = QWidget(self.gpu_usage)
        self.widget_gpu_util.setObjectName(u"widget_gpu_util")

        self.gridLayout_4.addWidget(self.widget_gpu_util, 2, 1, 1, 1)

        self.widget_gpu_temp = QWidget(self.gpu_usage)
        self.widget_gpu_temp.setObjectName(u"widget_gpu_temp")

        self.gridLayout_4.addWidget(self.widget_gpu_temp, 1, 1, 1, 1)

        self.widget_gpu_mem = QWidget(self.gpu_usage)
        self.widget_gpu_mem.setObjectName(u"widget_gpu_mem")

        self.gridLayout_4.addWidget(self.widget_gpu_mem, 3, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.gpu_usage)

        self.stackedWidget.addWidget(self.GPU)
        self.System = QWidget()
        self.System.setObjectName(u"System")
        self.verticalLayout_6 = QVBoxLayout(self.System)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.System)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_36 = QLabel(self.frame_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font4)

        self.gridLayout_5.addWidget(self.label_36, 0, 0, 1, 1, Qt.AlignTop)

        self.label_37 = QLabel(self.frame_2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_5.addWidget(self.label_37, 1, 0, 1, 1)

        self.label_46 = QLabel(self.frame_2)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_5.addWidget(self.label_46, 1, 1, 1, 1)

        self.label_41 = QLabel(self.frame_2)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_5.addWidget(self.label_41, 2, 0, 1, 1)

        self.label_47 = QLabel(self.frame_2)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_5.addWidget(self.label_47, 2, 1, 1, 1)

        self.label_38 = QLabel(self.frame_2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_5.addWidget(self.label_38, 3, 0, 1, 1)

        self.label_48 = QLabel(self.frame_2)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_5.addWidget(self.label_48, 3, 1, 1, 1)

        self.label_39 = QLabel(self.frame_2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_5.addWidget(self.label_39, 4, 0, 1, 1)

        self.label_49 = QLabel(self.frame_2)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_5.addWidget(self.label_49, 4, 1, 1, 1)

        self.label_40 = QLabel(self.frame_2)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_5.addWidget(self.label_40, 5, 0, 1, 1)

        self.label_50 = QLabel(self.frame_2)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_5.addWidget(self.label_50, 5, 1, 1, 1)

        self.label_42 = QLabel(self.frame_2)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_5.addWidget(self.label_42, 6, 0, 1, 1)

        self.label_51 = QLabel(self.frame_2)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_5.addWidget(self.label_51, 6, 1, 1, 1)

        self.label_43 = QLabel(self.frame_2)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_5.addWidget(self.label_43, 7, 0, 1, 1)

        self.label_52 = QLabel(self.frame_2)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_5.addWidget(self.label_52, 7, 1, 1, 1)

        self.label_44 = QLabel(self.frame_2)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_5.addWidget(self.label_44, 8, 0, 1, 1)

        self.label_53 = QLabel(self.frame_2)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_5.addWidget(self.label_53, 8, 1, 1, 1)

        self.label_45 = QLabel(self.frame_2)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_5.addWidget(self.label_45, 9, 0, 1, 1)

        self.label_54 = QLabel(self.frame_2)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_5.addWidget(self.label_54, 9, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.System)
        self.RAM = QWidget()
        self.RAM.setObjectName(u"RAM")
        self.verticalLayout_7 = QVBoxLayout(self.RAM)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.RAM)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_58 = QLabel(self.frame_3)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_6.addWidget(self.label_58, 7, 0, 1, 1)

        self.label_57 = QLabel(self.frame_3)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_6.addWidget(self.label_57, 3, 0, 1, 1)

        self.label_55 = QLabel(self.frame_3)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font4)

        self.gridLayout_6.addWidget(self.label_55, 1, 0, 1, 1, Qt.AlignTop)

        self.label_63 = QLabel(self.frame_3)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_6.addWidget(self.label_63, 7, 1, 1, 1)

        self.label_56 = QLabel(self.frame_3)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_6.addWidget(self.label_56, 2, 0, 1, 1)

        self.label_62 = QLabel(self.frame_3)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_6.addWidget(self.label_62, 6, 1, 1, 1)

        self.label_59 = QLabel(self.frame_3)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_6.addWidget(self.label_59, 6, 0, 1, 1)

        self.label_61 = QLabel(self.frame_3)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_6.addWidget(self.label_61, 3, 1, 1, 1)

        self.label_60 = QLabel(self.frame_3)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_6.addWidget(self.label_60, 2, 1, 1, 1)

        self.label_66 = QLabel(self.frame_3)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_6.addWidget(self.label_66, 4, 0, 1, 1)

        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_6.addWidget(self.label_33, 4, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.RAM)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_64 = QLabel(self.frame_4)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font4)

        self.gridLayout_7.addWidget(self.label_64, 0, 0, 1, 1, Qt.AlignTop)

        self.label_65 = QLabel(self.frame_4)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_7.addWidget(self.label_65, 1, 0, 1, 1)

        self.label_67 = QLabel(self.frame_4)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_7.addWidget(self.label_67, 3, 0, 1, 1)

        self.widget_ram_usage = QWidget(self.frame_4)
        self.widget_ram_usage.setObjectName(u"widget_ram_usage")

        self.gridLayout_7.addWidget(self.widget_ram_usage, 1, 1, 1, 1)

        self.widget_ram_used = QWidget(self.frame_4)
        self.widget_ram_used.setObjectName(u"widget_ram_used")

        self.gridLayout_7.addWidget(self.widget_ram_used, 3, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.RAM)
        self.Disk = QWidget()
        self.Disk.setObjectName(u"Disk")
        self.verticalLayout_9 = QVBoxLayout(self.Disk)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.Disk)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_71 = QLabel(self.frame_7)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font4)

        self.gridLayout_10.addWidget(self.label_71, 0, 0, 1, 1, Qt.AlignTop)

        self.label_72 = QLabel(self.frame_7)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_10.addWidget(self.label_72, 1, 0, 1, 1)

        self.label_78 = QLabel(self.frame_7)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_10.addWidget(self.label_78, 1, 1, 1, 1)

        self.label_73 = QLabel(self.frame_7)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_10.addWidget(self.label_73, 2, 0, 1, 1)

        self.label_79 = QLabel(self.frame_7)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_10.addWidget(self.label_79, 2, 1, 1, 1)

        self.label_74 = QLabel(self.frame_7)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_10.addWidget(self.label_74, 3, 0, 1, 1)

        self.label_80 = QLabel(self.frame_7)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_10.addWidget(self.label_80, 3, 1, 1, 1)

        self.label_75 = QLabel(self.frame_7)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_10.addWidget(self.label_75, 4, 0, 1, 1)

        self.label_81 = QLabel(self.frame_7)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_10.addWidget(self.label_81, 4, 1, 1, 1)

        self.label_76 = QLabel(self.frame_7)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_10.addWidget(self.label_76, 5, 0, 1, 1)

        self.label_82 = QLabel(self.frame_7)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_10.addWidget(self.label_82, 5, 1, 1, 1)

        self.label_77 = QLabel(self.frame_7)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_10.addWidget(self.label_77, 6, 0, 1, 1)

        self.label_83 = QLabel(self.frame_7)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_10.addWidget(self.label_83, 6, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.Disk)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_95 = QLabel(self.frame_8)
        self.label_95.setObjectName(u"label_95")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_95.setFont(font5)

        self.gridLayout_9.addWidget(self.label_95, 1, 0, 1, 1)

        self.label_84 = QLabel(self.frame_8)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font4)

        self.gridLayout_9.addWidget(self.label_84, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.label_96 = QLabel(self.frame_8)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_9.addWidget(self.label_96, 1, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_8)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setStyleSheet(u"background-color: rgb(21, 21, 21);\n"
"gridline-color: rgb(42, 42, 42);\n"
"color: rgb(0, 0, 0);")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(102, 102, 102));
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(102, 102, 102));
        __qtablewidgetitem1.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setBackground(QColor(102, 102, 102));
        __qtablewidgetitem2.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setBackground(QColor(102, 102, 102));
        __qtablewidgetitem3.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setBackground(QColor(102, 102, 102));
        __qtablewidgetitem4.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.tableWidget, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_5)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.Disk)
        self.Network = QWidget()
        self.Network.setObjectName(u"Network")
        self.verticalLayout_10 = QVBoxLayout(self.Network)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.Network)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_97 = QLabel(self.frame_9)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setFont(font4)

        self.gridLayout_11.addWidget(self.label_97, 0, 0, 1, 1, Qt.AlignTop)

        self.label_98 = QLabel(self.frame_9)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_11.addWidget(self.label_98, 1, 0, 1, 1)

        self.label_102 = QLabel(self.frame_9)
        self.label_102.setObjectName(u"label_102")

        self.gridLayout_11.addWidget(self.label_102, 1, 1, 1, 1)

        self.label_99 = QLabel(self.frame_9)
        self.label_99.setObjectName(u"label_99")

        self.gridLayout_11.addWidget(self.label_99, 2, 0, 1, 1)

        self.label_103 = QLabel(self.frame_9)
        self.label_103.setObjectName(u"label_103")

        self.gridLayout_11.addWidget(self.label_103, 2, 1, 1, 1)

        self.label_100 = QLabel(self.frame_9)
        self.label_100.setObjectName(u"label_100")

        self.gridLayout_11.addWidget(self.label_100, 3, 0, 1, 1)

        self.label_104 = QLabel(self.frame_9)
        self.label_104.setObjectName(u"label_104")

        self.gridLayout_11.addWidget(self.label_104, 3, 1, 1, 1)

        self.label_101 = QLabel(self.frame_9)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_11.addWidget(self.label_101, 4, 0, 1, 1)

        self.label_105 = QLabel(self.frame_9)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout_11.addWidget(self.label_105, 4, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.Network)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.stackedWidget.addWidget(self.Settings)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.center_frame)

        self.right_frame = QFrame(self.main_body_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMinimumSize(QSize(400, 0))
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.right_frame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.right_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setStyleSheet(u"background-color: rgb(80, 80, 80);\n"
"color: rgb(255, 255, 255);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pushButton_13 = QPushButton(self.frame_10)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_8.addWidget(self.pushButton_13, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.pushButton_14 = QPushButton(self.frame_10)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_8.addWidget(self.pushButton_14, 1, 1, 1, 1)

        self.stackedWidget_2 = QStackedWidget(self.frame_10)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(0, 0))
        self.statistics = QWidget()
        self.statistics.setObjectName(u"statistics")
        self.stackedWidget_2.addWidget(self.statistics)
        self.assistant = QWidget()
        self.assistant.setObjectName(u"assistant")
        self.gridLayout_12 = QGridLayout(self.assistant)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.scrollArea = QScrollArea(self.assistant)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 400))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 358, 445))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_12.addWidget(self.scrollArea, 0, 0, 1, 2)

        self.plainTextEdit = QPlainTextEdit(self.assistant)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_12.addWidget(self.plainTextEdit, 1, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.assistant)
        self.pushButton_15.setObjectName(u"pushButton_15")
        icon11 = QIcon()
        icon11.addFile(u"icons/icons8-paper-plane-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon11)
        self.pushButton_15.setIconSize(QSize(24, 24))

        self.gridLayout_12.addWidget(self.pushButton_15, 1, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.assistant)

        self.gridLayout_8.addWidget(self.stackedWidget_2, 2, 0, 1, 2)


        self.verticalLayout_12.addWidget(self.frame_10)


        self.horizontalLayout_8.addWidget(self.right_frame)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.footer_left_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.footer_right_frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_5)

        self.size_grip = QFrame(self.footer_right_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMaximumSize(QSize(5, 5))
        self.size_grip.setStyleSheet(u"background-color: rgb(177, 177, 177);")
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.size_grip)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_4.setDefault(False)
        self.pushButton.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Performance Monitoring", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.pushButton_8.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_7.setText("")
        self.pushButton_6.setText("")
        self.pushButton_12.setText("")
        self.pushButton_9.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"System Info", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"RAM", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Disk Storage", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Base Frequency", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Threads", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Cores", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CPU Name", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CPU Info", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"GPU Info", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"GPU Name", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"GPU Index", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Dedicated Memory", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"GPU Usage", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Used Memory", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Utilization", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"System Informations", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Operating System", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Hostname", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"OS Version", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"OS Release", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"OS Architecture", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"CPU Type", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"CPU Cores", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Slots", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Maximum Capacity", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"RAM Info", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"RAM Type", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Base Speed", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Total Memory", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"RAM Usage", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Usage Percentage", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Used Memory", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Disk Info", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Pool Option", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Operational Status", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Health", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Partitions", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Storage Usage", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"2", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Partition Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Used Percent", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Free Memory", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Used Memory", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Newtwork Data", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Bytes Sent", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Bytes Received", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Packages Sent", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Packages Received", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Statistics Generator", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Assistant", None))
        self.pushButton_15.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Alpha", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

