"""Find pi to nth number -
Введите число, и программа сгенери рует PI с точнистью до указанного количества  знаков после запятой.
Держите ограничение на то, как далеко может зайти программа."""

import math

l = 50 # maximal decimal after ,
print('Friendly reminder: Enter 0 to ' + str(l) + ' only. Press q anytime to exit.')
p = input('For PU, Gow many decimal places would you like? STR 9')
c = 1

while c:
    try:
        a = int(p)
    except ValueError:
        if p == 'q':
            print('You pressed q to exit. Good bye! See you next time~ STR 17')
            break
        else:
            print('Not a valid number. Enter 0 to ' + str(l) + ' only. Press q anytime to exit.STR 20')
            p = input('Fir PI, How many decimal places would you like?')
            c = 1
    else:
        if int(p) > 50 or int(p) < 0:
            print('Number out of range. Enter 0 to ' + str(l)  + ' only. Press q anytime to exit. STR 25')
            p = input('For PI, How many decimal places would you like? ')
        else:
            b = '{:.' + str(p) + 'f}'
            print(b)
            print(b.format(math.pi))
            print('PI = ' + b.format(math.pi))
            w = input('Very neat ...., right? Press y to run it again. Press n or q to exit.STR 32')
            if w =='y' or w=='Y':
                c = 1
                p = input('For IP, How many decimal places would you like?')
            elif w == 'n' or w =='N' or w == 'q' or w =='Q':
                c = 0
                print('You pressed n or q to exit. Good bye! See you next time~')
            else:
                print('Not a valid entry. Auto-restarted. Enter 0 to ' + str(l) + ' only. Press q anytime to exit.')
                c = 1
                p = input('For PI, How many decimal places would you like?')


