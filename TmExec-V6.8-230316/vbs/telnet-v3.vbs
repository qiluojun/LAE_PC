Dim wsh
Set wsh = CreateObject("wscript.shell")

wsh.Run "cmd.exe /K ver"
WScript.Sleep 500*4

wsh.SendKeys "+"
WScript.Sleep 500*2

wsh.SendKeys "telnet 192.168.100.102"
WScript.Sleep 500*4

wsh.SendKeys "{ENTER}"
WScript.Sleep 500*4

wsh.SendKeys "admin"
WScript.Sleep 500*4

wsh.SendKeys "{ENTER}"
WScript.Sleep 500*4

wsh.SendKeys "password"
WScript.Sleep 500*4

wsh.SendKeys "{ENTER}"
WScript.Sleep 500*4

Set wsh = Nothing
Wscript.Quit 0
