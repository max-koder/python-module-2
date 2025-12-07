num_1 = [1, 2, 3, 4, 5, 6]
num_2 = [4, 5, 6, 7, 8, 9]
union = str(set(num_1) & set(num_2))
union = union.replace("{", "")
union = union.replace("}", "")
union = union.replace(",", "")

print(len(set(num_1)))
print(len(set(num_2)))
print(max(num_1))
print(max(num_2))
print(min(num_1))
print(min(num_2))
print(union)

