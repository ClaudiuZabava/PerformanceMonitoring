import ctypes
import sqlite3
import time
import os
import win32gui
from datetime import datetime
import psutil
import win32process


class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [
        ('cbSize', ctypes.c_uint),
        ('dwTime', ctypes.c_uint),
    ]