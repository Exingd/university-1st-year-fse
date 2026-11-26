number = input('Введите номер карты: ')
def card(number):
    if len(number) == 15 and (number[0] == '3' and (number[1] == '4' or number[1] == '7')):
        return 'American Express'
    if len(number) == 16 and (number[0] == '5' and (number[1] == '1' or number[1] == '2' or number[1] == '3' or number[1] == '4' or number[1] == '5')):
        return 'Mastercard'
    if (len(number) == 13 or len(number) == 16) and (number[0] == '4'):
        return 'Visa'
    else: 
        return 'Invalid' 
print(card(number))
