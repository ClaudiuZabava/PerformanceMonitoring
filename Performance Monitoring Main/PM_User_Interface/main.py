import os
import sys
from assistantPanel import *

from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QProgressBar, QTableWidgetItem
from PySide6 import QtCore
from PySide6.QtCore import QEvent, QTimer, QThread, Signal, Slot, QSemaphore
from PySide6 import QtGui
from ui_App import *
from progressBar import RoundProgressBar, TempProgressBar, CustomProgressBar

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
parent_dir = os.path.dirname(current_dir)
data_collection_dir = os.path.join(parent_dir, "PM_Data_Collection")
sys.path.insert(0, data_collection_dir)

# Broken Imports
from cpuData import cpu_info, cpu_frequency, cpu_usage
from gpuData import get_gpu_info, get_gpu_usage_data
from memoryData import ram_info, ram_usage_data
from diskData import all_disks_mem_data, disk_read_write_speed
from driveInfo import get_disk_info
from DataCollection import system_Information
from diskData import all_disks_mem_data, disk_read_write_speed





class WorkerThread(QThread):
    valueChanged = Signal(float)
    freqChanged = Signal(str)
    tempChanged = Signal(float)
    memChanged = Signal(float)

    def __init__(self, data_type, parent=None):
        super().__init__(parent)
        self.data_type = data_type  # store the data type to collect

    def run(self):
        sleep_time = 500
        while True:  # continuously update the value
            if self.data_type == 'CPU':
                freq = cpu_frequency()
                usage = cpu_usage()['CPUUsage'] / 100.0
                self.valueChanged.emit(usage)
                self.freqChanged.emit(str(freq['CPU-0']) + " GHz")
                sleep_time = 500
            elif self.data_type == 'GPU':
                gpu_usage = get_gpu_usage_data()['utilization_percent'] /100.0
                gpu_temp = get_gpu_usage_data()['temperature'] / 100.0
                gpu_mem = round(get_gpu_usage_data()['memory_used_MB'] / 1024.0, 2)
                self.valueChanged.emit(gpu_usage)
                self.tempChanged.emit(gpu_temp)
                self.memChanged.emit(gpu_mem)
                sleep_time = 200
            elif self.data_type == 'RAM':
                ram_usage = ram_usage_data()['RAMUsagePr'] / 100.0
                ram_mem = ram_usage_data()['RAMUsedGB']
                self.valueChanged.emit(ram_usage)
                self.memChanged.emit(ram_mem)
                sleep_time = 200
            self.msleep(sleep_time)


