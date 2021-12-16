import module16

def test_hexa_to_bin():
    assert module16.hex_to_bin('D2FE28') == '110100101111111000101000'
    
#def test_parse_literal_value():
#    assert module16.parse_literal_value('101111111000101000') == 2021
    
def test_get_version_nr():
    assert module16.get_version_number('110100101111111000101000') == 6
    
def test_get_type():
    assert module16.get_type('110100101111111000101000') == 4

def get_ltid():
    assert module16.get_length_type_id('00111000000000000110111101000101001010010001001000000000') == 0
    
#def test_parse_lit_packet():
#    assert module16.parse_literal_packet('110100101111111000101000') == (6, 2021)
    
    
def test_extract_packet_starting():
    #literal
    assert module16.extract_first_packet_and_sum_versions('110100101111111000101000222')[0] == '110100101111111000101'
    
    # container by length
    cont_pack = '00111000000000000110111101000101001010010001001000000000XXZZ'
    expected_result = '0011100000000000011011110100010100101001000100100'
    module16.extract_first_packet_and_sum_versions(cont_pack, True)[0] == expected_result
    
    # container by count
    cont_pack = '11101110000000001101010000001100100000100011000001100000'
    expected_result = '111011100000000011010100000011001000001000110000011'
    module16.extract_first_packet_and_sum_versions(cont_pack, True)[0] == expected_result
    
def test_solve1():
    assert module16.solve1('D2FE28') == 6 
    assert module16.solve1('8A004A801A8002F478') == 16 
    assert module16.solve1('620080001611562C8802118E34') == 12
    assert module16.solve1('C0015000016115A2E0802F182340') == 23
    assert module16.solve1('A0016C880162017C3686B18A3D4780') == 31

def test_apply_operation():
    
    assert module16.apply_operator(0, [1,2,3,4]) == 10
    assert module16.apply_operator(1, [1,2,3,4]) == 24
    assert module16.apply_operator(2, [1,2,3,4]) == 1
    assert module16.apply_operator(3, [1,2,3,4]) == 4
    assert module16.apply_operator(5, [1,2,3,4]) == 0
    assert module16.apply_operator(5, [3,2,3,4]) == 1
    assert module16.apply_operator(6, [1,2,3,4]) == 1
    assert module16.apply_operator(6, [3,2,3,4]) == 0
    assert module16.apply_operator(7, [1,2,3,4]) == 0
    assert module16.apply_operator(7, [1,1,3,4]) == 1
    
    
    """
    operator_def = {
        0: lambda values: np.sum(values),
        1: lambda values: np.product(values),
        2: lambda values: np.min(values),
        3: lambda values: np.max(values),
        5: lambda values: int(values[0] >= values[1]),
        6: lambda values: int(values[0] <= values[1]),
        7: lambda values: int(values[0] == values[1]),
    }
    """
    
def test_values():
    
    tests = [
        ('C200B40A82', 3),
        ('04005AC33890', 54),
        ('880086C3E88112', 7),
        ('CE00C43D881120', 9),
        ('D8005AC2A8F0', 1),
        ('F600BC2D8F', 0),
        ('9C005AC2F8F0', 0),
        ('9C0141080250320F1802104A08', 1)
    ]
    for test in tests:
        assert module16.extract_first_packet_and_sum_versions(module16.hex_to_bin(test[0]))[2] == test[1]
    
    """
    C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
04005AC33890 finds the product of 6 and 9, resulting in the value 54.
880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
D8005AC2A8F0 produces 1, because 5 is less than 15.
F600BC2D8F produces 0, because 5 is not greater than 15.
9C005AC2F8F0 produces 0, because 5 is not equal to 15.
9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2."""