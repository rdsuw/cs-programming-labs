a = input()
len = len(a)

if '-' in a:
    df = True
else:
    df = False

print('Длина:', len)
print('Только буквы:', a.isalpha())
print('Только цифры:', a.isdigit())
print('Буквенно-цифровая:', a.isalnum())
print('Содержит дефис:', df)