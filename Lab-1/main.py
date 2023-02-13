firstValue = input("Введите первый коэффициент: ")
print("a:", firstValue)

secondValue = input("Введите второй коэффициент: ")
print("b:", secondValue)

thirdValue = input("Введите третий коэффициент: ")
print("c:", thirdValue)

print(f"\nКвадратное уравнение: ({firstValue})x^2 + ({secondValue})x + ({thirdValue}) = 0")

disk = int(secondValue) ** 2 - 4 * int(firstValue) * int(thirdValue)

if -disk > 0:
    print("Уравнение не имеет корней")
else:
    root1 = ((int(secondValue) * (-1)) + (round(disk)**0.5)) / (2 * int(firstValue))
    root2 = ((int(secondValue) * (-1)) - (round(disk)**0.5)) / (2 * int(firstValue))

    print("\nДействительные корни: ")
    if root1 > 0:
        print("\nX1: ", root1)

    if root2 > 0:
        print("\nX2: ", root2)