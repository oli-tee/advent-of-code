import day05


def test_convert():
    assert day05.convert(79, (52, 50, 48)) == 81
    assert day05.convert(79, (48, 50, 48)) == 77
    assert day05.convert(50, (52, 50, 48)) == 52
    assert day05.convert(49, (52, 50, 48)) == None
    assert day05.convert(98, (52, 50, 48)) == None
    assert day05.convert(97, (52, 50, 48)) == 99
    

def test_convert_multi():
    map_list = [(52, 50, 48), (50, 98, 2)]
    assert day05.convert_multi(79, map_list) == 81
    assert day05.convert_multi(14, map_list) == 14
    assert day05.convert_multi(55, map_list) == 57
    assert day05.convert_multi(13, map_list) == 13

def test_end_to_end_convert():
    map_dict = day05.parse_data(day05.read_data('test_input05.txt'))['maps']
    assert day05.end_to_end_convert(79, map_dict) == 82
    assert day05.end_to_end_convert(14, map_dict) == 43
    assert day05.end_to_end_convert(55, map_dict) == 86
    assert day05.end_to_end_convert(13, map_dict) == 35
    
def test_solve_p1():
    assert day05.solve_p1('test_input05.txt') == 35