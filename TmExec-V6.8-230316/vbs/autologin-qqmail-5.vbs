''
'' Auto Login Script V2.0
'' Author: boomworks
'' E-mail: boomworks#hotmail.com
'' WeChat ID: boomwxsoft
''

Dim url,username,userpwd,browser
''必须配置 -> 引号中填登录网页的地址
url = "https://mail.qq.com"
''必须配置 -> 引号中填登录用的账号
username = "boomworks@hotmail.com"
''必须配置 -> 引号中填登录用的密码
userpwd = "PAss1234567890"
''可选配置 -> 可配置其他浏览器 msedge chrome iexplore
browser = "chrome"

'****** 下面的代码不要动 ******

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

wsh.Run browser & ".exe" & " " & url
WScript.Sleep 1000*4

wsh.Run nCmdPath & "movecursor -9999 -9999"
WScript.Sleep 500*1
wsh.Run nCmdPath & "movecursor 1186 258"
WScript.Sleep 500*1
wsh.Run nCmdPath & "sendmouse left click"

'wsh.SendKeys "+"
'WScript.Sleep 500*1

wsh.SendKeys username
WScript.Sleep 500*1 

wsh.SendKeys "{TAB}"
WScript.Sleep 500*1

wsh.SendKeys userpwd
WScript.Sleep 500*1
  
'wsh.SendKeys "{ENTER}"
'WScript.Sleep 500*1

wsh.Run nCmdPath & "movecursor -9999 -9999"
WScript.Sleep 500*1
wsh.Run nCmdPath & "movecursor 1110 410"
WScript.Sleep 500*1
wsh.Run nCmdPath & "sendmouse left click"

'WScript.Sleep 1000*4
'wsh.SendKeys "^w"

Set wsh = Nothing