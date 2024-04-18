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

Dim url
url = "https://mail.qq.com/"	'引号中填登录网页的地址

wsh.Run"chrome.exe" + " " + url	'可配置其他浏览器 msedge chrome iexplore
WScript.Sleep 1000*4

wsh.SendKeys "+"
WScript.Sleep 500*1

wsh.SendKeys "boomworks@qq.com"	'引号中填登录用的账号 
WScript.Sleep 500*1 

wsh.SendKeys "{TAB}"
WScript.Sleep 500*1

wsh.SendKeys "boomworks123"	'引号中填登录用的密码 
WScript.Sleep 500*1

'Mouse operation
wsh.Run strNCmdPath & "movecursor -9999 -9999"
WScript.Sleep 500*1
wsh.Run strNCmdPath & "movecursor 1110 410"
WScript.Sleep 500*1
wsh.Run strNCmdPath & "sendmouse left click"
WScript.Sleep 500*1

'wsh.SendKeys "{TAB}"	'1
'WScript.Sleep 500*1
'wsh.SendKeys "{ENTER}"
'WScript.Sleep 500*1

'WScript.Sleep 1000*3
'wsh.SendKeys "^w"

Set wsh = Nothing