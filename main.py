#libs
import json
import socket
import sys
import subprocess
from threading import Thread
import time
from datetime import datetime
import random
import os
import re
import threading
from simple_term_menu import TerminalMenu
from better_profanity import profanity

par_dir = os.getcwd()

RESET = '\033[0m'
def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

#startup
os.system('clear')
print(f'\r{get_color_escape(255, 255, 255)}initializing'+get_color_escape(21, 170, 13)+'                [##                 ]', end='')

with open(f'{par_dir}/settings/options.ini')as opt_f:
    ini_opt2 = opt_f.read()

dict_opt = {}

ini_opt = ini_opt2.split('\n')
for x in range(len(ini_opt)):
    dict_opt[ini_opt[x].split('=')[0]] = ini_opt[x].split('=')[1]


str11 = ["select server", "select theme", "options"]
def create_menu(list_items, use_list=True):
    os.system('clear')
    main_menu = TerminalMenu(list_items, menu_highlight_style=(f"bg_{str(main_theme['theme'][0]['menu']['color']).lower()}",
    "fg_yellow"), clear_screen=True)
    option_out = main_menu.show() 
    if option_out == None:
        menu1()
    else:
        if use_list == True:
            return list_items[option_out]
        else:
            return option_out

def options_menu():
    global dict_opt
    global ini_opt
    opt = create_menu(ini_opt)
    opt = opt.split('=')
    if dict_opt[opt[0]].lower() == 'true':
        with open(f'{par_dir}/settings/options.ini', 'r')as opt_f:
            opt_ = opt_f.read()
        with open(f'{par_dir}/settings/options.ini', 'w')as opt_f:
            opt_f.write(f"{opt_.replace(f'{opt[0]}={opt[1]}', f'{opt[0]}=false')}")
        
        with open(f'{par_dir}/settings/options.ini')as opt_f:
            ini_opt2 = opt_f.read()

        ini_opt = ini_opt2.split('\n')
        for x in range(len(ini_opt)):
            dict_opt[ini_opt[x].split('=')[0]] = ini_opt[x].split('=')[1]
    else:
        with open(f'{par_dir}/settings/options.ini', 'r')as opt_f:
            opt_ = opt_f.read()
        with open(f'{par_dir}/settings/options.ini', 'w')as opt_f:
            opt_f.write(f"{opt_.replace(f'{opt[0]}={opt[1]}', f'{opt[0]}=true')}")
        
        with open(f'{par_dir}/settings/options.ini')as opt_f:
            ini_opt2 = opt_f.read()

        ini_opt = ini_opt2.split('\n')
        for x in range(len(ini_opt)):
            dict_opt[ini_opt[x].split('=')[0]] = ini_opt[x].split('=')[1]
    options_menu()
count = 0
with open('themes.ini')as theme_count1:
        for x in theme_count1:
            count = count + 1
        
theme_list = []

with open('themes.ini')as theme_list_file1:
    theme_name_list = theme_list_file1.read()

def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

def add_menu_item(menu_name):
    str11.append(menu_name)

def add_menu_sel(command):
    exec(command)

if dict_opt['mods'].lower() == 'true':
    nr1 = 0
    nr2 = 0
    module_l = []
    with open('modules.ini')as modules_f:
        modules_s = modules_f.readlines()
    for xs in modules_s:
        nr1 = nr1 + 1
        modules_ss = re.findall(r'\>.*?\<', modules_s[nr1-1])
        modules_ss = (str(modules_ss[0]).replace('>', '').replace('<', ''))
        if os.path.exists(f'{par_dir}/modules/{modules_ss}.py'):
            with open(f'{par_dir}/modules/{modules_ss}.py')as module_fd:
                module_sd = module_fd.read()
            exec(module_sd.split("':::'")[0])
            module_l.append(module_sd)
else:
    module_l = ''

print(get_color_escape(255, 255, 255)+'\ropening settings.json'+get_color_escape(21, 170, 13)+'       [#####              ]', end='')

with open(f'{par_dir}/settings/settings.json') as settings_f:
    settings = json.load(settings_f)
selected_theme1 = settings['settings'][0]['theme']

with open(f'{par_dir}/themes/{selected_theme1}/theme.json') as settings_f2:
    main_theme = json.load(settings_f2) 


print(get_color_escape(255, 255, 255)+'\rloading client items'+get_color_escape(21, 170, 13)+'        [###########        ]', end='')

#client theme
count_theme = 0
with open('themes.ini')as theme_count1:
        for x in theme_count1:
            count_theme = count_theme + 1

with open('themes.ini')as theme_list_file:
    theme_str = theme_list_file.readlines()

