def abb(a):
    a = a.split(' ')
    c = 0
    abb = ''
    for i in range(len(a)):
        b = a[0 + c]
        if len(b) >= 3:
            abb = abb + b[0]
        c = c + 1
    return abb.upper()
text = input('Введите текст: ')
print(abb(text))
    