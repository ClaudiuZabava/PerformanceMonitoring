import psutil

# Colelct my cpu usage data oance:

tempo=1
cpu_usage = 0.0
hard_disks={}

cpu_usage = psutil.cpu_percent(interval=1)
ram=psutil.virtual_memory()
ram_usage = ram.percent
ram_total_mb = round(ram.total / 1024 ** 3 ,2)
ram_used_mb = round(ram.used / 1024 ** 3 ,2)
ram_free_mb = round(ram.free / 1024 ** 3 ,2)

for partition in psutil.disk_partitions():
    hard_disks.append(psutil.disk_usage(partition.device).percent)


print("CPU usage: {}%".format(cpu_usage))
print("RAM usage: {}%".format(ram_usage))
print("RAM total: {} GB".format(ram_total_mb))
print("RAM used: {} GB".format(ram_used_mb))
print("RAM free: {} GB".format(ram_free_mb))
for hard_disk in hard_disks:
    print("Hard disk usage: {}%".format(hard_disk))


# NETWORK
# GPU

# On other languages maybe:
# - all running processes with names and pids
# - all running processes with names and pids and cpu usage and ram usage