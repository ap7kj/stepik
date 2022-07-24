// step 1 //
Что покажет приведенный ниже фрагмент кода?
s = 'i Learn Python language'
print(s.capitalize())
--- I learn python language ---

// step 2 //
Что покажет приведенный ниже фрагмент кода?
s = 'i LEARN Python LAnguaGE'
print(s.lower())
--- i learn python language ---

// step 3 //
Что покажет приведенный ниже фрагмент кода?
s = '$12344%^$#@!'
print(s.lower())
--- $12344%^$#@! ---

// step 4 //
Что покажет приведенный ниже фрагмент кода?
s1 = 'a'
s2 = s1.upper()
print(s1, s2)
--- a A ---

// step 5 //
Что покажет приведенный ниже фрагмент кода?
s = 'i LEARN Python LAnguaGE'
print(s.upper())
--- I LEARN PYTHON LANGUAGE ---

// step 6 //
Что покажет приведенный ниже фрагмент кода?
s = 'i LEARN Python LAnguaGE'
print(s.swapcase())
--- I learn pYTHON laNGUAge ---

// step 7 //
На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом. Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
string = input()
print('YES' if string == string.title() else 'NO')

// step 8 //
На вход программе подается строка. Напишите программу, которая меняет регистр символов, другими словами замените все строчные символы заглавными и наоборот.
print(input().swapcase())

// step 9 //
На вход программе подается строка текста. Напишите программу, которая определяет является ли оттенок текста хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.
string = input().lower()
print('YES' if 'хорош' in string else 'NO')

// step 10 //
На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
string = input()
counter = 0
for i in string:
    if 'a' <= i <= 'z':
        counter += 1
print(counter)