def hour_rate(hour_wage, hours_worked):
    gross_salary = hour_wage * hours_worked
    ir_discount = gross_salary * 0.11
    inss_discount = gross_salary * 0.08
    union_discount = gross_salary * 0.05
    net_salary = gross_salary - (ir_discount + inss_discount + union_discount)
    return gross_salary, ir_discount, inss_discount, union_discount, net_salary

hourly_wage = float(input("Digit your hourly wage: "))
hours_worked = float(input("Digit the number of hours worked: "))

gross_salary, ir_discount, inss_discount, union_discount, net_salary = hour_rate(hourly_wage, hours_worked)

print("Salary : R$", round(gross_salary, 2))
print("IR: R$", round(ir_discount, 2))
print("INSS: R$", round(inss_discount, 2))
print("Union: R$", round(union_discount, 2))
print("Net: R$", round(net_salary, 2))
