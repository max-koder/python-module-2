A = [1, 3, -6, 9, -1, -4, 7, 9, -23, 15, 8]
B = [A[i] for i in range(len(A)) if i%2 == 0]
print(" ".join(map(str, B)))
B.remove(-23)
print(sum(B)/len(B))