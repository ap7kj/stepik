// step 1 //
Что покажет приведенный ниже фрагмент кода?
num = 12345
product = 1
while num != 0:
    last_digit = num % 10
    product = product * last_digit
    num = num // 10
print(product)
--- 120 ---

// step 2 //
Что покажет приведенный ниже фрагмент кода?
num = 123456789
total = 0
while num != 0:
    last_digit = num % 10
    if last_digit > 4:
        total += 1
    num = num // 10
print(total)

--- 5 ---

// step 3 //
Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.
number = int(input())
while number != 0:
    last_digit = number % 10
    print(last_digit)
    number //= 10

// step 4 //
Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
number = int(input())
while number != 0:
    last_digit = number % 10
    print(last_digit, end="")
    number //= 10

// step 5 //
Дано натуральное число n, (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.
num = int(input())
max_, min_ = 0, 9
while num != 0:
    last_digit = num % 10
    if last_digit > max_:
        max_ = last_digit
    if last_digit < min_:
        min_ = last_digit
    num //= 10
print(f"Максимальная цифра равна {max_}")
print(f"Минимальная цифра равна {min_}")

// step 6 //
Дано натуральное число. Напишите программу, которая вычисляет:
сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.

num = int(input())
how_numbers = 0  # счётчик
total = 0  # сумматор
multi = 1  # мультипликатор
last = num % 10
while num != 0:
    last_digit = num % 10
    total += last_digit  # сумму его цифр;
    how_numbers += 1  # количество цифр в нем;
    multi *= last_digit  # произведение его цифр;
    arifmet = total / how_numbers  # среднее арифметическое его цифр;
    first_digit = num % 10  # его первую цифру;
    summa_1_2 = first_digit + last  # сумму его первой и последней цифры.
    num //= 10  # убираем последнию цифру
print(total, how_numbers, multi, arifmet, first_digit, summa_1_2, sep="\n")

// step 7 //
Дано натуральное число n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.
num = int(input())
total = 0
while num > 99:
    last_digit = num % 10
    num //= 10
print(num % 10)

// step 8 //
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
num = int(input())
flag = True
last_digit = num % 10
while num != 0:
    last = num % 10
    num //= 10
    if last != last_digit:
        flag = False
if flag == True:
    print("YES")
else:
    print("NO")

// step 9 //
Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
num = int(input())
flag = True
while num // 10 != 0:
    if not num % 100 // 10 >= num % 10:
        flag = False
    num //= 10
print("YES" if flag == True else "NO")