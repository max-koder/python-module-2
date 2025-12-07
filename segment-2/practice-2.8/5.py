nail_style=['Шеллак', 'Френч', 'Обычный лак', 'Гель-лак', 'Акрил']
price = [2000, 1500, 1000, 3000, 3500]
week = [4, 5, 4, 8, 6]
money = [price[i] * week[i] for i in range(len(week))]

print(sum(week))
print(f"{(sum(week)/7):.2f}")
print(sum(money))
print(str(money).replace("[", "").replace("]","").replace(",", ""))
print(f"{(sum(money)/7):.0f}")