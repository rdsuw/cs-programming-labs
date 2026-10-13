n = int(input())
if n < 0:
    raise ValueError('Число должно быть неотрицательным')

while n > -1:
    print(n)
    n -= 1