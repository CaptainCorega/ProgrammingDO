import math

x = float(input("Введи дробное число:"))

cell = math.ceil(x)
flor = math.floor(x)

print("Верхнее значение: " + str(cell))
print("Нижнее значение: " + str(flor))

print("Их сумма:")
print(cell + flor)




