# 5

len_km = float(input())
rash_topl = float(input())
pay_litr = float(input())

a = (len_km*rash_topl)/100
b = a*pay_litr

print(f'Топливо: {a:.2f} л')
print(f'Стоимость: {b:.2f} руб')