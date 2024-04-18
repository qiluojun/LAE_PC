''
'' Auto Operation Script
''
'' Author: boomworks#hotmail.com
'' WeChat ID: boomwxsoft
''
'' Update:
''		2022-10-14
''		2022-10-31
''
'' USAGE:
''	SETCURSOR		S
''	LCLICK			LC
''	MOVE & LCLICK	MLC
''	DBLCLICK		DBLC
''	MDBLCLICK		MDBLC
''	RCLICK			RC
''	MVOE & RCLICK	MRC
''	SNDKEY			K
''	MVOE			M
''

Option Explicit

On Error Resume Next

'''''''''''''''''''''
'' Setting Parameter
'''''''''''''''''''''

Const NS_SLEEP_MIN = 200
Const NS_SLEEP_MAX = 2000

Dim OpArray(0,2)	'' n,m: n+1 row & m+1 col

''				prop1					prop2							prop3
OpArray(0, 0) = "LC"  : OpArray(0, 1) = "1183 248"	: OpArray(0, 2) = NS_SLEEP_MIN


'''''''''''''''''''
'' DO NOT CHANGE
'''''''''''''''''''

Dim strCurrPath,strParentPath,strNCmdPath
strCurrPath = CreateObject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
strParentPath = Mid(strCurrPath, 1, InStrRev(strCurrPath, "\"))
'Wscript.echo strParentPath
strNCmdPath = strParentPath & "nircmd\\nircmd.exe "
'Wscript.echo strNCmdPath

Dim oShell
Set oShell = CreateObject("wscript.shell")
'MsgBox ncmpath ' & "\\nircmd"

wscript.sleep 200

''
'' loop
''

Dim iOp,prop1,prop2,prop3

For iOp = 0 To UBound(OpArray)
	prop1 = OpArray(iOp, 0)
	prop2 = OpArray(iOp, 1)
	prop3 = OpArray(iOp, 2)
	'MsgBox prop1 & prop2
	
	If Not IsEmpty(prop1) Then
		'' S
		If prop1 = "S" Then
			If prop2 = "" Then
				MsgBox "prop2 is empty!"
				Exit For
			End If
			oShell.Run strNCmdPath & "setcursor "& prop2
			wscript.sleep prop3
		End If
		
		'' LC
		If prop1 = "LC" Then
			If prop2 = "" Then
				MsgBox "prop2 is empty!"
				Exit For
			End If
			oShell.Run strNCmdPath & "setcursor "& prop2
			wscript.sleep prop3
			oShell.Run strNCmdPath & "sendmouse left click"
			wscript.sleep prop3
		End If
		
		'' MLC
		If prop1 = "MLC" Then
			If prop2 = "" Then
				MsgBox "prop2 is empty!"
				Exit For
			End If
			oShell.Run strNCmdPath & "movecursor "& prop2
			wscript.sleep prop3
			oShell.Run strNCmdPath & "sendmouse left click"
			wscript.sleep prop3
		End If
		
		'' DBLC
		If prop1 = "DBLC" Then
			If prop2 = "" Then
				MsgBox "prop2 is empty!"
				Exit For
			End If
			oShell.Run strNCmdPath & "setcursor "& prop2
			wscript.sleep prop3
			oShell.Run strNCmdPath & "sendmouse left dblclick"
			wscript.sleep prop3
		End If
		
		'' MDBLC
		If prop1 = "MDBLC" Then
			If prop2 = "" Then
				MsgBox "prop2 is empty!"
				Exit For
			End If
			oShell.Run strNCmdPath & "movecursor "& prop2
			wscript.sleep prop3
			oShell.Run strNCmdPath & "sendmouse left dblclick"
			wscript.sleep prop3
		End If
		
		'' RC
		If prop1 = "RC" Then
			oShell.Run strNCmdPath & "setcursor "& prop2
			wscript.sleep prop3
			oShell.Run strNCmdPath & "sendmouse Right click"
			wscript.sleep prop3
		End If
		
		'' MRC
		If prop1 = "MRC" Then
			oShell.Run strNCmdPath & "movecursor "& prop2
			wscript.sleep prop3
			oShell.Run strNCmdPath & "sendmouse Right click"
			wscript.sleep prop3
		End If
		
		'' M
		If prop1 = "M" Then
			oShell.Run strNCmdPath & "movecursor "& prop2
			wscript.sleep prop3
		End If
		
		'' K
		If prop1 = "K" Then
			oShell.SendKeys prop2
			wscript.sleep prop3
		End If
	Else
		MsgBox "prop1 is empty!"
	End If
Next

On Error Goto 0

Wscript.Quit 0