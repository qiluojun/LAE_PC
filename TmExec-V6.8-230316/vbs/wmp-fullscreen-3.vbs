''
'' WMP Auto FullScreen Play Script V1.0
'' Author: boomworks
'' E-mail: boomworks#hotmail.com
'' WeChat ID: boomwxsoft  
'' Date: 2022-08-26  
''

'' *** DO NOT CHANGE THE FOLLOWWING CODE ***

'' Get NCmd Path
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

'' -- Biz logic go here ---
WScript.Sleep 3000*1
wsh.Run strNCmdPath & "setcursor 1000 500"
WScript.Sleep 500*1
wsh.Run strNCmdPath & "sendmouse left dblclick"	'' double click to fullscreen
'wsh.Run strNCmdPath & "sendmouse right click"
WScript.Sleep 500*1