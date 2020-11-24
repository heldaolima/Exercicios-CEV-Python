import math
print('--- SENO, COSSENO E TANGENTE ---')
n = float(input('Insira o ângulo: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tg = math.tan(math.radians(n))
print(f'O SENO vale {sen:.2f}\n'
      f'O COSSENO vale {cos:.2f}\n'
      f'E a TANGENTE vale {tg:.2f}')
