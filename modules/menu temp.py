#on startup
item1_list = ["test", "test2"]
add_menu_item('test')
def menu_test1():
    pyautogui.keyUp('enter')
    subprocess.call('cls', shell=True)
    for cxld1 in range(len(item1_list)):
        print(item1_list[cxld1])
    num1 = 1
    num2 = 2
    print_there(num1, 16, '<')
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
            sel_menuitem = num3
            sel_menuitem_ = int(sel_menuitem) -1
            sel_menuitem = item1_list[sel_menuitem_]
            sel_menuitem = sel_menuitem.replace('\n', '')
            sel_menuitem1 = sel_menuitem
            print_there(sel_menuitem_+1, 17, sel_menuitem1)
        elif kb.is_pressed('Esc'):
                menu1()

':::' #once it started


':::' #on menu selection
if sel_opt_str == 'test':
    menu_test1()

':::' #once joined server

':::' #once message sent