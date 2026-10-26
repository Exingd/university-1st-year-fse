def remove_text(a):
    while '(' in a:
        pos_1 = a.find('(')
        pos_2 = a.find(')')
        if pos_1 < pos_2:
            a = a.replace(a[pos_1:pos_2 + 1], " ")
        else:
            break
    return a
text = input('Наберите текст: ')
print(remove_text(text))