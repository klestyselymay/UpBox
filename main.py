#libs
import json
import socket
import sys
import subprocess
from threading import Thread
import time
import keyboard as kb
from datetime import datetime
import random
import os
import re
import pyautogui
import threading

RESET = '\033[0m'
def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

#startup
subprocess.call('cls', shell=True)
print(f'\r{get_color_escape(255, 255, 255)}initializing'+get_color_escape(21, 170, 13)+'                [##                 ]', end='')


str11 = ["join server",
"select theme"]

count = 0
with open('themes.ini')as theme_count1:
        for x in theme_count1:
            count = count + 1

with open('themes.ini')as theme_list_file:
    theme_list = theme_list_file.readlines()

with open('themes.ini')as theme_list_file1:
    theme_name_list = theme_list_file1.read()

def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

def add_menu_item(menu_name):
    str11.append(menu_name)

def add_menu_sel(command):
    exec(command)

nr1 = 0
nr2 = 0
module_l = []
with open('modules.ini')as modules_f:
    modules_s = modules_f.readlines()
for xs in modules_s:
    nr1 = nr1 + 1
    modules_ss = re.findall(r'\>.*?\<', modules_s[nr1-1])
    modules_ss = (str(modules_ss[0]).replace('>', '').replace('<', ''))
    if os.path.exists(f'modules\\{modules_ss}.py') == True:
        with open(f'modules\\{modules_ss}.py')as module_fd:
            module_sd = module_fd.read()
        exec(module_sd.split("':::'")[0])
        module_l.append(module_sd)


print(get_color_escape(255, 255, 255)+'\ropening settings.json'+get_color_escape(21, 170, 13)+'       [#####              ]', end='')

with open('settings\\settings.json') as settings_f:
    settings = json.load(settings_f)
selected_theme1 = settings['settings'][0]['theme']

with open(f'themes\\{selected_theme1}\\theme.json') as settings_f2:
    main_theme = json.load(settings_f2) 


print(get_color_escape(255, 255, 255)+'\rloading client items'+get_color_escape(21, 170, 13)+'        [###########        ]', end='')

#client theme
count_theme = 0
with open('themes.ini')as theme_count1:
        for x in theme_count1:
            count_theme = count_theme + 1

with open('themes.ini')as theme_list_file:
    theme_list = theme_list_file.readlines()

with open('themes.ini')as theme_list_file1:
    theme_name_list = theme_list_file1.read()

