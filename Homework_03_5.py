# Задание 5.
quit = False
total_summ = 0


def sum_str():
    global quit
    str = input("Введите числа через пробел. Для завершения ввода введите q: ")

    if str == []:
        """ Проверка на пустую строку"""
        sum_str = 0
        return sum_str
    else:
        """ Вычисление последнего символа"""
        last_symbol = str[len(str) - 1]

        if last_symbol == 'q':
            quit = True
            str = str[0:len(str) - 2]

        str = str.split()
        x_numbers = []

        """ Перевод строки в числа"""
        for i in range(len(str)):
            x_numbers.append(float(str[i]))

        sum_str = sum(x_numbers)
        return sum_str


while quit == False:
    total_summ = total_summ + sum_str()
    print(f"Общая сумма равна: {total_summ}")
