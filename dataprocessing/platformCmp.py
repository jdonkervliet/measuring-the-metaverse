import LogCatParsing
import SysInfoParsing
import statParser as sp
import utils as ut

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def getSubdirName():
    return "platfCmp"

def processExperiment(rt):

    datapPaths, datapNames = ut.getSubdirs(rt)
    statSets = []
    statisticSets = []
    ftSet = []

    for datapIdx in range(0, len(datapPaths)):
        datapName = datapNames[datapIdx]
        datapPath = datapPaths[datapIdx]
        print(datapName)
        statSets.append(sp.getCpuData(f"{datapPath}/stat_{datapName}.log"))
                                                    
        statisticSets.append(LogCatParsing.StatsFile(datapPath + f"/logcat_VrApi_{datapName}.log"))
        print(list(set(map(type, statisticSets[-1].dataFrame['Main Thread']))))
        # ftSet.append({f"": list(map(lambda x : (x * 1e-9)/1e-3, statisticSets[-1].dataFrame['Main Thread'][300:]))})
        ftSet.append({f"{datapName}": list(map(lambda x: (x * 1e-9)/1e-3, statisticSets[-1].dataFrame['Main Thread']))})
        
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

    ut.boxPlotPerDatapValue(ftSet,["","","",""], 99)
    plt.show()
    

try:
    registered.append(processExperiment)
except:
    pass
if(__name__ == "__main__"):
    processExperiment("C:\\Users\\joach\\Desktop\\measuring-the-metaverse\\measurements\\platfCmp")