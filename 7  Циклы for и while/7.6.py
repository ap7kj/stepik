// step 1 //
Что покажет приведенный ниже фрагмент кода?
for i in range(10):
    print(i, end='*')
    if i > 6:
        break
--- 0*1*2*3*4*5*6*7* ---

// step 2 //
Что покажет приведенный ниже фрагмент кода?
i = 100
while i > 0:
    if i == 40:
        break
    print(i, end='*')
    i -= 20
--- 100*80*60* ---

// step 3 //
Что покажет приведенный ниже фрагмент кода?
n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end='*')
--- 9*8*7*6*5*4*3*1*0* ---

// step 4 //
 Что покажет приведенный ниже фрагмент кода?
result = 0
for i in range(10):
    if i % 2 == 0:
        continue
    result += i
print(result)
--- 25 ---

// step 5 //
 Что покажет приведенный ниже фрагмент кода?
mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
print(mult)
--- 105 ---

// step 6 //
На вход программе подается число n>1. Напишите программу, которая выводит его наименьший отличный от 1 делитель.
num = int(input())
for i in range(2, num + 1):
    if num % i == 0:
        print(i)
        break

// step 7 //
На вход программе подается натуральное числоnn. Напишите программу, которая выводит числа от 1 до n включительно за исключением:
чисел от 5 до 9 включительно;
чисел от 17 до 37 включительно;
чисел от 78 до 87 включительно.
num = int(input())
for i in range(1, num + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)

// step 8 //
Будет ли выполнен блок кода else, в приведенном ниже фрагменте кода?
n = 0
while n < 10:
    n += 2
    print(n)
else:
    print('Цикл завершен.')
--- Да ---

// step 9 //
Будет ли выполнен блок кода else, в приведенном ниже фрагменте кода?
n = 0
while n < 10:
    n += 2
    if n == 8:
        break
    print(n)
else:
    print('Цикл завершен.')
--- Нет ---

// step 10 //
Будет ли выполнен блок кода else, в приведенном ниже фрагменте кода?
n = 0
while n < 10:
    n += 2
    if n == 7:
        break
    print(n)
else:
    print('Цикл завершен.')
--- Да ---