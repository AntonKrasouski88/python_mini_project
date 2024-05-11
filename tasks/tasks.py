# 4. The total sales
# Налог с продаж
TAX = 0.07 

# Создаем список с ценами на продукты
products = []

# Стоимость товаров
cost_goods = 0

# Принимаем стоимоть пяти товаров
for i in range(5):
    price = int(input('Enter the cost of the goods: '))
    products.append(price)

for el in products:
    cost_goods += el


tax_goods = cost_goods * TAX
tax_cost = cost_goods + tax_goods

print(f'Стоисть товаров: {cost_goods:,.2f}$', f'Налог состовляет: {tax_goods:,.2f}$', f'Итого стоимость к оплате: {tax_cost:,.2f}', sep = '\n')


# 5. The distance traveled
# Car speed
SPEED = 70

hours = [6, 10, 15]
for el in hours:
    distance = el * SPEED
    print(distance)


# 6. Sales tax
FEDERAL_TAX = 0.05
REGIONAL_TAX = 0.025

amount_purchases = int(input('Enter the amount of the purchases: '))
amount_federal_tax = amount_purchases * FEDERAL_TAX
amount_regional_tax = amount_purchases * REGIONAL_TAX
full_cost_purchases = amount_purchases + amount_federal_tax + amount_regional_tax

print(f'Стоиость покупок: {amount_purchases}')
print(f'Федеальный налог: {amount_federal_tax}', f'Региональный налог: {amount_regional_tax}', sep='\n')
print(f'Полная стоимость покупок: {full_cost_purchases:,.2f}')


# 7. Gasoline consumption
distance = int(input('Enter the path traveled: '))
spent_litres = int(input('Enter the amount of spent gasoline in liters: '))
consumption = distance / spent_litres

print(f'Gasoline consumption per kilometer of the traveled path: {consumption:,.2f}')


# 8. Tips, tax and total amount
TIPS = 0.18
SALES_TAX = 0.07

cost_food = int(input('Enter the cost of food: '))
total_amount = cost_food + cost_food * TIPS + cost_food * SALES_TAX

print(f'Total amount with tips and sales tax: {total_amount:,.2f}')


# 9. Temperature converting on a Celsius scale 
# into a temperature along the pharyngeite scale
degrees_celsius = int(input('Enter degrees Celsius: '))
degrees_fahrenheit = (9 / 5) * degrees_celsius + 32

print(f'{degrees_fahrenheit:.2f}F') 