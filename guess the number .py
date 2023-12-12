from random import *
c = random.randint(1,100)

print('Добро пожаловать в \"угадай число\"')
def is_valid(s):
    if s.isdigit() and 1 <= int(s) <= 100:
        if int(s) < c:
            return 'Ваше число меньше загаданного, попробуйте ещё раз'
        elif int(s) > c:
            return 'Ваше число больше загаданного, попробуйте ещё раз'
        elif int(s) == c:
            return 'Вы угадали, поздравляем!'
        else:
            return 'Нужно ввести число от 1 до 100!'
s = input()
print(is_valid(s))
while is_valid(s) != 'Вы угадали, поздравляем!':
    s = input()
    print(is_valid(s))
print('Спасибо, что играли в \"угадай число\". Eщё увидимся...')