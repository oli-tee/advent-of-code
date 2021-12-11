import module09
import numpy as np


def test_solve():
    data = module09.read_data('test_input.txt')
    assert module09.solve(data) == 15
    
def test_solve2():
    data = module09.read_data('test_input.txt')
    assert module09.solve2(data) == 1134
    

    
def test_lowest_neighbour():
    """
    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    """
    data = module09.read_data('test_input.txt')
    assert module09.find_lowest_neighbour(data, (0, 0)) == (0, 1)
    assert module09.find_lowest_neighbour(data, (0, 1)) is None
    assert module09.find_lowest_neighbour(data, (0, 2)) is None
    assert module09.find_lowest_neighbour(data, (1, 0)) == (0, 0)
    assert module09.find_lowest_neighbour(data, (2, 1)) == (2, 2)
    assert module09.find_lowest_neighbour(data, (2, 3)) == (2, 2)
    assert module09.find_lowest_neighbour(data, (4, 9)) == (4, 8)
    assert module09.find_lowest_neighbour(data, (4, 1)) == (3, 1)
    assert module09.find_lowest_neighbour(data, (4, 0)) is None
    
def test_find_endpoint():
    data = module09.read_data('test_input.txt')
    assert module09.find_endpoint(data, (0, 0)) == (0, 1)
    assert module09.find_endpoint(data, (0, 1)) == (0, 1)
    assert module09.find_endpoint(data, (1, 1)) is None
    assert module09.find_endpoint(data, (1, 0)) == (0, 1)
    assert module09.find_endpoint(data, (2, 5)) == (2, 2)

    
def test_find_3_largest_basin_sizes():
    basins = {
        (1, 1): [(1, 1), (1, 2), (1, 3)],
        (2, 1): [(2, 1)],
        (3, 1): [(3, 1), (3, 2), (3, 3), (3, 4)],
        (4, 1): [(4, 1), (4, 2)]
    }
    
    assert module09.find_score_from_basins_definition(basins) == 4 * 3 * 2
