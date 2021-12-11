from collections import defaultdict
import numpy as np

def parse_row(row):
    
    output = row.strip().replace('  ', ' ').split(' ')
    return [int(x) for x in output]
    
    
def read_data(file_name):
    data = open(file_name).read().split('\n')[:-1]

    output = dict()
    
    output['sequence'] = [int(x) for x in data[0].split(',')]
    
    boards = data[2:]
    
    boards = '\n'.join(boards).split('\n\n')
    
    boards = [[parse_row(row) for row in board.split('\n')] for board in boards]
    
    output['boards'] = boards
    
    return output



def create_hash(data):
    my_hash = defaultdict(list)
    for i_board, board in enumerate(data['boards']):
        for i_row, row in enumerate(board):
            for i_number, number in enumerate(row):
                my_hash[number].append((i_board, i_row, i_number))
     
    return my_hash

def is_complete(row_or_col):
    return np.sum(row_or_col) == len(row_or_col)


def transpose(board):
    return [[row[i] for row in board] for i in range(len(board[0]))]

def test_for_victory(index):
    for i_board, board in enumerate(index):
        for row in board:
            if is_complete(row):
                return i_board
        
        for row in transpose(board):
            if is_complete(row):
                return i_board
    
    return None



def test_for_victory_all(index):
    winning_boards = []
    for i_board, board in enumerate(index):
        for row in board:
            if is_complete(row):
                winning_boards.append(i_board)
        
        for row in transpose(board):
            if is_complete(row):
                winning_boards.append(i_board)
    
    return list(set(winning_boards))

def solve(data):
    ncol = len(data['boards'][0][0])
    nrow = len(data['boards'][0])
    nboards = len(data['boards'])
    
    boards = data['boards']
    
    index = [[[0 for x in range(ncol)] for y in range(nrow)] for z in range(nboards)]
    
    my_hash = create_hash(data)
    
    i_number = 0
    
    i_winning_board = None

    while (i_winning_board is None) and (i_number <= len(data['sequence']) - 1):
        new_number = data['sequence'][i_number]

        positions = my_hash[new_number]
 
        for position in positions:
            boards[position[0]][position[1]][position[2]] = 0
            index[position[0]][position[1]][position[2]] = 1
        
        i_winning_board = test_for_victory(index)
        
        i_number += 1

        
    total_unmarked = sum([sum(row) for row in boards[i_winning_board]])
    
    
    return total_unmarked * data['sequence'][i_number - 1]



def solve2(data):
    ncol = len(data['boards'][0][0])
    nrow = len(data['boards'][0])
    nboards = len(data['boards'])
    
    boards = data['boards']
    
    index = [[[0 for x in range(ncol)] for y in range(nrow)] for z in range(nboards)]
    
    my_hash = create_hash(data)
    
    i_number = 0
    i_winning_board = None
    i_winning_boards = []
    
    
    while (len(i_winning_boards) < nboards) and (i_number <= len(data['sequence']) - 1):
        new_number = data['sequence'][i_number]

        positions = my_hash[new_number]
 
        for position in positions:
            boards[position[0]][position[1]][position[2]] = 0
            index[position[0]][position[1]][position[2]] = 1
            
        previously_winning_boards = i_winning_boards
        i_winning_boards = test_for_victory_all(index)
        
        i_number += 1

    i_losing_board = [i for i in range(nboards) if i not in previously_winning_boards][0]
    total_unmarked = sum([sum(row) for row in boards[i_losing_board]])
    
    return total_unmarked * data['sequence'][i_number - 1]