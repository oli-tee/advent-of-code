import module25

def test_is_next_free():
    from module25 import is_next_space_free
    mat = module25.read_data('test_input.txt')
    assert is_next_space_free(mat, (0, 0), 0)
    assert is_next_space_free(mat, (0, 0), 1)
    assert not is_next_space_free(mat, (3, 6), 1)
    assert not is_next_space_free(mat, (2, 0), 0)
    assert not is_next_space_free(mat, (5, 2), 0)
    assert is_next_space_free(mat, (6, 2), 0)
    assert not is_next_space_free(mat, (6, 3), 0)
    
    
    
    
    """
    array([['.', '.', '.', '>', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.', '>'],
           ['v', '.', '.', '.', '.', '.', '>'],
           ['.', '.', '.', '.', '.', '.', '>'],
           ['.', '.', '.', '.', '.', '.', '.'],
           ['.', '.', 'v', 'v', 'v', '.', '.']], dtype='<U1')
    """