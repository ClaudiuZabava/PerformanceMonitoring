import ctypes
import sqlite3
import time
import os
import win32gui
from datetime import datetime
import psutil
import win32process



def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    return window, title

def get_app_name(window_handle):
    try:
        _, pid = win32process.GetWindowThreadProcessId(window_handle)  # modificat pentru a obtine PID
        return psutil.Process(pid).name()
    except:
        return "unknown"

class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [
        ('cbSize', ctypes.c_uint),
        ('dwTime', ctypes.c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = ctypes.sizeof(lastInputInfo)
    if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo)):
        millis = ctypes.windll.kernel32.GetTickCount() - lastInputInfo.dwTime
        return millis / 1000.0  # Convert to seconds
    else:
        return 0  # Could not get idle time


# def monitor(conn, c, thread):
#     nr=0
#
#
#     while thread.running:
#         nr+=1



def monitor(conn, c, thread):

    _stats={}
    print("Start monitoring...")
    current_app = ''
    start_time = datetime.now()
    idle_time_start = None
    real_active_time = 0

    try:
        while thread.running:
            print("Monitor running")
            try:
                new_app_handle, new_app_title = get_active_window_title()
                new_app_name = get_app_name(new_app_handle)
                print(new_app_name, new_app_title)
                idle_duration = get_idle_duration()
                print(idle_duration)

                # Verifica daca utilizatorul a fost inactiv
                if idle_duration > 10.0:  # Daca inactivitatea este mai mare de 10 sec
                    if idle_time_start is None:  # Prima data cand detectam inactivitate
                        print("Reached ")
                        idle_time_start = datetime.now()
                else:
                    if idle_time_start is not None:  # Daca a fost o perioada de inactivitate
                        idle_duration = (datetime.now() - idle_time_start).seconds
                        print("Idle for", idle_duration, "seconds")
                        real_active_time -= idle_duration  # Scade perioada de inactivitate din timpul de activitate
                        idle_time_start = None  # Reseteaza timpul de start al inactivitatii

                if new_app_name != current_app:
                    end_time = datetime.now()
                    usage_time = (end_time - start_time).seconds
                    real_active_time = usage_time - abs(real_active_time)

                    if current_app != '':
                        c.execute("INSERT INTO usagestat VALUES (?, ?, ?, ?, ?, ?, ?)",
                                  (current_app, current_title, str(datetime.now().date()), str(start_time), str(end_time),
                                   usage_time, real_active_time))

                    current_app = new_app_name
                    current_title = new_app_title
                    start_time = datetime.now()
                time.sleep(1)  # Cateva secunde de pauza
            except Exception as e:
                break
    except Exception as d:
        pass






# import sqlite3
# import time
# import os
# import win32gui
# from datetime import datetime
#
# # Cream baza de date si tabela
# conn = sqlite3.connect('app_usage.db')
# c = conn.cursor()
# c.execute("""
#           CREATE TABLE IF NOT EXISTS usagestat
#           (appname TEXT, currentdate TEXT, starttime TEXT, endtime TEXT, usagetime INTEGER)
#           """)
#
# # Functia care returneaza numele ferestrei active
# def get_active_window_title():
#     window = win32gui.GetForegroundWindow()
#     title = win32gui.GetWindowText(window)
#     return title
#
# def main():
#     print("Start monitoring...")
#     current_app = ''
#     start_time = datetime.now()
#
#     try:
#         while True:
#             new_app = get_active_window_title()
#             if new_app != current_app:
#                 end_time = datetime.now()
#                 usage_time = (end_time - start_time).seconds
#
#                 if current_app != '':
#                     c.execute("INSERT INTO usagestat VALUES (?, ?, ?, ?, ?)",
#                               (current_app, str(datetime.now().date()), str(start_time), str(end_time), usage_time))
#
#                 current_app = new_app
#                 start_time = datetime.now()
#
#             time.sleep(1)  # Cateva secunde de pauza
#     except KeyboardInterrupt:
#         print("Stop monitoring...")
#     finally:
#         # La finalizarea monitorizarii, înregistrează timpul petrecut în ultima aplicație
#         end_time = datetime.now()
#         usage_time = (end_time - start_time).seconds
#         if current_app != '':
#             c.execute("INSERT INTO usagestat VALUES (?, ?, ?, ?, ?)",
#                       (current_app, str(datetime.now().date()), str(start_time), str(end_time), usage_time))
#
#         # Salvează toate modificările și închide conexiunea cu baza de date
#         conn.commit()
#         conn.close()
#
# if __name__ == '__main__':
#     main()
