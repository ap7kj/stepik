// step 1 //
На плоскости евклидово расстояние между двумя точками (x1; y1) и (x1; y2) определяет так
p = (x1 - x2)**2+(y1-y2)**2
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print((pow((x1 - x2), 2) + pow((y1 - y2), 2)) ** 0.5)

// step 2 //
Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.
from math import pi
radius = float(input())
print(pi * pow(radius, 2), 2 * pi * radius, sep="\n")

// step 3 //
В математике выделяют следующие средние значения:
a, b = float(input()), float(input())
mid_arif = (a + b) / 2
mid_geom = (a * b) ** 0.5
mid_garm = (2 * a * b) / (a + b)
ass_jian_yang = ((pow(a, 2) + pow(b, 2)) / 2) ** 0.5
print(mid_arif, mid_geom, mid_garm, ass_jian_yang, sep="\n")

// step 4 //
Напишите программу, вычисляющую значение тригонометрического выражения sinx + cosx + tan**2x
from math import radians, sin, cos, tan
x_gradus = float(input())
radian = radians(x_gradus)
print(sin(radian) + cos(radian) + pow(tan(radian), 2))

// step 5 //
Напишите программу, вычисляющую значение [x] + [x] по заданному вещественному числу x
from math import ceil, floor
x = float(input())
print(ceil(x) + floor(x))

// step 6 //
Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения
a, b, c = float(input()), float(input()), float(input())
d = pow(b, 2) - 4 * a * c
if not a == 0:
    if d > 0:
        x2 = (-b + d ** 0.5) / (2 * a)
        x1 = (-b - d ** 0.5) / (2 * a)
        print(min(x1, x2), max(x1, x2), sep="\n")
    if d == 0:
        x1 = x2 = - b / (2 * a)
        print(x1)
    if d < 0:
        print("Нет корней")

// step 7 //
Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами. Площадь правильного многоугольника с
длиной стороны aa и количеством сторон nn вычисляется по формуле
from math import pi, tan
n, a = float(input()), float(input())
print((n * a ** 2) / (4 * tan ((pi / n))))
