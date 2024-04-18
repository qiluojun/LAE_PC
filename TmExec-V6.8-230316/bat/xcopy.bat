@echo off
setlocal

set PATH_CURR=%~dp0

xcopy   %PATH_CURR%src\locales\                     %PATH_CURR%src\bin\debug\locales\           /D /S /Y
xcopy   %PATH_CURR%src\locales\                     %PATH_CURR%src\bin\release\locales\         /D /S /Y

xcopy   %PATH_CURR%src\img\                         %PATH_CURR%src\bin\debug\img\           /D /S /Y
xcopy   %PATH_CURR%src\img\                         %PATH_CURR%src\bin\release\img\         /D /S /Y

xcopy   %PATH_CURR%src\bin\debug\data\              %PATH_CURR%src\bin\release\data\         /S /Y
xcopy   %PATH_CURR%src\doc\              %PATH_CURR%src\bin\release\doc\        /D /S /Y

endlocal
pause
