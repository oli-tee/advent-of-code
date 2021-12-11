import module_04

def test_parse_row():
    assert module_04.parse_row(' 8  2 23  4 24') == [8, 2, 23, 4, 24]
    
def test_transpose():
    assert module_04.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    
def test_solve():
    data = module_04.read_data('test_input.txt')
    assert module_04.solve(data) == 4512
        
def test_solve2():
    data = module_04.read_data('test_input.txt')
    assert module_04.solve2(data) == 1924
    
def test_is_complete():
    assert module_04.is_complete([1, 0, 1]) == False
    assert module_04.is_complete([1, 1, 1, 1]) == True
    

def test_test_for_victory():
    assert module_04.test_for_victory([[[0, 0, 0], [1, 1, 1], [0, 0, 1]]]) == 0
    assert module_04.test_for_victory([[[0, 1, 0], [1, 1, 0], [0, 1, 1]]]) == 0
    assert module_04.test_for_victory([[[0, 0, 0], [1, 0, 1], [0, 0, 1]]]) == None
    assert module_04.test_for_victory([[[0, 1, 0], [0, 1, 1], [0, 0, 1]]]) == None