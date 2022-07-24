// step 1 //
Что покажет приведенный ниже фрагмент кода?
num1 = 4
num2 = 6
num1 += num2
num1 *= num1
print(num1)

--- 100 ---

// step 2 //
Что покажет приведенный ниже фрагмент кода?
total = 0
for i in range(1, 6):
    total += i
print(total)

--- 15 ---

// step 3 //
Что покажет приведенный ниже фрагмент кода?
total = 0
for i in range(1, 6):
    total += i
    print(total, end='')

--- 1361015 ---

// step 4 //
На вход программе подаются два целых числа a и b (a≤b). Напишите программу, которая подсчитывает количество чисел в диапазоне
от a до b включительно, куб которых оканчивается на 4 или 9.
counter, a, b = 0, int(input()), int(input())
for i in range(a, b + 1):
    if i ** 3 % 10 in [4, 9]:
        counter += 1
print(counter)

// step 5 //
На вход программе подается натуральное число n, а затем nn целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел.
key, total = int(input()), 0
for _ in range(key):
    num = int(input())
    total += num
print(total)

// step 6 //
На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения
from math import log
total = 0
n = int(input())
for i in range(1, n + 1):
    x = 1 / i
    total += x

print(total - log(n))

// step 7 //
На вход программе подается натуральное число nn. Напишите программу, которая
подсчитывает сумму тех чисел от 1 до n (включительно) квадрат которых оканчивается на 2,5 или 8.
total = 0
n = int(input())
for i in range(1, n + 1):
    if i ** 2 % 10 in [2, 5, 8]:
        total += i
print(total)

// step 8 //
На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.
n, total = int(input()), 1
for i in range(1, n + 1):
    total *= i
print(total)

// step 9 //
Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
total = 1
for _ in range(10):
    num = int(input())
    if not num == 0:
        total *= num
print(total)

// step 10 //
На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.
total = 0
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)

// step 11 //
На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей сумм
total = 0
n = int(input())
for i in range(1, n + 1):
    total += ((-1) ** (i + 1)) * i
print(total)

// step 12 //
На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
how_many = int(input())
largest = 0
previously_largest = 0
for _ in range(1, how_many + 1):
    num = int(input())
    if previously_largest < num < largest:
        previously_largest = num
    elif num > previously_largest and num > largest:
        previously_largest = largest
        largest = num
print(largest, previously_largest, sep="\n")

// step 13 //
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.
counter = 0
for _ in range(10):
    num = int(input())
    if num % 2 == 0:
        counter += 1
if counter == 10:
    print("YES")
else:
    print("NO")

// step 14 //
Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.
n = int(input())
f1, f2 = 1, 0
for i in range(1, n + 1):
    f1, f2 = f2, (f1 + f2)
    print(f2, end=" ")