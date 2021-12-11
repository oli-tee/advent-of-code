def read_data(file_name):
    output = open(file_name).read().split('\n\n')
    return output
    
def parse_item(string):
    
    output = string.replace('\n', ' ').split(' ')

    output2 = {x.split(':')[0]: x.split(':')[1] for x in output}
    
    return output2