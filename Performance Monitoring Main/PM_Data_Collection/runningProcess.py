import psutil
import win32api

def active_proc():
    _info_procese = []

    active_pids = psutil.pids()

    for pid in active_pids:
        try:
            process = psutil.Process(pid)
        except psutil.NoSuchProcess:
            return -1

        _details = {}

        _details['PID'] = pid
        _details['Name'] = process.name()
        _details['Status'] = process.status()
        _details['Private Bytes'] = process.memory_info().private
        _details['Resident Set Size (RAM)'] = process.memory_info().rss
        _details['Virtual Memory'] = process.memory_info().vms
        _details['Working Set'] = process.memory_info().wset

        try:
            _details['Company Name'] = win32api.GetFileVersionInfo(process.exe(), '\\StringFileInfo\\040904b0\\CompanyName')
        except Exception:
            _details['Company Name'] = 'N/A'

        _info_procese.append(_details)

    return _info_procese if _info_procese else None


def get_user_from_pid(pid):
    user = None
    try:
        process = psutil.Process(pid)
        user = process.username()
        return user
    except psutil.NoSuchProcess:
        return -1
    except psutil.AccessDenied:
        return 0

def express_kill(pid):
    try:
        parent = psutil.Process(pid)
    except psutil.NoSuchProcess:
        return -1

    children = parent.children(recursive=True)

    for child in children:
        try:
            child.terminate()
        except psutil.NoSuchProcess:
            return 0
        except psutil.AccessDenied:
            return -1

    parent.terminate()

    gone, still_alive = psutil.wait_procs([parent] + children, timeout=3)

    for p in still_alive:
        p.kill()

    return 1

def terminate_process_and_children(pid):

    if get_user_from_pid(pid) != 0 and get_user_from_pid(pid) != -1:
        return express_kill(pid)
    else:
        return 1020




