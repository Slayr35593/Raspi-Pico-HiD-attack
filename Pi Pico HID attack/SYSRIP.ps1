start-process devmgmt.msc
ping 1.1.1.1
Write-Host "The device is in sterile mode, no payload has been executed." -BackgroundColor Red
Read-Host -Prompt "Press Enter to exit"