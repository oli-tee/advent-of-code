import re

def read_data(file_name):
    rows = open(file_name, 'r').read().split('\n')
    return [row.strip() for row in rows if row.strip() != '']


def find_first_digit(word: str) -> str:
    matches = re.findall(pattern='\d', string=word)
    if len(matches) > 0:
        return matches[0]
    else:
        return None

    
def find_last_digit(word: str) -> str:
    matches = re.findall(pattern='\d', string=word)
    if len(matches) > 0:
        return matches[-1]
    else:
        return None

    
def decode(word: str) -> int:
    digit1 = find_first_digit(word)
    digit2 = find_first_digit(word[::-1])
    return int(digit1 + digit2)


def solve(word_list):
    numbers = [decode(word) for word in word_list]
    return sum(numbers)

def replace_this_number(word, i, number_str):
    key = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    number_len = len(number_str)
    if i + number_len <= len(word) and word[i:i+number_len] == number_str:
        number_int = key[number_str]
        word = word[:i] + f"{number_int}" + word[i+number_len:]
    return word, i

def parse_numbers_forward(word):
    i = 0
    while i < len(word):
        for number_str in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
            word, i = replace_this_number(word, i, number_str)   
        i += 1
        # print(f"{i} / {len(word)}")
    return word

def parse_numbers_backward(word):
    i = len(word)
    while i >= 0:
        for number_str in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
            word, i = replace_this_number(word, i, number_str)   
        i -= 1
       # print(f"{i} / {len(word)}")
    return word

def decode_p2(word: str) -> int:
    digit1 = find_first_digit(parse_numbers_forward(word))
    digit2 = find_last_digit(parse_numbers_backward(word))
    return int(digit1 + digit2)

def solve_p2(word_list):
    numbers = [decode_p2(word) for word in word_list]
    return sum(numbers)

    