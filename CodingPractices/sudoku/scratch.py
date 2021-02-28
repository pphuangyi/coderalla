#! /Users/yhuang10/opt/anaconda3/bin/python3.8

matrix = [[0 for _ in range(9)] for _ in range(9)] 
for i in range(9):
	br, bc = i // 3, i % 3
	for j in range(9):
		r, c = br * 3 + j // 3, bc * 3 + j % 3
		matrix[r][c] = j + 1

for vec in matrix:
	print(vec)

A = {'A': 1, 'B': 2}
B = {'C': 3}

A.update(B)
print(A)
