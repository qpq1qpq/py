all_price = 0
quan = int(input('Введите количество билетов: '))
if quan == 0:
    quan = int(input('Введите введите целое чилсло: '))
for i in range(quan):
    i += 1
    if quan != 0:
        age_tick = int(input(f'Для какого возраста билет №{i} '))
        if age_tick < 18:
            print('Билет бесплатный')
        if 18 <= age_tick < 25: 
            print('Стоимость билета 990')
            all_price += 990
        if 25 <= age_tick:
            print('Стоимость билета 1390')
            all_price += 1390
        if age_tick == 0:
            print('Введите целое число!')
            continue
if 3 < i:
    sell = (all_price / 100) * 10
    all_price -= sell
print('Сумма к олате: ', all_price)

