import psutil
import time

net_data = {}

def get_network_usage():
    net_usage_data={}
    net_io_counters = psutil.net_io_counters()
    net_usage_data['bytes_sent'] = net_io_counters.bytes_sent
    net_usage_data['bytes_received'] = net_io_counters.bytes_recv
    net_usage_data['packets_sent'] = net_io_counters.packets_sent
    net_usage_data['packets_received'] = net_io_counters.packets_recv
    return net_usage_data


def net_stat(interval=1):

    usage_start = get_network_usage()
    time.sleep(interval)
    usage_end = get_network_usage()

    bytes_sent_per_second = (usage_end['bytes_sent'] - usage_start['bytes_sent']) / interval
    bytes_received_per_second = (usage_end['bytes_received'] - usage_start['bytes_received']) / interval
    packets_sent_per_second = (usage_end['packets_sent'] - usage_start['packets_sent']) / interval
    packets_received_per_second = (usage_end['packets_received'] - usage_start['packets_received']) / interval

    net_data['bytes_sent_per_second'] = bytes_sent_per_second
    net_data['bytes_received_per_second'] = bytes_received_per_second
    net_data['packets_sent_per_second'] = packets_sent_per_second
    net_data['packets_received_per_second'] = packets_received_per_second

    return net_data

