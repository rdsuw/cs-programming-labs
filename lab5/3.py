n = int(input())
if n < 0:
    raise ValueError('Число должно быть неотрицательным')

below = 0
equal = 0
upper = 0

for _ in range(n):

    t = float(input())
    
    if t < 0:
        below += 1
    elif t == 0:
        equal += 1
    else:
        upper += 1

print('Ниже нуля:', below)
print('Равны нулю:', equal)
print('Выше нуля:', upper)