import webbrowser
import win32gui, win32con
import speech_recognition as sr
from datetime import datetime
from links import youtube_link
from g_links import google_link
import os
import send2trash
import ctypes
import subprocess



def no_disturb():
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_MINIMIZE)

def go_youtube(txt):
    link = youtube_link(txt)
    webbrowser.open_new_tab(link)
    #root.after(690, lambda: no_disturb()) # use 550 for a very fast pc || use 1000 for low end pc

def go_google(txt):
    link = google_link(txt)
    webbrowser.open_new_tab(link)
def search_google(txt):
    link = "https://www.google.com/search?q=" + txt
    webbrowser.open_new_tab(link)


def go_wiki(txt):
    link = "https://en.wikipedia.org/wiki/"+txt
    webbrowser.open_new_tab(link)


# ======================== Welcome Text ==========================
def welcome_text():
    now = datetime.now()
    time = int(now.strftime("%H"))
    salut=" Hello, Sir!"
    if (time > 18 and time <=23) or (time >= 0 and time <=6):
        salut=" Good Evening, Sir!"
    elif time > 6 and time<=11:
        salut=" Good Morning, Sir!"
    elif time > 11 and time <= 14:
        salut=" Good day, Sir!"
    elif time > 14 and time <= 18:
        salut=" Good Afternoon, Sir!"
    salut = salut+ " How can I help you?"
    return salut

# ======================== Voice Listener ==========================
def voice_cmd():
    init_rec = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = init_rec.record(source, duration=5)
        try:
            text = init_rec.recognize_google(audio_data)
        except Exception as e:
            return 1911
        else:
            return text


# ======================== Find and Delete ==========================


def find_file(fname, ext, bdir, condition=0):
    check = 0
    finds =[]
    message = " I found this file in those folders: "
    for roots, dirs, files in os.walk(bdir):
        for file in files:
            if file.endswith(ext) and str(file).upper() == fname.upper():
                check += 1
                finds.append(roots + '\\' + str(file))
                if condition == 0:
                    subprocess.run(f'explorer /select,"{os.path.join(roots, file)}"')
    if check == 0:
        message = " Looks like this file doesn't exist on this partition"

    if condition == 0:
        return message
    else:
        return finds if len(finds) > 0 else None


def delete_all(filename, ext, bdir):
    message = ""
    check = 0
    paths = find_file(filename, ext, bdir, 1)
    confirm = 0
    if paths != None:
        confirm = ctypes.windll.user32.MessageBoxW(None, f"Are you sure you want to delete all the files with name {filename}?",
                                               "Delete Confirm", 1)
    if confirm == 1:
        for file_path in paths:
            if os.path.exists(file_path):
                file_path = os.path.normpath(file_path)
                try:
                    print(file_path)
                    send2trash.send2trash(file_path)

                    check += 1
                except OSError:
                    message = " The file " + str(filename) + " could not be deleted. The remove process has stopped."
                    break

            else:
                message = " The file " + str(filename) + " could not be found. The remove process has stopped."
                break
    else:
        message = " The remove process has ben canceled."

    if check == len(paths):
        message = "A number of " + str(check) + " files with the name " + str(filename) + " have been deleted."

    return message if message != "" else None
