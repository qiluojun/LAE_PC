''
'' TimingExecutor Script V1.0
'' Author: boomworks
'' E-mail: boomworks#hotmail.com
'' WeChat ID: boomwxsoft
'' Date: 2022-9-30
''

Option Explicit

Dim strSpecTitle
strSpecTitle = Chr(34) & " Inpx " & Chr(34)

''''''''''''''''''''''''''''''''''''''''''''
'' *** DO NOT CHANGE THE FOLLOWING CODE ***
''''''''''''''''''''''''''''''''''''''''''''

'' Get NCmd Path
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


'''''''''''''''''''''
'' Biz logic go here
'''''''''''''''''''''

'' close
wsh.Run strNCmdPath & "win close ititle " & strSpecTitle
WScript.Sleep 200*1