from typing import List
import numpy as np

def read_data(file_name):
    temp = open(file_name).read().split(',')
    return [int(x) for x in temp]


def calculate_fuel_cost(positions: List[int], target: int) -> int:
    return np.sum(np.abs(np.array(positions) - target))
    
    
def solve_bruteforce(data):
    min_x = min(data)
    max_x = max(data)
    best_cost = None
    for x in range(min_x, max_x+1):
        this_cost = calculate_fuel_cost(data, x)
        if best_cost is None or this_cost < best_cost:
            best_cost = this_cost
    
    return best_cost

def solve_median(data):
    med = int(np.median(data))
    best_cost = None
    for x in range(med-1, med+2):
        this_cost = calculate_fuel_cost(data, x)
        if best_cost is None or this_cost < best_cost:
            best_cost = this_cost
    
    return best_cost


def calculate_individual_cost_2(start, end):
    n = abs(start - end)
    return int(n*(n+1) / 2)

def calculate_fuel_cost_2(positions: List[int], target: int) -> int:
    dist_array = np.abs((np.array(positions) - target))
    cost = int(np.sum(dist_array * (dist_array + 1) / 2))
    return cost
    
    
def solve_2(data):
    min_x = min(data)
    max_x = max(data)
    best_cost = None
    for x in range(min_x, max_x+1):
        this_cost = calculate_fuel_cost_2(data, x)
        if best_cost is None or this_cost < best_cost:
            best_cost = this_cost
    
    return best_cost