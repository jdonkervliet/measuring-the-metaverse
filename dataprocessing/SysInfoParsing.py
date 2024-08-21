from typing import List

def subtract_dicts(dict1, dict2):
    return {key: dict1[key] - dict2.get(key, 0) for key in dict2.keys()}

def toIntList(stringList):
    print(stringList)
    return list(map(int, filter(lambda x : x != "" ,stringList.split(" "))))

class loadavgEntry():
    def __init__(self, loadAvg1Min, loadAvg5Min, loadAvg15Min,
                  nProcesses, totProcesses) -> None:
        self.loadAvg1Min = 0
        self.loadAvg5Min = 0
        self.loadAvg15Min = 0
        self.nProcesses = 0
        self.totProcesses = 0
    
'''Code generated with chatgpt3.5, prompt: 
make a class called meminfoEntry that parses this file into members
MemTotal:        7916544 kB
MemFree:         1918384 kB (...)
link: https://chat.openai.com/share/8a45f6e0-1e15-4df6-8a2c-980dc112e042
'''
class MeminfoEntry:
    def __init__(self, meminfostring):
        self.meminfo = {}
        for line in meminfostring.split('\n'):
            if(line != ""):
                key, value = line.strip().split(':')
                self.meminfo[key.strip()] = int(value.strip().split()[0])

    def get_mem_total(self):
        return self.meminfo.get('MemTotal', 0)

    def get_mem_free(self):
        return self.meminfo.get('MemFree', 0)

    def get_mem_available(self):
        return self.meminfo.get('MemAvailable', 0)

    def get_buffers(self):
        return self.meminfo.get('Buffers', 0)

    def get_cached(self):
        return self.meminfo.get('Cached', 0)

    def get_swap_total(self):
        return self.meminfo.get('SwapTotal', 0)

    def get_swap_free(self):
        return self.meminfo.get('SwapFree', 0)
'''End of generated code'''

def parseMeminfo(fileName):
    file = open(fileName, 'r')
    meminfoListRaw = file.read()
    memInfoListSplit = splitNoRemove(meminfoListRaw, "MemTotal")
    return list(map(MeminfoEntry, memInfoListSplit))

'''Code generated with chatgpt 3.5, prompt:
write me  a python class called netDevEntry that parses this file into members Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
    lo: 675797585   65432    0    0    (...)
link: https://chat.openai.com/share/8a45f6e0-1e15-4df6-8a2c-980dc112e042
'''
class NetDevEntry:
    def __init__(self, entry_str):
        self.interface = ""
        self.receive_bytes = 0
        self.receive_packets = 0
        self.receive_errors = 0
        self.receive_dropped = 0
        self.receive_fifo = 0
        self.receive_frame = 0
        self.receive_compressed = 0
        self.receive_multicast = 0
        self.transmit_bytes = 0
        self.transmit_packets = 0
        self.transmit_errors = 0
        self.transmit_dropped = 0
        self.transmit_fifo = 0
        self.transmit_colls = 0
        self.transmit_carrier = 0
        self.transmit_compressed = 0
        
        parts = entry_str.split()
        if len(parts) >= 17:
            self.interface = parts[0].strip(':')
            self.receive_bytes = int(parts[1])
            self.receive_packets = int(parts[2])
            self.receive_errors = int(parts[3])
            self.receive_dropped = int(parts[4])
            self.receive_fifo = int(parts[5])
            self.receive_frame = int(parts[6])
            self.receive_compressed = int(parts[7])
            self.receive_multicast = int(parts[8])
            self.transmit_bytes = int(parts[9])
            self.transmit_packets = int(parts[10])
            self.transmit_errors = int(parts[11])
            self.transmit_dropped = int(parts[12])
            self.transmit_fifo = int(parts[13])
            self.transmit_colls = int(parts[14])
            self.transmit_carrier = int(parts[15])
            self.transmit_compressed = int(parts[16])

    def get_interface_data(self, interface):
        return self.interfaces.get(interface, {})
'''end of generated code'''

'''code generated by chatgpt 3.5, prompt: 
please write me a class called statEntry which parses a string in the 
following format cpu  485318 6028 198342 7177714 30508 0 435 (...)
link: https://chat.openai.com/share/8a45f6e0-1e15-4df6-8a2c-980dc112e042
'''
class StatEntry:
    def __init__(self, data_string):
        lines = data_string.strip().split('\n')
        self.stats = {}
        for line in lines:
            parts = line.split()
            key = parts[0]
            values = [int(value) for value in parts[1:]]
            self.stats[key] = values

    def get_cpu_data(self, cpu):
        return self.stats.get(cpu, [])

    def get_context_switches(self):
        return self.stats.get('ctxt', [0])[0]

    def get_boot_time(self):
        return self.stats.get('btime', [0])[0]

    def get_process_count(self):
        return self.stats.get('processes', [0])[0]

    def get_running_processes(self):
        return self.stats.get('procs_running', [0])[0]

    def get_blocked_processes(self):
        return self.stats.get('procs_blocked', [0])[0]

    def get_softirq(self):
        return self.stats.get('softirq', [])
