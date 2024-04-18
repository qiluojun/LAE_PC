Set objShell = CreateObject("WScript.Shell") 
objShell.Run("cmd.exe /c ""D:\TimingExecutor\bat\checkproc-2.bat""") , 0 ' ,True
Set objShell = Nothing 
