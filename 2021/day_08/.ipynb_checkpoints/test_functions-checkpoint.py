import module08

def test_solve1():
    data = module08.read_data('test_input.txt')
    assert module08.solve1(data) == 26
    
def test_solve2():
    data = module08.read_data('test_input.txt')
    assert module08.solve2(data) == 61229

def test_parse_row():
    assert module08.parse_row(
        'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
    ) == (['acedgfb','cdfbe','gcdfa','fbcad','dab','cefabd','cdfgeb','eafb','cagedb','ab'], ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'])
    
    
def test_get_mapping_from_line():
    the_input = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
    parsed_input = module08.parse_row(the_input)
    assert module08.get_mapping_from_line(parsed_input) == {'d': 0, 'e': 1, 'a': 2, 'f': 3 ,'g': 4, 'b': 5, 'c': 6}
    
def test_resolve_one_line():
    the_input = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
    parsed_input = module08.parse_row(the_input)
    assert module08.resolve_one_line(parsed_input) == 5353