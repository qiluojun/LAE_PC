Dim Name,Msg
Name="boomworks"
Msg ="test"
set ws=wscript.createobject("wscript.shell")
ws.Run "cmd.exe /c echo " & Name & " | clip.exe",0,True
ws.Run "mshta javascript:window.execScript('window.close','vbs')",0,True
ws.sendKeys "^%w"
wscript.sleep 500
ws.sendKeys "^f"
wscript.sleep 500
ws.sendKeys "^v"
wscript.sleep 500
ws.sendKeys "{ENTER}"
wscript.sleep 500
ws.Run "cmd.exe /c echo " & Msg & " | clip.exe",0,True
wscript.sleep 500
ws.sendKeys "^v"
wscript.sleep 500
ws.sendKeys "{ENTER}"