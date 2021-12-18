from typing import Tuple, Dict
import numpy as np



def solve1_positive(target: Tuple[Tuple, Tuple]):
    "assuming the best choice is to go right"
    max_abs_x = max(abs(target[0][0]), abs(target[0][1]))
    max_abs_y = max(abs(target[1][0]), abs(target[1][1]))
    
    got_a_hit = False
    
    current_vy = max_abs_y + 1
    
    while not got_a_hit and current_vy > -1000:
        current_vy -= 1
        for vx in range(max_abs_x + 1):
            if is_hitting_target((vx, current_vy), target)[0]:
                return is_hitting_target((vx, current_vy), target)[1]


def solve2_positive(target):
    "assuming the best choice is to go right"
    max_abs_x = max(abs(target[0][0]), abs(target[0][1]))
    max_abs_y = max(abs(target[1][0]), abs(target[1][1]))
    
    got_a_hit = False
    
    current_vy = max_abs_y + 1
    
    hit_counter = 0
    
    while not got_a_hit and current_vy > -1000:
        current_vy -= 1
        for vx in range(max_abs_x + 1):
            if is_hitting_target((vx, current_vy), target)[0]:
                hit_counter += 1
            
    return hit_counter
    
    
def reduce_horizontal_velocity(horizontal_velocity):
    if horizontal_velocity > 0:
        return horizontal_velocity - 1
    elif horizontal_velocity < 0:
        return horizontal_velocity + 1
    else:
        return horizontal_velocity

def move(position_and_velocity: Dict[str, Tuple]) -> Dict[str, Tuple]:
    final_position = (
        position_and_velocity['pos'][0] + position_and_velocity['vel'][0],
        position_and_velocity['pos'][1] + position_and_velocity['vel'][1]
    )
    
    final_velocity = (
        reduce_horizontal_velocity(position_and_velocity['vel'][0]),
        position_and_velocity['vel'][1] - 1
    )
    
    return {
        'pos': final_position,
        'vel': final_velocity
    }

def get_final_x(intial_x_velocity):
    n = intial_x_velocity
    return int(intial_x_velocity * (intial_x_velocity + 1)/2)

def is_hit(pos_and_vel, target):
    return (
        pos_and_vel['pos'][0] >= target[0][0] and
        pos_and_vel['pos'][0] <= target[0][1] and
        pos_and_vel['pos'][1] >= target[1][0] and
        pos_and_vel['pos'][1] <= target[1][1]
    )
        
        
def is_hit_possible(pos_and_vel: Dict, target: Tuple):
    # on vertical axis:
    if pos_and_vel['vel'][1] < 0 and pos_and_vel['pos'][1] < target[1][0]:

        return False
    
    # on horizontal:
    if pos_and_vel['vel'][0] > 0:
        min_x = pos_and_vel['pos'][0]
        max_x = pos_and_vel['pos'][0] + (pos_and_vel['vel'][0] * (pos_and_vel['vel'][0] + 1)) / 2

    else:
        max_x = pos_and_vel['pos'][0]
        min_x = pos_and_vel['pos'][0] - (-pos_and_vel['vel'][0] * (-pos_and_vel['vel'][0] + 1)) / 2

    if max_x < target[0][0]:

        return False
    elif min_x > target[0][1]:

        return False
    
    return True

def is_hitting_target(start_velocity: Tuple[int], target: Tuple[Tuple[int], Tuple[int]], verbose=False) -> bool:

    john = {'pos': (0, 0), 'vel': start_velocity}
    
    if verbose:
        print(john)
    max_y_pos = -np.inf
    
    while is_hit_possible(john, target) and not is_hit(john, target):
        
        john = move(john)
        max_y_pos = max(max_y_pos, john['pos'][1])
        if verbose:
            print(john)
    
    return (is_hit(john, target), max_y_pos)
    
