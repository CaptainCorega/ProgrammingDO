#Импорт библиотек
import math

#Функция расчета
def raschet_distancii(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#Вводи координат в виде переменных
koordinata_x1, koordinata_y1 = map(float, input("Введите координаты первой точки(x y): ").split())
koordinata_x2, koordinata_y2 = map(float, input("Введите координаты второй точки(x y): ").split())

#Вывод евклидова значения на экран
print(f"Расстояние между двумя координатами: {raschet_distancii(koordinata_x1, koordinata_y1, koordinata_x2, koordinata_y2):.2f}см")
