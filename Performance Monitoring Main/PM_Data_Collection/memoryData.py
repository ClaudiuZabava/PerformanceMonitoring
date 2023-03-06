import psutil


_ram_data = {}


def ram_info():
    # RAM TYPE
    # RAM base speed
    # SLOTS
    pass


def ram_usage_data():
    _ram = psutil.virtual_memory()
    _ram_usage = _ram.percent
    _ram_data['RAMUsagePr'] = _ram_usage
    _ram_total_gb = round(_ram.total / 1024 ** 3, 2)
    _ram_data['RAMTotalGB'] = _ram_total_gb
    _ram_used_gb = round(_ram.used / 1024 ** 3, 2)
    _ram_data['RAMUsedGB'] = _ram_used_gb
    _ram_free_gb = round(_ram.free / 1024 ** 3, 2)
    _ram_data['RAMFreeGB'] = _ram_free_gb

    # ram cached

    # ram page pool


    return _ram_data
