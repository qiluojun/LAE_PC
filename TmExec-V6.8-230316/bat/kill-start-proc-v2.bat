@echo off

rem if "%1"=="h" goto begin
rem start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit

:begin
tasklist|find /i "wubilex.exe"
if %errorlevel%==0 (
	echo running
	taskkill /f /im "wubilex.exe"
	ping 127.0.0.1 >nul
	start /d "D:\xxx" wubilex.exe
) else (
	echo not running
	start /d "D:\xxx" wubilex.exe
)