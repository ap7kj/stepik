// step 1 //
Что покажет приведенный ниже фрагмент кода?
s = 'abcdefg'
print(s[0] + s[2] + s[4] + s[6])
--- aceg ---

// step 2 //
Что покажет приведенный ниже фрагмент кода?
s = 'abcdefg'
print(s[0]*3 + s[-1]*3 + s[3]*2 + s[3]*2)
--- aaagggdddd ---

// step 3 //
Что покажет приведенный ниже фрагмент кода?
s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')
--- 051217 ---

// step 4 //
Дополните приведенный код, используя индексатор, так чтобы он вывел символ запятой.
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])

// step 5 //
Дополните приведенный код, используя индексатор, так чтобы он вывел символ w.
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-10])

// step 6 //
На вход программе подается одна строка. Напишите программу, которая выводит элементы строки с индексами 0, 2, 4, ... в столбик.
string = input()
for i in range(0, len(string), 2):
    print(string[i])

// step 7 //
На вход программе подается одна строка. Напишите программу, которая выводит в столбик элементы строки в обратном порядке.
string = input()[::-1]
for i in string:
    print(i)

// step 8 //
На вход программе подаются три строки: имя, фамилия и отчество. Напишите программу, которая выводит инициалы человека.
name, surname, patronymic = input(), input(), input()
print(surname[0] + name[0] + patronymic[0])

// step 9 //
На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.
number = int(input())
total = 0
while number:
    last_digit = number % 10
    total += last_digit
    number //= 10

print(total)

// step 10 //
На вход программе подается одна строка. Напишите программу, которая выводит сообщение «Цифра» (без кавычек), если строка содержит цифру. В противном случае вывести сообщение «Цифр нет» (без кавычек).
numbers = '0123456789'
string = input()
flag = False
for i in string:
    if i in numbers:
        flag = True
        break
if flag == True:
    print('Цифра')
else:
    print('Цифр нет')

// step 11 //
На вход программе подается одна строка. Напишите программу, которая определяет сколько раз в строке встречаются символы + и *
counter_star, counter_plus = 0, 0
string = input()
for i in string:
    if i in '*':
        counter_star += 1
    elif i in '+':
        counter_plus += 1
print(f'Символ + встречается {counter_plus} раз')
print(f'Символ * встречается {counter_star} раз')

// step 12 //
На вход программе подается одна строка. Напишите программу, которая определяет сколько в ней одинаковых соседних символов.
string = input()
counter = 0
for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        counter += 1
print(counter)

// step 13 //
На вход программе подается одна строка с буквами русского языка. Напишите программу, которая определяет количество гласных и согласных букв.
vowels = 'бвгджзйклмнпрстфхцчшщ'
consonants = 'ауоыиэяюёе'
counter_vowels = 0
counter_consonants = 0
string = input().lower()
for i in string:
    if i in vowels:
        counter_vowels += 1
    if i in consonants:
        counter_consonants += 1
print(f'Количество гласных букв равно {counter_consonants}')
print(f'Количество согласных букв равно {counter_vowels}')

// step 14 //
На вход программе подается натуральное число, записанное в десятичной системе счисления. Напишите программу, которая переводит данное число в двоичную систему счисления.
number = int(input())
s = ''
while number:
    s = str(number % 2) + s
    number //= 2
print(s)