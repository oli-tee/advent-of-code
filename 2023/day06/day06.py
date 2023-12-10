import re

def read_data(file_name):
    rows = open(file_name, 'r').read().split('\n')
    rows = [row.strip() for row in rows if row.strip() != '']
    return rows

def parse_data(rows):
    list_time = [int(x) for x in re.findall(r'(\d*)', rows[0]) if len(x) > 0]
    list_distance = [int(x) for x in re.findall(r'(\d*)', rows[1]) if len(x) > 0]
    data = [(list_time[i], list_distance[i]) for i in range(len(list_time))]
    return data

def parse_data_p2(rows):
    rows = [r.replace(' ', '') for r in rows]  
    return parse_data(rows)


def count_winning_strategies(time, record_distance):
    counter = 0
    for hold_time in range(time):
        
        distance = hold_time * (time - hold_time)
        if distance > record_distance:
            counter += 1
        
    return counter
        
        
def solve_p1(file_name):
    data = parse_data(read_data(file_name))
    
    score = 1
    for game in data:
        score *= count_winning_strategies(game[0], game[1])
    
    return score

        
def solve_p2(file_name):
    data = parse_data_p2(read_data(file_name))
    
    score = 1
    for game in data:
        score *= count_winning_strategies(game[0], game[1])
    
    return score