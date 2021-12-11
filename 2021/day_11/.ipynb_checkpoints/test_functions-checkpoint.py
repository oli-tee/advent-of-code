import numpy as np

import module11


def test_step():
    state1 = module11.convert_to_matrix([
        '11111', 
        '19991',
        '19191',
        '19991',
        '11111'
    ])
    
    state2 = module11.convert_to_matrix([
        '34543',
        '40004',
        '50005',
        '40004',
        '34543',
    ])
    
    state3 = module11.convert_to_matrix([
        '45654',
        '51115',
        '61116',
        '51115',
        '45654',
    ])
        
    assert (module11.apply_step(state1)[0] == state2).all()
    assert module11.apply_step(state1)[1] == 9
    assert (module11.apply_step(state2)[0] == state3).all()
    assert module11.apply_step(state2)[1] == 0
    
def test_solve1():
    data = module11.read_data('test_input.txt')
    assert module11.solve1(data, nsteps=10) == 204
    
    assert module11.solve1(data, nsteps=100) == 1656
    
def test_solve2():
    data = module11.read_data('test_input.txt')
    assert module11.solve2(data) == 195