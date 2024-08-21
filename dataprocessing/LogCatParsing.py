import os as Os
import pandas as pd
class StatsFile:
    def __init__(self, logcatFilePath):
        print(logcatFilePath)
        self.csvFilePath = Os.path.splitext(str(logcatFilePath))[1] + ".csv"
        if(Os.path.isfile(logcatFilePath)):
            self.csvMem = ""
            if(Os.path.isfile(self.csvFilePath)):
                Os.remove(self.csvFilePath)
            csv = open(self.csvFilePath, 'w+')
            heading = ("Frame Number;Main Thread;System Used Memory;GC "
                    "Reserved Memory;Total Reserved Memory;NFE Snapshot Tick;NFE"
                    " Snapshot Size (bits);NFE RTT;NFE Jitter;Multiplay FPS;"
                    "Multiplay BitRate In;Multiplay BitRate Out;Multiplay RTT(ms)"
                    ";Multiplay PacketLoss;Number of Terrain Areas (Server);Number"
                    " of Players (Client);Number of Players (Server);Number of "
                    "Terrain Areas (Client);dtime;\n")
           # csv.write(heading.replace(";",","))
            self.csvMem += heading
            
            with open(logcatFilePath, 'r') as statsFile:
                for line in statsFile:
                    key = "[STATISTIC]"
                    startIndex = line.find(key) + len(key)
                    csv.write(line[startIndex:].replace(";",","))
                    self.csvMem += line[startIndex:]
            csv.close()        
        self.dataFrame = pd.read_csv(self.csvFilePath)
    
    def getFramesPerSecond(self):
        # print(f"=========================================================={self.csvFilePath}")
        # print(self.dataFrame)
        # print(self.dataFrame.columns)
        # print(self.dataFrame["Frame Number"])
        return self.dataFrame["Frame Number"].iloc[-1] / 180
    



def main():
    fileTest = StatsFile("C:/Users/joach/Desktop/measuring-the-metaverse/measurements/PHO-S-T-rd-9/logcat_VrApi_PHO-S-T-rd-9.log")
    print(fileTest.getTotalFrameCount())
    return

if(__name__ == "__main__"):
    main()