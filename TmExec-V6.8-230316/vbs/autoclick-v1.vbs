Dim strPosRun
strPosRun = "150 150"

Dim strCurrPath,strParentPath,strNCmdPath
strCurrPath = CreateObject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
strParentPath = Mid(strCurrPath, 1, InStrRev(strCurrPath, "\"))
'Wscript.echo strParentPath
strNCmdPath = strParentPath & "nircmd\\nircmd.exe "
'Wscript.echo strNCmdPath

Dim wsh
Set wsh = CreateObject("wscript.shell") 
'ncmdpath = wsh.CurrentDirectory
'MsgBox ncmpath ' & "\\nircmd"
WScript.Sleep 100*2

'' click run btn
'wsh.Run strNCmdPath & "movecursor -9999 -9999"
wsh.Run strNCmdPath & "setcursor " & strPosRun
WScript.Sleep 100*1
wsh.Run strNCmdPath & "sendmouse left click"
WScript.Sleep 100*1
