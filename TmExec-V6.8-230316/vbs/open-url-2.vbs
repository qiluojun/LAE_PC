''
'' Open URL Script
''
'' Author: boomworks
'' Email: boomworks#hotmail.com
'' Date:
''		221022
''

Option Explicit

Dim arrURL(0)	'' n: n+1

arrURL(0) = "https://mail.qq.com/"
'arrURL(1) = "https://mail.qq.com/"
'arrURL(2) = "https://taobao.com"
'arrURL(3) = "https://www.baidu.com"
'arrURL(4) = "https://mail.qq.com/"
'arrURL(5) = "https://taobao.com"
'arrURL(6) = "https://www.baidu.com"
'arrURL(7) = "https://mail.qq.com/"
'arrURL(8) = "https://taobao.com"
'arrURL(9) = "https://www.baidu.com"

Dim strTitle
strTitle = Chr(34) & "QQ" & Chr(34)

'' Google Chrome - chrome.exe, Edge - msedge.exe
Dim strBrowser
'strBrowser = "D:\Program Files (x86)\360Chrome\Chrome\Application\360chrome.exe "
'strBrowser = "chrome.exe "
strBrowser = "msedge.exe "
'strBrowser = "" ' Default browser

WScript.sleep 500

''
''
''
Dim strCurrPath,strParentPath,strNCmdPath
strCurrPath = CreateObject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
strParentPath = Mid(strCurrPath, 1, InStrRev(strCurrPath, "\"))
'Wscript.echo strParentPath
strNCmdPath = strParentPath & "nircmd\\nircmd.exe "
'Wscript.echo strNCmdPath


'' 
Dim oShell
Set oShell = CreateObject("WScript.shell") 


''
'' Open URL
''
Dim i,strURL
For i = 0 To UBound(arrURL)
	strURL = arrURL(i)
	'MsgBox strURL
	oShell.Run strBrowser & strURL
	
	WScript.sleep 1000
Next

WScript.sleep 3000

'MsgBox strNCmdPath & "win setsize ititle " & strTitle & "20 20 40 40"
'oShell.Run strNCmdPath & "win setsize ititle " & strTitle & "20 20 40 40"
'oShell.Run strNCmdPath & "win trans ititle " & strTitle '& " 192"
'WScript.Sleep 500

oShell.Run strNCmdPath & "win min ititle " & strTitle
WScript.Sleep 500

oShell.Run strNCmdPath & "win hide ititle " & strTitle
WScript.Sleep 500

oShell.Run strNCmdPath & "win show ititle " & strTitle
WScript.Sleep 1000

oShell.Run strNCmdPath & "win close ititle " & strTitle
WScript.Sleep 500

Set oShell = Nothing
WScript.Quit 0