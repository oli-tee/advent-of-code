def read_data(file_name):
    data = open(file_name).read().split('\n')
    return [x for x in data if x != '']

def parse_row(row):
    return (row.split(' ')[0], int(row.split(' ')[1]))


def solve(data):
    import pandas as pd
    
    rows = [parse_row(x) for x in data]
    pdf = pd.DataFrame(data=rows, columns=['direction', 'magnitude'])
    grouped_df = pdf.groupby('direction').sum('magnitude')
    final_depth = grouped_df.loc['down']['magnitude'] - grouped_df.loc['up']['magnitude']
    final_x = grouped_df.loc['forward']['magnitude']
    return final_depth * final_x

def solve2(data):
    rows = [parse_row(x) for x in data]
    
    aim = 0
    depth = 0
    horz = 0
    
    for row in rows:
        if row[0] == 'up':
            aim -= row[1]
        elif row[0] == 'down':
            aim += row[1]
        elif row[0] == 'forward':
            horz += row[1]
            depth += row[1] * aim
        else:
            print(row[0])
            raise ValueError
    return horz * depth
        

def test_functions():
    assert parse_row('forward 2') == ('forward', 2)
    assert solve(['down 10', 'down 20', 'up 5', 'forward 1', 'forward 9']) == 250
    assert solve(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 150
    assert solve2(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 900
