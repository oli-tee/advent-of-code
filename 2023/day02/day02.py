import re

def test():
    return True

def read_data(file_name):
    rows = open(file_name, 'r').read().split('\n')
    return [row.strip() for row in rows if row.strip() != '']


def parse_game(game_desc):
    game_desc = re.sub(r"Game \d*: ", '', game_desc)
    draws = game_desc.split(';')
    draws = [draw.strip() for draw in draws]
    return [parse_draw(draw) for draw in draws]
    

def parse_draw(draw):
    colors = ['red', 'green', 'blue']
    draw_dict = {}
    for color in colors:
        scan = re.findall(r"(\d*) " + color, draw)
        if len(scan) > 0:
            draw_dict[color] = int(scan[0])
        else:
            draw_dict[color] = 0
    return draw_dict

def is_valid_game(game_desc, nr_red, nr_green, nr_blue):
    draws = parse_game(game_desc)
    max_red = max([draw['red'] for draw in draws])
    max_green = max([draw['green'] for draw in draws])
    max_blue = max([draw['blue'] for draw in draws])
    
    is_valid = max_red <= nr_red and max_green <= nr_green and max_blue <= nr_blue
    return is_valid


def solve(data):
    score = 0
    for i in range(len(data)):
        if is_valid_game(data[i], 12, 13, 14):
            print(f'game {i} is valid!')
            score += (i + 1)
        
    return score

def get_power(game_desc):
    draws = parse_game(game_desc)
    max_red = max([draw['red'] for draw in draws])
    max_green = max([draw['green'] for draw in draws])
    max_blue = max([draw['blue'] for draw in draws])
    
    return max_red * max_green * max_blue

def solve_p2(data):
    return sum([get_power(game_desc) for game_desc in data])
