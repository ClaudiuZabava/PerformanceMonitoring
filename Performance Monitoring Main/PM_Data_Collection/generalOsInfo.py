import platform
import socket
import os
import datetime
import psutil

_system_general_info = {}

def get_system_info():
    os_info = platform.uname()
    system = os_info.system
    os_version = os_info.version
    os_release = os_info.release
    architecture = os_info.machine
    processor_type = os_info.processor
    hostname = socket.gethostname()

    # Extrage OS installation date
    os_installation_time = os.path.getctime("/")
    os_installation_date = datetime.datetime.fromtimestamp(os_installation_time).strftime("%Y-%m-%d")

    _system_general_info['system'] = system
    _system_general_info['os_version'] = os_version
    _system_general_info['os_release'] = os_release
    _system_general_info['architecture'] = architecture
    _system_general_info['processor_type'] = processor_type
    _system_general_info['hostname'] = hostname
    _system_general_info['os_installation_date'] = os_installation_date



    return _system_general_info if _system_general_info else None

