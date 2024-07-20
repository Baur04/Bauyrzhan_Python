value = input("Введите значение: ")

if value.isdigit():
    value = int(value)
    if value > 7:
        print('Привет')
    else:
        print('Введите число больше 7')

elif value == 'Вячеслав':
    print('Привет,', value)
else:
    print('Нет такого имени')

def test (list):
    res = []
    for i in list:
        if i % 3 == 0:
            res.append(i)

    print('Числа, кратные 3: ', res)

array = [3, 17, 5, 22, 87, 6, 27]
test(array)
