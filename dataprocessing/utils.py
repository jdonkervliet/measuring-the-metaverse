import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def getSubdirs(experimentPath):
    # print("====================")
    ls = os.listdir(experimentPath)
    # print(f"ls gave {ls}")
    out = list(map(lambda x: f"{experimentPath}/{x}", ls))
    # print(f"appending gave {out}")
    return out, ls        
        
def mergeList(dfList, suffixes, key):
    fpsTotFrame = dfList[0]

    if(len(dfList) > 1):
        fpsTotFrame = pd.merge(fpsTotFrame, dfList[1], on=key, suffixes= suffixes[:2])

    if(len(dfList) > 2):
        for i in range(2, len(dfList)):
            print(f"{i} > {len(suffixes)}")
            suffixesStep = ["", suffixes[i]]        
            fpsTotFrame = pd.merge(fpsTotFrame, dfList[i], on=key, suffixes= suffixesStep)
    return fpsTotFrame
    
def mergeListAsym(dfList, suffixes):
    assert(len(dfList) == len(suffixes))
    for i in range(0,len(dfList)):
        newColNames = {}
        
        for j in range(0,len(dfList[i].columns)):
            newColNames[dfList[i].columns[j]] = dfList[i].columns[j] + suffixes[i]
        dfList[i].rename(columns=newColNames, inplace= True)
    return pd.concat(dfList, axis=1)

# concatenates the rows of dfElement to dfBig, with a newColValue for all rows
# of dfElem
def concatList(dflist, newColValues):
    assert(len(dflist) == len(newColValues))
    for i in range(0, len(newColValues)):
        dflist[i]['render distance'] = newColValues[i]
    return pd.concat(dflist, axis=0)

def minmaxY(ftFrame, percent):
    ydata = ftFrame.to_numpy().flatten()
    ydata = ydata[~np.isnan(ydata)]

    # Finding limits for y-axis Thanks to user FNia on stackoverflow for the 
    # logic of calculating the miny and maxy in plot to disregard outliers when 
    # plotting
    # link: https://stackoverflow.com/questions/11882393/matplotlib-disregard-outliers-when-plotting
    ypbot = np.percentile(ydata, 0)
    yptop = np.percentile(ydata, percent)
    ypad = 0.2*(yptop - ypbot)
    ymin = ypbot - ypad
    ymax = yptop + ypad
    return ymin, ymax


def boxPlotPerDatapValue(ftSet, datapNames, percent):
    frames = list(map(lambda x: pd.DataFrame(x), ftSet))
    ftFrame = mergeListAsym(frames, datapNames)
    ymin, ymax = minmaxY(ftFrame, percent)

    return ftFrame.boxplot(showfliers = False)
    
def plotPerDatapValue(ftSet, datapNames):
    frames = list(map(lambda x: pd.DataFrame(x), ftSet))
    ftFrame = mergeListAsym(frames, datapNames)
    
    print(ftFrame.head())
    return ftFrame.plot()