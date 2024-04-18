import tkinter as tk
import os
import time
import win32api
import win32con
import win32gui

class FullscreenWindow:
    def __init__(self):
        # Register the window class
        wc = win32gui.WNDCLASS()
        wc.hInstance = win32gui.GetModuleHandle(None)
        wc.lpszClassName = "FullscreenWindow"
        wc.lpfnWndProc = self.wnd_proc
        self.class_atom = win32gui.RegisterClass(wc)

        # Create the window
        style = win32con.WS_POPUP | win32con.WS_VISIBLE
        self.hwnd = win32gui.CreateWindowEx(
            0,
            self.class_atom,
            "Fullscreen Window",
            style,
            0, 0, win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN),
            None, None, wc.hInstance, None
        )

        # Set the window to be topmost
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    def wnd_proc(self, hwnd, msg, wParam, lParam):
        if msg == win32con.WM_CLOSE:
            return 0
        return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)

    def run(self):
        # Run the message loop
        win32gui.PumpMessages()

def lock_screen():
    os.system("rundll32.exe user32.dll,LockWorkStation")

def unlock_screen():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    time.sleep(10 - 1)
    win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)

def on_button_click():
    lock_screen()
    fw = FullscreenWindow()
    fw.run()
    unlock_screen()

root = tk.Tk()
root.title("Lock Screen")
root.geometry("300x200")

button = tk.Button(root, text="Lock Screen", command=on_button_click)
button.pack(pady=50)

root.mainloop()