for x in theme_str:
    theme_list.append(re.search('<import type": "theme">(.*)</import>', x).group(1))

theme_list_m = list(map(lambda x: x.replace(selected_theme1, '[*]'+selected_theme1), theme_list))

with open('themes.ini')as theme_list_file1:
    theme_name_list = theme_list_file1.read()


def selected_theme_opt(th_name, th_no):
    global theme_list_m
    global theme_list
    global main_theme
    global settings
    global selected_theme1
    with open(f'themes/{th_name}/theme.pys')as th_f:
        th_title = json.load(th_f)['theme'][0]['description']
    selected_theme_menu = TerminalMenu(['select theme'], title=th_title, menu_highlight_style=(f"bg_{str(main_theme['theme'][0]['menu']['color']).lower()}",
    "fg_yellow"))
    selected_theme_menu_index = selected_theme_menu.show()
    if selected_theme_menu_index == None:
        select_theme()
    elif selected_theme_menu_index == 0:
        theme_list_m = list(map(lambda x: x.replace('[*]', ''), theme_list))
        theme_list_m[th_no] = '[*]'+th_name
        settings = {"settings": [{"theme": th_name}]}
        with open('settings/settings.json', 'w')as sf:
            json.dump(settings, sf, indent=3)
        with open(f'themes/{th_name}/theme.json')as ssf:
            main_theme = json.load(ssf)
        select_theme()

def select_theme():
    global theme_list_m
    global theme_list
    global main_theme
    global settings
    global selected_theme1
    theme_menu = TerminalMenu(theme_list_m, menu_highlight_style=(f"bg_{str(main_theme['theme'][0]['menu']['color']).lower()}",
    "fg_yellow"), title=f"[theme] {settings['settings'][0]['theme']}\n")
    theme_menu_index = theme_menu.show()
    if theme_menu_index == None:
        menu1()
    else:
        selected_theme_opt(theme_list[theme_menu_index], theme_menu_index)


#client server join

with open(f'{par_dir}/data/user.json') as user_data_f:
    user_data = json.load(user_data_f)

name = user_data['data'][0]['name']

def join_srv(name1, address1 ,sud):
    os.system('clear')
    address1 = address1.split(':')
    opt1 = '//'+name1+'//'
    # opt2 = '//'+name1
    name123 = f'[{name1}]'
    host = address1[0]
    port = int(address1[1])
    uname = name1
    def connect():
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        s.send('389237489264738728402938242'.encode())
        time.sleep(.7)
        s.send(uname.encode())
        print(f'[CLIENT] connected')
        new_data = s.recv(1024).decode()
        message_s = str(re.findall(r'\[.*?\]', new_data)[0])
        message = new_data.replace(f'{message_s}', '')
        print(get_color_escape(main_theme['client'][0]['server color']['red'],main_theme['client'][0]['server color']['green'],main_theme['client'][0]['server color']['blue'])+message_s,get_color_escape(main_theme['theme'][0]['fg']['red'],main_theme['theme'][0]['fg']['green'],main_theme['theme'][0]['fg']['blue']),message)
        print(get_color_escape(main_theme['client'][0]['client color']['red'], main_theme['client'][0]['client color']['green'], main_theme['client'][0]['client color']['blue']))
        for cx0 in range(len(module_l)):
            exec(module_l[cx0].split("':::'")[3])
    
            
    connect()
    clientRunning = True

    def echo_data(sock):
       serverDown = False
       lio = False
       while clientRunning and (not serverDown):
          try:
            data = sock.recv(1024).decode()
            if dict_opt['filter.cuss'].lower() == 'true':
                data = profanity.censor(data)
            if opt1 in data:
                data = data.replace(opt1, '')
                data = data.replace('; ', '\n')
                data = data.replace(';', '\n')
                exec(data)

            else:
                if lio == False:
                    print(data)
                    lio = True

                else:
                    message_s = re.findall(r'\[.*?\]', data)
                    if len(message_s) == 0:
                        False
                    else:
                        message_s = message_s[0]
                        message = data.replace(f'{message_s}', '')
                        if message_s == name123:
                            print(get_color_escape(main_theme['client'][0]['client color']['red'], main_theme['client'][0]['client color']['green'], main_theme['client'][0]['client color']['blue'])+name123+get_color_escape(main_theme['theme'][0]['fg']['red'], main_theme['theme'][0]['fg']['green'],main_theme['theme'][0]['fg']['blue']), message.replace(name123, ''))
                        else:
                            print(get_color_escape(main_theme['client'][0]['server color']['red'],main_theme['client'][0]['server color']['green'],main_theme['client'][0]['server color']['blue'])+"\n"+message_s,get_color_escape(main_theme['theme'][0]['fg']['red'],main_theme['theme'][0]['fg']['green'],main_theme['theme'][0]['fg']['blue']),message)
                
          except Exception as e:
            print(f'[CLIENT] You are Disconnected. Quitting to main menu... [ERRCODE] {e}')
            serverDown = True
            time.sleep(1)
            menu1()


    threading.Thread(target=echo_data, args = (s,)).start()
    while clientRunning:
        try:
            msg=input()
            if len(msg) == 0:
                data = name123 + msg
                s.send(data.encode())
            else:
                if msg[0] == '?':
                    if msg == '?q':
                        menu1()
                    elif msg == '?r':
                        s.close()
                        connect()
                    elif msg == '?info':
                        sel_srv_ini = (f'servers/{sud}.ini')
                        with open(sel_srv_ini)as sel_srv_ini_f:
                            addr1 = sel_srv_ini_f.read()
                        addr = addr1.split('\n')
                        srv_ds = {}
                        for x in range(len(addr)):
                            srv_ds[addr[x].split('=')[0]] = addr[x].split('=')[1]
                        print(f"""name: {sud}\ndescription: {srv_ds['description']}\naddress: {srv_ds['address']}""")
                    elif msg == '?nm':
                        print(sud)

                    for cx349 in range(len(module_l)):
                        exec(module_l[cx349].split("':::'")[4])

                else:
                    data = name123 + msg
                    s.send(data.encode())
        except Exception as e:
            print(e)
    s.close()

