from typing import Tuple
from collections import Counter

def read_data(file_name):
    rows = open(file_name, 'r').read().split('\n')
    rows = [row.strip() for row in rows if row.strip() != '']
    return rows

def parse_row(row: str) -> Tuple[str, int]:
    split = row.split(' ')
    return (split[0], int(split[1]))
    
def parse_data(rows):
    return [parse_row(row) for row in rows]

def convert_hand_to_hex(hand: str):
    hex_str = (
        hand
        .replace('A', 'e')
        .replace('K', 'd')
        .replace('Q', 'c')
        .replace('J', 'b')
        .replace('T', 'a')
    )
    return int(hex_str, 16)


def convert_hand_to_hex_p2(hand: str):
    hex_str = (
        hand
        .replace('A', 'e')
        .replace('K', 'd')
        .replace('Q', 'c')
        .replace('J', '1')
        .replace('T', 'a')
    )
    return int(hex_str, 16)

def score_pattern(hand: str):
    counters = dict(Counter(hand))
    values = [counters[key] for key in counters]
    value_counter = dict(Counter(values))
    
    if 5 in values:
        return 6
    elif 4 in values:
        return 5
    elif (3 in values) and (2 in values):
        return 4
    elif 3 in values:
        return 3
    elif 2 in values and value_counter[2] == 2:
        return 2
    elif 2 in values:
        return 1
    else:
        return 0
    

def get_possible_value(card: str):
    if card == 'J':
        return ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    else:
        return [card]

def score_pattern_p2(hand: str, verbose=False):
    best_virtual_score = -1
    best_virtual_hand = ""
    
    for card1 in get_possible_value(hand[0]):
        for card2 in get_possible_value(hand[1]):
            for card3 in get_possible_value(hand[2]):
                for card4 in get_possible_value(hand[3]):
                    for card5 in get_possible_value(hand[4]):
                        virtual_hand = card1 + card2 + card3 + card4 + card5
                        virtual_score = score_pattern(virtual_hand)
                        if verbose:
                            print(f"{virtual_hand}: {virtual_score}")
                        if virtual_score >= best_virtual_score:
                            best_virtual_score = virtual_score
                            best_virtual_hand = virtual_hand
    
    return best_virtual_score, best_virtual_hand
    
def score_hand(hand):
    pattern_score = score_pattern(hand)
    hand_content_score = convert_hand_to_hex(hand)
    return pattern_score * (16**5) + hand_content_score

def score_hand_p2(hand):
    pattern_score, best_virtual_hand = score_pattern_p2(hand)
    hand_content_score = convert_hand_to_hex_p2(hand)
    score = pattern_score * (16**5) + hand_content_score
    return score, best_virtual_hand

def score_hands(data):
    scored =  sorted([(score_hand(x[0]), x[0], x[1]) for x in data])
    
    ranked  = [(i+1, scored[i][0], scored[i][1], scored[i][2]) for i in range(len(scored))]
    return ranked

def score_hands_p2(data):
    scored =  sorted([(score_hand_p2(x[0])[0], x[0], x[1], score_hand_p2(x[0])[1]) for x in data])
    
    ranked  = [(i+1, scored[i][0], scored[i][1], scored[i][2], scored[i][3]) for i in range(len(scored))]
    return ranked

def solve_p1(file_name):
    data = parse_data(read_data(file_name))
    
    scored = score_hands(data)
    
    return sum([x[0] * x[3] for x in scored])

def solve_p2(file_name):
    data = parse_data(read_data(file_name))
    
    scored = score_hands_p2(data)
    
    return sum([x[0] * x[3] for x in scored])