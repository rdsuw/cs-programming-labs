price = float(input())
age = int(input())

if price <= 0 or age < 0 or age > 120:
    print('Ошибка')
else:
    if 0 <= age <= 5:
        print(f'Стоимость: {price * 0:.2f}')
    elif 6 <= age <= 17:
        print(f'Стоимость: {price * 0.5:.2f}')
    elif 18 <= age <= 59:
        print(f'Стоимость: {price:.2f}')
    else:
        print(f'Стоимость: {price * 0.7:.2f}')