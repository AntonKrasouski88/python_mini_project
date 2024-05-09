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
