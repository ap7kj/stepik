// step 1  //
Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы была выведена длина строки s.
s = 'Python rocks!'
print(len(s))

// step 2 //
Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы был выведен четвертый символ строки s.
s = 'Python rocks!'
print(s[3])

// step 3 //
Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы были выведены символы строки s со 2 по 5 включительно.
s = 'Python rocks!'
print(s[1:5])

// step 4 //
Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы была выведена строка s без ведущих и замыкающих пробельных символов.
s = '    Python rocks!     '
print(s.strip())

// step 5 //
Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы была выведена строка s заглавными буквами (в верхнем регистре).
s = 'Python rocks!'
print(s.upper())

// step 6 //
Вставьте пропущенный фрагмент кода, так чтобы в результате выполнения программы была выведена строка s в которой символ «o» заменен на символ «@».
s = 'Python rocks!'
print(s.replace('o', '@'))

// step 7 //
На вход программе подается строка текста. Напишите программу, которая удаляет из нее все символы с индексами кратными 3, то есть символы с индексами 0, 3, 6, ....
s = input()
for i in range(len(s)):
    if i % 3 == 0:
        continue
    print(s[i], end='')

// step 8 //
На вход программе подается строка текста. Напишите программу, которая заменяет все вхождения цифры 1 на слово «one»
print(input().replace('1', 'one'))

// step 9 //
На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения символа «@».
print(input().replace('@', ''))

// step 10 //
На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f». Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.
s = input()
counter = 0
for i in s:
    if i == 'f':
        counter += 1
if counter == 1:
    print(-1)
elif counter == 0:
    print(-2)
else:
    n = s.replace('f', '1', 1)
    print(n.find('f', ))

// step 11 //
На вход программе подается строка текста в которой буква «h» встречается как минимум два раза. Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним вхождением буквы «h».
string = input()
h_index_1 = string.find('h') + 1
h_index_2 = string.rfind('h')
result = string[h_index_1:h_index_2]
print(string[:h_index_1] + result[::-1] + string[h_index_2:])