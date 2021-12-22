import module22
from module22 import Cube

def test_parse_line():
    pass
    #assert module22.parse_line('on x=10..12,y=20..22,z=30..32') == {'target_value': 1, 'coord_range':module22.Cube(((10, 12), (20, 22), (30, 32)))}
    #assert module22.parse_line('on x=10..12,y=-20..22,z=-40..-4') == {'target_value': 1, 'coord_range':module22.Cube(((10, 12), (-20, 22), (-40, -4)))}
    

def test_threshold():
    assert module22.apply_threshold(-52, 50) == -50
    assert module22.apply_threshold(-48, 50) == -48
    
    assert module22.apply_threshold(52, 50) == 50
    
    assert module22.apply_threshold(48, 50) == 48

def test_do_ranges_intersect():
    assert module22.do_ranges_intersect((10, 20), (20, 24))
    assert module22.do_ranges_intersect((10, 20), (5, 10))
    assert module22.do_ranges_intersect((-10, 20), (5, 10))
    assert not module22.do_ranges_intersect((10, 20), (21, 24))
    assert not module22.do_ranges_intersect((-40, -21), (-20, 24))

    
def test_do_cubes_intersect():
    assert module22.Cube(((0, 10), (0, 10), (0, 10))).is_intersecting_with(
        module22.Cube(((10, 110), (10, 110), (10, 110)))
    )
    
def test_is_intersecting_with_any():
    cube = Cube(((0, 5), (0, 5), (0, 5)))
    
    cubes_overlap = [
        Cube(((3, 10), (3, 10), (3, 10))),
        Cube(((0, 5), (6, 10), (0, 5))),
        Cube(((0, 5), (0, 5), (-5, -1)))
        
    ]
    
    cubes_no_overlap = [
        Cube(((6, 10), (0, 5), (0, 5))),
        Cube(((0, 5), (6, 10), (0, 5))),
        Cube(((0, 5), (0, 5), (-5, -1)))
        
    ]
    
    
    assert cube.is_intersecting_with_any(cubes_overlap)
    assert not cube.is_intersecting_with_any(cubes_no_overlap)
    assert not cube.is_intersecting_with_any([])
    
def test_solve1():
    data = module22.read_data('test_input_1.txt')
    #assert module22.solve1(data) == 39
    
    data = module22.read_data('test_input_2.txt')
    #assert module22.solve1(data) == 590784
    