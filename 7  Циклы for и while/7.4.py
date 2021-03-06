// step 1 //
Когда цикл while проверяет свое условие: до или после того, как он выполнит итерацию?
--- до ---

// step 2 //
Сколько раз сообщение «Python awesome!» будет напечатано в приведенном ниже фрагменте кода?
count = 10
while count < 1:
    print('Python awesome!')
--- 0 ---

// step 3 //
Сколько раз сообщение «Python awesome!» будет напечатано в приведенном ниже фрагменте кода?
count = 1
while count < 10:
    print('Python awesome!')
    count += 1
--- 9 ---

// step 4 //
Сколько раз сообщение «Python awesome!» будет напечатано в приведенном ниже фрагменте кода?
count = 1
while count < 10:
    print('Python awesome!')
--- бесконечно много раз ---

// step 5 //
Какое число нужно написать вместо многоточия, чтобы цикл выполнился ровно 7 раз?
i = 5
while i <= ...:
    print('Python awesome!')
    i += 1
--- 11 ---

// step 6 //
Что покажет приведенный ниже фрагмент кода?
i = 7
a = 5
while i < 11:
    a += i
    i += 2
print(a)
--- 21 ---

// step 7 //
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» (без кавычек).
Напишите программу, которая выводит члены данной последовательности.
text = input()
while text != "КОНЕЦ":
    print(text)
    text = input()

// step 8 //
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ»
или «конец» (большими или маленькими буквами, без кавычек). Напишите программу, которая выводит члены данной последовательности.
text = input()
while text not in "КОНЕЦконец":
    print(text)
    text = input()

// step 9 //
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности
является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек).
Напишите программу, которая выводит общее количество членов данной последовательности.
text = input()
counter = 0
while text not in ("стоп", "хватит", "достаточно"):
    counter += 1
    text = input()
print(counter)

// step 10 //
На вход программе подается последовательность целых чисел делящихся на 7, каждое число на отдельной строке. Концом последовательности является любое число не делящееся на 7.
Напишите программу, которая выводит члены данной последовательности.
numbers = int(input())
while numbers % 7 == 0:
    print(numbers)
    numbers = int(input())

// step 11 //
На вход программе подается последовательность целых чисел, каждое число на отдельной строке. Концом последовательности является любое отрицательное число. Напишите программу, которая выводит сумму всех членов данной последовательности.
numbers = int(input())
total = 0
while numbers > -1:
    total += numbers
    numbers = int(input())
print(total)

// step 12 //
На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика, каждое число на отдельной строке.
Концом последовательности является любое отрицательное число, либо число большее 5. Напишите программу, которая выводит количество пятерок.
numbers = int(input())
counter = 0
while 0 <= numbers < 6:
    if "5" in str(numbers):
        counter += 1
    numbers = int(input())
print(counter)

// step 13 //
Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, к тому же ведьмак не принимает купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 1, 5, 10, 25
banknote = int(input())
counter_of_banknote = 0
while banknote >= 25:
    counter_of_banknote += 1
    banknote -= 25
while banknote >= 10:
    counter_of_banknote += 1
    banknote -= 10
while banknote >= 5:
    counter_of_banknote += 1
    banknote -= 5
while banknote >= 1:
    counter_of_banknote += 1
    banknote -= 1

print(counter_of_banknote)
