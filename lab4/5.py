a = int(input())
if a not in range(1, 9999+1):
    raise ValueError('Ошибка')

if a % 400 == 0 or\
a % 4 == 0 and a % 100 != 0:
    print('Високосный')
else:
    print('Невисокосный')