import module20
import numpy as np

def test_padding_array():
    assert (module20.padding_array('.', 4) == np.array(['.', '.', '.', '.'])).all()

def test_convert():
    input = np.array(
        [['.', '.', '.'],
        ['#', '.', '.'],
        ['.', '#', '.']]
    )
    
    assert module20.convert_matrix_to_number(input) == 34
    
def test_solve1():
    data = module20.read_data('test_input.txt')
    module20.solve1(data) == 35
    
def test_solve2():
    data = module20.read_data('test_input.txt')
    module20.solve2(data) == 3351