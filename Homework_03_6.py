# Задание 6.

error_mark = False


def inc_func(word):
    global error_mark
    if word.islower() == False:
        error_mark = True
        print("Не удовлетворяет правилу ввода. Все буквы в слове должны быть маленькими")
        return ''
    else:
        return word.title()


Req_str = ''
user_str = input("Введите слова маленькими латинскими буквами через пробел: ")
user_str = user_str.split()

for i in range(len(user_str)):
    Req_str = Req_str + inc_func(user_str[i]) + ' '
    if error_mark == True:
        Req_str = ''
        break

print(Req_str)
