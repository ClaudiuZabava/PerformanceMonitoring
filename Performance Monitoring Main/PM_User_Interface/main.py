import os
import re
import sys
from assistantPanel import *
from chatBot import *
from statisticsGeneratorLibs import *

from datetime import datetime, timedelta
import sqlite3
from collections import defaultdict
from operator import itemgetter
import matplotlib.pyplot as plt

from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QProgressBar, QTableWidgetItem, QLabel
from PySide6 import QtCore
from PySide6.QtCore import QEvent, QTimer, QThread, Signal, Slot, QSemaphore, QMutex, QWaitCondition
from PySide6 import QtGui
from ui_App import *
from progressBar import RoundProgressBar, TempProgressBar, CustomProgressBar

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
parent_dir = os.path.dirname(current_dir)
data_collection_dir = os.path.join(parent_dir, "PM_Data_Collection")
sys.path.insert(0, data_collection_dir)

# Import la filele de colectare aflate in folderul local
from cpuData import cpu_info, cpu_frequency, cpu_usage
from gpuData import get_gpu_info, get_gpu_usage_data
from memoryData import ram_info, ram_usage_data
from driveInfo import get_disk_info
from DataCollection import system_Information
from diskData import all_disks_mem_data, disk_read_write_speed
from networkData import net_stat
from runningProcess import active_proc, terminate_process_and_children, express_kill



# =========================================== Worker Thread ===========================================

class WorkerThread(QThread):
    valueChanged = Signal(float)
    freqChanged = Signal(str)
    tempChanged = Signal(float)
    memChanged = Signal(float)
    readChanged = Signal(str)
    writeChanged = Signal(str)
    btSentChanged = Signal(str)
    btRecvChanged = Signal(str)
    pkSentChanged = Signal(str)
    pkRecvChanged = Signal(str)

    def __init__(self, data_type, parent=None):
        super().__init__(parent)
        self.data_type = data_type  # store the data type to collect
        self.running = True

    def run(self):
        sleep_time = 500
        while self.running:  # continuously update the value
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
            elif self.data_type == 'NET':
                net_usage = net_stat()
                self.btSentChanged.emit(str(net_usage['bytes_sent_per_second']) + '/s')
                self.btRecvChanged.emit(str(net_usage['bytes_received_per_second']) + '/s')
                self.pkSentChanged.emit(str(net_usage['packets_sent_per_second']) + '/s')
                self.pkRecvChanged.emit(str(net_usage['packets_received_per_second']) + '/s')
                sleep_time = 500
            elif self.data_type == 'DISK':
                disk_read, disk_write = disk_read_write_speed()
                if disk_read >= 1:
                    disk_read = str(round(disk_read,2)) + " MB/s"
                else:
                    disk_read = str(round(disk_read * 1024,2)) + " kB/s"

                if disk_write >=1:
                    disk_write = str(round(disk_write, 2)) + " MB/s"
                else:
                    disk_write = str(round(disk_write * 1024,2)) + " kB/s"

                self.readChanged.emit(disk_read)
                self.writeChanged.emit(disk_write)
                sleep_time = 500
            self.msleep(sleep_time)

    def stop(self):
        self.running = False
# ==================================================================================================


# =========================================== Processes Thread ===========================================

class ProcessTableUpdaterThread(QThread):
    processListUpdated = Signal(list)  # Emit acest semnal atunci cand lista de procese este actualizata
    old_process_list = []  # Lista de procese de la ultima actualizare

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        while self.running:
            process_list = active_proc()
            if self.old_process_list != process_list:
                print(True)
                self.processListUpdated.emit(process_list)
                self.old_process_list = process_list
            self.msleep(10000)

    def stop(self):
        print("Stopped Process Table Updater Thread")
        self.running = False
# ==================================================================================================


# =========================================== Assistant BOT Thread ===========================================

