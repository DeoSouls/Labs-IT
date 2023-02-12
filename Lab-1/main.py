firstValue = input("Введите первый коэффициент: ")
print("a:", firstValue)

secondValue = input("Введите второй коэффициент: ")
print("b:", secondValue)

thirdValue = input("Введите третий коэффициент: ")
print("c:", thirdValue)

disk = int(secondValue) ** 2 - 4 * int(firstValue) * int(thirdValue)

print(disk)
