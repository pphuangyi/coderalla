#! /Users/yhuang10/opt/anaconda3/bin/python3.8
import sys


def read_puzzle(fname):	
	puzzle = {}
	with open(fname, 'r') as fh:
		num_cells = int(fh.readline().strip())
		for n in range(num_cells):
			i, j, val = list(map(int, fh.readline().strip().split()))
			key = i * 9 + j
			puzzle[key] = val
	return puzzle


def print_puzzle(puzzle):
	print('\n======================= puzzle ======================= START')
	matrix = [[0] * 9 for _ in range(9)]
	for i in range(9):
		for j in range(9):
			key = i * 9 + j
			if key in puzzle:
				matrix[i][j] = puzzle[key]
		print(' '.join(map(str, matrix[i])).replace('0', ' '))
	print('======================= puzzle ======================= END\n')
	

def validate_(mydict):
	return sum([int(len(array) != len(set(array))) for _, array in mydict.items()]) == 0
		

def validate(puzzle):
	rows = {i: [] for i in range(9)}
	columns = {i: [] for i in range(9)}
	cells = {i: [] for i in range(9)}

	for key, val in puzzle.items():
		i, j = key // 9, key % 9
		rows[i].append(val)
		columns[j].append(val)
		c = (i // 3) * 3 + (j // 3)
		cells[c].append(val)
	
	return validate_(rows) and validate_(columns) and validate_(cells)
	


def elimination_fill(puzzle):
	memo = {}
	for i in range(9):
		for j in range(9):
			key = i * 9 + j
			if key not in puzzle:
				A = set()
				for k, v in puzzle.items():
					s, t = k // 9, k % 9
					if s == i:
						A.add(v)
					elif t == j:
						A.add(v)
					elif (i // 3) == (s // 3) and (j // 3) == (t // 3):
						A.add(v)
				R = set(range(1, 10)) - A
				if len(R) == 1:
					puzzle[key] = list(R)[0]
				else:
					if len(R) == 0:
						return None, None
					memo[key] = R					

	return puzzle, memo


def necessity_fill(puzzle, memo):

	to_be_removed = set()
	for k, A in memo.items():
		i, j = k // 9, k % 9
		row, column, cell = A.copy(), A.copy(), A.copy()
		for l, B in memo.items():
			if l == k:
				continue
			s, t = l // 9, l % 9
			if s == i:
				row -= memo[l]
			if t == j:
				column -= memo[l]
			if (i // 3) == (s // 3) and (j // 3) == (t // 3):
				cell -= memo[l]

		if len(row) == 1:
			puzzle[k] = list(row)[0]
			to_be_removed.add(k)
		if len(column) == 1:
			puzzle[k] = list(column)[0]
			to_be_removed.add(k)
		if len(cell) == 1:
			puzzle[k] = list(cell)[0]
			to_be_removed.add(k)
		
	for key in to_be_removed:
		del memo[key]
		
	return puzzle, memo


def solve_puzzle(puzzle):

	while len(puzzle) < 81:
		l0 = len(puzzle)
		puzzle, memo = elimination_fill(puzzle)	
		if puzzle is None:
			return None, None
		l1 = len(puzzle)

		if l0 == l1:
			puzzle, memo = necessity_fill(puzzle, memo)
			l1 = len(puzzle)
			print(f'necessity fill, l0 = {l0}, l1 = {l1}')
			print_puzzle(puzzle)
			if l0 == l1:
				break
		else:
			print(f'elimination fill, l0 = {l0}, l1 = {l1}')
			print_puzzle(puzzle)
	
	return puzzle, memo


def solve_puzzle_rec(puzzle):
	puzzle, memo = solve_puzzle(puzzle)
	if puzzle is None or len(puzzle) == 81:
		return puzzle
		
	print('Got a tie')
	key, value = memo.popitem()
	for v in value:
		puzzle_try = puzzle.copy()
		puzzle_try[key] = v
		puzzle_solved = solve_puzzle_rec(puzzle_try)
		if puzzle_solved is not None:
			
			return puzzle_solved
			


if __name__ == "__main__":

	index = sys.argv[1]
	fname = f'puzzle_{index}.txt'

	puzzle = read_puzzle(fname)	
	print(validate(puzzle))
	solved = solve_puzzle_rec(puzzle)
	print(validate(solved))
