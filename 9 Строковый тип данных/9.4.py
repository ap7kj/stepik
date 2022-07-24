from re import X


// step 1 //
Что покажет приведенный ниже фрагмент кода?
s = 'aabbAAccDDaa'
s = s.lower()
print(s.count('a'))
--- 6 ---

// step 2 //
Что покажет приведенный ниже фрагмент кода?
s = 'www.stepik.org'
print(s.startswith('www'))
--- True ---

// step 3 //
Что покажет приведенный ниже фрагмент кода?
s = 'www.stepik.org'
print(s.endswith('.ru'))
--- False ---

// step 4 //
Что покажет приведенный ниже фрагмент кода?
s = 'I learn Python language. Python - awesome!'
print(s.find('Python')
--- 8 ---

// step 5 //
Что покажет приведенный ниже фрагмент кода?
s = '     I learn Python language               '
print(s.strip())
--- I learn Python language ---

// step 6 //
Что покажет приведенный ниже фрагмент кода?
s = 'abcdababa'
print(s.replace('ab', '123'))
--- 123cd123123a ---

// step 7 //
На вход программе подается строка текста, состоящая из слов, разделенных ровно одним пробелом. Напишите программу, которая подсчитывает количество слов в ней.
s = input()
print(s.count(' ') + 1)

// step 8 //
На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин). Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.
string = input().lower()
print('Аденин:', string.count('а'))
print('Гуанин:', string.count('г'))
print('Цитозин:', string.count('ц'))
print('Тимин:', string.count('т'))

// step 9 //
Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди. На приемник ему поступает nn различных последовательностей кода Морзе. Декодировав их, он получает последовательности из цифр и строчного латинского алфавита, при этом во всех сообщениях
Оди содержится число 11, причем минимум 3 раза. Помогите определить Джиму количество сообщений от Оди.
count_message = int(input())
counter = 0
for _ in range(count_message):
    radio_messagies = input()
    if radio_messagies.count('11') >= 3:
        counter += 1
print(counter)

// step 10 //
На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
string = input()
counter = 0
for i in string:
    if i.isdigit():
        counter += 1
print(counter)

// step 11 //
На вход программе подается строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.
url = input()
print('YES' if url.endswith('.ru') or url.endswith('.com') else 'NO')

// step 12 //
На вход программе подается строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
string = input()
maximum = 0
result = 0
for i in string:
    if string.count(i) >= maximum:
        maximum = string.count(i)
        result = i
print(result)

// step 13 //
На вход программе подается строка текста. Если в этой строке буква «f» встречается только один раз, выведите её индекс. Если она встречается два и более раз, выведите индекс её первого и последнего вхождения на одной строке,
разделенных символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO».
string = input()
counter = 0
for i in range(len(string)):
    if string[i] == 'f':
        counter += 1
if counter == 1:
    print(string.find('f'))
elif counter >= 1:
    print(string.find('f'), string.rfind('f'))
else:
    print('NO')

// step 14 //
На вход программе подается строка текста, в которой буква «h» встречается минимум два раза. Напишите программу, которая удаляет из этой строки первое и последнее
вхождение буквы «h», а также все символы, находящиеся между ними
string = input()
for i in string:
    index_1 = string.find('h')
    index_2 = string.rfind('h')
    res = string[:index_1] + string[index_2:]
    res = res.replace('h', '')

print(res)