class BotThread(QThread):
    assistant = GenericAssistant('intents.json', model_name="assistant_bot")
    assistant.load_model('assistant_bot')


    tt = ["FIRSTTIME"]
    bdir ='D:\\' if os.path.exists('D:\\') else 'C:\\' if os.path.exists('C:\\') else 'E:\\'
    message = ""
    botMessage = Signal(str)
    botSemaphore = QSemaphore(0)  # Inițializare semafor cu 0, ceea ce înseamnă că este blocat

    def __init__(self):
        super().__init__()
        self.running = True


    def actions(self, k):
        ct = '[' + datetime.now().strftime('%H:%M:%S') + ']'
        if self.tt[k].upper() == "PLAY":
            if len(self.tt) > (k+1):
                target = ' '.join(self.tt[(k+1):])
                self.message = "💻"+ ct+ " I'll play: " + target
                go_youtube(target)
            else:
                self.message ="💻"+ ct+" Type Play then the name of the song / video you would like to play, sir!"
                pass
        elif self.tt[k].upper() == "GO":
            if len(self.tt) > (k+1):
                target = ' '.join(self.tt[(k+1):])
                self.message = "💻"+ ct+" I'll go to: " + target
                go_google(target)
            else:
                self.message ="💻"+ ct+" Type Go and the destination site name, sir!"
                pass
        elif self.tt[k].upper() == "WIKI":
            if len(self.tt) > (k+1):
                target = '_'.join(self.tt[(k+1):])
                self.message ="💻"+ ct+" I'll wiki: " + target
                go_wiki(target)
            else:
                self.message ="💻"+ ct+" Type Wiki and the text you would like to search on Wikipedia, sir!"
                pass
        elif self.tt[k].upper() == "SEARCH":
            if len(self.tt) > (k+1):
                target = ' '.join(self.tt[(k+1):])
                self.message ="💻"+ ct+" I'll search: " + target
                target = '%20'.join(self.tt[(k + 1):])
                search_google(target)
            else:
                self.message = "💻"+ ct+" Type Search and the text you would like to search on google, sir!"
                pass
        if self.tt[k].upper() == "CHANGE":
            if len(self.tt) > (k+2) and self.tt[(k+1)].upper() == "TO":
                self.bdir = self.tt[(k+2)]+':'+'/'
                self.message = "💻"+ ct+" I'll change current directory to: " + self.bdir
            else:
                self.message ="💻"+ ct+" Type the name of the partition you want to look into. "
                pass
        elif self.tt[k].upper() == "FIND":
            if len(self.tt) > (k+2):
                ext = self.tt[(k+2)]
                fname = self.tt[(k+1)]+'.'+ext
                txt = find_file(fname, ext, self.bdir)
                self.message ="💻"+ ct + txt
            else:
                self.message = "💻"+ ct+" Please specify the file name and extension (eg: run.exe)"
                pass
        elif self.tt[k].upper() == "REMOVE":
            if self.tt[(k+1)].upper() == "ALL":
                if len(self.tt) > (k+3):
                    ext = self.tt[(k+3)]
                    fname = self.tt[(k+2)]+'.'+ext
                    txt = delete_all(fname, ext, self.bdir)
                    self.message ="💻"+ ct + txt
                else:
                    self.message = "💻"+ ct+" Please specify the file name and extension (eg: run.exe)"
                    pass
            else:
                if len(self.tt) > (k + 2):
                    ext = self.tt[(k + 2)]
                    fname = self.tt[(k + 1)] + '.' + ext
                    txt = delete_all(fname, ext, self.bdir)
                    self.message = "💻" + ct + txt
                else:
                    self.message = "💻" + ct + " Please specify the file name and extension (eg: run.exe)"
                    pass
        elif self.tt[k].upper() == "INFO":
            if len(self.tt) > (k+2):
                check = 0
                ext = self.tt[(k+2)]
                procname = self.tt[(k+1)]+'.'+ext
                list = active_proc()
                for pr in list:
                    if str(pr['Name']).upper() == procname.upper():
                        check +=1
                        self.message = "💻" + ct + " Info for process called " + procname + ": " + "\n PID: " + str(
                            pr['PID']) + "\n Name: " + str(pr['Name']) + \
                                       "\n Status: " + str(pr['Status']) + "\n Private Bytes: " + str(pr['Private Bytes']) + "\n RSS: " + str(
                            pr['Resident Set Size (RAM)']) + \
                                       "\n Virtual Memory: " + str(pr['Virtual Memory']) + "\n Working Set: " + str(pr['Working Set']) + "\n Company: " + str(
                            pr['Company Name'])
                        break

                if check == 0:
                    self.message ="💻"+ ct + "No process called " + procname + " is running!"
            elif len(self.tt) > (k+1):
                check = 0
                procID = self.tt[(k + 1)]
                list = active_proc()
                for pr in list:
                    if str(pr['PID']) == procID:
                        check += 1
                        self.message = "💻" + ct + " Info for process with ID " + procID + ": " + "\n PID: " + str(
                            pr['PID']) + "\n Name: " + str(pr['Name']) + \
                                       "\n Status: " + str(pr['Status']) + "\n Private Bytes: " + str(pr['Private Bytes']) + "\n RSS: " + str(
                            pr['Resident Set Size (RAM)']) + \
                                       "\n Virtual Memory: " + str(pr['Virtual Memory']) + "\n Working Set: " + str(pr['Working Set']) + "\n Company: " + str(
                            pr['Company Name'])
                        break
                if check == 0:
                    self.message = "💻" + ct + " No process with ID " + str(procID) + " is running!"
            else:
                self.message = "💻" + ct + " Please specify the process name and extension (eg: run.exe) or just the PID"
                pass


    def retrive(self):
        ct = '[' + datetime.now().strftime('%H:%M:%S') + ']'
        t=' '.join(self.tt) if len(self.tt)>1 else self.tt[0]
        if len(self.tt)>1:
            if self.tt[0].upper() in open(os.getcwd()+"/Vocabulary/Action.txt").read():
                if len(self.tt)>2 and self.tt[0].upper() == "LET" and self.tt[1].upper() == "S":
                    self.actions(2)
                else:
                    self.actions(0)
                    pass
            elif self.tt[0].upper() == "HEAR" and self.tt[1].upper() == "ME":
                verify = voice_cmd()
                if verify != 1911:
                    self.tt = re.split('\W+', verify)
                    if self.tt[0].upper() in open(os.getcwd() + "/Vocabulary/Action.txt").read():
                        if len(self.tt) > 1:
                            if self.tt[0].upper() == "LET" and self.tt[1].upper() == "S":
                                self.actions(2)
                            else:
                                self.actions(0)
                                pass
                        else:
                            self.message = "💻"+ ct+ "Sorry Sir, I didn't understand that..."
                    else:
                        bot_reply = self.assistant.request(verify)
                        self.message = "💻" + ct + "I think I heared: " + verify + "\n" + "💻" + ct + bot_reply
                else:
                    self.message = "💻"+ ct+ "Sorry Sir, I didn't understand that..."
            else:
                bot_reply = self.assistant.request(t)
                self.message = "💻" + ct + bot_reply
                pass
        elif len(self.tt)==1 and self.tt[0].upper() == "FIRSTTIME":
            self.message = "💻"+ ct + welcome_text()
        else:
            bot_reply = self.assistant.request(t)
            self.message = "💻"+ ct+ bot_reply
            pass


    def run(self):
        while self.running:
            self.botSemaphore.acquire()  # Așteaptă până când semaforul este deblocat

            if self.running == False:
                break

            self.retrive()
            self.botMessage.emit(self.message)
    def unlock(self, text):  # Apelat când vrem ca botul să scrie un mesaj
        if text == None or text == "":
            text = "Hello"
        self.tt = re.split('\W+', text)
        self.botSemaphore.release()  # Deblocare semafor

    def stop(self):
        self.running = False



