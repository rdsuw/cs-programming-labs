a = input()
len = len(a)

print('Длина:', len)
print('Только буквы:', a.isalpha())
print('Только цифры:', a.isdigit())
print('Буквенно-цифровая:', a.isalnum())
print('Содержит дефис:', '-' in a)