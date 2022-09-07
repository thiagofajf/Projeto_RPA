import win32api
import pyautogui
import ctypes
import time

inicio = time.time()  # Inicio tem o valor da era;

with open("Log de eventos.txt", "w") as arquivo:
    arquivo.write("\nimport pyautogui\n")
    arquivo.write("\n")
    arquivo.write("\nwhile True:\n""\n")


ativo = True
while ativo:
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    state_right = win32api.GetKeyState(0x02)
    state_zero = win32api.GetKeyState(0x30)
    state_one = win32api.GetKeyState(0x31)
    state_two = win32api.GetKeyState(0x32)
    state_three = win32api.GetKeyState(0x33)
    state_four = win32api.GetKeyState(0x34)
    state_five = win32api.GetKeyState(0x35)
    state_six = win32api.GetKeyState(0x36)
    state_seven = win32api.GetKeyState(0x37)
    state_eight = win32api.GetKeyState(0x38)
    state_nine = win32api.GetKeyState(0x39)
    state_enter = win32api.GetKeyState(0x0D)
    state_Q = win32api.GetKeyState(0x51)
    state_VK_LEFT = win32api.GetKeyState(0x25)
    state_VK_UP = win32api.GetKeyState(0x26)
    state_VK_RIGHT = win32api.GetKeyState(0x27)
    state_VK_DOWN = win32api.GetKeyState(0x28)
    state_ponto = win32api.GetKeyState(0xBE)
    state_a = win32api.GetKeyState(0x41)
    state_b = win32api.GetKeyState(0x42)
    state_c = win32api.GetKeyState(0x43)
    state_d = win32api.GetKeyState(0x44)
    state_e = win32api.GetKeyState(0x45)
    state_f = win32api.GetKeyState(0x46)
    state_g = win32api.GetKeyState(0x47)
    state_h = win32api.GetKeyState(0x48)
    state_i = win32api.GetKeyState(0x49)
    state_j = win32api.GetKeyState(0x4A)
    state_k = win32api.GetKeyState(0x4B)
    state_l = win32api.GetKeyState(0x4C)
    state_m = win32api.GetKeyState(0x4D)
    state_n = win32api.GetKeyState(0x4E)
    state_o = win32api.GetKeyState(0x4F)
    state_p = win32api.GetKeyState(0x50)
    state_q = win32api.GetKeyState(0x51)
    state_r = win32api.GetKeyState(0x52)
    state_s = win32api.GetKeyState(0x53)
    state_t = win32api.GetKeyState(0x54)
    state_u = win32api.GetKeyState(0x55)
    state_v = win32api.GetKeyState(0x56)
    state_w = win32api.GetKeyState(0x57)
    state_x = win32api.GetKeyState(0x58)
    state_y = win32api.GetKeyState(0x59)
    state_z = win32api.GetKeyState(0x5A)
    state_space = win32api.GetKeyState(0x20)
    while True:

        click_left = win32api.GetKeyState(0x01)
        click_right = win32api.GetKeyState(0x02)
        zero = win32api.GetKeyState(0x30)
        one = win32api.GetKeyState(0x31)
        two = win32api.GetKeyState(0x32)
        three = win32api.GetKeyState(0x33)
        four = win32api.GetKeyState(0x34)
        five = win32api.GetKeyState(0x35)
        six = win32api.GetKeyState(0x36)
        seven = win32api.GetKeyState(0x37)
        eight = win32api.GetKeyState(0x38)
        nine = win32api.GetKeyState(0x39)
        Enter = win32api.GetKeyState(0x0D)
        Q = win32api.GetKeyState(0x51)
        VK_LEFT = win32api.GetKeyState(0x25)
        VK_UP = win32api.GetKeyState(0x26)
        VK_RIGHT = win32api.GetKeyState(0x27)
        VK_DOWN = win32api.GetKeyState(0x28)
        ponto = win32api.GetKeyState(0xBE)
        a = win32api.GetKeyState(0x41)
        b = win32api.GetKeyState(0x42)
        c = win32api.GetKeyState(0x43)
        d = win32api.GetKeyState(0x44)
        e = win32api.GetKeyState(0x45)
        f = win32api.GetKeyState(0x46)
        g = win32api.GetKeyState(0x47)
        h = win32api.GetKeyState(0x48)
        i = win32api.GetKeyState(0x49)
        j = win32api.GetKeyState(0x4A)
        k = win32api.GetKeyState(0x4B)
        l = win32api.GetKeyState(0x4C)
        m = win32api.GetKeyState(0x4D)
        n = win32api.GetKeyState(0x4E)
        o = win32api.GetKeyState(0x4F)
        p = win32api.GetKeyState(0x50)
        q = win32api.GetKeyState(0x51)
        r = win32api.GetKeyState(0x52)
        s = win32api.GetKeyState(0x53)
        t = win32api.GetKeyState(0x54)
        u = win32api.GetKeyState(0x55)
        v = win32api.GetKeyState(0x56)
        w = win32api.GetKeyState(0x57)
        x = win32api.GetKeyState(0x58)
        y = win32api.GetKeyState(0x59)
        z = win32api.GetKeyState(0x5A)
        space = win32api.GetKeyState(0x20)

        if click_left != state_left:
            state_left = click_left
            x, y = pyautogui.position()
            if click_left < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                positionStr = 'pyautogui.moveTo(' + str(x).rjust(4) + ',' + str(y).rjust(4) + ', ' + str(tempo) + ')\n'
                lines = ['    ', positionStr, '    pyautogui.click()\n\n']
                print(''.join(lines))

                # return 'VK_LBUTTON' #O return fica muito bugado no Main. Não pega as teclas direito.
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write(''.join(lines))

        elif click_right != state_right:
            state_right = click_right
            x, y = pyautogui.position()
            if click_right < 0:
                click_right_time = time.time()
                tempo = click_right_time - inicio
                inicio = time.time()
                positionStr = 'pyautogui.moveTo(' + str(x).rjust(4) + ',' + str(y).rjust(4) + ', ' + str(tempo) + ')\n'
                #print(positionStr, end='')
                lines = ["    ", positionStr, "    pyautogui.click(button='right')\n\n"]
                print(''.join(lines))
                # return 'VK_RBUTTON'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write(''.join(lines))

        elif zero != state_zero:
            if zero < 0:
                state_zero = zero
                zero_time = time.time()
                tempo = zero_time - inicio
                inicio = time.time()
                print("0")
                positionStr = "pyautogui.write('0', interval = " + str(tempo) + ")\n"
                print(positionStr, end='')
                lines = ["    ", positionStr, "    pyautogui.click(button='right')\n\n"]
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('0', interval = tempo)\n")

        elif one != state_one:
            state_one = one
            if one < 0:
                print('1')
                # return '1'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('1')\n")

        elif two != state_two:
            state_two = two
            if two < 0:
                print('2')
                # return '2'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('2')\n")

        elif three != state_three:
            state_three = three
            if three < 0:
                print('3')
                # return '3'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('3')\n")

        elif four != state_four:
            state_four = four
            if four < 0:
                print('4')
                # return '4'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('4')\n")

        elif five != state_five:
            state_five = five
            if five < 0:
                print('5')
                # return '5'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('5')\n")

        elif six != state_six:
            state_six = six
            if six < 0:
                print('6')
                # return '6'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('6')\n")

        elif seven != state_seven:
            state_seven = seven
            if seven < 0:
                print('7')
                # return '7'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('7')\n")

        elif eight != state_eight:
            state_eight = eight
            if eight < 0:
                print('8')
                # return '8'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('8')\n")

        elif nine != state_nine:
            state_nine = nine
            if nine < 0:
                print('9')
                # return '9'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('9')\n")

        elif Enter != state_enter:
            state_enter = Enter
            if Enter < 0:
                print("'\n enter'")
                # return 'enter'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    time.sleep(3)\n")
                    arquivo.write("    pyautogui.press('enter')\n")
                    arquivo.write("    time.sleep(3)\n")

        elif Q != state_Q:
            state_Q = Q
            if Q < 0:
                ativo = False
                print("'\n Q'")
                ctypes.windll.user32.MessageBoxW(0, "Finalizado", "Lupa Automação", 1)

        elif VK_LEFT != state_VK_LEFT:
            state_VK_LEFT = VK_LEFT
            if VK_LEFT < 0:
                print("'\n VK_LEFT'")
                # return 'enter'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('left')\n")

        elif VK_UP != state_VK_UP:
            state_VK_UP = VK_UP
            if VK_UP < 0:
                print("'\n VK_UP'")
                # return 'enter'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('up')\n")

        elif VK_RIGHT != state_VK_RIGHT:
            state_VK_RIGHT = VK_RIGHT
            if VK_RIGHT < 0:
                print("'\n VK_RIGHT'")
                # return 'enter'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('right')\n")

        elif VK_DOWN != state_VK_DOWN:
            state_VK_DOWN = VK_DOWN
            if VK_DOWN < 0:
                print("'\n VK_DOWN'")
                # return 'enter'
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('down')\n")

        elif a != state_a:
            state_a = a
            if a < 0:
                print("'a'")
                # return 'enter'
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('a')\n")

        elif b != state_b:
            state_b = b
            if b < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('b')\n")

        elif c != state_c:
            state_c = c
            if c < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('c')\n")

        elif d != state_d:
            state_d = d
            if d < 0:
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('d')\n")

        elif e != state_e:
            state_e = e
            if e < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('e')\n")

        elif f != state_f:
            state_f = f
            if f < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('f')\n")

        elif g != state_g:
            state_g = g
            if g < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('g')\n")

        elif h != state_h:
            state_h = h
            if h < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('h')\n")

        elif i != state_i:
            state_i = i
            if i < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('i')\n")

        elif j != state_j:
            state_j = j
            if j < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('j')\n")

        elif k != state_k:
            state_k = k
            if k < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('k')\n")

        elif l != state_l:
            state_l = l
            if l < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('l')\n")

        elif m != state_m:
            state_m = m
            if m < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('m')\n")

        elif n != state_n:
            state_n = n
            if n < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('n')\n")

        elif o != state_o:
            state_o = o
            if o < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('o')\n")

        elif p != state_p:
            state_p = p
            if p < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('p')\n")

        elif q != state_q:
            state_q = q
            if q < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('q')\n")

        elif r != state_r:
            state_r = r
            if r < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('r')\n")

        elif s != state_s:
            state_s = s
            if s < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('s')\n")

        elif t != state_t:
            state_t = t
            if t < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('t')\n")

        elif u != state_u:
            state_u = u
            if u < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('u')\n")

        elif v != state_v:
            state_v = v
            if v < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('v')\n")

        elif w != state_w:
            state_w = w
            if w < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('w')\n")

        elif x != state_x:
            state_x = x
            if x < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('x')\n")

        elif y != state_y:
            state_y = y
            if y < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('y')\n")

        elif z != state_z:
            state_z = z
            if z < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write('z')\n")

        elif space != state_space:
            state_space = space
            if space < 0:
                click_left_time = time.time()
                tempo = click_left_time - inicio
                inicio = time.time()
                with open("Log de eventos.txt", "a") as arquivo:  # adiciona uma informação ao texto original
                    arquivo.write("    pyautogui.write(' ')\n")