# ==================================================================================================


# =========================================== Statistics Thread ===========================================

class AppUsageMonitor(QThread):

    def __init__(self, mutex, wait_cond):
        super().__init__()
        self.conn = None
        self.c = None
        self.mutex = mutex
        self.wait_cond = wait_cond
        self.sibling_thread = None
        self.running = True

    def get_app_usage(self):
        self.c.execute("""
            SELECT currentdate, appname, realactivetime, usagetime
            FROM usagestat 
            ORDER BY realactivetime DESC
        """)
        rows = self.c.fetchall()
        result_dict = defaultdict(list)
        for row in rows:
            date, app, real_active_time, usage_time = row
            result_dict[date].append((app, real_active_time, usage_time))

        return dict(result_dict) if result_dict else None

    def get_sibling_thread(self, sibling_thread):
        self.sibling_thread = sibling_thread

    def get_active_window(self):
        window = win32gui.GetForegroundWindow()
        return window


    def get_app_name(self,window_handle):
        try:
            _, pid = win32process.GetWindowThreadProcessId(window_handle)  # modificat pentru a obtine PID
            return psutil.Process(pid).name()
        except:
            return "unknown"

    def get_idle_duration(self):
        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = ctypes.sizeof(lastInputInfo)
        if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo)):
            millis = ctypes.windll.kernel32.GetTickCount() - lastInputInfo.dwTime
            return millis / 1000.0  # Convert to seconds
        else:
            return 0  # Nu se poate obține durata inactivității



    def run(self):
        self.conn = sqlite3.connect('app_usage.db')
        self.c = self.conn.cursor()
        self.c.execute("""
                  CREATE TABLE IF NOT EXISTS usagestat
                  (appname TEXT, currentdate TEXT, starttime TEXT, endtime TEXT, usagetime INTEGER, realactivetime INTEGER)
                  """)
        rez = self.get_app_usage()
        self.mutex.lock()
        if self.sibling_thread is not None:
            self.sibling_thread.rez_dict = rez
            self.wait_cond.wakeAll()
        self.mutex.unlock()

        current_app = ''
        start_time = datetime.now()
        idle_time_start = None
        real_active_time = 0
        try:
            while self.running:
                try:
                    new_app_handle = self.get_active_window()
                    new_app_name = self.get_app_name(new_app_handle)
                    idle_duration = self.get_idle_duration()

                    if idle_duration > 10.0:  # Daca inactivitatea este mai mare de 10 sec
                        if idle_time_start is None:  # Prima data cand detectam inactivitate
                            idle_time_start = datetime.now()
                    else:
                        if idle_time_start is not None:  # Daca a fost o perioada de inactivitate
                            idle_duration = (datetime.now() - idle_time_start).seconds
                            #print("Idle for", idle_duration, "seconds")
                            real_active_time -= idle_duration  # Scade perioada de inactivitate din timpul de activitate
                            idle_time_start = None  # Reseteaza timpul de start al inactivitatii

                    if new_app_name != current_app:
                        end_time = datetime.now()
                        usage_time = (end_time - start_time).seconds
                        real_active_time = usage_time - abs(real_active_time)

                        if current_app != '':
                            self.c.execute("INSERT INTO usagestat VALUES (?, ?, ?, ?, ?, ?)",
                                           (current_app, str(datetime.now().date()), str(start_time),
                                            str(end_time),
                                            usage_time, real_active_time))

                        current_app = new_app_name
                        real_active_time = 0
                        start_time = datetime.now()
                    time.sleep(1)  # Cateva secunde de pauza
                except Exception as e:
                    print(f"Exception occurred: {e}")
                    break
        except Exception as d:
            print("Stop aici")
            pass

        if self.running == False:
            end_time = datetime.now()
            usage_time = (end_time - start_time).seconds
            real_active_time = usage_time - abs(real_active_time)
            print(usage_time)
            print(real_active_time)
            if current_app != '':
                self.c.execute("INSERT INTO usagestat VALUES (?, ?, ?, ?, ?, ?)",
                               (current_app, str(datetime.now().date()), str(start_time),
                                str(end_time),
                                usage_time, real_active_time))
            real_active_time = 0
            print("AppUsageMonitor thread is exiting...")
            self.conn.commit()
            self.conn.close()

        self.quit()





    def stop(self):
        print("Stop method was called.")
        self.running = False
        print(self.running)



