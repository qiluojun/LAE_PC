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

WScript.Sleep 200*5

'''''''''''''''''''''
'' Biz logic go here
'''''''''''''''''''''

'wsh.SendKeys "^{F5}"
wsh.SendKeys "%(^{F10})"
'wsh.SendKeys "^(%{F10})"
'wsh.SendKeys "+(^0)"

WScript.Sleep 200*1