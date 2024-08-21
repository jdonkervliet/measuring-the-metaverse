import os
import pandas as pd

'''
Thanks to http://stackoverflow.com/questions/23367857/accurate-calculation-of-cpu-usage-given-in-percentage-in-linux
This code has been almost copy pasted from this user
'''


def getSplitRawStat(statFilePath):
    statListFile = open(statFilePath, 'r')
    statListRaw = statListFile.read()
    delim = 'cpu  '
    statListRawSplit =  statListRaw.split(delim)
    
    statListRawSplit.remove("")
    statListRawSplit = list(map(lambda x: delim + x , statListRawSplit))
    return statListRawSplit

def parseSample(statRaw):
    cpu_infos = {} #collect here the information
    lines = [line.split(' ') for line in statRaw.split('\n') if line.startswith('cpu')]
    #compute for every cpu
    for cpu_line in lines:
        if '' in cpu_line: cpu_line.remove('')#remove empty elements
        cpu_line = [cpu_line[0]]+[float(i) for i in cpu_line[1:]]#type casting
        cpu_id, user, nice, system, idle, iowait, irq, softrig, steal, guest, guest_nice = cpu_line

        Idle = idle + iowait
        NonIdle = user + nice + system + irq + softrig + steal

        Total=Idle+NonIdle
        #update dictionionary
        cpu_infos.update({cpu_id:{'total':Total,'idle':Idle}})
    return cpu_infos

def getLoad(sample1, sample2):
    cpu_load = {}

    for cpu in sample1:
        Total = sample2[cpu]['total']
        PrevTotal = sample1[cpu]['total']

        Idle = sample2[cpu]['idle']
        PrevIdle = sample1[cpu]['idle']
        CPU_Percentage= ((Total - PrevTotal) - (Idle - PrevIdle) ) / (Total - PrevTotal) * 100
        cpu_load.update({cpu: CPU_Percentage})
    return cpu_load

def getCpuData(statFilePath):
    statListRawSplit = getSplitRawStat(statFilePath)
    samples = list(map(parseSample, statListRawSplit))
    # print(getLoad(sample1=samples[0], sample2=samples[1]))
    
    loadSamples = []

    for i in range(1, len(samples)):
        loadSamples.append(getLoad(samples[i - 1], samples[i]))
    
    colnames = list(loadSamples[0].keys())
    sampleTable = {}

    for j in range(0, len(colnames)):
        col = []
        for i in range(0, len(loadSamples)):
            col.append(loadSamples[i][colnames[j]])
        sampleTable[colnames[j]] = col
    return (pd.DataFrame(sampleTable))
    # for statRaw in statListRawSplit:
    

if(__name__ == "__main__"):
    getCpuData("C:/Users/joach/Desktop/measuring-the-metaverse/measurements/RD\HMD-S-T-rd-06/stat_HMD-S-T-rd-06.log")
