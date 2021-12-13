import module13

def test_fold_one_dot():
    assert module13.fold_one_dot((0, 8), 'y', 7) == (0, 6)
    assert module13.fold_one_dot((0, 14), 'y', 7) == (0, 0)
    assert module13.fold_one_dot((9, 0), 'x', 5) == (1, 0)
    assert module13.fold_one_dot((4, 0), 'x', 5) == (4, 0)
    assert module13.fold_one_dot((1, 1), 'y', 2) == (1, 1)
    
def test_fold():
    data = module13.read_data('test_input.txt')
    dots = data['dots']
    result = module13.fold_all_dots(module13.fold(dots, 'y', 7), 'x', 5)
    expected_result = [
        (0, 0), (0, 1), (0,2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), 
        (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0)
    ]
    
    assert set(result) == set(expected_result)
    
def test_solve1():
    data = module13.read_data('test_input.txt')
    assert module13.solve1(data) == 17