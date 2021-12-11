import module_06
from collections import defaultdict


def test_read_data():
    file_name = 'test_input.txt'
    data = module_06.read_data(file_name)
    assert data == [3, 4, 3, 1, 2]
   
def test_transform_1_day():
    assert module_06.transform_1_day([0,1,0,5,6,7,8]) == [6,0,6,4,5,6,7,8,8]
    
def test_solve_expo():
    file_name = 'test_input.txt'
    data = module_06.read_data(file_name)
    assert module_06.solve_expo(data, 18) == 26
    assert module_06.solve_expo(data, 80) == 5934
 
def test_solve_linear():
    file_name = 'test_input.txt'
    data = module_06.read_data(file_name)
    assert module_06.solve_linear(data, 18) == 26
    assert module_06.solve_linear(data, 80) == 5934
    
def test_transform_1_day_dict():
    input = {3: 3, 4: 2, 1: 1, 2: 1, 5: 2, 6: 1}
    output = {2: 3, 3: 2, 0: 1, 1: 1, 4: 2, 5: 1}
    assert module_06.transform_1_day_dict(input) == output