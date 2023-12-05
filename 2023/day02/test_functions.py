import day02

def test_test():
    assert day02.test() 
    
def test_parse_draw():
    res1 = day02.parse_draw("1 red, 10 blue, 5 green")
    assert res1['red'] == 1
    assert res1['blue'] == 10
    assert res1['green'] == 5
    
    
    res2 = day02.parse_draw("5 green, 1 red, 10 blue")
    assert res1['red'] == 1
    assert res1['blue'] == 10
    assert res1['green'] == 5
    
    res3 = day02.parse_draw("5 green, 10 blue")
    assert res1['blue'] == 10
    assert res1['green'] == 5
    
    
def test_parse_game():
    res1 = day02.parse_game("'1 red, 10 blue, 5 green; 11 blue, 6 green; 6 green; 1 green, 1 red, 12 blue; 3 blue; 3 blue, 4 green, 1 red'")
    draw1 = res1[0]
    assert draw1['red'] == 1
    assert draw1['blue'] == 10
    assert draw1['green'] == 5
    
    
    draw2 = res1[1]
    assert draw2['blue'] == 11
    assert draw2['green'] == 6

