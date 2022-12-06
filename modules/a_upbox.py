srv_joined = False

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

def get_color_escape(r, g, b, background=False):
    print(r, g, b, background)

def print_there(x, y, text):
    print(x, y, text)

def select_theme(number1):
    print(number1)

def join_srv(name1, address1):
    print(name1, address1)

def select_server():
    print()

def start1():
    print()

def menu1():
    print()

def add_menu_item(menu_name):
    print(menu_name)

def add_menu_sel(command):
    print(command)