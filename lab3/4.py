a = input().split(';')

train = a[0]
route = a[1] + ' - ' + a[2]
depart = a[3]
price = float(a[4])


print('Поезд:', train)
print('Маршрут:', route)
print('Отправление:', depart)
print(f'Цена: {price:.2f} руб')