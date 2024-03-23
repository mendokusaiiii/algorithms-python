def calculate_square(square):
    area = square ** 2
    return area

square_value = float(input("Digit the value of the square: "))

square_area = calculate_square(square_value)

double_the_value = square_value * 2

print("The value os the area of the square is: ", double_the_value)