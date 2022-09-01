import qrcode
import pyperclip as pc
import time
import os
import platform
from datetime import datetime

# Static
ans = 1

def title():
    with open('title.txt', 'r') as f:
        for line in f:
            print(line.strip())
            time.sleep(0.1)
            
def make_qr():
    date = datetime.now().strftime('%Y%m%d_%H-%M-%S')
    ssid = str(input('SSID: '))
    pword = str(input('Password: '))
    filename = str(input('File Name: '))
    wificode = 'WIFI:T:WPA;P:'+pword+';S:'+ssid+';H:false'
    img = qrcode.make(wificode)
    type(img)
    img.save('export/' + filename + ' ' + str(date) + '.png')

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def loop_func():
    global ans
    loop_ans = input('Would you like to generator another QR Code? (Y,N): ')
    f_loop_ans = loop_ans.upper().replace(' ','')
    if f_loop_ans == 'Y':
        ans = 1
    else:
        ans = 0

def run():
    title()
    make_qr()
    clear()
    loop_func()
        
if __name__ == '__main__':
    while ans == 1:
        run()

