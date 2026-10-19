f = str(input('Введите фигуру (прямоугольник, рамка, правый треугольник): '))
n = int(input('Введите первое измерение: '))
if f.lower() == 'рамка' or f.lower() == 'прямоугольник':
    m = int(input('Введите второе измерение: '))
    print(f, n, 'x', m)
    h = '#' * m
if f.lower() == 'правый треугольник':
    print('Правый треугольник, количество строк: ', n)
y = 1
if f.lower() == 'прямоугольник':
    for i in range(n):
        print('#' * m)
if f.lower() == 'рамка':
    print(h)
    for i in range(n - 2):
        print('#', ' ' * (len(h) - 4), '#')
    print('#' * m) 
if f.lower() == 'правый треугольник':
    for i in range(n):
        print('#' * y)
        y = y + 1
