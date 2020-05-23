import os
import time

print('Por favor, digite abaixo os valores da equação.')

a = str(input('\nValor de A: '))
b = str(input('Valor de B: '))
c = str(input('Valor de C: '))

print('\nAguarde um instante...')
time.sleep(1)
os.system('cls || clear')

print('='*50 + '\n' + f'{"Resolução":^50}' + '\n' + '='*50)


def print_equacao(a, b, c):

    if int(b) < 0:
        bn = b[1]
        vb = f' - {bn}x'
    else:
        vb = f' + {b}x'

    if int(c) < 0:
        cn = c[1]
        vc = f' - {cn}x'
    else:
        vc = f' + {c}x'
    if b == 0:
        vb = ''
    if c == 0:
        vc = ''

    print(f'Equação = {a}x²{vb}{vc} = 0')
    
print_equacao(a, b, c)
a = int(a)
b = int(b)
c = int(c)

delta = (b*b) - 4 * a * c
print(f'\n∆ = {delta}')

if delta < 0:
    print('\n\nDelta é menor que zero. Esta equação não tem x1/x2.')
else:
    x1 = (-b + (delta ** 0.5)) / (2*a)
    x2 = (-b - (delta ** 0.5)) / (2*a)

    if x1 > 0:
        x1 = int(x1)
    else:
        if (-b + (delta ** 0.5)) % (2*a) == 0:
            x1 = int(x1)
        else:
            x1 = f'{x1:.1f}'


    if x2 > 0:
        x2 = int(x2)
    else:
        if (-b - (delta ** 0.5)) % (2*a) == 0:
            x2 = int(x2)
        else:
            x2 = f'{x2:.1f}'

    print(f'\nX1 => {x1}')

    print(f'X2 => {x2}')