mun = int(input("Введи 4-х значное число: "))

thou = mun//1000
hun = (mun - (thou * 1000))//100
ten = (mun - (thou * 1000) - (hun * 100))//10
ones = mun - (thou * 1000) - (hun * 100) - (ten * 10)

print("Количество тысяч: ", thou)
print("Количество сотен: ", hun)
print("Количество десятков: ", ten)
print("Количество единиц: ", ones)