// step 1 //
Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
a, b = float(input()), float(input())
print(1 / 2 * a * b

// step 2 //
Две старушки идут навстречу друг другу с постоянными скоростями V_1 и V_2 км/ч. Определите, через какое время старушки встретятся,
если расстояние между ними равно S км.
s1, v1, v2 = float(input()), float(input()), float(input())
print(s1 / (v1 + v2))

// step 3 //
Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. Если при этом введённое с клавиатуры число – ноль,
то вывести «Обратного числа не существует» (без кавычек).
number = float(input())
if number != 0:
    print(1 / number)
else:
    print("Обратного числа не существует")

// step 4 //
У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». Напишите программу, которая определяет, какой температуре по шкале
Цельсия соответствует указанное значение по шкале Фаренгейта.
f = float(input())
print(5 / 9 * (f - 32))

// step 5 //
На вход программе подается число nn – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих годах.
n = int(input())
if n == 1:
    print(10.5)
elif n == 2:
    print(10.5 + 10.5)
elif n >= 3:
    print(21 + (n - 2) * 4)

// step 6 //
Дано положительное действительное число. Выведите его первую цифру после десятичной точки.
number = float(input())
x = number * 10
print(int(x % 10))

// step 7 //
Дано положительное действительное число. Выведите его дробную часть.
number = float(input())
print(number % int(number))

// step 8 //
Какое число будет выведено на экран в результате выполнения следующего кода?
num = max(1, 3, -5, 7) + min(-3, 6, -8, -1) + abs(-17)
print(num)
--- 16 ---

// step 9 //
Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.
num1, num2, num3, num4, num5 = int(input()), int(input()), int(input()), int(input()), int(input())
print(f"Наименьшее число = {min(num1, num2, num3, num4, num5)}")
print(f"Наибольшее число = {max(num1, num2, num3, num4, num5)}")

// step 10 //
Напишите программу, которая упорядочивает три числа от большего к меньшему.
num1, num2, num3 = int(input()), int(input()), int(input())
lst_ = [num1, num2, num3]
lst_.sort()
print(lst_[2], lst_[1], lst_[0], sep="\n")


// step 11 //
Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
Напишите программу, которая определяет интересное число или нет.
Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».
number = int(input())
x = sorted([str(number)[0], str(number)[1], str(number)[2]])
if int(x[-1]) - int(x[0]) == int(x[1]):
    print("Число интересное")
else:
    print("Число неинтересное")

// step 12 //
Даны пять чисел a1, a2, a3, a4, a5. Напишите программу, которая вычисляет сумму их модулей |a_1| + |a_2| +|a_3| +|a_4| + |a_5|.
a1, a2, a3, a4, a5 = abs(float(input())), abs(float(input())), abs(float(input())), abs(float(input())), \
    abs(float(input()))
print(a1 + a2 + a3 + a4 + a5)

// step 13 //
Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути. Если только вы не умеете проходить сквозь стены,
вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.
p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
print(abs(p1 - q1) + abs(p2 - q2))
