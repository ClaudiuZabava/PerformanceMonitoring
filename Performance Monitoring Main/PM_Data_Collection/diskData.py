import psutil
import math
import time


_hard_disks = {}


def all_disks_mem_data():
    _total_memory = 0.0
    for _partition in psutil.disk_partitions():
        _key = _partition.device
        if _key not in _hard_disks:
            _hard_disks[_key] = {}
        _hard_disks[_key]['PartitionMem'] = psutil.disk_usage(_key).total
        _total_memory = _total_memory + _hard_disks[_key]['PartitionMem']
        _hard_disks[_key]['UsedMem'] = psutil.disk_usage(_key).used
        _hard_disks[_key]['FreeMem'] = psutil.disk_usage(_key).free
        _hard_disks[_key]['UsedPer'] = psutil.disk_usage(_key).percent

    total_memory = math.ceil(_total_memory/1024**3)
    _hard_disks['TotalMem'] = total_memory

    return _hard_disks if _hard_disks else None


def disk_read_write_speed():
    _disk_io_counter = psutil.disk_io_counters()
    _disk_read_bytes = _disk_io_counter[2]
    _disk_write_bytes = _disk_io_counter[3]
    time.sleep(1)
    _disk_io_counter = psutil.disk_io_counters()
    _disk_read_bytes1 = _disk_io_counter[2]
    _disk_write_bytes1 = _disk_io_counter[3]

    _total_read = _disk_read_bytes1 - _disk_read_bytes
    _total_write = _disk_write_bytes1 - _disk_write_bytes

    _r_speed_mb = _total_read / (1024**2)
    _w_speed_mb = _total_write / (1024**2)

    return _r_speed_mb, _w_speed_mb

