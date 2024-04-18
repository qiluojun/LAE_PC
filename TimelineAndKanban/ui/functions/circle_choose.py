from pynput import keyboard
import pyperclip
from PySide6.QtCore import QThread, Signal


'''
def on_release(key):
    if key == keyboard.Key.ctrl_l:  # 检测到左Ctrl键释放
        print(pyperclip.paste())  # 打印剪贴板内容

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()'''
    

class MyListener(QThread):
    text_copied = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.join()

    def on_release(self, key):
        if key == keyboard.Key.ctrl_l:  # 检测到左Ctrl键释放
            self.text_copied.emit(pyperclip.paste())  # 发出信号