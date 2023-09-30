import keyboard,time,random,os


emoji =['😊','⚛','👍','🚩','🏹','🕉','💗','💚','☀️','🔱','⚔','☸','🇮✡']
keyboard.wait('ctrl+i')
for ram in range(12):
    rand_number = random.randint(1,12)
    select_emoji = emoji[rand_number]
    # time.sleep(1)
    # keyboard.press_and_release('enter')
    time.sleep(1)
    keyboard.write(f' {select_emoji}जय श्री राम{select_emoji}')


time.sleep(1)
keyboard.press_and_release('enter')

os.system('python multi.py')


