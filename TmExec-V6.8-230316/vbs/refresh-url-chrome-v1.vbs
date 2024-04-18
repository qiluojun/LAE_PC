''
'' Refresh URL by Chrome Script V1.0
'' Author: boomworks
'' E-mail: boomworks#hotmail.com
'' WeChat ID: boomwxsoft
'' Date: 2022-10-19
''
''

'''''''''''''''''''''
'' Setting
'''''''''''''''''''''

Dim strTitle_1,strTitle_2,strTitle_3

strTitle_1 = Chr(34) & "LLС" & Chr(34)
strTitle_2 = Chr(34) & "_??" & Chr(34) 
strTitle_3 = Chr(34) & "_?" & Chr(34) 


''''''''''''''''''''''''''''''''''''''''''''
'' *** DO NOT CHANGE THE FOLLOWING CODE ***
''''''''''''''''''''''''''''''''''''''''''''

'' Get NCmd Path
Dim strCurrPath,strParentPath,strNCmdPath
strCurrPath = CreateObject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
strParentPath = Mid(strCurrPath, 1, InStrRev(strCurrPath, "\"))
strNCmdPath = strParentPath & "nircmd\\nircmd.exe "

Dim oShell
Set oShell = CreateObject("wscript.shell") 


''''''''''''''''''''
'' Biz logic go here
''''''''''''''''''''

'' delay for auto-click-1-0.vbs run
'WScript.Sleep 1000*1

'oShell.Run "chrome.exe " & strUrl
'WScript.Sleep 1000*5


'' Activate and Max Window
oShell.Run strNCmdPath & "win activate ititle " & strTitle_1
WScript.Sleep 500
'oShell.Run strNCmdPath & "win max ititle " & strTitle
'WScript.Sleep 200*1

'' send home key, for get correct next link pos
oShell.SendKeys "{F5}"
WScript.Sleep 1000*4
oShell.SendKeys "{F5}"
WScript.Sleep 1000*1
'oShell.Run strNCmdPath & "win activate ititle " & strTitle
'WScript.Sleep 200*1

'' close win
'oShell.Run strNCmdPath & "win close ititle " & strTitle
'WScript.Sleep 500*1


oShell.Run strNCmdPath & "win activate ititle " & strTitle_2
WScript.Sleep 500
oShell.SendKeys "{F5}"
WScript.Sleep 1000*4
oShell.SendKeys "{F5}"
WScript.Sleep 1000*1

oShell.Run strNCmdPath & "win activate ititle " & strTitle_3
WScript.Sleep 500
oShell.SendKeys "{F5}"
WScript.Sleep 1000*4
oShell.SendKeys "{F5}"
WScript.Sleep 1000*1

Set oShell = Nothing
Wscript.Quit 0