import re
def split_str(a):
    b = a.replace(' ', '')
    b = re.split(r'(?<=[.?!])', b)
    c = 0
    for  i in range(len(b)):
        print(b[0 + c])
        c = c + 1
    return c - 1
text = input('Введите текст: ')
print('Количество предложений:', split_str(text))