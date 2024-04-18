import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from tkinter import END
import re

with open(r'D:\学习and学校\obsidian\qiluo\03-Projects\01-自由探索\02-搞事情\LAE\test.md','r',encoding='utf-8') as f:
    text = f.read()
sidelines = {}

for i in range(1, 9):
    sideline = {}
    name_pattern = re.compile(r'{}1【(.*?)】'.format(i))
    location_pattern = re.compile(r'{}2【(.*?)】'.format(i))
    date_pattern = re.compile(r'{}3【(.*?)】'.format(i))

    name_match = name_pattern.search(text)
    location_match = location_pattern.search(text)
    date_match = date_pattern.search(text)

    if name_match:
        sideline['name'] = name_match.group(1)
    else:
        print('No match found for name of sideline{}'.format(i))

    if location_match:
        sideline['location'] = location_match.group(1)
    else:
        print('No match found for location of sideline{}'.format(i))

    if date_match:
        sideline['date'] = date_match.group(1)
    else:
        print('No match found for date of sideline{}'.format(i))

    sidelines['sideline{}'.format(i)] = sideline