# Задание 1.

def division(a, b):
    try:
        return a / b
    except:
        print("ZeroDivisionError. На ноль делить нельзя")


print(division(2, 6))
