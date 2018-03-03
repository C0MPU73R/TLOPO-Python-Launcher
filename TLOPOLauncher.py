#!/usr/bin/env python2

import getpass
import os
import sys
import requests

sys.setrecursionlimit(999999999)

headers = {'Content-type': 'application/x-www-form-urlencoded'}
response = {'status': -1}

while True:
    status = response.get('status')
    if status == -1:
        username = raw_input('Username: ')
        password = getpass.getpass('Password: ')

        data = {'username': username, 'password': password}
        response = requests.post("https://api.tlopo.com/login/", headers=headers, data=data, verify=False).json()

        if response.get('status') == 7:
            sys.stdout.write('\n')
            sys.stdout.flush()
            break

# Move into the installation directory:
if sys.platform == 'win32':
    os.chdir(os.path.join(os.environ['HOMEDRIVE'], '\TLOPO'))

# Launch the game:
os.environ['TLOPO_PLAYCOOKIE'] = response['token']
os.environ['TLOPO_GAMESERVER'] = response['gameserver']

if sys.platform == 'win32':
    os.system('tlopo.exe')
