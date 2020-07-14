# Задание 4.

def my_func(x, y):
    z = 1
    for i in range(0, -y):
        z = z * x
    return 1 / z


my_func_2 = lambda x, y: x ** y

while True:
    x = float(input("Веведите положительное вещественное число: "))
    if x <= 0:
        print("Это не положительное число. Пожалуйста повторите попытку.")
    else:
        break
while True:
    y = int(input("Введите целое отрицательное число: "))
    if y >= 0:
        print("Это не отрицательное число. Пожалуйста повторите попытку")
    else:
        break

print(my_func(x, y))
print(my_func_2(x, y))
