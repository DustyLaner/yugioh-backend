Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Users\laein\yugioh_backend\start_backend_silent.bat" & Chr(34), 0
Set WshShell = Nothing

WScript.Sleep 3000
Set oShell = CreateObject("WScript.Shell")
oShell.Run "http://localhost:3000"
