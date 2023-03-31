def getIncomeTax(salary):
    taxable_salary = salary - 11850
    if taxable_salary <= 0:
        return "You are not getting taxed"
    elif  0 < taxable_salary <= 34501:
        return taxable_salary * 0.2
    elif 34501 <= taxable_salary <= 150000:
        return taxable_salary * 0.4
    else:
        return taxable_salary * 0.45

print(getIncomeTax(300000))