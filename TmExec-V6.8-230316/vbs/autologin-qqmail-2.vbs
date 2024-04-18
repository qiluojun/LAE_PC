Dim wsh,ie 
Set wsh = CreateObject("wscript.shell") 
Set ie = WScript.CreateObject("InternetExplorer.Application") 
URL=" https://mail.qq.com/"
ie.visible = True
ie.navigate URL
WScript.Sleep 1000*5 

wsh.AppActivate "登录QQ邮箱 - Internet Explorer" ' 引号中填浏览器最上面的标题 
'               "登录QQ邮箱 - Internet Explorer"
WScript.Sleep 1000*1 

wsh.SendKeys "{TAB}"	'1
WScript.Sleep 1000*1 
wsh.SendKeys "{TAB}"	'2
WScript.Sleep 1000*1 
wsh.SendKeys "{TAB}"
WScript.Sleep 1000*1 
wsh.SendKeys "{TAB}"
WScript.Sleep 1000*1 
wsh.SendKeys "{TAB}"	'5
WScript.Sleep 1000*1 
wsh.SendKeys "{TAB}"
WScript.Sleep 1000*1 
wsh.SendKeys "{TAB}"	'7 tab
WScript.Sleep 1000*1 

wsh.SendKeys "2546660220@qq.com" '引号中填帐号 
WScript.Sleep 1000*1 

wsh.SendKeys "{TAB}"
WScript.Sleep 1000*1 
wsh.SendKeys "password123" '引号中填密码 
WScript.Sleep 1000*1 

wsh.SendKeys "{TAB}"	'1
WScript.Sleep 1000*1 
wsh.SendKeys "{TAB}"	'2
WScript.Sleep 1000*1 

wsh.SendKeys "{ENTER}"

'wsh.SendKeys "{F11}"

Set wsh = Nothing
Set ie = Nothing