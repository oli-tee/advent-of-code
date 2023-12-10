import day06


def test_count():
    assert day06.count_winning_strategies(7, 9) == 4
    assert day06.count_winning_strategies(15, 40) == 8
    assert day06.count_winning_strategies(30, 200) == 9
    
def test_solve_p1():
    assert day06.solve_p1('test_input06.txt') == 288