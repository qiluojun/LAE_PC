Dim url,wsh
url = "https://mail.qq.com/"	'引号中填登录网页的地址

Set wsh = CreateObject("wscript.shell") 
wsh.Run "chrome.exe" + " " + url	'可配置其他浏览器 msedge chrome iexplore
WScript.Sleep 1000*4


wsh.SendKeys "201715201@qq.com"	'引号中填登录用的账号 
WScript.Sleep 1000*1 

wsh.SendKeys "{TAB}"
WScript.Sleep 1000*1

wsh.SendKeys "Pass1234"	'引号中填登录用的密码 
WScript.Sleep 1000*1

wsh.SendKeys "{TAB}"	'1	tab
WScript.Sleep 1000*1 
wsh.SendKeys "{TAB}"	'2
WScript.Sleep 1000*1 
wsh.SendKeys "{TAB}"	'3
WScript.Sleep 1000*1 
wsh.SendKeys "{TAB}"	'4
WScript.Sleep 1000*1 

'wsh.SendKeys "{ENTER}"

'WScript.Sleep 1000*3
'wsh.SendKeys "^w"

Set wsh = Nothing