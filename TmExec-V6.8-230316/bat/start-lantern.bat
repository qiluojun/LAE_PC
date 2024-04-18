@echo on

c:
cd C:\Users\leo\AppData\Roaming\Lantern

del lantern.exe
copy ltn.bmwx /b bmwx-ltn.exe /b /y

start "" "C:\Users\leo\AppData\Roaming\Lantern\bmwx-ltn.exe"

rem pause
exit