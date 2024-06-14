import time as t
print('======DESAFIO 03======')
print('Calculadora de soma em python, adicional...')
n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
r = int(n1 + n2)
print('Carregando...')
t.sleep(3)
print('A soma entre {} e {} é {}'.format(n1, n2, r))
