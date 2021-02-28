#!/home/yi/anaconda3/bin/python3

import numpy as np

def get_row(scratch, i, j):
	R = set()
	for k in range(9):
		if k != j:
			if len(scratch[i][k]) == 1:
				R.union(scratch[i][k])
	
	return R


def get_col(scratch, i, j):
	C = set()
	for k in range(9):
		if k != i:
			if len(scratch[k][j]) == 1:
				C.union(scratch[k][j])
	
	return C


def get_sqr(scratch, i, j):
	S = set()
	I = i // 3
	J = j // 3

	for k in range(I * 3, (I + 1) * 3):
		for l in range(J * 3, (J + 1) * 3):
			if (k != i) or (l != j):
				if len(scratch[k][l]) == 1:
					S.union(scratch[k][l])
	
	return S



def update(scratch, table):
	num_solved = 0
	for i in range(9):
		for j in range(9):
			if len(scratch[i][j]) > 1:
				W = set()
				W = W.union(get_row(scratch, i, j))
				W = W.union(get_col(scratch, i, j))
				W = W.union(get_sqr(scratch, i, j))
				scratch[i][j] = scratch[i][j].difference(W)
				if len(scratch[i][j]) == 1:
					table[i][j] = list(scratch[i][j])[0]
					num_solved += 1

	return num_solved
	

def sudoku_solver(table):
	num_solved = 0
	scratch = {i: {j: set(range(9)) for j in range(9)} for i in range(9)}
	for i in range(9):
		for j in range(9):
			value = table[i][j]
			if  value > 0:
				scratch[i][j] = set([value])
				num_solved += 1
	
	while update(scratch, table) > 0:
		print(table)

	print('now I can only help you by this much!')
	print('Improve me!')

if __name__ == '__main__':
	table = np.zeros((9, 9), dtype=int)
	table[0, 0] = 2
	
	table[1, 2] = 1
	table[1, 5] = 2
	table[1, 6] = 6
	
	table[2, 3] = 3
	table[2, 4] = 8
	
	table[3, 1] = 3
	table[3, 2] = 4
	table[3, 4] = 9
	table[3, 5] = 7
	table[3, 6] = 5
	table[3, 8] = 8
	
	table[4, 1] = 7
	table[4, 7] = 9
	table[4, 8] = 4

	table[5, 1] = 8
	table[5, 2] = 2
	table[5, 4] = 5
	table[5, 5] = 6
	table[5, 6] = 1
	table[5, 8] = 3

	table[6, 3] = 1
	table[6, 4] = 6
	
	table[7, 2] = 8
	table[7, 5] = 4
	table[7, 6] = 3

	table[8, 0] = 5

	sudoku_solver(table)
