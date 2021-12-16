from typing import Dict, List, Tuple
from collections import defaultdict

def read_data(file_name: str) -> Dict:
    content = open(file_name).read().split('\n\n')
    template = content[0].strip()
    rules = content[1]
    result = dict()
    
    result['template'] = template
    result['rules'] = {
        
            row.split(' -> ')[0].strip():
            row.split(' -> ')[1].strip()
         for row in rules.split('\n')
        if row != ''
    }
    return result


def solve1(data, nsteps, verbose=False):
    # we'll need those 2 for the element count, and the first and last are immutable through transformations
    first_element = data['template'][0]
    last_element = data['template'][-1]
    
    
    pair_hash = turn_template_into_hash(data['template'])
    rules = data['rules']

    for step in range(nsteps):
        pair_hash = apply_one_step(pair_hash, rules)
    
    element_hash = get_element_count(pair_hash, first_element, last_element)
    final_score = get_score_from_element_hash(element_hash)
    
    return final_score

def turn_template_into_hash(template:str) -> Dict[str, int]:
    
    counter = defaultdict(int)
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        counter[pair] += 1
        
    return counter

def apply_one_step(pair_hash: Dict[str, int], rules: Dict[str, str], verbose=False) -> Dict[str, int]:
    result = defaultdict(int)
    
    for pair, pair_count in pair_hash.items():
        to_insert = rules[pair]
        if pair not in rules:
            raise ValueError
        new_pair_1 = pair[0] + to_insert
        new_pair_2 = to_insert + pair[1]
        
        result[new_pair_1] += pair_count
        result[new_pair_2] += pair_count
        if verbose:
            print(result)
    
    return result


def get_element_count(pair_hash: Dict[str, str], first_element:str, last_element:str) -> Dict[str, str]:
    element_hash = defaultdict(int)
    
    for pair, pair_count in pair_hash.items():
        element_hash[pair[0]] += pair_count
        element_hash[pair[1]] += pair_count
    
    # actually each element was counted twice, except the first and last ones
    for element in element_hash:
        if element in [first_element, last_element]:
            element_hash[element] = int((element_hash[element] + 1) / 2)
        else:
            element_hash[element] = int(element_hash[element] / 2)
        
    return element_hash
        
def get_score_from_element_hash(element_hash: Dict[str, str]) -> int:
    # get the difference between the count of the most common element minus the least common
    score = max(element_hash.values()) - min(element_hash.values())
    return score 
