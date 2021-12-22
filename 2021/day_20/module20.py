import numpy as np
from typing import Dict, Tuple


def read_data(file_name: str) -> Dict:
    text = open(file_name).read().split('\n\n')
    algo = text[0]
    image = np.array([list(row) for row in text[1].split('\n') if row != ''])
    
    
    data = {
        'algo': algo,
        'image': image
        
    }
    
    return data


def solve1(data: Dict) -> int:
    enhanced_image, _ = enhance_n_times(
        data['image'],
        data['algo'], 
        '.',
        2
    )
    
    return np.sum(enhanced_image == '#')


def solve2(data: Dict) -> int:
    result, _ = enhance_n_times(
        data['image'],
        data['algo'], 
        '.',
        50
    )
    
    
    return np.sum(result == '#')


def enhance_n_times(image: "matrix", algo: str, background: str, n: int) -> Tuple["matrix", str]:

    result = image
    bg = background
    
    for i in range(n):
        print(f'enhancing #{i}...')
        result, bg = enhance(result, algo, bg)
    
    
    return result, bg



def enhance(image: "matrix", algo: str, background: str) -> Tuple["matrix", str]:
    verbose = False
    
    padded_image =  pad_matrix(pad_matrix(image, background), background)

    new_image = np.array([['.' for i in range(padded_image.shape[1])] for j in range(padded_image.shape[0])])

    for r in range(1,new_image.shape[0]-1):
        for c in range(1,new_image.shape[1]-1):
            sub_matrix = padded_image[r-1:r+2, c-1:c+2]
            score = convert_matrix_to_number(sub_matrix)
            pixel = algo[score]
            new_image[r, c] = pixel
    
    temp = new_image[1:-1, 1:-1]
    
    new_background = algo[int((background * 9).replace('.', '0').replace('#', '1'), 2)]
    
    result = pad_matrix(temp, new_background)
    return result, new_background


def pad_matrix(matrix: 'matrix', char: str) -> 'matrix':
    """
    add a column of char on either sides, and a row of char on either side of the matrix
    """
    new_matrix = np.c_[padding_array(char, len(matrix)), matrix, padding_array(char, len(matrix))]
    new_matrix = np.r_[[padding_array(char, len(new_matrix[0]))], new_matrix, [padding_array(char, len(new_matrix[0]))]]
    return new_matrix


def padding_array(char: str, n: int) -> 'array':
    return np.array([char for i in range(n)])


def convert_matrix_to_number(mat: 'matrix') -> int:
    flat_string = ''.join([''.join(list(x)) for x in mat])
    bin_string = flat_string.replace('#', '1').replace('.', '0')
    result = int(bin_string, 2)
    return result


def display(image: 'matrix'):
    for row in image:
        print(''.join(list(row)))
        

        