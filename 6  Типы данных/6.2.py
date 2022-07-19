// step 1 //
Что покажет приведенный ниже фрагмент кода?
mystr = 'да'
mystr = mystr + 'нет'
mystr = mystr + 'да'
print(mystr)
--- данетда ---

// step 2 //
Что покажет приведенный ниже фрагмент кода?
str1 = '1'
str2 = str1 + '2' + str1
str3 = str2 + '3' + str2
str4 = str3 + '4' + str3
print(str4)
--- 121312141213121 ---

// step 3 //
Что покажет приведенный ниже фрагмент кода?
mystr = '123' * 3 + '456' * 2 + '789' * 1
print(mystr)
--- 123123123456456789 ---

// step 4 //
Напишите программу, которая выводит текст:
"Python is a great language!", said Fred. "I don't ever remember having this much fun before."
print(""""Python is a great language!", said Fred. "I don't ever remember having this much fun before.\"""")

// step 5 //
Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
«Hello [введенное имя] [введенная фамилия]! You just delved into Python».
firstname, lastname = input(), input()
print("Hello {0} {1}! You just delved into Python".format(firstname, lastname))

// step 6 //
Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу
name_of_club = input()
length = len(name_of_club)
print("Футбольная команда {n} имеет длину {l} символов".format(n = name_of_club, l = length))

// step 7 //
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
a, b, c = input(), input(), input()
if(len(a) < len(b)): b, a = a, b
if(len(c) > len(b)): c, b = b, c
if(len(c) > len(a)): c, a = a, c
print(c, a, sep='\n')

// step 8 //
Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
a, b, c = len(input()), len(input()), len(input())
if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0:
    print("YES")
else:
    print("NO")

// step 9 //
Какие значения может принимать строковая переменная s, чтобы в результате выполнения кода было выведено слово «YES»?
if s in 'abc123abc':
    print('YES')
else:
    print('NO')
---
s = '23'
s = '3ab'
s = 'a'
s = '123abc'
s = '1' ---

// step 10 //
Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.
text = input()
if "синий" in text:
    print("YES")
else:
    print("NO")

// step 11 //
Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
text = input()
if "суббота" in text or "воскресенье" in text:
    print("YES")
else:
    print("NO")

// step 12 //
Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.
post = input()
if ("@" in post) and ("." in post):
    print("YES")
else:
    print("NO")