import keyboard,time,pyautogui
myfile = open(r"./files/mycodingno1-js-posts-list.txt","r")

keyboard.wait('ctrl+space')
number=1
indx=1
for ln in myfile.readlines():
    if keyboard.is_pressed('esc'):
        exit(0)
    s = str(indx)
   
    if number%2!=0:
        time.sleep(1)
        keyboard.press_and_release('enter')
        keyboard.write(f"{s}.{ln}")
        indx+=1
        
    else:
        #link paste
        
        time.sleep(1)
        keyboard.press_and_release('ctrl+k')
        time.sleep(1)
        keyboard.write(ln)
        time.sleep(1)
        keyboard.press_and_release('enter')
        
        

    number+=1

pyautogui.alert("Done")



