import math

def calculate_radius(area):
    radius = math.sqrt(area/ math.pi)
    return radius

def circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

area_value = float(input("Digit the area of the circule: "))
radius_value = calculate_radius(area_value)
circle_value = circle_area(radius_value)

print("The radius of the circle is: ", radius_value)
print("The area of the circle is: ", circle_value)
