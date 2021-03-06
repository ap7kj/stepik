// step 1 //
Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии с примером:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
height = int(input())
total = 0
for i in range(1, height + 1):
    for j in range(1, i + 1):
        total += 1
        print(total, end=' ')
    print()

// step 2 //
Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии с примером:
1
121
12321
1234321
123454321
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 2 * i):
        print(min(j, 2 * i - j), end='')
    print()

// step 3 //
На вход программе подается два натуральных числа a и b (a< b). Напишите программу, которая находит натуральное число из отрезка [a;b]
с максимальной суммой делителей.
a, b = int(input()), int(input())
x = [sum([j for j in range(1,i+1) if i%j == 0]) for i in range(a, b+1)][::-1]
print(b - x.index(max(x)), max(x))

// step 4 //
На вход программе подается натуральное число n. Напишите программу, выводящую графическое изображение делимости чисел от 1 до n включительно. В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.
n = int(input())
for i in range(1, n+1):
    print(i, end = '')
    for j in range(1, i+1):
        if i%j == 0:
            print('+', end = '')
    print()

// step 5 //
На вход программе подается натуральное число n. Напишите программу, которая находит цифровой корень данного числа. Цифровой корень числа n
получается следующим образом: если сложить все цифры этого числа, затем все цифры найденной суммы и повторить этот процесс, то в результате будет получено однозначное число (цифра), которое и называется цифровым корнем данного числа.
num = int(input())
while num // 10 > 0:
    num = num // 10 + num % 10
print(num)

// step 6 //
Дано натуральное число n. Напишите программу, которая выводит значение суммы 1! + 2! + 3! + ... +n!
num = int(input())
multi = 1
total = 0
for i in range(1, num + 1):
    multi *= i
    total += multi
print(total)

// step 7 //
На вход программе подается два натуральных числа a и b (a< b). Напишите программу, которая находит все простые числа от a до b включительно.
start, stop = int(input()), int(input())
for i in range(start, stop + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    if counter != 2:
        continue
    print(i)