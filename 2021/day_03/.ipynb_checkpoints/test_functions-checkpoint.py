import module_03

def test_functions():
    assert module_03.get_most_common_bits(['1011', '1000', '0100']) == '1000'
    
    assert module_03.get_least_common_bits(['1011', '1000', '0100']) == '0111'
    
def test_functions_02():
    
    input = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    
    assert module_03.get_oxygen(input) == 23
    assert module_03.get_co2(input) == 10
    assert module_03.solve2(input) == 230