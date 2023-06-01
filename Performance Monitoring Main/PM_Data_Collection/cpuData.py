import psutil
import wmi
import win32com.client
import time
import ctypes
_cpu_data = {}


def cpu_info():
    _info={}
    c = wmi.WMI()
    processor_info = c.Win32_Processor()[0]
    cpu_name = processor_info.Name
    cpu_cores = processor_info.NumberOfCores
    cpu_threads = processor_info.ThreadCount
    cpu_freq = processor_info.MaxClockSpeed

    _info['Name'] = cpu_name
    _info['Cores'] = cpu_cores
    _info['Threads'] = cpu_threads
    _info['BaseFrequency'] = str(round(cpu_freq / 1000,2)) + ' GHz'
    _cpu_data['CPUBaseInfo'] = _info
    return _info if _info else None


def cpu_temperature():
    # Need admin privileges
    w = wmi.WMI(namespace="root\\wmi")
    print((w.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0) - 273.15)

def cpu_frequency():
    _cpu_freq = {}
    def get_cpu_nominal_frequencies():
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(".", "root\cimv2")
        colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_Processor")

        cpu_nominal_frequencies = []
        for objItem in colItems:
            cpu_nominal_frequencies.append(objItem.MaxClockSpeed)
        return cpu_nominal_frequencies

    def get_cpu_percent_performance():
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        objSWbemServices = objWMIService.ConnectServer(".", "root\cimv2")
        colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_PerfFormattedData_Counters_ProcessorInformation")

        cpu_percent_performance = []
        for objItem in colItems:
            cpu_percent_performance.append(float(objItem.PercentProcessorPerformance))
        return cpu_percent_performance

    #while True:
    cpu_nominal_freqs = get_cpu_nominal_frequencies()
    cpu_percent_performance = get_cpu_percent_performance()

    for i, (nominal_freq, percent_perf) in enumerate(zip(cpu_nominal_freqs, cpu_percent_performance)):
        real_time_freq = nominal_freq * percent_perf / 100
        _cpu_freq['CPU-' + str(i)] = round(real_time_freq / 1000, 2)
    _cpu_data['CPUFrequency'] = _cpu_freq
    return _cpu_freq if _cpu_freq else None

def cpu_usage():
    _cpu_usage = {}
    cpu_usage = psutil.cpu_percent(interval=0.5)
    _cpu_usage['CPUUsage'] = cpu_usage
    _cpu_data['CPUUsage'] = _cpu_usage
    return _cpu_usage if _cpu_usage else None






