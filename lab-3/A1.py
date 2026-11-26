x1 = int(input('Введите координату x1: '))
y1 = int(input('Введите координаут y1: '))
x2 = int(input('Введите координату x2: '))
y2 = int(input('Введите координаут y2: '))
if x1 > 0 and y1 > 0 and x2 >0 and y2 > 0:
    print('Да, I четверть')
elif x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0:
    print('Да, II четверть')
elif x1 < 0 and x2 < 0 and y1 < 0 and y2 < 0:
    print('Да, III четверть')
elif x1 > 0 and x2 > 0 and y1 < 0 and y2 < 0:
    print('Да, IV четверть')
else:
    print('NO')