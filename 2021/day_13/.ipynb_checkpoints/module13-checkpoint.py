from typing import Dict, Tuple, List
import numpy as np


def read_data(file_name: str) -> Dict:
    content = open(file_name).read().split('\n\n')
    dots = content[0]
    folds = content[1]
    result = dict()
    
    result['dots'] = [(int(row.split(',')[0]), int(row.split(',')[1])) for row in dots.split('\n')]
    result['folds'] = [
        (
            row.replace('fold along ', '').split('=')[0],
            int(row.replace('fold along ', '').split('=')[1])
        ) for row in folds.split('\n')
        if row != ''
    ]
    return result


def solve1(data: Dict) -> int:
    "only performing one fold"
    dots = data['dots']
    folds = data['folds']

    dots = fold_all_dots(dots=dots, fold_axis=folds[0][0], fold_position=folds[0][1])
    
    return len(dots)


def fold_all_dots(dots: List[Tuple[int]], fold_axis: str, fold_position: int) -> List[Tuple[int]]:
    folded_dots = [fold_one_dot(dot, fold_axis, fold_position) for dot in dots]
    
    unique_dots = list(set(folded_dots))
    
    return unique_dots


def fold_one_dot(dot_coord: Tuple[int], fold_axis: str, fold_position: int) -> Tuple[int]:
    if fold_axis == 'x':
        if dot_coord[0] > fold_position:
            dot_coord = (2 * fold_position - dot_coord[0], dot_coord[1])
    elif fold_axis == 'y':
        if dot_coord[1] > fold_position:
            dot_coord = (dot_coord[0], 2 * fold_position - dot_coord[1])
    else:
        print(fold_axis)
        raise ValueError
    
    return dot_coord


def solve2(data):
    folded_dots = apply_all_folds(data)
    return render_dots(folded_dots)


def apply_all_folds(data: Dict) -> int:
    dots = data['dots']
    folds = data['folds']
    for fold in folds:
        dots = fold_all_dots(dots=dots, fold_axis=fold[0], fold_position=fold[1])
    
    return dots


def render_dots(dots: List[Tuple[int]]) -> List[str]:
    max_x = max([dot[0] for dot in dots])
    max_y = max([dot[1] for dot in dots])
    
    matrix = np.array([['.' for col in range(max_x + 1)] for row in range(max_y + 1)])
    
    for dot in dots:
        matrix[dot[1], dot[0]] = '#'
        
    return [''.join(row) for row in matrix]
        

def print_rendered_dots(rendered_dots: List[str]) -> None:
    for row in rendered_dots:
        print(row)
