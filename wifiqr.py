import qrcode
import time
import os
from os.path import isfile, join, dirname
import platform
from datetime import datetime
import sys
import subprocess
import io

# Static
ans = 1
myos = platform.system()
export_path = '/export'

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

def viewqr():
    dir_path = str(dirname(os.path.realpath(__file__))) + '\export\\'
    filenames = next(os.walk(dir_path), (None, None, []))[2]
    o = 0
    while o < len(filenames):
        print('['+str(o)+'] '+filenames[o])
        o += 1
    ch = input('\nSelect number: ')
    if ch.isnumeric() == 0 or len(filenames)-1<int(ch):
        print('Please enter an option from the list')
    filepath = dir_path + filenames[int(ch)]
    print(filepath)
    terminal_qr(filepath)
    
def options():
    print('\nWhat would you like to do?\n\n[0] Generate new WiFiQR\n[1] View existing WiFiQR')
    opt = input('\nChoose option: ')
    optlist = {'0':make_qr,
               '1':viewqr}
    try:
        function = optlist[opt]
    except KeyError:
        raise ValueError('invalid input')
    function()

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
    terminal_qr(savestr)
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
    loop_ans = input('Would you like to start over? (Y,N): ')
    f_loop_ans = loop_ans.upper().replace(' ','')
    if f_loop_ans == 'Y':
        ans = 1
    else:
        ans = 0


def run():
    title()
    options()
    clear()
    loop_func()
    clear()
        
if __name__ == '__main__':
    while ans == 1:
        run()

