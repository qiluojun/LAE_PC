@echo off
tasklist|find /i "notepad.exe"
if %errorlevel%==0 (
	echo running
) else (
	echo not running
	start /d "C:\Windows\System32" notepad.exe
)