prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 165000, 140000, 125000, 85000, 90000, 128000, 230000, 225000, 100000, 300000]
value, count = sum(prices), len(prices)
medium_value = value/count
homes_above_medium = 0
for i in range(len(prices)):
    if prices[i] > medium_value:
        homes_above_medium +=1
    else:
        continue
print(homes_above_medium)