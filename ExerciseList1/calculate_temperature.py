def calulate_temperature(fahrenheit):
    celsius = (5 * (fahrenheit - 32)) / 9
    return celsius

fahrenheit = float(input("Digit temperature in fahrenheit: "))
celsius = calulate_temperature(fahrenheit)
print("The temperature in celsius is:", round(celsius, 2))