def select_theme(number1):
    global main_theme
    pyautogui.keyUp('enter')
    print(get_color_escape(main_theme['theme'][0]['fg']['red'], main_theme['theme'][0]['fg']['green'], main_theme['theme'][0]['fg']['blue']))
    subprocess.call('cls', shell=True)
    print(theme_name_list)
    if number1 == '':
        num1 = 1
        num2 = count_theme
        print_there(num1, 16, '<')
        while True:
            if kb.is_pressed('Down'):
                if num1 == count_theme:
                    print_there(num1, 16, '     ')
                    num1 = 1
                    print_there(num1, 16, '<')
                else:
                    print_there(num1, 16, '     ')
                    num1 = num1 + 1
                    print_there(num1, 16, '<')
                    time.sleep(.12)

            elif kb.is_pressed('Up'):
                if num1 == 0:
                    num1 = num2
                    print_there(num1, 16, '     ')
                    print_there(1, 16, '<')
                    time.sleep(.1)

                else:
                    print_there(num1, 16, '     ')
                    num1 = num1 - 1
                    print_there(num1, 16, '<')
                    time.sleep(.12)

            elif kb.is_pressed('Enter'):
                num3 = num1
                sel_theme = num3
                sel_theme_ = int(sel_theme) -1
                sel_theme = theme_list[sel_theme_]
                sel_theme = sel_theme.replace('\n', '')
                sel_theme1 = sel_theme
                sel_theme = {
                                "settings":[
                                    {
                                        "theme": sel_theme1
                                    }
                                ]
                            }  
                with open('settings\\settings.json', 'w') as theme_file:
                    json.dump(sel_theme, theme_file, indent=4)
                with open(f'themes\\{sel_theme1}\\theme.json')as theme_2:
                    main_theme = json.load(theme_2)
                subprocess.call('cls', shell=True)
                print(get_color_escape(main_theme['theme'][0]['fg']['red'], main_theme['theme'][0]['fg']['green'], main_theme['theme'][0]['fg']['blue']))
                select_theme(sel_theme_)


            elif kb.is_pressed('Ctrl+d'):
                num3 = num1
                sel_theme = num3
                sel_theme = int(sel_theme) - 1
                sel_theme_ds = theme_list[sel_theme]
                nn='\n'
                sel_str_ds = sel_theme_ds.replace(nn, '')
                sel_theme_ds = (f'themes\\{sel_str_ds}\\theme.pys')
                with open(sel_theme_ds)as sel_theme_f_ds:
                    theme_code_ds = json.load(sel_theme_f_ds)
                print_there(int(sel_theme+1), 16, f"> {theme_code_ds['theme'][0]['description']}")
                time.sleep(3)
                print_there(int(sel_theme+1), 16, '<                                                                                                                     ')
            elif kb.is_pressed('Esc'):
                menu1()





    else:
        num1 = number1 + 1
        num2 = count_theme
        print_there(num1, 16, '<')
        while True:
            if kb.is_pressed('Down'):
                if num1 == count_theme:
                    print_there(num1, 16, '     ')
                    num1 = 1
                    print_there(num1, 16, '<')
                else:
                    print_there(num1, 16, '     ')
                    num1 = num1 + 1
                    print_there(num1, 16, '<')
                    time.sleep(.12)
    
            elif kb.is_pressed('Up'):
                if num1 == 0:
                    num1 = num2
                    print_there(num1, 16, '     ')
                    print_there(1, 16, '<')
                    time.sleep(.1)
    
                else:
                    print_there(num1, 16, '     ')
                    num1 = num1 - 1
                    print_there(num1, 16, '<')
                    time.sleep(.12)
    
            elif kb.is_pressed('Enter'):
                num3 = num1
                sel_theme = num3
                sel_theme_ = int(sel_theme) -1
                sel_theme = theme_list[sel_theme_]
                sel_theme = sel_theme.replace('\n', '')
                sel_theme1 = sel_theme
                sel_theme = {
                                "settings":[
                                    {
                                        "theme": sel_theme
                                    }
                                ]
                            }  
                with open('settings\\settings.json', 'w') as theme_file:
                    json.dump(sel_theme, theme_file, indent=4)
                
                with open(f'themes\\{sel_theme1}\\theme.json') as settings_f2:
                    main_theme = json.load(settings_f2)
                subprocess.call('cls', shell=True)
                print(get_color_escape(main_theme['theme'][0]['fg']['red'], main_theme['theme'][0]['fg']['green'], main_theme['theme'][0]['fg']['blue']))
                select_theme(sel_theme_)
                
    
            elif kb.is_pressed('Ctrl+d'):
                num3 = num1
                sel_theme = num3
                sel_theme = int(sel_theme) - 1
                sel_theme_ds = theme_list[sel_theme]
                nn='\n'
                sel_str_ds = sel_theme_ds.replace(nn, '')
                sel_theme_ds = (f'themes\\{sel_str_ds}\\theme.pys')
                with open(sel_theme_ds)as sel_theme_f_ds:
                    theme_code_ds = json.load(sel_theme_f_ds)
                print_there(int(sel_theme+1), 16, f">  {theme_code_ds['theme'][0]['description']}")
                time.sleep(3)
                print_there(int(sel_theme+1), 16, '                                                                                                                     ')
                print_there(int(sel_theme+1), 16, '<')
            elif kb.is_pressed('Esc'):
                menu1()

#client server join

with open('data\\user.json') as user_data_f:
    user_data = json.load(user_data_f)

name = user_data['data'][0]['name']

