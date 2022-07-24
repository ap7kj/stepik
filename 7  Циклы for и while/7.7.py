// step 1 //
На обработку поступает последовательность из 10 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^6 .
Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности и их произведение. Если неотрицательных чисел нет, требуется вывести на
экран «NO». Программист торопился и написал программу неправильно.
count = 0
p = 1
for i in range(10):
    x = int(input())
    if x >=  0:
        count += 1
        p = p * x
if count > 0:
    print(count)
    print(p)
else:
    print('NO')

// step 2 //
На обработку поступает последовательность из 10 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^6
Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности и максимальное отрицательное число в последовательности.
Если отрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.
mx = -10**6 - 1
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
    if x < 0 and x > mx:
        mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')

// step 3 //
На обработку поступает последовательность из 7 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^6
Нужно написать программу, которая подсчитывает и выводит сумму всех чётных чисел последовательности или 00, если чётных чисел
в последовательности нет. Программист торопился и написал программу неправильно.
total = 0
for _  in range(7):
    n = int(input())
    if n % 2 == 0:
        total += n
print(total)

// step 4 //
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран максимальную цифру числа, кратную 3. Если в числе нет цифр, кратных 3,
требуется на экран вывести «NO». Программист торопился и написал программу неправильно.
n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)

// step 5 //
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран его первую (старшую) цифру. Программист торопился и написал программу неправильно.
n = int(input())
while n:
    last_digit = n % 10
    n //= 10
print(last_digit)

// step 6 //
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран произведение цифр введенного числа. Программист торопился и написал программу неправильно.
n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
