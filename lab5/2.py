a = int(input())
b = int(input())

if a > b:
    raise ValueError('a должно быть меньше или равно b')

sum = 0
multipl = 1

for i in range(a, b+1):
    sum += i
    multipl *= i

print('Сумма:', sum)
print('Произведение:', multipl)