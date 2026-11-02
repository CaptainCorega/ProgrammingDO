try:
    biba = int(input("введите первое число"))
    boba = int(input("введите второе число"))

    print(biba + boba)
except ValueError:
    print("ты ввел не числа ")