print(get_color_escape(255, 255, 255)+'\ropening server.ini'+get_color_escape(21, 170, 13)+'          [################   ]', end='')
with open('server.ini')as srv_list_file:
    srv_list_str = srv_list_file.readlines()
srv_list = ["[+]new"]
for x_ in srv_list_str:
    srv_list.append(x_.replace('\n', ''))

count = 0
with open('server.ini')as srv_count1:
        for x in srv_count1:
            count = count + 1

print(get_color_escape(255, 255, 255)+'\rloading server.ini'+get_color_escape(21, 170, 13)+'          [###################]', end='')

optls = ['join server', 'rename', 'change address', 'delete']

def selected_server_opt(curr_name):
    os.system('clear')
    global srv_list
    with open(f'servers/{curr_name}.ini')as f_oad:
        cr_f = f_oad.read()
    addr = cr_f.split('\n')
    cr_title = {}
    for x in range(len(addr)):
        cr_title[addr[x].split('=')[0]] = addr[x].split('=')[1]
    cr_title = cr_title['description']
    sel_server_menu = TerminalMenu(optls, title=cr_title, menu_highlight_style=(f"bg_{str(main_theme['theme'][0]['menu']['color']).lower()}",
    "fg_yellow"))
    sel_server_menu_index = sel_server_menu.show()
    if sel_server_menu_index == None:
        select_server(srv_list)
    elif optls[sel_server_menu_index] == 'join server':
        with open(f'servers/{curr_name}.ini')as f_addr:
            addr1 = f_addr.read()
        addr1 = addr1.split('\n')
        addr = {}
        for x in range(len(addr1)):
            addr[addr1[x].split('=')[0]] = addr1[x].split('=')[1]
        join_srv(name, addr['address'], curr_name)

    elif optls[sel_server_menu_index] == 'rename':
        new_name = input(f'{curr_name} -> ')
        if new_name == '':
            selected_server_opt(curr_name)
        if 'y' in input('are you sure you want to make these changes? [y/n] ').lower():
            with open('server.ini')as f_srv:
                srv_str = f_srv.read().replace(curr_name, new_name)
 
            os.rename(f'servers/{curr_name}.ini', f'servers/{new_name}.ini')
            with open('server.ini', 'w')as w_srv:
                w_srv.write(srv_str)
            with open('server.ini')as srv_list_file1:
                srv_list = srv_list_file1.readlines()
            curr_name = new_name
        os.system('clear')
        selected_server_opt(curr_name)
    
    elif optls[sel_server_menu_index] == 'change address':
        with open(f'servers/{curr_name}.ini')as f_oad:
            addr1 = f_oad.read()
        addr = addr1.split('\n')
        old_addr = {}
        for x in range(len(addr)):
            old_addr[addr[x].split('=')[0]] = addr[x].split('=')[1]
        new_addr = input(f"{old_addr['address']} -> ")
        if new_addr == '':
            selected_server_opt(curr_name)
        else:
            with open(f'servers/{curr_name}.ini', 'w')as f_nad:
                f_nad.write(addr1.replace(f"address={old_addr['address']}", f"address={new_addr}"))
        print(curr_name)
        selected_server_opt(curr_name)
    
    elif optls[sel_server_menu_index] == 'delete':
        with open('server.ini', 'r')as ff:
            ff_st = ff.read().replace(curr_name, '')
        with open('server.ini', 'w')as ff2:
            ff2.write(ff_st)
        with open('server.ini','r+') as file:
            for line in file:
                if not line.isspace():
                    file.write(line)
                select_server('')

