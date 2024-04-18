@echo off

rem if "%1"=="h" goto begin
rem start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit

:begin
tasklist|find /i "timingexecutor.exe"
if %errorlevel%==0 (
	echo running
) else (
	echo not running
	start /d "D:\TimingExecutor" timingexecutor.exe
)