import numpy as np
from typing import List

BRACKET_MAP_OPENING_TO_CLOSING = {'{': '}' , '[': ']',  '(': ')', '<': '>'}
    
def read_data(file_name: str) -> List[str]:
    rows = open(file_name).read().split('\n')
    return [row for row in rows if row != '']


def solve1(data: List[str]) -> int:
    
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        None: 0
    }
    
    final_score = sum(
        [
            score_map[find_first_invalid_closing_bracket(row)]
            for row in data
        ]
    )
    
    return final_score


def find_first_invalid_closing_bracket(chunk: str) -> str:
    brackets_lifo = []
    index = 0
    first_invalid = None
    
    openers = get_list_of_openers()
    

    while index < len(chunk) and first_invalid is None:
        new_char = chunk[index]
        if new_char in openers:
            brackets_lifo = [new_char] + brackets_lifo
        else:
            expected_matching_opening = get_matching_opener(new_char)
            if brackets_lifo[0] != expected_matching_opening:
                first_invalid = new_char
            else:
                brackets_lifo = brackets_lifo[1:]
        
        index += 1
    
    return first_invalid


def get_list_of_openers():
    return BRACKET_MAP_OPENING_TO_CLOSING.keys()
    
def get_list_of_closers():
    return BRACKET_MAP_OPENING_TO_CLOSING.values()
    
def get_matching_closer(opener: str):
    if opener in BRACKET_MAP_OPENING_TO_CLOSING:
        return BRACKET_MAP_OPENING_TO_CLOSING[opener]
    else:
        return None
    
def get_matching_opener(closer: str):
    inv_map = {v: k for k, v in BRACKET_MAP_OPENING_TO_CLOSING.items()}
    if closer in inv_map:
        return inv_map[closer]
    else:
        return None

def solve2(data: List[str]) -> int:
    scores = [
        get_autocomplete_score(find_missing_sequence(row))
        for row in data
    ]
    
    return int(np.median([x for x in scores if x > 0]))


def find_missing_sequence(chunk:str) -> List[str]:
    brackets_lifo = []
    index = 0
    
    closers = get_list_of_closers()
    openers = get_list_of_openers()

    chunk_is_invalid = False
    
    while index < len(chunk) and not chunk_is_invalid:
        new_char = chunk[index]
        if new_char in opening:
            brackets_lifo = [new_char] + brackets_lifo
        else:
            expected_matching_opening = get_matching_opener(new_char)
            if brackets_lifo[0] == expected_matching_opening:
                brackets_lifo = brackets_lifo[1:]
            else:
                chunk_is_invalid = True
        
        index += 1
    
    if chunk_is_invalid:
        return None
    else:
        return ''.join([get_matching_closer(opener) for opener in brackets_lifo])


def get_autocomplete_score(autocomplete_chunk: str) -> int:
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

