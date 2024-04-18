''
'' Auto Refresh Webpage Script V1.0
'' Author: boomworks
'' E-mail: boomworks#hotmail.com
'' WeChat ID: boomwxsoft
'' Date: 2022-6-29
''

Option Explicit

Dim oIE
Set oIE = CreateObject("InternetExplorer.Application")

On Error Resume Next

Sub WaitForLoad
 Do While oIE.Busy
 WScript.Sleep 200
 Loop
End Sub

oIE.Left = 0
oIE.Top = 400
oIE.Toolbar = 0
oIE.StatusBar = 0
oIE.Height = 1
oIE.Width = 1
oIE.Resizable = 0
oIE.Visible = False ' True	False

oIE.Navigate "https://blog.csdn.net/boomworks/article/details/113486307"
Call WaitForLoad

wScript.Sleep 500*2
oIE.quit