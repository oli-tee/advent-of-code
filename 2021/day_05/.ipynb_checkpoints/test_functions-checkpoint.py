import module_05

def test_solve():
    data = module_05.read_data('test_input.txt')
    assert module_05.solve(data) == 5
    
def test_solve2():
    data = module_05.read_data('test_input.txt')
    assert module_05.solve2(data) == 12
   
def test_parse_row():
    assert module_05.parse_row('9,4 -> 3,4') == ((9, 4), (3, 4))
    
def test_generate_list_coord():
    assert module_05.generate_list_of_coords((1, 2), (1, 4)) == [(1, 2), (1, 3), (1, 4)]
    assert module_05.generate_list_of_coords((1, 2), (5, 2)) == [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)]
    
def test_generate_list_coord_2():
    assert module_05.generate_list_of_coords((1, 2), (1, 4), True) == [(1, 2), (1, 3), (1, 4)]
    assert module_05.generate_list_of_coords((1, 2), (5, 2), True) == [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2)]
    assert module_05.generate_list_of_coords((1, 1), (3, 3), True) == [(1, 1), (2, 2), (3, 3)]
    assert module_05.generate_list_of_coords((9, 7), (7, 9), True) == [(9, 7), (8, 8), (7, 9)]
    
    
def test_get_board_dimension():
    assert (module_05.get_board_dimension([((1,2), (3,4)), ((1, 3), (2, 5))]) == (3, 5))
    

def test_get_score():
    assert module_05.get_score([[0, 1, 2], [0, 3, 1], [2, 1, 1]]) == 3
    
def test_get_list():
    assert module_05.generate_list_of_int(1, 5) == [1, 2, 3, 4, 5]
    assert module_05.generate_list_of_int(6, 2) == [6, 5, 4, 3, 2]