import module17

def test_move():
    
    assert module17.move({'pos': (0, 0), 'vel': (10, 10)}) == {'pos': (10, 10), 'vel': (9, 9)}
    assert module17.move({'pos': (10, 10), 'vel': (-5, 5)}) == {'pos': (5, 15), 'vel': (-4, 4)}
    
def test_is_hitting_target():
    target = ((20, 30), (-10, -5))
    assert module17.is_hitting_target((7, 2), target, True)[0] == True
    assert module17.is_hitting_target((6, 3), target, True)[0] == True
    assert module17.is_hitting_target((6, 9), target, True)[0] == True
    assert module17.is_hitting_target((7, 9), target, True)[0] == True
    assert module17.is_hitting_target((9, 0), target, True)[0] == True
    assert module17.is_hitting_target((17, -4), target, True)[0] == False

def test_solve1():
    test_target = ((20,30), (-10,-5))
    module17.solve1_positive(test_target) == 45
    
def test_solve2():
    test_target = ((20,30), (-10,-5))
    module17.solve2_positive(test_target) == 112
    
