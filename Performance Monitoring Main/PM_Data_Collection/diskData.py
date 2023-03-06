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
        _total_memory = _total_memory + _hard_disks[_key]['TotalMem']
        _hard_disks[_key]['UsedMem'] = psutil.disk_usage(_key).used
        _hard_disks[_key]['FreeMem'] = psutil.disk_usage(_key).free
        _hard_disks[_key]['UsedPer'] = psutil.disk_usage(_key).percent

    total_memory = math.ceil(_total_memory/1024**3)
    _hard_disks['TotalMem'] = total_memory

    return _hard_disks


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
    if int(_r_speed_mb) > 0:
        print("Read speed: {} MB/s".format(_r_speed_mb))
    else:
        print("Read speed: {} KB/s".format(_total_read / 1024))

    _w_speed_mb = _total_write / (1024**2)
    if int(_w_speed_mb) > 0:
        print("Write speed: {} MB/s".format(_w_speed_mb))
    else:
        print("Write speed: {} KB/s".format(_total_write / 1024))




# while(True):
#     disk_io_counter = psutil.disk_io_counters()
#     disk_read_count = disk_io_counter[0]  # read_count
#     disk_write_count = disk_io_counter[1] #  write_count
#     disk_read_bytes = disk_io_counter[2]  # read_bytes
#     disk_write_bytes = disk_io_counter[3] #  write_byte
#     disk_read_time = disk_io_counter[4]  # read_time
#     disk_write_time = disk_io_counter[5] #  write_time
#     time.sleep(1)
#     disk_io_counter = psutil.disk_io_counters()
#     disk_read_count1 = disk_io_counter[0]  # read_count
#     disk_write_count1 = disk_io_counter[1] #  write_count
#     disk_read_bytes1 = disk_io_counter[2]   # read_bytes
#     disk_write_bytes1 = disk_io_counter[3] #  write_byte
#     disk_read_time1 = disk_io_counter[4]  # read_time
#     disk_write_time1 = disk_io_counter[5] #  write_time
#
#
#     total_read = disk_read_bytes1 -disk_read_bytes
#     total_write = disk_write_bytes1 - disk_write_bytes
#     total_read_time = disk_read_time1 -disk_read_time
#     total_write_time = disk_write_time1 - disk_write_time
#
#
#     print("Read : ", total_read)
#     print("Write : ", total_write)
#
#     print("Read_Count : ", disk_read_count1 - disk_read_count)
#     print("Write_Count : ", disk_write_count1 - disk_write_count)
#
#
#     print("Time_Read : ",total_read_time )
#     print("Time_Write : ",total_write_time )
