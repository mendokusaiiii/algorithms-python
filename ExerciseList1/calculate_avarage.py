def calculate_avarege(num1, num2, num3, num4):
    avarage = (num1 + num2 + num3 + num4) / 2
    return avarage

grade1 = int(input("Digit your first grade: "))
grade2 = int(input("Digit your second grade: "))
grade3 = int(input("Digit your third grade: "))
grade4 = int(input("Digit your fourth grade: "))

print("The avarage grade is: ", calculate_avarege(grade1, grade2, grade3, grade4))