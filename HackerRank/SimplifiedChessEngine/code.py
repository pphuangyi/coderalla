#!/usr/bin/python3

import os
import sys

I, D, C = lambda x: 4 - x, lambda x: x + 1, lambda x: 4
direction_map = {
    'r': [I, C, 1, 0], 'l': [D, C, -1, 0],
    'u': [C, I, 0, 1], 'd': [C, D, 0, -1],
    'ru': [I, I, 1, 1], 'lu': [D, I, -1, 1],
    'rd': [I, D, 1, -1], 'ld': [D, D, -1, -1]
}


def move(whites, blacks, board, idx, col, row):
    """
    'm': move to the position
    'q': capture black's queen
    'c': capture a black's piece that is not a queen
    'o': the position is occupied by a white piece 
    """
    if (col, row) not in board:
        whites_ = list(map(list, whites))
        whites_[idx][1], whites_[idx][2] = col, row
        return 'm', whites_, blacks
    else:
        occupant = board[(col, row)]
        if occupant[1] == 'b':
            if occupant[2] == 'Q':
                return 'q', None, None
            else:
                whites_ = list(map(list, whites))
                whites_[idx][1], whites_[idx][2] = col, row
                blacks_ = list(map(list, blacks)) 
                del blacks_[occupant[0]]
                return 'c', whites_, blacks_
        else:
            return 'o', None, None


def move_(whites, blacks, board, idx, direction):
    col, row = whites[idx][1:]
    cL, rL, cd, rd = direction_map[direction]
    results = []
    # print(f'({col}, {row}): ({cL(col)}, {rL(row)})')
    for i in range(1, min(cL(col), rL(row))):
        c, r = col + i * cd, row + i * rd
        # print(f'{direction}: new position: ({c}, {r})')
        case, w, b = move(whites, blacks, board, idx, c, r)
        # print(f'{whites}->{w}')
        if case == 'm' or case == 'c':
            results.append([w, b])
        elif case == 'q':
            return None
        else:
            break
    return results

    
def get_moves(whites, blacks):
    board = {(c, r): (i, 'w', p) for i, (p, c, r) in enumerate(whites)}
    board.update({(c, r): (i, 'b', p) for i, (p, c, r) in enumerate(blacks)})
    
    results = []
    for idx in range(len(whites)):
        piece, col, row = whites[idx]
        if piece == 'R':
            for direction in ['r', 'l', 'u', 'd']:
                r = move_(whites, blacks, board, idx, direction)
                if r is None:
                    return None
                else:
                    results += r
        elif piece == 'B':          
            for direction in ['ru', 'lu', 'rd', 'ld']:
                r = move_(whites, blacks, board, idx, direction)
                if r is None:
                    return None
                else:
                    results += r
        elif piece == 'Q':
            for direction in ['r', 'l', 'u', 'd', 'ru', 'lu', 'rd', 'ld']:
                r = move_(whites, blacks, board, idx, direction)
                # print(f'{direction}: {r}')
                if r is None:
                    return None
                else:
                    results += r
        else:
            for ci in [-2, -1, 1, 2]:
                for ri in [-(3 - abs(ci)), 3 - abs(ci)]:
                    ct, rt = col + ci, row + ri
                    if ct >= 0 and ct < 4 and rt >= 0 and rt < 4:
                        case, w, b = move(whites, blacks, board, idx, ct, rt)
                        if case == 'm' or case == 'c':
                            results.append([w, b])
                        elif case == 'q':
                            return None
    return results


def simplifiedChessEngine_(whites, blacks, num_moves):
    if num_moves == 0:
        return False
    
    moves_w = get_moves(whites, blacks)
    # if num_moves == 4:
    #     print(f'white moves {moves_w}')
    if moves_w is None:
        return True
    for w1, b1 in moves_w:
        moves_b = get_moves(b1, w1)
        if moves_b is None:
            continue
        winning = True
        for b2, w2 in moves_b:
            if not simplifiedChessEngine_(w2, b2, num_moves - 1):
                winning = False
                break
        if winning:
            return True
    
    return False


def simplifiedChessEngine(whites, blacks, num_moves):         
    if simplifiedChessEngine_(whites, blacks, num_moves):
        return 'YES'
    else:
        return 'NO'

        
if __name__ == '__main__':

    input_idx = sys.argv[1]
    input_fname = f'data/input{input_idx}.txt'
    output_fname = f'data/output{input_idx}.txt'

    with open(input_fname, 'r') as handle:
        g = int(handle.readline().strip())

        for g_itr in range(g):
            w, b, m = list(map(int, handle.readline().strip().split()))

            whites = []
            for _ in range(w):
                p = handle.readline().rstrip().split()
                whites.append([p[0], ord(p[1]) - ord('A'), ord(p[2]) - ord('1')])

            blacks = []
            for _ in range(b):
                p = handle.readline().rstrip().split()
                blacks.append([p[0], ord(p[1]) - ord('A'), ord(p[2]) - ord('1')])
                
            result = simplifiedChessEngine(whites, blacks, m)
            print(f'{g_itr}: {result}')