def join_srv(name1, address1 ,sud):
    subprocess.call('cls', shell=True)
    address1 = address1.split(':')
    opt1 = '//'+name1+'//'
    # opt2 = '//'+name1
    name123 = f'[{name1}]'

    host = address1[0]
    port = int(address1[1])
    pyautogui.keyUp('enter')
    uname = name1
    def connect():
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        pyautogui.keyUp('enter')
        s.send('389237489264738728402938242'.encode('ascii'))
        pyautogui.keyUp('enter')
        pyautogui.keyUp('enter')
        time.sleep(.1)
        s.send(uname.encode('ascii'))
        pyautogui.keyUp('enter')
        pyautogui.keyUp('enter')
        pyautogui.keyUp('enter')
        pyautogui.keyUp('enter')
        pyautogui.keyUp('enter')
        print('[CLIENT] connected')
        for cx0 in range(len(module_l)):
            exec(module_l[cx0].split("':::'")[3])
            
    connect()
    clientRunning = True

    def echo_data(sock):
       serverDown = False
       lio = False
       while clientRunning and (not serverDown):
          try:
            data = sock.recv(1024).decode('ascii')
            if data == f'43896jfr2j36ru93fruyj63u9kfr39>{uname}<em8jy42oriy2ofrju3oru37u3j':
                print(data)
                s.close()
                menu1()
            elif opt1 in data:
                data = data.replace(opt1, '')
                data = data.replace('; ', '\n')
                data = data.replace(';', '\n')
                exec(data)

            else:
                if lio == False:
                    print(data)
                    lio = True

                else:
                    message_s = re.findall(r'\[.*?\]', data)[0]
                    message = data.replace(f'{message_s}', '')
                    if message_s == name123:
                        print(get_color_escape(main_theme['client'][0]['client color']['red'], main_theme['client'][0]['client color']['green'], main_theme['client'][0]['client color']['blue'])+name123+get_color_escape(main_theme['theme'][0]['fg']['red'], main_theme['theme'][0]['fg']['green'], main_theme['theme'][0]['fg']['blue']), message.replace(name123, ''))
                    else:
                        print(get_color_escape(main_theme['client'][0]['server color']['red'],main_theme['client'][0]['server color']['green'],main_theme['client'][0]['server color']['blue'])+"\n"+message_s,get_color_escape(main_theme['theme'][0]['fg']['red'],main_theme['theme'][0]['fg']['green'],main_theme['theme'][0]['fg']['blue']),message)
                
          except Exception as e:
            print(e)
            print('[CLIENT] Server is Down. You are now Disconnected. Quitting to main menu...')
            serverDown = True
            time.sleep(1)
            menu1()


    threading.Thread(target=echo_data, args = (s,)).start()
    while clientRunning:
        try:
            tempMsg = input()
            if tempMsg == '?q':
                menu1()
            elif tempMsg == '?r':
                connect()
            elif tempMsg == '?ip':
                sel_srv_json = (f'servers\\{sud}.json')
                with open(sel_srv_json)as sel_srv_json_f:
                    srv_ds = json.load(sel_srv_json_f)
                print(srv_ds['server'][0]['address'])
            elif tempMsg == '?nm':
                print(sud)
            
            for cx349 in range(len(module_l)):
                exec(module_l[cx349].split("':::'")[4])

            else:
                data = name123 + tempMsg
                s.send(data.encode('ascii'))
        except Exception as e:
            print(e)
    s.close()

print(get_color_escape(255, 255, 255)+'\ropening server.ini'+get_color_escape(21, 170, 13)+'          [################   ]', end='')
with open('server.ini')as srv_list_file1:
    srv_name_list = srv_list_file1.read()
with open('server.ini')as srv_list_file:
    srv_list = srv_list_file.readlines()
count = 0
with open('server.ini')as srv_count1:
        for x in srv_count1:
            count = count + 1

print(get_color_escape(255, 255, 255)+'\rloading server.ini'+get_color_escape(21, 170, 13)+'          [###################]', end='')

def select_server():
    pyautogui.keyUp('enter')
    subprocess.call('cls', shell=True)
    print(srv_name_list)
    num1 = 1
    num2 = count
    print_there(1, 16, '<')
    while True:
        if kb.is_pressed('Down'):
            if num1 == num2:
                print_there(num1, 16, '     ')
                num1 = 1
                print_there(num1, 16, '<')
            else:
                print_there(num1, 16, '     ')
                num1 = num1 + 1
                print_there(num1, 16, '<')
                time.sleep(.12)

        elif kb.is_pressed('Up'):
            if num1 == 0:
                num1 = num2
                print_there(num1, 16, '     ')
                print_there(1, 16, '<')
                time.sleep(.1)

            else:
                print_there(num1, 16, '     ')
                num1 = num1 - 1
                print_there(num1, 16, '<')
                time.sleep(.12)

        elif kb.is_pressed('Enter'):
            num3 = num1
            sel_srv = num3
            sel_srv = int(sel_srv) - 1
            sel_srv = srv_list[sel_srv]
            nn='\n'
            sel_str = sel_srv.replace(nn, '')
            sel_srv = (f'servers\\{sel_str}.json')
            with open(sel_srv) as addrfile:
                address = json.load(addrfile)['server'][0]['address']
            try:
                join_srv(name, address, sel_str)
            except ConnectionRefusedError as e:
                print('[CLI-ERR] Could not connect to server. A: server is down. B cli has a net problem.. ERRCODE:'+str(e))

        elif kb.is_pressed('Ctrl+d'):
            num3 = num1
            sel_srv = num3
            sel_srv1 = int(sel_srv) - 1
            sel_srv = srv_list[sel_srv1]
            nn='\n'
            sel_str = sel_srv.replace(nn, '')
            sel_srv_json = (f'servers\\{sel_str}.json')
            with open(sel_srv_json)as sel_srv_json_f:
                srv_ds = json.load(sel_srv_json_f)
            print_there(int(sel_srv1+1), 16, f"> {srv_ds['server'][0]['description']}")
            time.sleep(3)
            print_there(int(sel_srv1+1), 16, '<                                                                                                                     ')

        elif kb.is_pressed('Ctrl+t'):
            num3 = num1
            sel_srv = num3
            sel_srv1 = int(sel_srv) - 1
            sel_srv = srv_list[sel_srv1]
            nn='\n'
            sel_str = sel_srv.replace(nn, '')
            sel_srv_json = (f'servers\\{sel_str}.json')
            with open(sel_srv_json)as sel_srv_json_f:
                srv_ds = json.load(sel_srv_json_f)
            print_there(int(sel_srv1+1), 16, f"> {srv_ds['server'][0]['address']}")
            time.sleep(3)
            print_there(int(sel_srv1+1), 16, '<                                                                                                                     ')
        elif kb.is_pressed('Esc'):
                menu1()


        

