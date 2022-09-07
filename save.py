import win32api
import pyautogui
import time
# import ctypes

VK_CODE = {'backspace': 0x08,
           'tab': 0x09,
           'clear': 0x0C,
           'enter': 0x0D,
           'shift': 0x10,
           'ctrl': 0x11,
           'alt': 0x12,
           'pause': 0x13,
           'caps_lock': 0x14,
           'esc': 0x1B,
           'spacebar': 0x20,
           'page_up': 0x21,
           'page_down': 0x22,
           'end': 0x23,
           'home': 0x24,
           'left_arrow': 0x25,
           'up_arrow': 0x26,
           'right_arrow': 0x27,
           'down_arrow': 0x28,
           'select': 0x29,
           'print': 0x2A,
           'execute': 0x2B,
           'print_screen': 0x2C,
           'ins': 0x2D,
           'del': 0x2E,
           'help': 0x2F,
           '0': 0x30,
           '1': 0x31,
           '2': 0x32,
           '3': 0x33,
           '4': 0x34,
           '5': 0x35,
           '6': 0x36,
           '7': 0x37,
           '8': 0x38,
           '9': 0x39,
           'a': 0x41,
           'b': 0x42,
           'c': 0x43,
           'd': 0x44,
           'e': 0x45,
           'f': 0x46,
           'g': 0x47,
           'h': 0x48,
           'i': 0x49,
           'j': 0x4A,
           'k': 0x4B,
           'l': 0x4C,
           'm': 0x4D,
           'n': 0x4E,
           'o': 0x4F,
           'p': 0x50,
           'q': 0x51,
           'r': 0x52,
           's': 0x53,
           't': 0x54,
           'u': 0x55,
           'v': 0x56,
           'w': 0x57,
           'x': 0x58,
           'y': 0x59,
           'z': 0x5A,
           'numpad_0': 0x60,
           'numpad_1': 0x61,
           'numpad_2': 0x62,
           'numpad_3': 0x63,
           'numpad_4': 0x64,
           'numpad_5': 0x65,
           'numpad_6': 0x66,
           'numpad_7': 0x67,
           'numpad_8': 0x68,
           'numpad_9': 0x69,
           'multiply_key': 0x6A,
           'add_key': 0x6B,
           'separator_key': 0x6C,
           'subtract_key': 0x6D,
           'decimal_key': 0x6E,
           'divide_key': 0x6F,
           'F1': 0x70,
           'F2': 0x71,
           'F3': 0x72,
           'F4': 0x73,
           'F5': 0x74,
           'F6': 0x75,
           'F7': 0x76,
           'F8': 0x77,
           'F9': 0x78,
           'F10': 0x79,
           'F11': 0x7A,
           'F12': 0x7B,
           'F13': 0x7C,
           'F14': 0x7D,
           'F15': 0x7E,
           'F16': 0x7F,
           'F17': 0x80,
           'F18': 0x81,
           'F19': 0x82,
           'F20': 0x83,
           'F21': 0x84,
           'F22': 0x85,
           'F23': 0x86,
           'F24': 0x87,
           'num_lock': 0x90,
           'scroll_lock': 0x91,
           'left_shift': 0xA0,
           'right_shift ': 0xA1,
           'left_control': 0xA2,
           'right_control': 0xA3,
           'left_menu': 0xA4,
           'right_menu': 0xA5,
           'browser_back': 0xA6,
           'browser_forward': 0xA7,
           'browser_refresh': 0xA8,
           'browser_stop': 0xA9,
           'browser_search': 0xAA,
           'browser_favorites': 0xAB,
           'browser_start_and_home': 0xAC,
           'volume_mute': 0xAD,
           'volume_Down': 0xAE,
           'volume_up': 0xAF,
           'next_track': 0xB0,
           'previous_track': 0xB1,
           'stop_media': 0xB2,
           'play/pause_media': 0xB3,
           'start_mail': 0xB4,
           'select_media': 0xB5,
           'start_application_1': 0xB6,
           'start_application_2': 0xB7,
           'attn_key': 0xF6,
           'crsel_key': 0xF7,
           'exsel_key': 0xF8,
           'play_key': 0xFA,
           'zoom_key': 0xFB,
           'clear_key': 0xFE,
           '+': 0xBB,
           ',': 0xBC,
           '-': 0xBD,
           '.': 0xBE,
           '/': 0xBF,
           ';': 0xBA,
           '[': 0xDB,
           '\\': 0xDC,
           ']': 0xDD,
           "'": 0xDE,
           '`': 0xC0}

