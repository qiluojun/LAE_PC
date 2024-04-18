''
'' TimingExecutor Script V1.0
'' Author: boomworks
'' E-mail: boomworks#hotmail.com
'' WeChat ID: boomwxsoft
'' Date: 2022-9-30
''

Option Explicit

Dim wsh
Set wsh = CreateObject("wscript.shell") 
'ncmdpath = wsh.CurrentDirectory
'MsgBox ncmpath ' & "\\nircmd"

WScript.Sleep 200*1

'''''''''''''''''''''
'' Biz logic go here
'''''''''''''''''''''

wsh.SendKeys "^b"
WScript.Sleep 200*1