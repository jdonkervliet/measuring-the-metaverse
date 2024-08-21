
# https://xkln.net/blog/powershell-sleep-duration-accuracy-and-windows-timers/

param (
    [Parameter(Mandatory=$true)][string]$apkPath
)

$sshTarget = "joachim@192.168.23.94"

cd "C:\Users\joach\Desktop\measuring-the-metaverse"

ssh -t $sshTarget "cat /proc/version" >> version.log
ssh -t $sshTarget "cat /proc/cpuinfo" >> cpuinfo.log

#$VrJob = Start-Process adb -PassThru -ArgumentList logcat >> logcat_VrApi.log
#$HostJob = Start-Process python -PassThru -ArgumentList .\sample-host-metrics.py 

$Freq = [System.Diagnostics.Stopwatch]::Frequency

$Start = [System.Diagnostics.Stopwatch]::GetTimestamp()
echo "this is VRJob"

$i = 0

#ssh -t $sshTarget am start com.AtlargeResearch.Opencraft2/com.unity3d.player.UnityPlayerActivity

try {
    While ($true) {
        [System.DateTime]::Now.ToString("HH:mm:ss.fff")

#        if ($VrJob.State -ne "Running") {
#            Write-Host "Oh no! Restarting adb logcat"
#            $VrJob = Start-Process adb -PassThru -ArgumentList logcat >> logcat_VrApi.log
#        }
       # if ($HostJob.State -ne "Running") {
       #     Write-Host "Oh no! Restarting python script"
       #     $HostJob = Start-Process python -PassThru -ArgumentList .\sample-host-metrics.py 
       # }

        ssh -t $sshTarget "cat /proc/uptime" >> uptime.log
        ssh -t $sshTarget "cat /proc/net/dev" >> net_dev.log
        ssh -t $sshTarget "cat /proc/meminfo" >> meminfo.log
        ssh -t $sshTarget "cat /proc/stat" >> stat.log
        ssh -t $sshTarget "cat /proc/loadavg" >> loadavg.log

        #ssh -t $sshTarget "dumpsys battery" >> battery.log
        #ssh -t $sshTarget "dumpsys OVRRemoteService" >> OVRRemoteService.log
        #ssh -t $sshTarget "dumpsys CompanionService" >> CompanionService.log

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
}
