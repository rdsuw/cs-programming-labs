# 4

time_all = int(input())
hours = time_all//3600
minutes = (time_all%3600)//60
seconds = (time_all%3600)%60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')