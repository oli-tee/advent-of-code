
import module07

def test_solve_bf():
    data = module07.read_data('test_input.txt')
    assert module07.solve_bruteforce(data) == 37

def test_solve_med():
    data = module07.read_data('test_input.txt')
    assert module07.solve_median(data) == 37

def test_solve_2():
    data = module07.read_data('test_input.txt')
    assert module07.solve_2(data) == 168
    
    
def test_fuel_cost():
    assert module07.calculate_fuel_cost([16,1,2,0,4,2,7,1,2,14], 2) == 37
    assert module07.calculate_fuel_cost([16,1,2,0,4,2,7,1,2,14], 10) == 71
    
def test_fuel_cost_2():
    assert module07.calculate_fuel_cost_2([16,1,2,0,4,2,7,1,2,14], 2) == 206
    assert module07.calculate_fuel_cost_2([16,1,2,0,4,2,7,1,2,14], 5) == 168
    
def test_calculate_individual_cost_2():
    assert module07.calculate_individual_cost_2(2, 2) == 0
    assert module07.calculate_individual_cost_2(2, 3) == 1
    assert module07.calculate_individual_cost_2(3, 2) == 1
    assert module07.calculate_individual_cost_2(2, 4) == 3
    assert module07.calculate_individual_cost_2(2, 5) == 6
    assert module07.calculate_individual_cost_2(2, 6) == 10
    assert module07.calculate_individual_cost_2(6, 2) == 10