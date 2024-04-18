Dim oShell
Set oShell = WScript.CreateObject("WScript.Shell")

WScript.Sleep(1000)

oShell.Run "taskkill /f /im fuwu.exe", 0

Set oShell = Nothing
WScript.quit