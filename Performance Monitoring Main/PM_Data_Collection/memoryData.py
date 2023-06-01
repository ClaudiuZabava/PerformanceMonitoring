import psutil
import wmi


_ram_usage_data = {}
_ram_base_data = {}


def ram_info():
    w = wmi.WMI()

    # Informatii despre RAM salvate intr-un array
    memory = w.Win32_PhysicalMemory()
    memory_array = w.Win32_PhysicalMemoryArray()[0]

    memory_type_map = {
        0: "Unknown",
        1: "Other",
        2: "DRAM",
        3: "Synchronous DRAM",
        4: "Cache DRAM",
        5: "EDO",
        6: "EDRAM",
        7: "VRAM",
        8: "SRAM",
        9: "RAM",
        10: "ROM",
        11: "Flash",
        12: "EEPROM",
        13: "FEPROM",
        14: "EPROM",
        15: "CDRAM",
        16: "3DRAM",
        17: "SDRAM",
        18: "SGRAM",
        19: "RDRAM",
        20: "DDR",
        21: "DDR2",
        22: "DDR2 FB-DIMM",
        24: "DDR3",
        25: "FBD2",
        26: "DDR4",
        27: "LPDDR",
        28: "LPDDR2",
        29: "LPDDR3",
        30: "LPDDR4",
        31: "Logical non-volatile device",
    }

    # Save Info
    if memory[0].MemoryType != 0:
        _ram_base_data['RAMType'] = memory_type_map[memory[0].MemoryType]
    else:
        _ram_base_data['RAMType'] = memory_type_map[memory[0].SMBIOSMemoryType]
    _ram_base_data['RAMCapacityMaxGB'] = round(memory_array.MaxCapacity / (1024 ** 2), 2)
    _ram_base_data['RAMBaseSpeed'] = memory[0].Speed
    _ram_base_data['RAMSlots'] = memory_array.MemoryDevices
    _ram_base_data['RAMTotalInstalledGB'] = round(psutil.virtual_memory().total / 1024 ** 3, 2)

    return _ram_base_data


def ram_usage_data():
    _ram = psutil.virtual_memory()
    _ram_usage = _ram.percent
    _ram_usage_data['RAMUsagePr'] = _ram_usage
    _ram_used_gb = round(_ram.used / 1024 ** 3, 2)
    _ram_usage_data['RAMUsedGB'] = _ram_used_gb
    _ram_free_gb = round(_ram.free / 1024 ** 3, 2)
    _ram_usage_data['RAMFreeGB'] = _ram_free_gb

    # ram cached

    # ram page pool


    return _ram_usage_data

# print(ram_info())
# print(ram_usage_data())
