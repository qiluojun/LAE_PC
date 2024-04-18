@echo off

if "%1"=="h" goto begin
start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit

:begin
tasklist|find /i "notepad.exe"
if %errorlevel%==0 (
	echo running
) else (
	echo not running
	start /d "C:\Windows\System32" notepad.exe
)