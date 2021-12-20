import module19

def test_solve1():
    data = module19.read_data('test_input.txt')
    assert module19.solve1(data) == 79
    
def test_solve2():
    data = module19.read_data('test_input.txt')
    assert module19.solve2(data) == 3621