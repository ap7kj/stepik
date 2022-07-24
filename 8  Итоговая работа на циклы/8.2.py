// step 1 //
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран сумму чётных цифр этого числа или 0, если чётных цифр в записи нет. Программист торопился и написал программу неправильно.
n = int(input())
total = 0
while n > 0:
    last_digit = n % 10
    if last_digit % 2 == 0:
        total += last_digit
    n //= 10
print(total)

// step 2 //
На обработку поступает последовательность из 8 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^12
Нужно написать программу, которая выводит на экран количество делящихся нацело на 4 чисел в исходной последовательности и максимальное делящееся нацело на 4 число. Если делящихся нацело на 4 чисел нет,
требуется на экран вывести «NO». Программист торопился и написал программу неправильно.
n = 8 #
count = 0
maximum = -10 ** 6 - 1
for i in range(n):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

// step 3 //
На обработку поступает последовательность из 4 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^8
Нужно написать программу, которая выводит на экран количество нечётных чисел в исходной последовательности и максимальное нечётное число. Если нечётных чисел нет,
требуется на экран вывести «NO». Программист торопился и написал программу неправильно.
n = 4
count = 0
maximum = 0
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

// step 4 //
На вход программе подается натуральное число n. Напишите программу, которая печатает звездную рамку размерами n×19.
key = int(input())
for i in range(1):
    print(19 * '*')
for j in range(key - 2):
    print('*', ' ' * 16 + '*')
print(19 * '*')

// step 5 //
Дано натуральное число n (n>99). Напишите программу, которая определяет его третью (с начала) цифру.
num = int(input())
while len(str(num)) >= 3:
    last_digit = num % 10
    num //= 10
print(last_digit)

// step 6 //
Дано натуральное число. Напишите программу, которая вычисляет:
количество цифр 3 в нем;
сколько раз в нем встречается последняя цифра;
количество четных цифр;
сумму его цифр, больших пяти;
произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
n = int(input())
d3, d0d5, last_d, last_d_count = 0, 0, n % 10, 0
sum_over_5, mul_over_7, chetn = 0, 1, 0
while n > 0:
    d3 += n % 10 == 3
    d0d5 += n % 10 == 0 or n % 10 == 5
    last_d_count += n % 10 == last_d
    chetn += (n % 10) % 2 == 0
    if n % 10 > 5:
        sum_over_5 += n % 10
    if n % 10 > 7:
        mul_over_7 *= n % 10
    n //= 10
print(d3, last_d_count, chetn, sum_over_5, mul_over_7, d0d5, sep='\n')

// step 7 //
Сриниваса Рамануджан – индийский математик, славившийся своей интуицией в области чисел. Когда английский математик Годфри Харди навестил его однажды в больнице, он обмолвился, что номером такси, на котором он приехал, было 17291729, такое скучное и заурядное число. На что Рамануджан ответил: "Нет, нет! Это очень интересное число. Это наименьшее число, выражаемое как сумма двух кубов двумя разными способами". Другими словами:
1729 = 1^3 + 12^3 = 9^3 + 10^3.
1 число = 1729
2 число = 4104
3 число = 13832
4 число = 20683
5 число = 32832