inicio = time.time()  # Inicio tem o valor da era;

with open("Log de eventos.txt", "w") as arquivo:
    arquivo.write("\nimport pyautogui\n")
    arquivo.write("\n")
    arquivo.write("\nwhile True:\n""\n")


ativo = True
while ativo:
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    state_right = win32api.GetKeyState(0x02)
    state_zero = win32api.GetKeyState(VK_CODE['0'])
    state_one = win32api.GetKeyState(VK_CODE['1'])
    state_two = win32api.GetKeyState(VK_CODE['2'])
    state_three = win32api.GetKeyState(VK_CODE['3'])
    state_four = win32api.GetKeyState(VK_CODE['4'])
    state_five = win32api.GetKeyState(VK_CODE['5'])
    state_six = win32api.GetKeyState(VK_CODE['6'])
    state_seven = win32api.GetKeyState(VK_CODE['7'])
    state_eight = win32api.GetKeyState(VK_CODE['8'])
    state_nine = win32api.GetKeyState(VK_CODE['9'])
    state_numpad_0 = win32api.GetKeyState(VK_CODE['numpad_0'])
    state_numpad_1 = win32api.GetKeyState(VK_CODE['numpad_1'])
    state_numpad_2 = win32api.GetKeyState(VK_CODE['numpad_2'])
    state_numpad_3 = win32api.GetKeyState(VK_CODE['numpad_3'])
    state_numpad_4 = win32api.GetKeyState(VK_CODE['numpad_4'])
    state_numpad_5 = win32api.GetKeyState(VK_CODE['numpad_5'])
    state_numpad_6 = win32api.GetKeyState(VK_CODE['numpad_6'])
    state_numpad_7 = win32api.GetKeyState(VK_CODE['numpad_7'])
    state_numpad_8 = win32api.GetKeyState(VK_CODE['numpad_8'])
    state_numpad_9 = win32api.GetKeyState(VK_CODE['numpad_9'])
    state_enter = win32api.GetKeyState(VK_CODE['enter'])
    state_VK_LEFT = win32api.GetKeyState(VK_CODE['left_arrow'])
    state_VK_UP = win32api.GetKeyState(VK_CODE['up_arrow'])
    state_VK_RIGHT = win32api.GetKeyState(VK_CODE['right_arrow'])
    state_VK_DOWN = win32api.GetKeyState(VK_CODE['down_arrow'])
    state_ponto = win32api.GetKeyState(VK_CODE['.'])
    state_a = win32api.GetKeyState(VK_CODE['a'])
    state_b = win32api.GetKeyState(VK_CODE['b'])
    state_c = win32api.GetKeyState(VK_CODE['c'])
    state_d = win32api.GetKeyState(VK_CODE['d'])
    state_e = win32api.GetKeyState(VK_CODE['e'])
    state_f = win32api.GetKeyState(VK_CODE['f'])
    state_g = win32api.GetKeyState(VK_CODE['g'])
    state_h = win32api.GetKeyState(VK_CODE['h'])
    state_i = win32api.GetKeyState(VK_CODE['i'])
    state_j = win32api.GetKeyState(VK_CODE['j'])
    state_k = win32api.GetKeyState(VK_CODE['k'])
    state_l = win32api.GetKeyState(VK_CODE['l'])
    state_m = win32api.GetKeyState(VK_CODE['m'])
    state_n = win32api.GetKeyState(VK_CODE['n'])
    state_o = win32api.GetKeyState(VK_CODE['o'])
    state_p = win32api.GetKeyState(VK_CODE['p'])
    state_q = win32api.GetKeyState(VK_CODE['q'])
    state_r = win32api.GetKeyState(VK_CODE['r'])
    state_s = win32api.GetKeyState(VK_CODE['s'])
    state_t = win32api.GetKeyState(VK_CODE['t'])
    state_u = win32api.GetKeyState(VK_CODE['u'])
    state_v = win32api.GetKeyState(VK_CODE['v'])
    state_w = win32api.GetKeyState(VK_CODE['w'])
    state_x = win32api.GetKeyState(VK_CODE['x'])
    state_y = win32api.GetKeyState(VK_CODE['y'])
    state_z = win32api.GetKeyState(VK_CODE['z'])
    state_space = win32api.GetKeyState(VK_CODE['spacebar'])
    while True:

        click_left = win32api.GetKeyState(0x01)
        click_right = win32api.GetKeyState(0x02)
        zero = win32api.GetKeyState(VK_CODE['0'])
        one = win32api.GetKeyState(VK_CODE['1'])
        two = win32api.GetKeyState(VK_CODE['2'])
        three = win32api.GetKeyState(VK_CODE['3'])
        four = win32api.GetKeyState(VK_CODE['4'])
        five = win32api.GetKeyState(VK_CODE['5'])
        six = win32api.GetKeyState(VK_CODE['6'])
        seven = win32api.GetKeyState(VK_CODE['7'])
        eight = win32api.GetKeyState(VK_CODE['8'])
        nine = win32api.GetKeyState(VK_CODE['9'])
        numpad_0 = win32api.GetKeyState(VK_CODE['numpad_0'])
        numpad_1 = win32api.GetKeyState(VK_CODE['numpad_1'])
        numpad_2 = win32api.GetKeyState(VK_CODE['numpad_2'])
        numpad_3 = win32api.GetKeyState(VK_CODE['numpad_3'])
        numpad_4 = win32api.GetKeyState(VK_CODE['numpad_4'])
        numpad_5 = win32api.GetKeyState(VK_CODE['numpad_5'])
        numpad_6 = win32api.GetKeyState(VK_CODE['numpad_6'])
        numpad_7 = win32api.GetKeyState(VK_CODE['numpad_7'])
        numpad_8 = win32api.GetKeyState(VK_CODE['numpad_8'])
        numpad_9 = win32api.GetKeyState(VK_CODE['numpad_9'])
        enter = win32api.GetKeyState(VK_CODE['enter'])
        VK_LEFT = win32api.GetKeyState(VK_CODE['left_arrow'])
        VK_UP = win32api.GetKeyState(VK_CODE['up_arrow'])
        VK_RIGHT = win32api.GetKeyState(VK_CODE['right_arrow'])
        VK_DOWN = win32api.GetKeyState(VK_CODE['down_arrow'])
        ponto = win32api.GetKeyState(VK_CODE['.'])
        a = win32api.GetKeyState(VK_CODE['a'])
        b = win32api.GetKeyState(VK_CODE['b'])
        c = win32api.GetKeyState(VK_CODE['c'])
        d = win32api.GetKeyState(VK_CODE['d'])
        e = win32api.GetKeyState(VK_CODE['e'])
        f = win32api.GetKeyState(VK_CODE['f'])
        g = win32api.GetKeyState(VK_CODE['g'])
        h = win32api.GetKeyState(VK_CODE['h'])
        i = win32api.GetKeyState(VK_CODE['i'])
        j = win32api.GetKeyState(VK_CODE['j'])
        k = win32api.GetKeyState(VK_CODE['k'])
        l_ = win32api.GetKeyState(VK_CODE['l'])
        m = win32api.GetKeyState(VK_CODE['m'])
        n = win32api.GetKeyState(VK_CODE['n'])
        o = win32api.GetKeyState(VK_CODE['o'])
        p = win32api.GetKeyState(VK_CODE['p'])
        q = win32api.GetKeyState(VK_CODE['q'])
        r = win32api.GetKeyState(VK_CODE['r'])
        s = win32api.GetKeyState(VK_CODE['s'])
        t = win32api.GetKeyState(VK_CODE['t'])
        u = win32api.GetKeyState(VK_CODE['u'])
        v = win32api.GetKeyState(VK_CODE['v'])
        w = win32api.GetKeyState(VK_CODE['w'])
        x = win32api.GetKeyState(VK_CODE['x'])
        y = win32api.GetKeyState(VK_CODE['y'])
        z = win32api.GetKeyState(VK_CODE['z'])
        space = win32api.GetKeyState(VK_CODE['spacebar'])

        if click_left != state_left:
            state_left = click_left
            x, y = pyautogui.position()
            if click_left < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = 'pyautogui.moveTo(' + str(x).rjust(4) + ',' + str(y).rjust(4) + ', ' + str(tempo) + ')\n'
                lines = ['    ', positionStr, '    pyautogui.click()\n\n']
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif click_right != state_right:
            state_right = click_right
            x, y = pyautogui.position()
            if click_right < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = 'pyautogui.moveTo(' + str(x).rjust(4) + ',' + str(y).rjust(4) + ', ' + str(tempo) + ')\n'
                lines = ["    ", positionStr, "    pyautogui.click(button='right')\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif zero != state_zero:
            state_zero = zero
            if zero < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('0', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif one != state_one:
            state_one = one
            if one < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('1', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif two != state_two:
            state_two = two
            if two < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('2', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif three != state_three:
            state_three = three
            if three < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('3', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif four != state_four:
            state_four = four
            if four < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('4', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif five != state_five:
            state_five = five
            if five < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('5', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif six != state_six:
            state_six = six
            if six < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('6', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif seven != state_seven:
            state_seven = seven
            if seven < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('7', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif eight != state_eight:
            state_eight = eight
            if eight < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('8', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif nine != state_nine:
            state_nine = nine
            if nine < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('9', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif numpad_0 != state_numpad_0:
            state_numpad_0 = numpad_0
            if numpad_0 < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('0', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif numpad_1 != state_numpad_1:
            state_numpad_1 = numpad_1
            if numpad_1 < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('1', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif numpad_2 != state_numpad_2:
            state_numpad_2 = numpad_2
            if numpad_2 < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('2', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif numpad_3 != state_numpad_3:
            state_numpad_3 = numpad_3
            if numpad_3 < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('3', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif numpad_4 != state_numpad_4:
            state_numpad_4 = numpad_4
            if numpad_4 < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('4', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif numpad_5 != state_numpad_5:
            state_numpad_5 = numpad_5
            if numpad_5 < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('5', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif numpad_6 != state_numpad_6:
            state_numpad_6 = numpad_6
            if numpad_6 < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('6', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif numpad_7 != state_numpad_7:
            state_numpad_7 = numpad_7
            if numpad_7 < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('7', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif numpad_8 != state_numpad_8:
            state_numpad_8 = numpad_8
            if numpad_8 < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('8', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif numpad_9 != state_numpad_9:
            state_numpad_9 = numpad_9
            if numpad_9 < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('9', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif VK_LEFT != state_VK_LEFT:
            state_VK_LEFT = VK_LEFT
            if VK_LEFT < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('left', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif VK_UP != state_VK_UP:
            state_VK_UP = VK_UP
            if VK_UP < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('up', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif VK_RIGHT != state_VK_RIGHT:
            state_VK_RIGHT = VK_RIGHT
            if VK_RIGHT < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('right', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif VK_DOWN != state_VK_DOWN:
            state_VK_DOWN = VK_DOWN
            if VK_DOWN < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('down', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif a != state_a:
            state_a = a
            if a < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('a', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif b != state_b:
            state_b = b
            if b < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('b', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif c != state_c:
            state_c = c
            if c < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('c', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif d != state_d:
            state_d = d
            if d < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('d', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif e != state_e:
            state_e = e
            if e < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('e', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif f != state_f:
            state_f = f
            if f < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('f', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif g != state_g:
            state_g = g
            if g < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('g', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif h != state_h:
            state_h = h
            if h < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('h', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif i != state_i:
            state_i = i
            if i < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('i', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif j != state_j:
            state_j = j
            if j < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('j', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif k != state_k:
            state_k = k
            if k < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('k', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif l_ != state_l:
            state_l = l_
            if l_ < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('l', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif m != state_m:
            state_m = m
            if m < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('m', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif n != state_n:
            state_n = n
            if n < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('n', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif o != state_o:
            state_o = o
            if o < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('o', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif p != state_p:
            state_p = p
            if p < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('p', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif q != state_q:
            state_q = q
            if q < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('q', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif r != state_r:
            state_r = r
            if r < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('r', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif s != state_s:
            state_s = s
            if s < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('s', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif t != state_t:
            state_t = t
            if t < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('t', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif u != state_u:
            state_u = u
            if u < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('u', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif v != state_v:
            state_v = v
            if v < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('v', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif w != state_w:
            state_w = w
            if w < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('w', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif x != state_x:
            state_x = x
            if x < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('x', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif y != state_y:
            state_y = y
            if y < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('y', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif z != state_z:
            state_z = z
            if z < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write('z', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))

        elif space != state_space:
            state_space = space
            if space < 0:
                step = time.time()
                tempo = step - inicio
                inicio = time.time()
                positionStr = "pyautogui.write(' ', interval = " + str(tempo)
                lines = ["    ", positionStr, "\n"]
                print(''.join(lines))
                with open("Log de eventos.txt", "a") as arquivo:
                    arquivo.write(''.join(lines))