class BotThread(QThread):
    botMessage = Signal(str)
    botSemaphore = QSemaphore(0)  # Inițializare semafor cu 0, ceea ce înseamnă că este blocat

    def run(self):
        while True:
            self.botSemaphore.acquire()  # Așteaptă până când semaforul este deblocat

            message = welcome_text()
            self.botMessage.emit(message)
    def unlock(self):  # Apelat când vrei ca botul să scrie un mesaj
        self.botSemaphore.release()  # Deblocare semafor







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

    def add_text_to_scrollarea(self, bot_text=None):
        state=0
        if bot_text is None:
            state=0
            text = self.ui.plainTextEdit.toPlainText()
        else:
            state=1
            text = bot_text

        # Creeaza un nou QLabel cu textul primit
        label = QLabel(text)

        # Adauga QLabel-ul in QScrollArea
        self.ui.scrollAreaWidgetContents.layout().addWidget(label)

        # Sterge textul initial din QPlainTextEdit
        self.ui.plainTextEdit.clear()
        if state == 0:
            self.botThread.unlock()

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

    @Slot(str)
    def update_freq(self, freq):
        self.ui.label_21.setText(freq)

    def toggle_bot_thread(self):
        if self.botThread.isRunning():
            pass
        else:
            self.botThread.start()
            self.botThread.botSemaphore.release()


    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(1200, 600)
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

        self.ui.pushButton_13.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.statistics))
        self.ui.pushButton_14.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.assistant))

        display_info={}
        # Getting Real Data - CPU:
        display_info['cpu'] = cpu_info()
        self.ui.label_16.setText(display_info['cpu']['Name'])
        self.ui.label_17.setText(str(display_info['cpu']['Cores']))
        self.ui.label_18.setText(str(display_info['cpu']['Threads']))
        self.ui.label_19.setText(display_info['cpu']['BaseFrequency'])


        # Getting Real Data - GPU:
        display_info['gpu'] = get_gpu_info()
        self.ui.label_26.setText(str(display_info['gpu']['name']))
        self.ui.label_27.setText(str(display_info['gpu']['index']))
        self.ui.label_28.setText(str(display_info['gpu']['memory_total_MB']) + "MB")

        # Getting Real Data - System:
        display_info['system'] = system_Information()
        self.ui.label_46.setText(str(display_info['system']['system']))
        self.ui.label_47.setText(str(display_info['system']['hostname']))
        self.ui.label_48.setText(str(display_info['system']['os_version']))
        self.ui.label_49.setText(str(display_info['system']['os_release']))
        self.ui.label_50.setText(str(display_info['system']['architecture']))
        self.ui.label_51.setText(str(display_info['system']['cpu_name']))
        self.ui.label_52.setText(str(display_info['system']['processor_type']))
        self.ui.label_53.setText(str(display_info['system']['cpu_cores']))
        self.ui.label_54.setText(str(display_info['system']['gpu_name']))


        # Getting Real Data - RAM:
        display_info['ram'] = ram_info()
        self.ui.label_60.setText(str(display_info['ram']['RAMType']))
        self.ui.label_61.setText(str(display_info['ram']['RAMCapacityMaxGB']) + "GB")
        self.ui.label_62.setText(str(display_info['ram']['RAMBaseSpeed']) + "MHz")
        self.ui.label_63.setText(str(display_info['ram']['RAMSlots']))
        self.ui.label_33.setText(str(display_info['ram']['RAMTotalInstalledGB']) + "GB")

        # Getting Real Data - Hard Drive:
        display_info['drive'] = get_disk_info()
        self.ui.label_78.setText(str(display_info['drive']['ModelName']))
        self.ui.label_79.setText(str(display_info['drive']['SerialNumber']))
        self.ui.label_80.setText(str(display_info['drive']['Type']))
        self.ui.label_81.setText(str(display_info['drive']['CanPool']))
        self.ui.label_82.setText(str(display_info['drive']['OperationalStatus']))
        self.ui.label_83.setText(str(display_info['drive']['HealthStatus']))


        # Getting Real Data - Disk:
        display_info['disk'] = all_disks_mem_data()
        self.ui.tableWidget.setRowCount(len(display_info['disk']))
        self.ui.tableWidget.setColumnCount(5)

        for partition_name, partition_data in display_info['disk'].items():
            if isinstance(partition_data, dict):  # asigura-te ca partition_data este un dictionar
                self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                i = self.ui.tableWidget.rowCount() - 1
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(partition_name))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(partition_data['UsedPer'])))
                self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(round(partition_data['FreeMem']/1024**3 , 2))))
                self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(round(partition_data['UsedMem']/1024**3 , 2))))
                self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(round(partition_data['PartitionMem']/1024**3 , 2))))

        for i in reversed(range(self.ui.tableWidget.rowCount())):
            is_row_empty = all(
                self.ui.tableWidget.item(i, j) is None or not self.ui.tableWidget.item(i, j).text() for j in
                range(self.ui.tableWidget.columnCount()))
            if is_row_empty:
                self.ui.tableWidget.removeRow(i)






        progress_bar = RoundProgressBar()

        # Add the progress bar to the cpu
        layout = QVBoxLayout(self.ui.widget_10)
        layout.addWidget(progress_bar)
        progress_bar.setGeometry(QRect(0, 0, 5, 5))
        progress_bar.setFixedSize(200, 200)

        self.worker_thread = WorkerThread('CPU')
        self.worker_thread.valueChanged.connect(progress_bar.setValue)
        self.worker_thread.freqChanged.connect(self.update_freq)
        self.worker_thread.start()

        progress_bar2 = RoundProgressBar()
        temperature_bar = TempProgressBar()
        gpu_memory_bar = CustomProgressBar()
        gpu_memory_bar.setMinimum(0)
        gpu_memory_bar.setMaximum(round(display_info['gpu']['memory_total_MB'] / 1024,2))

        # Add the progress bar to the gpu
        layout2 = QVBoxLayout(self.ui.widget_gpu_util)
        layout2.addWidget(progress_bar2)
        progress_bar2.setGeometry(QRect(0, 0, 5, 5))
        progress_bar2.setFixedSize(200, 200)

        layout3 = QVBoxLayout(self.ui.widget_gpu_temp)
        layout3.addWidget(temperature_bar)
        temperature_bar.setGeometry(QRect(0, 0, 5, 5))
        temperature_bar.setFixedSize(200, 200)

        layout4 = QVBoxLayout(self.ui.widget_gpu_mem)
        layout4.addWidget(gpu_memory_bar)
        gpu_memory_bar.setFixedSize(250, 50)

        self.worker_thread2 = WorkerThread('GPU')
        self.worker_thread2.valueChanged.connect(progress_bar2.setValue)
        self.worker_thread2.tempChanged.connect(temperature_bar.setValue)
        self.worker_thread2.memChanged.connect(gpu_memory_bar.setValue)
        self.worker_thread2.start()

        # Add the progress bar to the ram
        ram_usage_bar = RoundProgressBar()
        layout5 = QVBoxLayout(self.ui.widget_ram_usage)
        layout5.addWidget(ram_usage_bar)
        ram_usage_bar.setFixedSize(200, 200)

        ram_used_mem = CustomProgressBar()
        ram_used_mem.setMinimum(0)
        ram_used_mem.setMaximum(display_info['ram']['RAMTotalInstalledGB'])
        layout6 = QVBoxLayout(self.ui.widget_ram_used)
        layout6.addWidget(ram_used_mem)
        ram_used_mem.setFixedSize(250, 50)

        self.worker_thread3 = WorkerThread('RAM')
        self.worker_thread3.valueChanged.connect(ram_usage_bar.setValue)
        self.worker_thread3.memChanged.connect(ram_used_mem.setValue)
        self.worker_thread3.start()






#==============================================================================================================
#===========================================  Assistant  ======================================================

        scroll_layout =QVBoxLayout()
        scroll_layout.setAlignment(Qt.AlignTop)
        self.ui.scrollAreaWidgetContents.setLayout(scroll_layout)


        self.botThread = BotThread()
        self.botThread.botMessage.connect(self.add_text_to_scrollarea)
        self.ui.pushButton_14.clicked.connect(self.toggle_bot_thread)



        self.ui.pushButton_15.clicked.connect(lambda : self.add_text_to_scrollarea())






        self.show()







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    sys.exit(app.exec())