class StatisticsThread(QThread):

    def __init__(self, mutex, wait_cond):
        super().__init__()
        self.rez_dict = None
        self.mutex = mutex
        self.wait_cond = wait_cond
        self.running = True

    def get_total_real_active_time_per_day(self, rez_dict):
        result_dict = {}
        for date, app_infos in rez_dict.items():
            for app_info in app_infos:
                app, total_time, _ = app_info
                if date not in result_dict:
                    result_dict[date] = [(app, total_time)]
                else:
                    result_dict[date].append((app, total_time))
        return result_dict

    def get_total_usage_time_per_day(self, rez_dict):
        result_dict = {}
        for date, app_infos in rez_dict.items():
            for app_info in app_infos:
                app, _, usage_time = app_info
                if date not in result_dict:
                    result_dict[date] = usage_time
                else:
                    result_dict[date] += usage_time


        final_dict = {k: result_dict[k] for k in sorted(result_dict.keys(), reverse=True)[:7]}

        return final_dict if final_dict else None


    def get_top5_apps_last7days(self, stats_dict):

        app_time = defaultdict(int)
        sorted_dates = sorted(stats_dict.keys(), reverse=True)[:7]

        for date in sorted_dates:
            for app, time in stats_dict[date]:
                app_time[app] += time
        top5_apps = sorted(app_time.items(), key=itemgetter(1), reverse=True)[:5]
        return top5_apps if top5_apps else []

    def get_top5_apps_lastday(self, stats_dict):
        app_time = defaultdict(int)

        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        # Daca nu avem inregistrari pentru ziua de ieri, returnam o lista goala
        if yesterday not in stats_dict:
            return []

        for app, real_time in stats_dict[yesterday]:
            app_time[app] += real_time

        # Sortam dictionarul dupa timp si ne luam primele 5 aplicatii
        top5_apps = sorted(app_time.items(), key=itemgetter(1), reverse=True)[:5]

        return top5_apps if top5_apps else []

    def plot_generator(self,  top5_apps, total_usage_per_day, top5_daily):
        apps = [app for app, _ in top5_apps]
        times = [time / 3600 for _, time in top5_apps]
        daily_apps = [app for app, _ in top5_daily]
        daily_times = [time / 3600 for _, time in top5_daily]  # top 5 apps in ultima zi
        total_usage_times = [time / 3600 for time in total_usage_per_day.values()]
        dates = list(total_usage_per_day.keys())

        fig1, ax1 = plt.subplots(figsize=(4.0, 2.5), dpi=100)
        ax1.bar(apps, times, color='blue')
        ax1.set_xlabel("Apps")
        ax1.set_ylabel("Time Spent (hours)")
        ax1.set_title("Most used apps the last 7 days")
        plt.xticks(rotation=10)
        ax1.tick_params(axis='x', labelsize=6)
        fig1.savefig("statistics/top5_apps.png", dpi=100)

        fig2, ax2 = plt.subplots(figsize=(4.0, 2.5), dpi=100)
        ax2.plot(dates, total_usage_times, color='red')
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Time Spent (hours)")
        ax2.set_title("Time spent on PC the last 7 days")
        plt.xticks(rotation=10)
        ax2.tick_params(axis='x', labelsize=6)
        fig2.savefig("statistics/pc_time.png", dpi=100)

        fig1, ax1 = plt.subplots(figsize=(4.0, 2.5), dpi=100)
        ax1.bar(daily_apps, daily_times, color='blue')
        ax1.set_xlabel("Apps")
        ax1.set_ylabel("Time Spent (hours)")
        ax1.set_title("Most used apps the last day")
        plt.xticks(rotation=10)
        ax1.tick_params(axis='x', labelsize=6)
        fig1.savefig("statistics/top5_daily.png", dpi=100)

    def run(self):

        self.mutex.lock()
        while self.rez_dict is None:
            self.wait_cond.wait(self.mutex)
        self.mutex.unlock()
        stats_dict = self.get_total_real_active_time_per_day(self.rez_dict)
        top5_apps = self.get_top5_apps_last7days(stats_dict)
        top5_daily = self.get_top5_apps_lastday(stats_dict)
        total_usage_per_day = self.get_total_usage_time_per_day(self.rez_dict)
        self.plot_generator(top5_apps, total_usage_per_day, top5_daily)
        self.quit()

    def stop(self):
        self.running = False




