import sys
sys.coinit_flags = 2
from pywinauto import Desktop
import os




def checkEdge():
    danger = 0
    windows = Desktop(backend="uia").windows()
    current_names = set(w.window_text() for w in windows if w.window_text().strip())
    #print(type(current_names))
    #current_time = time.strftime("%H%M")
    #contains_zhihu = False
    for name in current_names:
        if "Edge" in name:
            danger = 1
    
    
    return danger