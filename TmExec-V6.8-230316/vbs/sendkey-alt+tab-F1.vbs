Set objShell = CreateObject("Wscript.Shell")
WScript.Sleep 200
objShell.SendKeys "%{TAB}"
WScript.Sleep 200
objShell.SendKeys "{F1}"
WScript.Sleep 400
objShell.SendKeys "%{TAB}"