from random import *
digits =  '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
symb = 'il1Lo0O'
chars = ''
kw_pass = int(input('Укажите количество паролей для генерации: '))
len_pass = int(input('Укажине длинну одного пароля: '))
num_mb =  input('Включать ли цифры 0123456789? (да/нет):')
Abc = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет): ')
abc = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет): ')
symbols = input('Включать ли символы !#$%&*+-=?@^_? (да/нет): ')
dels = input('Исключать ли неоднозначные символы il1Lo0O? (да/нет): ')
if num_mb=='да':
    chars+=num_mb
if Abc=='да':
    chars+=Abc
if abc=='да':
    chars+=abc
if symbols=='да':
    chars+=symbols
if dels=='да':
    for i in symb:
        chars = chars.replace(i, '')
def generate_password(len_pass, chars):
    password = ''
    for j in range(len_pass):
        password += random.choice(chars)
    return password
for _ in range(n):
    generate_password(len_pass, chars)