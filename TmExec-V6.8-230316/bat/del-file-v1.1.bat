@echo on
setlocal enabledelayedexpansion
set PATH_CURR=%~dp0
set src_dir=%PATH_CURR%png\2022-06-26
echo %src_dir%
cd /d %src_dir%
for /f "skip=1 delims=" %%i in ('dir *.png /b /o-n') do (del %%i /f /q)