''
'' Mouse Auto lClick Script V1.0
'' Author: boomworks
'' E-mail: boomworks#hotmail.com
'' WeChat ID: boomwxsoft
'' Date: 2022-10-12
''

Dim strPosRun
strPosRun = "50 50"

Dim strCurrPath,strParentPath,strNCmdPath
strCurrPath = CreateObject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
strParentPath = Mid(strCurrPath, 1, InStrRev(strCurrPath, "\"))
'Wscript.echo strParentPath
strNCmdPath = strParentPath & "nircmd\\nircmd.exe "
'Wscript.echo strNCmdPath


Dim wsh
Set wsh = CreateObject("wscript.shell") 
'strNCmdPath = wsh.CurrentDirectory
'MsgBox ncmpath ' & "\\nircmd"

'' wait
WScript.Sleep 200*1

'' LClick
'wsh.Run strNCmdPath & "movecursor -9999 -9999"
wsh.Run strNCmdPath & "setcursor " & strPosRun
WScript.Sleep 100*1
wsh.Run strNCmdPath & "sendmouse left click"
'wsh.Run strNCmdPath & "sendmouse right click"
WScript.Sleep 100*1