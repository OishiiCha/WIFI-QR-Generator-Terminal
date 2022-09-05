import qrcode
import time
import os
import platform
from datetime import datetime
import sys
import subprocess
import io

# Static
ans = 1
myos = platform.system()

def title():
    with open('title.txt', 'r') as f:
        for line in f:
            print(line.strip())
            time.sleep(0.1)

def openimage(path):
    imageViewerFromCommandLine = {'linux':'xdg-open',
                                  'win32':'explorer',
                                  'darwin':'open'}[sys.platform]
    subprocess.run([imageViewerFromCommandLine, path])

def terminal_qr(mqr):
    qr = qrcode.QRCode()
    qr.add_data(mqr)
    h = io.StringIO()
    qr.print_ascii(out=h)
    h.seek(0)
    print(h.read())

def make_qr():
    date = datetime.now().strftime('%Y%m%d_%H-%M-%S')
    ssid = str(input('SSID: '))
    pword = str(input('Password: '))
    filename = str(input('File Name: ') + ' ' + str(date) + '.png')
    wificode = 'WIFI:T:WPA;P:' + pword + ';S:' + ssid + ';H:false'
    img = qrcode.make(wificode)
    type(img)
    savestr = str('export/'+filename)
    img.save(savestr)
    terminal_qr(wificode)
    time.sleep(0.1)
    op = input('Would you like to open the Generated QR Code? (Y,N): ')
    f_op = op.upper().replace(' ','')
    if f_op == 'Y':
        if sys.platform == 'win32':
            filenamedir = str('export\\'+filename)
        else:
            filenamedir = str('export/'+filename)
        openimage(filenamedir)

def clear():
    if myos == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def loop_func():
    global ans
    loop_ans = input('Would you like to generate another QR Code? (Y,N): ')
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
        
