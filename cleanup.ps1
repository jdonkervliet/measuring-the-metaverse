param (
    [Parameter(Mandatory=$true)][string]$apkPath
)

cd "C:\Users\joach\Desktop\measuring-the-metaverse"
#cd $MyInvocation.MyCommand.Path

adb shell am force-stop com.AtlargeResearch.Opencraft2

$apkName = Split-Path $apkPath -LeafBase

$apkBase = ".\measurements\" + $apkName

if(Test-Path $apkBase){
    rm -r $apkBase
}

mkdir $apkBase | Out-Null
echo $apkBase
echo "./logcat_VrApi.log  ->  $apkBase\logcat_VrApi_$apkName.log"
mv ./logcat_VrApi.log $apkBase\logcat_VrApi_$apkName.log
mv ./uptime.log $apkBase\uptime_$apkName.log
mv ./net_dev.log $apkBase\net_dev_$apkName.log
mv ./meminfo.log $apkBase\meminfo_$apkName.log
mv ./stat.log $apkBase\stat_$apkName.log
mv ./loadavg.log $apkBase\loadavg_$apkName.log
mv ./battery.log $apkBase\battery_$apkName.log
mv ./OVRRemoteService.log $apkBase\OVRRemoteService_$apkName.log
mv ./CompanionService.log $apkBase\CompanionService_$apkName.log



