@echo off

c:
cd C:\Users\leo\AppData\Roaming\Lantern
rem dir replica-local-index*.sqlite
del replica-local-index*.sqlite

cd C:\Users\leo\AppData\Local\Temp
rem dir replica-local-index*
del replica-local-index*

d:
rem pause
exit