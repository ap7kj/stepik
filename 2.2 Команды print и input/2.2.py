# Напишите программу, которая выводит на экран текст «Здравствуй, мир!» (без кавычек).
print("Здравствуй, мир!")


# В популярном сериале «Остаться в живых» использовалась последовательность чисел 4 8 15 16 23 42,
# которая принесла героям удачу и помогла сорвать джекпот в лотерее.
# Напишите программу, которая выводит данную последовательность чисел с одним пробелом между ними.
print(4, 8, 15, 16, 23, 42)

#Измените предыдущую программу так, чтобы каждое число последовательности
# 4 8 15 16 23 42 печаталось на отдельной строке.
print(4, 8, 15, 16, 23, 42, sep="\n")

#Напишите программу, которая выводит указанный треугольник, состоящий из звездочек (*).
for i in range(8):
    print(i * "*")

#На вход программе подается строка текста – имя человека.
#Напишите программу, которая выводит на экран приветствие в
# виде слова «Привет» (без кавычек), после которого должна стоять запятая и пробел, а затем введенное имя.
name = input()
print(f"Привет, {name}")

#На вход программе подается строка текста – название футбольной команды. Напишите программу, На вход программе подается строка текста – название футбольной команды. Напишите программу, которая повторяет ее на экране со словами « - чемпион!» (без кавычек).
# которая повторяет ее на экране со словами « - чемпион!» (без кавычек).
name_of_club = input()
print(f"{name_of_club} - чемпион!")


#Напишите программу, которая считывает три строки по очереди, а затем выводит их в той же
#  последовательности, каждую на отдельной строчке.
a, b, c = input(), input(), input()
print(a, b, c, sep="\n")

#Напишите программу, которая считывает три строки по очереди, а затем выводит их в обратной последовательности, Напишите программу, которая считывает три строки по очереди, а затем выводит их в обратной последовательности, каждую на отдельной строчке.
# каждую на отдельной строчке.

a, b, c = input(), input(), input()
print(c, b, a, sep="\n")

#Команда print() используется для вывода данных на экран
#Значения для вывода, указываемые через запятую в команде print(), называются параметрами и аргументами
#Команда input() используется для считывания данных с клавиатуры
# 1 - Вывод текста «Какой язык программирования ты изучаешь?»
# 2 - Ввод данных (пользователь вводит текст)
# 3 - Нажатие клавиши Enter
# 4 - Запись введенного текста в переменную language
# 5 - Вывод текста