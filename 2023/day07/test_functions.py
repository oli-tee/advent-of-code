import day07

def test_score_pattern():
    assert day07.score_pattern('88888') == 6
    
    assert day07.score_pattern('88884') == 5
    assert day07.score_pattern('KKQKK') == 5
    
    assert day07.score_pattern('KKQKQ') == 4
    assert day07.score_pattern('KKQK6') == 3
    
    assert day07.score_pattern('KKQQ4') == 2
    assert day07.score_pattern('KKQ64') == 1
    assert day07.score_pattern('12345') == 0
    
def test_score_hand():
    assert day07.score_hand() > day07.score_hand()