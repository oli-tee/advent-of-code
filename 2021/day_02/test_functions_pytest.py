import module_02
    
    
def test_functions():
    assert module_02.parse_row('forward 2') == ('forward', 2)
    assert module_02.solve(['down 10', 'down 20', 'up 5', 'forward 1', 'forward 9']) == 250
    assert module_02.solve(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 150
    assert module_02.solve2(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 900