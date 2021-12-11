import numpy as np

from typing import List, Tuple

def read_data(file_name: str):
    rows = open(file_name).read().split('\n')
    
    return convert_to_matrix(rows)


def convert_to_matrix(rows: List[str]):
    matrix = np.array([[int(digit) for digit in row] for row in rows if row != ''])
    return matrix


def solve1(matrix, nsteps: int) -> int:
    total_flash_count = 0
    for i in range(nsteps):
        matrix, count_new_flashes = apply_step(matrix)
        total_flash_count += count_new_flashes
    return total_flash_count
        

def solve2(matrix, max_steps: int = 10000) -> int:
    for i in range(max_steps):
        matrix, count_new_flashes = apply_step(matrix)
        if count_new_flashes == matrix.shape[0] * matrix.shape[1]:
            return i + 1
    
    return None
            
    
def apply_step(matrix, verbose: bool = False):
    octopi_to_flash = list()

    already_flashed = list()
    
    matrix = matrix + 1
    
    unzipped_list_of_flashers = np.where(matrix > 9)
    zipped_list_of_flashers = [
        (unzipped_list_of_flashers[0][i], unzipped_list_of_flashers[1][i])
        for i in range(len(unzipped_list_of_flashers[0]))
    ]
    octopi_to_flash = octopi_to_flash + zipped_list_of_flashers
    
    
    fuse_counter = 1000
    
    while len(octopi_to_flash) > 0 and fuse_counter > 0:
        fuse_counter -= 1
        if verbose:
            print(octopi_to_flash)
        current_flasher = octopi_to_flash[0]
        matrix, new_flashers = flash(matrix, current_flasher)
        
        already_flashed.append(current_flasher)
        
        for f in new_flashers:
            if f not in octopi_to_flash and f not in already_flashed:
                octopi_to_flash.append(f)
        
        octopi_to_flash = octopi_to_flash[1:]
    
    matrix[matrix > 9] = 0
    
    return matrix, len(already_flashed)
            
        

def flash(matrix, coord: Tuple[int]):
    r = coord[0] + 1
    c = coord[1] + 1
    padded_matrix = pad_matrix(matrix)
    
    surrounding_positions = [
        (r-1, c-1),
        (r-1, c),
        (r-1, c+1),
        (r, c+1),
        (r+1, c+1),
        (r+1, c),
        (r+1, c-1),
        (r, c-1)
    ]
    
    new_flashers = []
    
    for coord in surrounding_positions:
        padded_matrix[coord[0]][coord[1]] += 1
        if padded_matrix[coord[0]][coord[1]] > 9:
            new_flashers.append((coord[0]-1, coord[1]-1))
        
    
    return unpad_matrix(padded_matrix), new_flashers


def pad_matrix(matrix):
    """
    add a column of 0 on either sides, and a row of 0 on either side of the matrix
    """
    new_matrix = np.c_[np.zeros(len(matrix)), matrix, np.zeros(len(matrix))]
    new_matrix = np.r_[[np.zeros(len(new_matrix[0]))], new_matrix, [np.zeros(len(new_matrix[0]))]]
    return new_matrix.astype('int')

def unpad_matrix(padded_matrix):
    """
    remove first and last lines and columns of matrix
    """
    return padded_matrix[1:-1, 1:-1]