# ==================================================================================================


# ==================================== Main Application =============================================

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


    def show_daily(self):
        pixmap = QPixmap("statistics/top5_daily.png")
        pixmap_r1 = pixmap.scaled(400,250, Qt.KeepAspectRatio)
        self.ui.label_90.setPixmap(pixmap_r1)

    def show_weekly(self):
        pixmap = QPixmap("statistics/top5_apps.png")
        pixmap_r1 = pixmap.scaled(400,250, Qt.KeepAspectRatio)
        self.ui.label_90.setPixmap(pixmap_r1)

    def load_image_into_frame(self):
        pixmap = QPixmap("statistics/pc_time.png")
        pixmap_r2 = pixmap.scaled(400,250, Qt.KeepAspectRatio)
        self.ui.label_89.setPixmap(pixmap_r2)
        self.show_weekly()
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.statistics)

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
            self.botThread.unlock(text)

    # metoda suprascrisa pentru a putea folosi enter pentru a trimite mesajul
    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and source is self.ui.plainTextEdit):
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                self.add_text_to_scrollarea()
                return True
        return super(MainApp, self).eventFilter(source, event)


    def add_process_to_table(self, process_info):
        self.ui.tableWidget2.insertRow(0)

        self.ui.tableWidget2.setItem(0, 0, QTableWidgetItem(str(process_info['PID'])))
        self.ui.tableWidget2.setItem(0, 1, QTableWidgetItem(process_info['Name']))
        self.ui.tableWidget2.setItem(0, 2, QTableWidgetItem(process_info['Status']))
        self.ui.tableWidget2.setItem(0, 3, QTableWidgetItem(str(process_info['Private Bytes'])))
        self.ui.tableWidget2.setItem(0, 4, QTableWidgetItem(str(process_info['Resident Set Size (RAM)'])))
        self.ui.tableWidget2.setItem(0, 5, QTableWidgetItem(str(process_info['Virtual Memory'])))
        self.ui.tableWidget2.setItem(0, 6, QTableWidgetItem(str(process_info['Working Set'])))
        self.ui.tableWidget2.setItem(0, 7, QTableWidgetItem(str(process_info['Company Name'])))

        button = QPushButton("Kill")
        button.setStyleSheet("background-color: #505050")
        button.clicked.connect(lambda: self.handle_button_click(process_info['PID']))
        self.ui.tableWidget2.setCellWidget(0, 8, button)

    def update_process_table(self, process_list):
        self.ui.tableWidget2.setRowCount(0)
        for process in process_list:
            self.add_process_to_table(process)  # Adauga fiecare proces in tabel

    def handle_button_click(self,pid):
        result = terminate_process_and_children(pid)
        if result == 1020:

            self.pending_kill_pid = pid
            self.ui.label_70.setText("This PID:{" + str(pid) + "} is A SYSTEM or a System-Related process. Are you sure you want to kill it?")
            self.ui.pushButton_16.show()
            self.ui.pushButton_17.show()
        elif result == 0:
            self.ui.label_70.setText("Error! Could not kill the process with PID:{" + str(pid) + "}")
        else:
            self.ui.pushButton_16.hide()
            self.ui.pushButton_17.hide()
            self.ui.label_70.setText("Process with PID:{" + str(pid) + "} has been killed!")

    def handle_express_kill_button_click(self):
        if self.pending_kill_pid is not None:
            try:
                res = express_kill(self.pending_kill_pid)
                if res != 1:
                    self.ui.label_70.setText("Error! Could not kill the process with PID:{" + str(self.pending_kill_pid) + "}")
                else:
                    self.ui.label_70.setText("Process with PID:{" + str(self.pending_kill_pid) + "} has been killed!")
                self.pending_kill_pid = None
            except Exception as e:
                self.ui.label_70.setText("Error! Could not kill the process with PID:{" + str(self.pending_kill_pid) + "}")
                self.pending_kill_pid = None
                print(e)
        self.ui.pushButton_16.hide()
        self.ui.pushButton_17.hide()

    def abort_kill(self):
        self.pending_kill_pid = None
        self.ui.pushButton_16.hide()
        self.ui.pushButton_17.hide()
        self.ui.label_70.setText("")

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
    def bt_sent(self, val):
        self.ui.label_102.setText(val)

    @Slot(str)
    def bt_recv(self, val):
        self.ui.label_103.setText(val)

    @Slot(str)
    def pk_sent(self, val):
        self.ui.label_104.setText(val)

    @Slot(str)
    def pk_recv(self, val):
        self.ui.label_105.setText(val)

    @Slot(str)
    def read_speed(self, val):
        self.ui.label_35.setText(val)

    @Slot(str)
    def write_speed(self, val):
        self.ui.label_69.setText(val)

    @Slot(str)
    def update_freq(self, freq):
        self.ui.label_21.setText(freq)

    def toggle_bot_thread(self):
        if self.botThread.isRunning():
            pass
        else:
            self.botThread.start()
            self.botThread.botSemaphore.release()

    def closeEvent(self, event):

        self.worker_thread.stop()
        self.worker_thread.wait()

        self.worker_thread2.stop()
        self.worker_thread2.wait()

        self.worker_thread3.stop()
        self.worker_thread3.wait()

        self.worker_thread4.stop()
        self.worker_thread4.wait()

        self.worker_thread5.stop()
        self.worker_thread5.wait()

        self.monitoring_thread.stop()
        self.monitoring_thread.wait()

        self.ProcessesThread.stop()
        self.ProcessesThread.wait()

        self.botThread.stop()
        self.botThread.botSemaphore.release()
        self.botThread.wait()

        event.accept()


    def __init__(self):
        QMainWindow.__init__(self)
        self.process_snapshot = {}
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

        self.ui.label_70.setText("")
        self.ui.pushButton_16.hide()
        self.ui.pushButton_17.hide()

        self.ui.pushButton_16.clicked.connect(lambda: self.handle_express_kill_button_click())
        self.ui.pushButton_17.clicked.connect(lambda: self.abort_kill())
        self.pending_kill_pid = None


        # Navigate between pages using buttons
        self.ui.pushButton_12.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.GPU))
        self.ui.pushButton_9.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.System))
        self.ui.pushButton_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.RAM))
        self.ui.pushButton_8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Disk))
        self.ui.pushButton_10.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Network))
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.CPU))
        self.ui.pushButton_11.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Processes))
        self.ui.pushButton_13.clicked.connect(lambda: self.load_image_into_frame())
        self.ui.pushButton_14.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.assistant))
        self.ui.pushButton_18.clicked.connect(lambda: self.show_daily())
        self.ui.pushButton_19.clicked.connect(lambda: self.show_weekly())



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
        self.ui.label_86.setText(str(display_info['system']['os_installation_date']))



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
        self.ui.tableWidget.setColumnCount(5)

        for partition_name, partition_data in display_info['disk'].items():
            if isinstance(partition_data, dict):  # asigura-te ca partition_data este un dictionar
                self.ui.tableWidget.insertRow(0)
                self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(partition_name))
                self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(str(partition_data['UsedPer'])))
                self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(str(round(partition_data['FreeMem']/1024**3 , 2))))
                self.ui.tableWidget.setItem(0, 3, QTableWidgetItem(str(round(partition_data['UsedMem']/1024**3 , 2))))
                self.ui.tableWidget.setItem(0, 4, QTableWidgetItem(str(round(partition_data['PartitionMem']/1024**3 , 2))))

        for i in reversed(range(self.ui.tableWidget.rowCount())):
            is_row_empty = all(
                self.ui.tableWidget.item(i, j) is None or not self.ui.tableWidget.item(i, j).text() for j in
                range(self.ui.tableWidget.columnCount()))
            if is_row_empty:
                self.ui.tableWidget.removeRow(i)

        # Prepare Table for Processes
        headers = ["PID", "Process Name", "Status", "Private Bytes", "Resident SetSize (RAM)", "Virtual Memory", "Working Set", "Company", "Actions"]
        for i in range(len(headers)):
            header_item = QTableWidgetItem(headers[i])
            brush = QBrush(QColor(0, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            header_item.setForeground(brush)
            self.ui.tableWidget2.setHorizontalHeaderItem(i, header_item)




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


        # Show changes on NET:

        self.worker_thread4 = WorkerThread('NET')
        self.worker_thread4.btSentChanged.connect(self.bt_sent)
        self.worker_thread4.btRecvChanged.connect(self.bt_recv)
        self.worker_thread4.pkSentChanged.connect(self.pk_sent)
        self.worker_thread4.pkRecvChanged.connect(self.pk_recv)
        self.worker_thread4.start()

        # Show changes on DISK:
        self.worker_thread5 = WorkerThread('DISK')
        self.worker_thread5.readChanged.connect(self.read_speed)
        self.worker_thread5.writeChanged.connect(self.write_speed)
        self.worker_thread5.start()


        # Show changes on Processes:

        self.ProcessesThread = ProcessTableUpdaterThread()
        self.ProcessesThread.processListUpdated.connect(self.update_process_table)
        self.ProcessesThread.start()






#==============================================================================================================
#===========================================  Assistant  ======================================================

        scroll_layout =QVBoxLayout()
        scroll_layout.setAlignment(Qt.AlignTop)
        self.ui.scrollAreaWidgetContents.setLayout(scroll_layout)

        self.ui.plainTextEdit.installEventFilter(self)

        self.botThread = BotThread()
        self.botThread.botMessage.connect(self.add_text_to_scrollarea)
        self.ui.pushButton_14.clicked.connect(self.toggle_bot_thread)



        self.ui.pushButton_15.clicked.connect(lambda : self.add_text_to_scrollarea())




# ==============================================================================================================
# ===========================================  Statistici  =====================================================
        self.query_mutex = QMutex()
        self.query_wait = QWaitCondition()
        self.monitoring_thread = AppUsageMonitor(self.query_mutex, self.query_wait)
        self.statistics_thread = StatisticsThread(self.query_mutex, self.query_wait)

        self.monitoring_thread.get_sibling_thread(self.statistics_thread)

        self.monitoring_thread.start()
        self.statistics_thread.start()






        self.show()







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    sys.exit(app.exec())

