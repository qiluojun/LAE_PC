''
'' Refresh Webpage Script
''
'' Author: boomworks
'' E-mail: boomworks#hotmail.com
'' WeChat ID: boomwxsoft
'' Date:    2022-06-29  V1.0
''          2022-10-16  V3.0
''

Option Explicit

Dim strUrl
strUrl = "https://www.baidu.com"

Const NS_SPAN = 200
WScript.Sleep NS_SPAN

'' create IE obj
On Error Resume Next

Dim oIE
Set oIE = CreateObject("InternetExplorer.Application")

On Error Goto 0

'' Sub wait loading
Sub WaitForLoad
  Do While oIE.Busy 'or oIE.ReadyState<>4
  WScript.Sleep NS_SPAN
  Loop
End Sub

'' get random num
Function getRandom(n)
  Dim MyValue, str
  Randomize
  str = Cint(trim(n))
  MyValue = Int(str * Rnd)
  getRandom = Cint(trim(MyValue))
End Function

''
'' main proc
''

On Error Resume Next

'' IE Settings
oIE.Left = 0
oIE.Top = 0
oIE.Toolbar = 0
oIE.StatusBar = 0

oIE.Height = 500
oIE.Width = 1200

oIE.Resizable = 0
oIE.Visible = True ' True   False

'' 1
oIE.Navigate strUrl
Call WaitForLoad
WScript.Sleep NS_SPAN
'' 2
'oIE.Navigate strUrl
'Call WaitForLoad
'WScript.Sleep NS_SPAN
''3
'oIE.Navigate strUrl
'Call WaitForLoad
'WScript.Sleep NS_SPAN

'' Quit
WScript.Sleep NS_SPAN*4
oIE.quit

Set oIE = Nothing


''
'' Kill IE Proc
''
Dim ret
ret = getRandom(5) + 1	'' 1~9
'MsgBox ret

If ret = 1 Then
	Dim oShell
	Set oShell = CreateObject("WScript.Shell")
	oShell.Run "taskkill.exe /F /IM iexplore.exe", 0, True
	''oShell.Run "taskkill.exe /F /FI ""IMAGENAME eq iexplore*"" /FI ""WINDOWTITLE eq https://blog.csdn.*""", 0, True
	Set oShell = Nothing
	
	WScript.Sleep NS_SPAN*4
END If

On Error Goto 0

WScript.Quit 0