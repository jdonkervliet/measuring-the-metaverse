echo "Logging cats"
adb logcat | Select-String -Pattern "(Unity)|(VrApi)" >> logcat_VrApi.log