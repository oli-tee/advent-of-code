import module10

def test_find_first_invalid_closing():
    #data = module10.read_data('test_input.txt')
    
    assert module10.find_first_invalid_closing_bracket('[)') == ')'
    assert module10.find_first_invalid_closing_bracket('{()()()>') == '>'
    assert module10.find_first_invalid_closing_bracket('{([(<{}[<>[]}>{[]{[(<()>') == '}'                    
    assert module10.find_first_invalid_closing_bracket('[[<[([]))<([[{}[[()]]]') == ')'
    assert module10.find_first_invalid_closing_bracket('[{[{({}]{}}([{[{{{}}([]') == ']'
    assert module10.find_first_invalid_closing_bracket('[{[{({}]{}}([{[{{{}}([]') == ']'
    
    
    valid_inputs = ['([])', '{()()()}', '<([{}])>', '[<>({}){}[([])<>]]', '(((((((((())))))))))']
    for input in valid_inputs:
        assert module10.find_first_invalid_closing_bracket(input) is None
    
def test_solve1():
    data = module10.read_data('test_input.txt')
    assert module10.solve1(data) == 26397
    
def test_autocomplete():
    assert module10.find_missing_sequence('(') == ')'
    assert module10.find_missing_sequence('()(') == ')'
    assert module10.find_missing_sequence('([<') == '>])'
    assert module10.find_missing_sequence('[({(<(())[]>[[{[]{<()<>>') == '}}]])})]'
    assert module10.find_missing_sequence('[(()[<>])]({[<{<<[]>>(') == ')}>]})'
    assert module10.find_missing_sequence('(((({<>}<{<{<>}{[]{[]{}') == '}}>}>))))'
    assert module10.find_missing_sequence('{<[[]]>}<{[{[{[]{()[[[]') == ']]}}]}]}>'
    assert module10.find_missing_sequence('<{([{{}}[<[[[<>{}]]]>[]]') == '])}>'
    
    assert module10.find_missing_sequence('(]') is None
    
    valid_inputs = ['([])', '{()()()}', '<([{}])>', '[<>({}){}[([])<>]]', '(((((((((())))))))))']
    for input in valid_inputs:
        assert module10.find_missing_sequence(input) == ''
        

def test_get_autocomplete_score():
    assert module10.get_autocomplete_score('}}]])})]') == 288957
    assert module10.get_autocomplete_score(')}>]})') == 5566
    assert module10.get_autocomplete_score('}}>}>))))') == 1480781
    assert module10.get_autocomplete_score(']]}}]}]}>') == 995444
    assert module10.get_autocomplete_score('])}>') == 294
    
def test_solve2():
    data = module10.read_data('test_input.txt')
    assert module10.solve2(data) == 288957
    
def test_opener_closer_helpers():
    assert set(module10.get_list_of_openers()) == set(['(', '[', '{', '<']) 
    assert set(module10.get_list_of_closers()) == set([')', ']', '}', '>'])
    assert module10.get_matching_opener(']') == '['
    assert module10.get_matching_closer('{') == '}'
    assert module10.get_matching_closer('}') is None
    assert module10.get_matching_opener('(') is None