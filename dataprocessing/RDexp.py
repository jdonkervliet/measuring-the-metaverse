import LogCatParsing
import SysInfoParsing
import statParser as sp
import utils as ut

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def getSubdirName():
    return "RD"

def processExperiment(rt):
    datapPaths, datapNames = ut.getSubdirs(rt)
    statSets = []
    statisticSets = []
    ftSet = []

    for datapIdx in range(0, len(datapPaths)):
    
        datapName = datapNames[datapIdx]
        datapPath = datapPaths[datapIdx]
        statSets.append(sp.getCpuData(f"{datapPath}/stat_{datapName}.log"))
                                                    
        statisticSets.append(LogCatParsing.StatsFile(datapPath + f"/logcat_VrApi_{datapName}.log"))
        print(statisticSets[-1].dataFrame.columns)
        # ftSet.append({f"": list(map(lambda x : (x * 1e-9)/1e-3, statisticSets[-1].dataFrame['Main Thread'][300:]))})
        ftSet.append({f"": list(map(lambda x: (x * 1e-9)/1e-3, statisticSets[-1].dataFrame['Main Thread']))})
        
    print(datapNames)
    print(len(ftSet))
    print(type(statSets[-1]))

    fig, axes = plt.subplots(nrows=len(statSets), ncols = 1)

    for i in range(0, len(statSets)):
        statSets[i].plot(ax=axes[i])
        plt.xlabel("time in seconds")
        plt.ylabel("cpu usage (%)")
        axes[i].set_title(f"cpu usage of platform {datapNames[i]}")
        plt.subplots_adjust(hspace=0.6, wspace=0.6)

    plt.show()

    ut.boxPlotPerDatapValue(ftSet,list(map(lambda x: str(x), [6,12,18,24,30,36,42])),99)
    
    plt.show()

try:
    registered.append(processExperiment)
except:
    pass
if(__name__ == "__main__"):
    processExperiment("C:\\Users\\joach\\Desktop\\measuring-the-metaverse\\measurements\\RD")