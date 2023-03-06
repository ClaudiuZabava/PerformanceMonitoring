import psutil

_cpu_data = {}


def cpu_info():
    # CPU TYPE
    # VENDOR
    # CPU CORES
    # CPU BASE FREQUENCY
    pass


def cpu_temperature():
    # CPU TEMPERATURE
    pass


def cpu_frequency():
    # CPU FREQUENCY
    pass


def cpu_usage_data():

    _cpu_usage = psutil.cpu_percent(interval=1)
    _cpu_data['CPUUsage'] = _cpu_usage

    return _cpu_data

