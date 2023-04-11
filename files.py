car_sales = open('car_sale.txt')

lines = car_sales.readlines()

companies = []
sales = []

for x in range(0, len(lines), 2):
    companies.append(lines[x])

print(companies)

for x in range(1, len(lines), 2):
    data = lines[x].strip().split(',')
    sales.append(list(map(int, data)))

print(sales)

for string in companies:
    string.strip()
    print(string)

total = 0

for list in sales:
    for sale in list:
        total += sale

print(total)


