import module12 
from typing import List, Dict

def test_solve1():
    data = module12.read_data('test_input.txt')
    assert module12.solve1(data) == 19

    
def test_solve2():
    data = module12.read_data('test_input.txt')
    assert module12.solve2(data) == 103

def test_solve2_fast():
    data = module12.read_data('test_input.txt')
    assert module12.solve2_fast(data) == 103
    
def test_parse_input():
    input = ['a-B', 'B-c', 'a-D', 'c-D']
    expected_output = {'a': ['B', 'D'], 'B': ['c', 'a'], 'c': ['D', 'B'], 'D': ['a', 'c']}
    actual_output = module12.parse_input(input)
    for k in expected_output:
        assert set(expected_output[k]) == set(actual_output[k])
        
def test_is_valid_path():
    assert module12.is_valid_path_2(['start', 'a', 'b', 'end'])
    assert module12.is_valid_path_2(['start', 'A', 'b', 'A', 'end'])
    assert module12.is_valid_path_2(['start', 'A', 'b', 'A', 'b', 'c', 'd', 'end'])
    
    assert not module12.is_valid_path_2(['start', 'a', 'b', 'a', 'b', 'end'])
    assert not module12.is_valid_path_2(['start', 'a', 'start', 'b', 'end'])
    assert not module12.is_valid_path_2(['start', 'a', 'end', 'b', 'end'])
    
    