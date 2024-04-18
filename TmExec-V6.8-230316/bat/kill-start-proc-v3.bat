@echo off

rem if "%1"=="h" goto begin
rem start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit

%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c "^&chr(34)^&"%~0"^&chr(34)^&" ::","%cd%","runas",1)(window.close)&&exit

:begin
tasklist|find /i "notepad.exe"
if %errorlevel%==0 (
	echo running
	taskkill /f /im "notepad.exe"
	ping 127.0.0.1 >nul
	start /d "C:\Windows\system32" notepad.exe
) else (
	echo not running
	start /d "C:\Windows\system32" notepad.exe
)