def select_server(srv_list_):
    os.system('clear')
    with open('server.ini')as srv_list_file:
        srv_list_str = srv_list_file.readlines()
    srv_list_ = ["[+]new"]
    for x_ in srv_list_str:
        if x_ == '':
            False
        else:
            srv_list_.append(x_.replace('\n', ''))
    server_menu = TerminalMenu(srv_list_, menu_highlight_style=(f"bg_{str(main_theme['theme'][0]['menu']['color']).lower()}",
    "fg_yellow"))
    server_menu_index = server_menu.show()
    if server_menu_index == None:
        menu1()
    elif server_menu_index == 0:
        new_srv_name = input('name: ')
        if new_srv_name == '':
            os.system('clear')
            select_server('')
        else:
            new_srv_addr = input(f'{new_srv_name} -> ip:port: ')
            if new_srv_addr == '':
                select_server('')
            else:
                new_srv_desc = input(f'name: {new_srv_name} -> ip:port: {new_srv_addr} -> desc: ')
                if new_srv_desc == '':
                    select_server('')
                else:
                    with open(f'servers/{new_srv_name}.ini', 'w')as f:
                        json.dump({"address": new_srv_addr, "description": new_srv_desc}, f, indent=3)
                    with open('server.ini')as ffp:
                        ffp_str = ffp.read()
                    with open('server.ini', 'w')as ff:
                        ff.write(f"""{ffp_str}{new_srv_name}""")
                    select_server('')
    else:
        selected_server_opt(srv_list_[server_menu_index])


print('\r                                                                                      ', end='')

#os.system('clear')
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

release: v2.0.9 (beta)
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
            with open('data/user.json', 'w')as user_2:
                json.dump(newname, user_2, indent=3)
            with open('data/user.json')as wqyei:
                user_data = json.load(wqyei)
            break


if not '#' in user_data['data'][0]['name']:
    num39 = random.randint(1000, 9999)
    new_user_data = f"{user_data['data'][0]['name']}#{num39}"
    new_user_data = {"data":[{"name":new_user_data, "type": user_data['data'][0]['type']}]}
    with open('data/user.json', 'w')as user_2:
        json.dump(new_user_data, user_2, indent=3)
    with open('data/user.json')as wqyei:
        user_data = json.load(wqyei)
if str(user_data['data'][0]['name']).split('#')[1] == '':
    num39 = random.randint(1000, 9999)
    new_user_data = f"{user_data['data'][0]['name']}{num39}"
    new_user_data = {"data":[{"name":new_user_data, "type": user_data['data'][0]['type']}]}
    with open('data/user.json', 'w')as user_2:
        json.dump(new_user_data, user_2, indent=3)
    with open('data/user.json')as wqyei:
        user_data = json.load(wqyei)

print(copyright1+"\n"+"\n")
if user_data['data'][0]['type'] == 'new':
    newjson = {
        "data":[
            {
            "name": user_data['data'][0]['name'],
            "type": "normal"
            }
        ]
    }
    print('Hello There '+user_data['data'][0]['name']+' Welcome To UpBox-2.0.9 (beta)!'+'\n')
    with open('data/user.json', 'w')as user_1:
        json.dump(newjson, user_1, indent=4)
else:
    print('Welcome Back '+user_data['data'][0]['name']+'!')

for cx1 in range(len(module_l)):
    exec(module_l[cx1].split("':::'")[1])

print('\n')
print('Hit Enter To Continue.\n\n')
def start1():
    while True:
        input()
        break
start1()

sel_opt_str = ''


def menu1():
    os.system('clear')
    main_menu = TerminalMenu(str11, menu_highlight_style=(f"bg_{str(main_theme['theme'][0]['menu']['color']).lower()}",
    "fg_yellow"), clear_screen=True)
    option = main_menu.show()
    sel_option = str11[option]
    if option == None:
        menu1()
    elif str11[option] == 'select server':
        select_server(srv_list)
    elif str11[option] == 'select theme':
        select_theme()
    elif str11[option] == 'options':
        options_menu()
    else:
        for cx1 in range(len(module_l)):
            exec(module_l[cx1].split("':::'")[2])
menu1()