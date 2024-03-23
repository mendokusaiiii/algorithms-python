def calculate_weight(height):
    weight = (72.7*height) - 58
    return weight

height_value = float(input("Digit the height: "))
weight_value = calculate_weight(height_value)

print("The weight is: ", weight_value)