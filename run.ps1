
# https://xkln.net/blog/powershell-sleep-duration-accuracy-and-windows-timers/

<<<<<<< Updated upstream
adb shell "cat /proc/version" >> version.log
adb shell "cat /proc/cpuinfo" >> cpuinfo.log

$VrJob = adb logcat -s VrApi >> logcat_VrApi.log &
$HostJob = python .\sample-host-metrics.py &
=======
param (
    [Parameter(Mandatory=$true)][string]$apkPath
)

cd "C:\Users\joach\Desktop\measuring-the-metaverse"

adb logcat -c

adb shell "cat /proc/version" >> version.log
adb shell "cat /proc/cpuinfo" >> cpuinfo.log

$VrJob = pwsh ./filteredLogCat.ps1 &
# $HostJob = Start-Process python -PassThru -ArgumentList ".\sample-host-metrics.py"
>>>>>>> Stashed changes

$Freq = [System.Diagnostics.Stopwatch]::Frequency

$Start = [System.Diagnostics.Stopwatch]::GetTimestamp()
<<<<<<< Updated upstream
=======
echo "this is VRJob"$VRJob

>>>>>>> Stashed changes
$i = 0

try {
    While ($True) {
        [System.DateTime]::Now.ToString("HH:mm:ss.fff")

<<<<<<< Updated upstream
        if ($VrJob.State -ne "Running") {
            Write-Host "Oh no! Restarting adb logcat"
            $VrJob = adb logcat -s VrApi >> logcat_VrApi.log &
        }
        if ($HostJob.State -ne "Running") {
            Write-Host "Oh no! Restarting python script"
            $HostJob = python .\sample-host-metrics.py &
        }
=======
        if ($VrJob.HasExited) {
            Write-Host "Oh no! Restarting adb logcat"
            
            $VrJob = Start-Process pwsh -PassThru -RedirectStandardOutput "logcat_VrApi.log" -ArgumentList "./filteredLogCat.ps1"
        }
       # if ($HostJob.State -ne "Running") {
       #     Write-Host "Oh no! Restarting python script"
       #     $HostJob = Start-Process python -PassThru -ArgumentList .\sample-host-metrics.py 
       # }
>>>>>>> Stashed changes

        adb shell "cat /proc/uptime" >> uptime.log
        adb shell "cat /proc/net/dev" >> net_dev.log
        adb shell "cat /proc/meminfo" >> meminfo.log
        adb shell "cat /proc/stat" >> stat.log
        adb shell "cat /proc/loadavg" >> loadavg.log

        adb shell "dumpsys battery" >> battery.log
        # adb shell "dumpsys OVRRemoteService" >> OVRRemoteService.log
        # adb shell "dumpsys CompanionService" >> CompanionService.log

        $End = [System.Diagnostics.Stopwatch]::GetTimestamp()
        Do {
        $i = $i + 1
        $Next = $Start + ($i * $Freq)
        $Sleep = $Next - $End
        } While($Sleep -lt 0)
        [System.Threading.Thread]::Sleep($Sleep * (1000.0 / $Freq))
    }
}
finally {
<<<<<<< Updated upstream
    Write-Host "Stopping VR monitor..."
    Stop-Job $VrJob
    Write-Host "Stopping host monitor..."
    Stop-Job $HostJob
=======
    Write-Host "killing "$VRJob.ToString()
    Stop-Job $VRJob.Id
    Wait-Job $VRJob.Id
    # Stop-Process $HostJob
>>>>>>> Stashed changes
}
