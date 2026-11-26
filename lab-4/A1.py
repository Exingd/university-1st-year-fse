import random
import time
N = int(input('Введите количество примеров: '))
for i in range(N):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    start_time = time.time()
    c = int(input(f"{a} x {b} = "))
    time_spend = time.time() - start_time
    if c == a * b:
        print('Правильно! Время: ', f"{time_spend:.2f}", ' секунд')
    else:
        print('Неправильно! Правильно: ', a * b)
    

    