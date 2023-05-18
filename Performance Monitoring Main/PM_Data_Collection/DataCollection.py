import psutil
import cpuData
import networkData
import diskData
import gpuData
import memoryData
import driveInfo
import time
import generalOsInfo



# retriving remaining system general data
_system_info = {}
static_data = {}
real_time_data = {}
def system_Information():
    global _system_info
    _system_info = generalOsInfo.get_system_info()
    _system_info['cpu_name'] = cpuData.cpu_info()['Name']
    _system_info['cpu_cores'] = cpuData.cpu_info()['Cores']
    _system_info['gpu_name'] = gpuData.get_gpu_info()['name']
    return _system_info if _system_info else None






# retriving static data ( one time )
def get_static_data_info():
    global static_data
    static_data['general_system_info'] = system_Information()
    static_data['cpu_info'] = cpuData.cpu_info()
    static_data['disk_data'] = diskData.all_disks_mem_data()
    static_data['gpu_data'] = gpuData.get_gpu_usage_data()
    static_data['memory_data'] = memoryData.ram_info()
    static_data['drive_data'] = driveInfo.get_disk_info()

    return static_data if static_data else None

# retriving real time data ( every 1 second)
def get_real_time_data():
    global real_time_data
    while True:
        real_time_data['cpu_usage'] = cpuData.cpu_frequency()
        real_time_data['net_data'] = networkData.net_stat()
        real_time_data['disk_rw_data_speed'] = diskData.disk_read_write_speed()
        real_time_data['gpu_data'] = gpuData.get_gpu_usage_data()
        real_time_data['ram_usage_data'] = memoryData.ram_usage_data()

        print(real_time_data['net_data'])
        #print(real_time_data['disk_rw_data_speed']) ---> already printed in diskData.py
        print(real_time_data['gpu_data'])
        print(real_time_data['ram_usage_data'])
        print(real_time_data['cpu_usage'])

        time.sleep(1)

# print(get_static_data_info())
#
# get_real_time_data()

print(system_Information())













# # Colelct my cpu usage data oance:
#
# tempo=1
# cpu_usage = 0.0
# hard_disks={}
#
# cpu_usage = psutil.cpu_percent(interval=1)
# ram=psutil.virtual_memory()
# ram_usage = ram.percent
# ram_total_mb = round(ram.total / 1024 ** 3 ,2)
# ram_used_mb = round(ram.used / 1024 ** 3 ,2)
# ram_free_mb = round(ram.free / 1024 ** 3 ,2)
#
# for partition in psutil.disk_partitions():
#     hard_disks.append(psutil.disk_usage(partition.device).percent)
#
#
# print("CPU usage: {}%".format(cpu_usage))
# print("RAM usage: {}%".format(ram_usage))
# print("RAM total: {} GB".format(ram_total_mb))
# print("RAM used: {} GB".format(ram_used_mb))
# print("RAM free: {} GB".format(ram_free_mb))
# for hard_disk in hard_disks:
#     print("Hard disk usage: {}%".format(hard_disk))


# NETWORK
# GPU

# On other languages maybe:
# - all running processes with names and pids
# - all running processes with names and pids and cpu usage and ram usage