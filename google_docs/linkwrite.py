import keyboard
import os
import time
import pyperclip
import datetime
import pyautogui

# filename =  datetime.datetime.now().timestamp()
filename = pyautogui.prompt(text='', title='Enter Your File Name' , default='')
f = open(f"./files/{filename}",'a')
# f = open(f"./files/neerj.txt",'a')
myfile = open(f"./files/{filename}")

stored =[]

for line in myfile.readlines():
        stored.append(line.casefold().replace('\n',''))


while True:
    keyboard.wait('ctrl+c')
    time.sleep(1)
    mycopy = pyperclip.paste()
    lowertxt = mycopy.casefold()
    if stored.count(lowertxt)>1:
        pyautogui.alert(text=f'"{mycopy}" is already exist.', title='Error')
    else:
        f.write('\n'+mycopy)
        stored.append(lowertxt)



    