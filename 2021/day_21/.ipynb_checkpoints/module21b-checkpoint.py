import numpy as np
from typing import List, Dict, Tuple


def solve2(start_pos_1: int, start_pos_2: int, target: int) -> int:
    return max(
        count_wins(start_pos_1, start_pos_2, target, this_player_starts=True),
        count_wins(start_pos_2, start_pos_1, target, this_player_starts=False)
    )

def count_wins(start_pos: int, start_pos_opponent: int, target: int, this_player_starts: bool) -> int:
    
    winning_trajectories_1 = find_all_winning_trajectories(start_pos, target_score=target)

    min_moves_1 = np.min([len(win['rolls']) for win in winning_trajectories_1])
    max_moves_1 = np.max([len(win['rolls']) for win in winning_trajectories_1])

    min_moves_1, max_moves_1

    how_many_actual_ways_to_lose = dict()

    # generate losing counts
    for max_rolls in range(min_moves_1 - 2, max_moves_1 + 1):
        losers = find_all_losing_trajectories(start_pos_opponent, target_score=target, max_rolls=max_rolls)
        how_many_actual_ways_to_lose[max_rolls] = np.sum([how_many_ways_to_get_sequences(t['rolls']) for t in losers])
    
    
    
    if this_player_starts:
        turn_count_offset = 0
    else:
        turn_count_offset = 1
    
    result1 = np.sum([
        how_many_ways_to_get_sequences(win1['rolls'])
        * how_many_actual_ways_to_lose[len(win1['rolls']) - 1 + turn_count_offset]

        for win1 in winning_trajectories_1  
    ])
        
    
    return result1


def find_all_winning_trajectories(start_position: int,target_score: int) -> List[Dict[str, List[int]]]:
    return find_all_trajectories_recurs(0, start_position, target_score, [], [])


def find_all_trajectories_recurs(
    start_score: int, start_position: int,target_score: int, draws_so_far: List[int], scores_so_far: List[int]
) -> List[Dict[str, List[int]]]:

    
    if start_score >= target_score:

        all_possibles = [{'rolls': draws_so_far, 'scores': scores_so_far}]

        return all_possibles
 

    else:
        all_possibles = []
        possible_rolls = [3, 4, 5, 6, 7, 8, 9]
        for draw in possible_rolls:

            new_score, new_pos = score_after_rolling_x(start_score, start_position, draw)
            #print('ok so far')
            possibles_trajectories = find_all_trajectories_recurs(
                new_score,
                new_pos,
                target_score,
                draws_so_far + [draw],
                scores_so_far + [new_score]
            )

            all_possibles += possibles_trajectories
        

        return all_possibles

    
def score_after_rolling_x(initial_score: int, initial_position: int, roll: int) -> Tuple[int, int]:
    new_position = (initial_position + roll - 1) % 10 + 1
    new_score = initial_score + new_position
    return new_score, new_position


def how_many_ways_to_get_sequences(seq: List[int]) -> int:
    how_many_ways_to_roll_x = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    return np.product([how_many_ways_to_roll_x[x] for x in seq])


def find_all_losing_trajectories(start_position: int, target_score: int, max_rolls: int) -> List[Dict[str, List[int]]]:
    trajs = find_all_losing_trajectories_nrolls_recurs(0, start_position, max_rolls, target_score, [], [])
    if len(trajs) == 1:
        return trajs
    else:
        losing_trajs = [t for t in trajs if t['scores'][-1] < target_score]
    
    return losing_trajs
        

def find_all_losing_trajectories_nrolls_recurs(
    start_score: int, start_position: int, max_rolls: int, target: int, draws_so_far: List[int], scores_so_far: List[int]
) -> List[Dict[str, List[int]]]:
    #BFS

    if len(draws_so_far) >= max_rolls:

        all_possibles = [{'rolls': draws_so_far, 'scores': scores_so_far}]

        return all_possibles
 
    elif len(scores_so_far)>0 and scores_so_far[-1] > target:
        return []
    else:
        all_possibles = []
        possible_rolls = [3, 4, 5, 6, 7, 8, 9]
        for draw in possible_rolls:
            new_score, new_pos = score_after_rolling_x(start_score, start_position, draw)
            if new_score < target:

                possibles_trajectories = find_all_losing_trajectories_nrolls_recurs(
                    new_score,
                    new_pos,
                    max_rolls,
                    target,
                    draws_so_far + [draw],
                    scores_so_far + [new_score]
                )

                all_possibles += possibles_trajectories
        
        return [x for x in all_possibles if x['scores'][-1] < target]
    


