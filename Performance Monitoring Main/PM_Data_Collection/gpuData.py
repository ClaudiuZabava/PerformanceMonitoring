import gpustat



def get_gpu_info():
    gpu_stats = gpustat.GPUStatCollection.new_query()
    gpu_info = {}
    for gpu in gpu_stats:
        gpu_info['index'] = gpu.index
        gpu_info['name'] = gpu.name
        gpu_info['memory_total_MB'] = gpu.memory_total

    return gpu_info if gpu_info else None

def get_gpu_usage_data():
    gpu_stats = gpustat.GPUStatCollection.new_query()
    gpu_data = {}

    for gpu in gpu_stats:
        gpu_data['temperature'] = gpu.temperature
        gpu_data['utilization_percent'] = gpu.utilization
        gpu_data['memory_used_MB'] = gpu.memory_used

    return gpu_data if gpu_data else None



