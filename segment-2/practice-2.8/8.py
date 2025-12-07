X = [8, 11, -4, -9, 1, -10, 5, 9, -18, -27, -2, 1, 3, 12]
Y = []
for i in range(len(X)):
    if X[i] >= 0:
        Y.append(X[i])
print(str(Y).replace(",", "").replace("[", "").replace("]", ""))
print(len(Y))
print(sum(X))
prod = 1
for i in range(len(Y)):
    prod = prod * Y[i]
print(prod)
