a = int(input())
b = int(input())
c = int(input())

if (a <= 0 or b <= 0 or c <= 0) or\
    (a+b<c or a+c<b or b+c<a):
    print('Треугольник не существует')

if a == b == c:
    print('Равносторонний')
elif a == b and a!= c or\
    a == c and a!= b or\
    b == c and b!= a:
    print('Равнобедренный')
else:
    print('Разносторонний')