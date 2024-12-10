import time 
import sys
import os 
import re 
import pyperclip 
import pytesseract
from PIL import Image,ImageGrab
import numpy as np 

def is_Clipboard_Image(data):
    try:
        # imgData = ImageGrab.grabclipboard()
        if isinstance(data,Image.Image):
            return True
    except Exception as e :
        print("err:",e)
    
    return False
    

# recent_value = ""
configText = "--psm 3" 
while True:
    clipData = ImageGrab.grabclipboard()
    try:
        if is_Clipboard_Image(clipData):
            text = pytesseract.image_to_string(np.array(clipData),lang='jpn',config=configText)
            text=text.replace(" ","").replace("\n"," ")
            print(text)
            pyperclip.copy(text)

    except KeyboardInterrupt:
        break
        

# clipData = ImageGrab.grabclipboard()
# if is_Clipboard_Image(clipData):
#     # img = Image.open(clipData)
#     text = pytesseract.image_to_string(np.array(clipData),lang="jpn")
#     print(text)
# else:
#     print("N")