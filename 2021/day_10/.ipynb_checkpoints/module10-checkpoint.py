import numpy as np

def read_data(file_name):
    rows = open(file_name).read().split('\n')
    return [row for row in rows if row != '']


def find_first_invalid_closing_bracket(chunk):
    brackets_lifo = []
    index = 0
    first_invalid = None
    closing = ['}', ')', ']', '>']
    opening = ['{', '(', '[', '<']
    bracket_map_closing_to_opening = {'}': '{', ']': '[', ')': '(', '>': '<'}

    while index < len(chunk) and first_invalid is None:
        new_char = chunk[index]
        if new_char in opening:
            brackets_lifo = [new_char] + brackets_lifo
        else:
            expected_matching_opening = bracket_map_closing_to_opening[new_char]
            if brackets_lifo[0] != expected_matching_opening:
                first_invalid = new_char
            else:
                brackets_lifo = brackets_lifo[1:]
        
        index += 1
    
    return first_invalid
    
def solve1(data):
    
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        None: 0
    }

    return sum([score_map[find_first_invalid_closing_bracket(row)] for row in data])


def find_missing_sequence(chunk):
    brackets_lifo = []
    index = 0
    
    closing = ['}', ')', ']', '>']
    opening = ['{', '(', '[', '<']
    bracket_map_closing_to_opening = {'}': '{', ']': '[', ')': '(', '>': '<'}
    bracket_map_opening_to_closing = {'{': '}' , '[': ']',  '(': ')', '<': '>'}
    chunk_is_invalid = False
    
    while index < len(chunk) and not chunk_is_invalid:
        new_char = chunk[index]
        if new_char in opening:
            brackets_lifo = [new_char] + brackets_lifo
        else:
            expected_matching_opening = bracket_map_closing_to_opening[new_char]
            if brackets_lifo[0] != expected_matching_opening:
                chunk_is_invalid = True
            else:
                brackets_lifo = brackets_lifo[1:]
        
        index += 1
    
    if chunk_is_invalid:
        return None
    else:
        return ''.join([bracket_map_opening_to_closing[opener] for opener in brackets_lifo])

def get_autocomplete_score(autocomplete_chunk):
    score_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    
    if autocomplete_chunk == '' or autocomplete_chunk is None:
        return 0
    
    total_score = 0
    for char in autocomplete_chunk:
        total_score *= 5
        total_score += score_map[char]
    
    return total_score

def solve2(data):
    scores = [get_autocomplete_score(find_missing_sequence(row)) for row in data]
    
    return int(np.median([x for x in scores if x > 0]))