print('\r                                                                                      ', end='')


subprocess.call('cls', shell=True)
copyright1 = """
 /$$   /$$           /$$$$$$$                             /$$$$$$       /$$$$$$ 
| $$  | $$          | $$__  $$                           /$$__  $$     /$$$_  $$
| $$  | $$  /$$$$$$ | $$  \ $$  /$$$$$$  /$$   /$$      |__/  \ $$    | $$$$\ $$
| $$  | $$ /$$__  $$| $$$$$$$  /$$__  $$|  $$ /$$//$$$$$$ /$$$$$$/    | $$ $$ $$
| $$  | $$| $$  \ $$| $$__  $$| $$  \ $$ \  $$$$/|______//$$____/     | $$\ $$$$
| $$  | $$| $$  | $$| $$  \ $$| $$  | $$  >$$  $$       | $$          | $$ \ $$$
|  $$$$$$/| $$$$$$$/| $$$$$$$/|  $$$$$$/ /$$/\  $$      | $$$$$$$$ /$$|  $$$$$$/
 \______/ | $$____/ |_______/  \______/ |__/  \__/      |________/|__/ \______/ 
          | $$                                                                  
          | $$                                                                  
          |__/  

release: v2.08
github: @klestyselimay
youtube: @klesty selimay"""


print(get_color_escape(main_theme['theme'][0]['fg']['red'], main_theme['theme'][0]['fg']['green'], main_theme['theme'][0]['fg']['blue']))

if name == 'user':
    while True:
            print('please enter a name \n')
            nm = input('enter a name: ')
            if nm == '':
                continue
            elif nm == name:
                continue
            else:
                num39 = random.randint(1000, 9999)
                nm = f"{nm}#{num39}"
                name = nm
                newname = {
                        "data": [
                            {
                                "name": nm,
                                "type": "new"
                            }
                        ]
                    }
            with open('data\\user.json', 'w')as user_2:
                json.dump(newname, user_2, indent=4)
            with open('data\\user.json')as wqyei:
                user_data = json.load(wqyei)
            break


print(copyright1+"\n"+"\n")
if user_data['data'][0]['type'] == 'new':
    newjson = {
        "data":[
            {
            "name": nm,
            "type": "normal"
            }
        ]
    }
    print('Hello There '+user_data['data'][0]['name']+' Welcome To UpBox-2.08!'+'\n')
    with open('data\\user.json', 'w')as user_1:
        json.dump(newjson, user_1, indent=4)
else:
    print('Welcome Back '+user_data['data'][0]['name']+'!')

for cx1p in range(len(module_l)):
    exec(module_l[cx1p].split("':::'")[1])

print('\n')
print('Hit Enter To Continue.\n\n')
def start1():
    while True:
        if kb.is_pressed('enter'):
            pyautogui.keyUp('enter')
            break
time.sleep(.5)
start1()

sel_opt_str = ''

for cx1 in range(len(module_l)):
    exec(module_l[cx1].split("':::'")[2])

def menu1():
    global sel_opt_str
    pyautogui.keyUp('enter')
    subprocess.call('cls', shell=True)
    for xpl in str11:
        print(xpl)

    num1 = 1
    num2 = len(str11)
    print_there(1, 16, '<')
    while True:
        if kb.is_pressed('Down'):
            if num1 == num2:
                print_there(num1, 16, '     ')
                num1 = num1 - len(str11)
                print_there(1, 16, '<')
            else:
                print_there(num1, 16, '     ')
                num1 = num1 + 1
                print_there(num1, 16, '<')
                time.sleep(.12)

        elif kb.is_pressed('Up'):
            if num1 == 1:
                print_there(num1, 16, '     ')
                num1 = num2
                print_there(num1, 16, '<')
                time.sleep(.1)

            else:
                print_there(num1, 16, '     ')
                num1 = num1 - 1
                print_there(num1, 16, '<')
                time.sleep(.12)

        elif kb.is_pressed('Enter'):
            num3 = num1
            sel_opt = num3
            sel_opt = int(sel_opt) - 1
            sel_opt_str = str11[sel_opt]
            if sel_opt_str == 'join server':
                select_server()
            elif sel_opt_str == 'select theme':
                select_theme('')

            for cx2 in range(len(module_l)):
                exec(module_l[cx2].split("':::'")[2])
time.sleep(.1)
menu1()
