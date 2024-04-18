@echo off

if "%1"=="h" goto begin
start mshta vbscript:createobject("wscript.shell").run("""%~fs0"" h",0)(window.close)&&exit

:begin
tasklist|find /i "timingexecutor.exe"
if %errorlevel%==0 (
	echo running
) else (
	echo not running
	start /d "D:\TimingExecutor" timingexecutor.exe
)