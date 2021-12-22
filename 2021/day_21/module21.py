class Die():
    def __init__(self):
        pass
    
    def throw(self) -> int:
        pass
    
    
class DeterministicDie(Die):
    def __init__(self):
        self.status = 0
        
    
    def throw(self):
        self.status = (self.status + 1 - 1) % 100 + 1
        return self.status
    

class Game():
    def __init__(self, starting_position_1: int, starting_position_2: int, die: Die):
        self.pos = [starting_position_1, starting_position_2]

        self.score = [0, 0]

        self.die = die
        self.next_player_to_play = 1
        self.die_roll_count = 0

        
    
    def display(self):
        print(f"positions: {self.pos[0]}  -  {self.pos[1]}")
        print(f"scores.  : {self.score[0]}  -  {self.score[1]}")
        print(f"{self.die_roll_count} rolls of dice")

    def play(self):
        player_index = self.next_player_to_play
        die_throw = self.die.throw() + self.die.throw() + self.die.throw()
        self.die_roll_count += 3
        self.pos[player_index-1] = (self.pos[player_index-1] + die_throw - 1) % 10 + 1
        self.score[player_index-1] += self.pos[player_index-1]
        self.next_player_to_play = 3 - self.next_player_to_play
        
    def get_winner(self):
        if self.score[0] >= 1000: 
            return 1
        elif self.score[1] >= 1000: 
            return 2
        else:
            return None
        
    def play_until_win(self):
        while self.get_winner() is None:
            self.play()
        

        print("Victory!")
        self.display()
        return self.get_winner()
            
        
def solve1(start_pos_1, start_pos_2):
    g = Game(start_pos_1, start_pos_2, DeterministicDie())
    g.play_until_win()
    
    score = g.score[3 - g.get_winner()-1] * g.die_roll_count
    
    return score


