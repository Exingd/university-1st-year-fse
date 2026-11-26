password = input('Введите пароль: ')
s = '*-#'
x = 0
import string
if not len(password) == 8:
    print('Длина пароля не равна 8')
    x = 1
if password == password.lower():
    print('В пароле отсутствуют заглавные буквы')
    x = 1
if not any(symbol.isdigit() for symbol in password):
    print('В пароле отсутствуют цифры')
    x = 1
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
if not all(symbol in allowed for symbol in password):
    print ('В пароле используются непредусмотренные символы')
    x = 1
if not any(symbol in s for symbol in password):
    print('В пароле отсутствуют специальные символы')
    x = 1
if password == password.upper():
    print('В пароле отсутствуют строчные буквы')
    x = 1
if not x == 1:
    print('Пароль надежный')