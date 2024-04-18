''
'' Active Chrome Script V1.0
'' Author: boomworks
'' E-mail: boomworks#hotmail.com
'' WeChat ID: boomwxsoft
'' Date: 2022-9-28
''

Option Explicit

Dim strSpecTitle, strPosPlay, strPos10x, strPos20x, strPOsFullScreen
strSpecTitle = Chr(34) & " Google " & Chr(34)

''''''''''''''''''''''''''''''''''''''''''''
'' *** DO NOT CHANGE THE FOLLOWING CODE ***
''''''''''''''''''''''''''''''''''''''''''''

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

'' max win
wsh.Run strNCmdPath & "win activate ititle " & strSpecTitle
WScript.Sleep 200*1
wsh.Run strNCmdPath & "win max ititle " & strSpecTitle
WScript.Sleep 200*1

wsh.SendKeys "{F11}"
WScript.Sleep 200*1