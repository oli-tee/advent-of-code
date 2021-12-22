import module21
import module21b

def test_game():
    g = module21.Game(4, 8, module21.DeterministicDie())
    g.play()
    assert g.pos[0] == 10
    assert g.score[0] == 10
    
    g.play()
    assert g.pos[1] == 3
    assert g.score[1] == 3
    
    g.play()
    assert g.pos[0] == 4
    assert g.score[0] == 14
    
    g.play()
    assert g.pos[1] == 6
    assert g.score[1] == 9
    
def test_solve1():
    assert module21.solve1(4, 8) == 739785

def test_solve2():
    assert module21b.solve2(4, 8, 21) == 444356092776315
    
def test_count_wins():
    
    assert module21b.count_wins(4, 8, 21, this_player_starts=True) == 444356092776315
    assert module21b.count_wins(8, 4, 21, this_player_starts=False) == 341960390180808