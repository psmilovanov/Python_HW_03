# Задание 3.


def my_func(x_1, x_2, x_3):
    x = [x_1, x_2, x_3]
    x.sort()
    x.reverse()
    return x[0] + x[1]


print(my_func(12, 6, 8))
