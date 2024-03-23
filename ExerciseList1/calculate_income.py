def calculate_income(rate, hours):
    total_hours = hours
    monthly_income = rate * total_hours

    return monthly_income, total_hours

rate_per_hour = float(input("Digit the rate: "))
hours_worked = float(input("Digit the hours: "))

month_income, total_hours = calculate_income(rate_per_hour, hours_worked)

print("The month income is: ", month_income)
print("The number of hours is: ", total_hours)