'''end of generated code'''

'''works like split() but does not destroy the terminator
Thank you user P.Melch and Wes Modes on stackoverflow
https://stackoverflow.com/questions/7866128/python-split-without-removing-the-delimiter
'''
def splitNoRemove(string, separator):
    return [separator + e for e in string.split(separator) if e] 


class SysInfo():
    def __init__(self, meminfoLogPath, netdevLogPath, statLogPath) -> None:
        memInfoLogFile = open(meminfoLogPath)
        netdevLogFile = open(netdevLogPath)
        statLogFile = open(statLogPath)

        memInfoStr = memInfoLogFile.read()
        netdevStr = netdevLogFile.read()
        statLogStr = statLogFile.read()

        self.meminfoEntries = self.parseMemInfoEntries(memInfoStr)
        self.netdevEntries = self.parseNetDevEntries(netdevStr)
        self.statEntries = self.parseStatEntries(statLogStr)

        memInfoLogFile.close()
        netdevLogFile.close()
        statLogFile.close()

    def parseMemInfoEntries(self, entriesStr):
        entries = splitNoRemove(entriesStr, "MemTotal")
        parsedEntries =  list(map(MeminfoEntry, entries))
        return parsedEntries


    def parseNetDevEntries(self, entriesStr):
        entrieLines = entriesStr.split('\n')
        devEntries = list(filter(lambda line : line.startswith(' wlan0'), entrieLines))
        entries = list(map(NetDevEntry, devEntries))
        return entries

    def parseStatEntries(self, entriesStr):
        entries = splitNoRemove(entriesStr, "cpu ") #note the space
        statEntries = list(map(StatEntry, entries))
        #print(statEntries[0].get_context_switches())
        return statEntries
    
    def getCpuPoint(self, idx):
        pointMeasurement = []
        for i in range(0, 6):
            pointMeasurement.append(self.statEntries[idx].get_cpu_data(f"cpu{i}"))
        return pointMeasurement

    def getAverageCpu(self):
        # 2-dim list of cpu data
        first = self.getCpuPoint(0)
        last = self.getCpuPoint(len(self.statEntries) - 1)

        diffMeasurement = []
        for i in range(0, len(first)):
            diffCpu = []
            for j in range(0, len(first[i])):
                diffCpu.append(last[i][j] - first[i][j])
            diffMeasurement.append(diffCpu)
        
        return diffMeasurement
    
        


def main():
    print("=================================================================")

    # Example usage:
    data_string = "cpu 485318 6028 198342 7177714 30508 0 43547 0 0 0\nctxt 94468056\nbtime 1715330203\nprocesses 87125\nprocs_running 1\nprocs_blocked 0\nsoftirq 14618634 91376 1169398 143 227589 25530 0 584650 7245163 1541 5273244"
    stat_entry = StatEntry(data_string)

    print("CPU data for cpu0:", stat_entry.get_cpu_data("cpu0"))
    print("Context switches:", stat_entry.get_context_switches())
    print("Boot time:", stat_entry.get_boot_time())
    print("Process count:", stat_entry.get_process_count())
    print("Running processes:", stat_entry.get_running_processes())
    print("Blocked processes:", stat_entry.get_blocked_processes())
    print("Softirq data:", stat_entry.get_softirq())

    # Example usage:
    entry_str = "wlan0: 72480783  147336    0    0    0     0          0         0 143127751  184785    0    0    0     0       0          0"
    net_dev_entry = NetDevEntry(entry_str)
    print("Interface:", net_dev_entry.interface)
    print("Receive Bytes:", net_dev_entry.receive_bytes)
    print("Transmit Bytes:", net_dev_entry.transmit_bytes)
    print("=================================================================")

    # Example usage:
    meminfoFile = open("/proc/meminfo")
    meminfoString = meminfoFile.read()
    meminfoFile.close()
    print("=================================================================")
    meminfo = MeminfoEntry(meminfoString)
    print("MemTotal:", meminfo.get_mem_total(), "kB")
    print("MemFree:", meminfo.get_mem_free(), "kB")
    print("MemAvailable:", meminfo.get_mem_available(), "kB")
    print("Buffers:", meminfo.get_buffers(), "kB")
    print("Cached:", meminfo.get_cached(), "kB")
    print("SwapTotal:", meminfo.get_swap_total(), "kB")
    print("SwapFree:", meminfo.get_swap_free(), "kB")

    print("=================================================================")
    SysInfo("./meminfo.log", "./net_dev.log", "./stat.log")

if(__name__ == "__main__"):
    main()