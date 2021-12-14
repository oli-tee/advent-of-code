import module14

def test_turn_template_into_hash():
    assert module14.turn_template_into_hash('ABCDAB') == {'AB': 2, 'BC': 1, 'CD': 1, 'DA': 1}
    assert module14.turn_template_into_hash('AB') == {'AB': 1}
    assert module14.turn_template_into_hash('A') == {}
    
def test_apply_one_step():
    data = module14.read_data('test_input.txt')
    
    rules = data['rules']
    template = module14.turn_template_into_hash(data['template'])
    step1 = module14.apply_one_step(template, rules)
    step2 = module14.apply_one_step(step1, rules)
    step3 = module14.apply_one_step(step2, rules)
    step4 = module14.apply_one_step(step3, rules)
    
    assert module14.apply_one_step({'AB': 4}, {'AB': 'C'}) == {'AC': 4, 'CB': 4}
    assert module14.apply_one_step({'AB': 4, 'CB': 3}, {'AB': 'C', 'CB': 'A'}) == {'AC': 4, 'CB': 4, 'CA': 3, 'AB': 3}
    assert module14.apply_one_step({'AB': 4, 'CB': 3}, {'AB': 'D', 'CB': 'D'}) == {'AD': 4, 'DB': 7, 'CD': 3}
    
    assert step1 == module14.turn_template_into_hash('NCNBCHB')
    assert step2 == module14.turn_template_into_hash('NBCCNBBBCBHCB')
    assert step3 == module14.turn_template_into_hash('NBBBCNCCNBBNBNBBCHBHHBCHB')
    assert step4 == module14.turn_template_into_hash('NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')

    
def test_get_element_count():
    #'ABCDABC'
    assert module14.get_element_count({'AB': 2, 'BC': 2, 'CD': 1, 'DA': 1}, 'A', 'C') == {'A': 2, 'B': 2, 'C': 2, 'D': 1}

    
    
def test_get_score():
    assert module14.get_score_from_element_hash({'A': 5, 'B': 2, 'C': 4, 'D': 1}) == 4
    assert module14.get_score_from_element_hash({'A': 5, 'B': 2, 'C': 1, 'D': 1}) == 4
    assert module14.get_score_from_element_hash({'A': 5, 'B': 5}) == 0
    assert module14.get_score_from_element_hash({'A': 5}) == 0
    

def test_solve1():
    data = module14.read_data('test_input.txt')
    assert module14.solve1(data, 10) == 1588