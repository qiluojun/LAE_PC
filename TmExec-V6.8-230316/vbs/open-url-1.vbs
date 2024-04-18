''
'' Open URL Script
''
'' Author: boomworks
'' Email: boomworks#hotmail.com
'' Date:
''		221022
''

Option Explicit

Dim arrURL(2)	'' n: n+1

arrURL(0) = "https://www.baidu.com"
arrURL(1) = "https://mail.qq.com/"
arrURL(2) = "https://taobao.com"
'arrURL(3) = "https://www.baidu.com"
'arrURL(4) = "https://mail.qq.com/"
'arrURL(5) = "https://taobao.com"
'arrURL(6) = "https://www.baidu.com"
'arrURL(7) = "https://mail.qq.com/"
'arrURL(8) = "https://taobao.com"
'arrURL(9) = "https://www.baidu.com"


'' Google Chrome - chrome.exe, Edge - msedge.exe
Dim strBrowser
'strBrowser = "D:\Program Files (x86)\360Chrome\Chrome\Application\360chrome.exe "
'strBrowser = "chrome.exe "
'strBrowser = "msedge.exe "
strBrowser = "" ' Default browser

WScript.sleep 500

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

Set oShell = Nothing
WScript.Quit 0