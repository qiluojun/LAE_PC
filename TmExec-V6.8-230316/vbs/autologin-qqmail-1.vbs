Dim url,wsh
url = "https://mail.qq.com/"	'引号中填登录网页的地址

Set wsh = CreateObject("wscript.shell") 
wsh.Run"iexplore.exe" & " " & url		'可配置其他浏览器 msedge chrome iexplore
WScript.Sleep 1000*4

wsh.SendKeys "+"
WScript.Sleep 200*1

wsh.SendKeys "1234567890@qq.com"	'引号中填登录用的账号 
WScript.Sleep 400*1 

wsh.SendKeys "{TAB}"
WScript.Sleep 40*1

wsh.SendKeys "abcde12345"	'引号中填登录用的密码 
WScript.Sleep 40*1

wsh.SendKeys "{TAB}"	'1
WScript.Sleep 400*1
wsh.SendKeys "{TAB}"	'1
WScript.Sleep 400*1

'wsh.SendKeys "{ENTER}"

'1585 587
Dim currPath,nCmdPath
currPath = CreateObject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
'Wscript.echo currPath
nCmdPath = currPath & "\\nircmd\\nircmd.exe "

'WScript.Sleep 500*1
'wsh.Run nCmdPath & "movecursor -9999 -9999"
WScript.Sleep 500*1
wsh.Run nCmdPath & "setcursor 1585 587"
WScript.Sleep 500*1
wsh.Run nCmdPath & "sendmouse left click"

WScript.Sleep 1000*3
wsh.SendKeys "^w"

Set wsh = Nothing