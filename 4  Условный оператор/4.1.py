// step 1 //
Работа каких операторов дает верный ответ при любом значении переменной i?
if i / 2:
    print(i, 'чётное')
else:
    print(i, 'нечётное')
if i // 2:
    print(i, 'чётное')
else:
    print(i, 'нечётное')
if i % 2 == 0:
    print(i, 'чётное')
else:
    print(i, 'нечётное')
if i // 2 == 0:
    print(i, 'чётное')
else:
    print(i, 'нечётное')
if i % 2 != 0:
    print(i, 'нечётное')
else:
    print(i, 'чётное')
if i // 2 != 0:
    print(i, 'нечётное')
else:
    print(i, 'чётное')

--- 3 и 5 ---

// step 2 //
При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности, поскольку такой подход уменьшает
возможность неверного ввода пароля.
password, repeat = input(), input()
if password == repeat:
    print("Пароль принят")
else:
    print("Пароль не принят")

// step 3 //
Напишите программу, которая определяет, является число четным или нечетным.
number = int(input())
if number % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

// step 4 //
Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой
и последней цифр равна разности второй и третьей цифр.
number = int(input())
first_digit, second_digit, third_digit, last_digit = number // 1000, number // 100 % 10, number // 10 % 10, number % 10
first_and_last = first_digit + last_digit
second_and_third = second_digit - third_digit

if first_and_last == second_and_third:
    print("ДА")
else:
    print("НЕТ")

// step 5 //
Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.
age = int(input())
if age < 18:
    print("Доступ запрещен")
else:
    print("Доступ разрешен")

// step 6 //
Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке)
последовательными членами арифметической прогрессии.
num1, num2, num3 = int(input()), int(input()), int(input())
if num2 - num1 == num3 - num2:
    print("YES")
else:
    print("NO")

// step 7 //
Напишите программу, которая определяет наименьшее из двух чисел.
num1, num2 = int(input()), int(input())
if num1 > num2:
    print(num2)
else:
    print(num1)

// step 8 //
Напишите программу, которая определяет наименьшее из четырёх чисел.
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    print(c)
else:
    print(a)

// step 9 //
Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
age = int(input())
if age <= 13:
    print("детство")
if 14 <= age < 24:
    print("молодость")
if 25 <= age < 59:
    print("зрелость")
if 60 <= age:
    print("старость")

// step 10 //
Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
a, b, c = int(input()), int(input()), int(input())
total = 0
if a > 0:
    total = total + a
if b > 0:
    total = total + b
if c > 0:
    total = total + c
print(total)