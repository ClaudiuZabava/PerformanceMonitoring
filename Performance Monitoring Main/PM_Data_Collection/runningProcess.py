import psutil

def active_proc():
    _info_procese = []

    for proces in psutil.process_iter(['pid', 'name', 'status', 'memory_info']):
        _info_proces = {
            'PID': proces.info['pid'],
            'Name': proces.info['name'],
            'Status': proces.info['status'],
            'Memory(MB)': proces.info['memory_info'].rss / (1024 * 1024),
        }

        _info_procese.append(_info_proces)

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


prr = active_proc()

for p in prr:
    print(p)


