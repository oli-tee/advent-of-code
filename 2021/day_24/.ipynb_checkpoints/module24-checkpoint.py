import numpy as np
from typing import List, Dict

 
class Alu():
    
    
    def __init__(self):
        self.state = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    
    def load_instructions_from_list(self, data: List[Dict]):
        self.data = data
        
    def load_instructions_from_file(self, file_name: str):
        self.instructions = Alu.read_data(file_name)

    def load_input(self, input):
        self.input = input
    
    def clean_instructions(self):
        self.instructions = [
            row for row in self.instructions if not(row['operation'] == 'div' and row['input_2'] == '1')
            
        ]
        
    def run_operation_v2(self, row, input):
        
        func_dict = {
            'add': lambda a, b: a + b,
            'mul': lambda a, b: a * b,
            'div': lambda a, b: a // b,
            'mod': lambda a, b: np.mod(a, b),
            'eql': lambda a, b: int(a == b),
            'inp': None
        }

        operation = row['operation']
        input_1 = row['input_1']


        if operation == 'inp':
            self.state[input_1] = int(input)
        else:
            input_2 = row['input_2']
            if input_2.isnumeric() or (input_2[0] == '-' and input_2[1:].isnumeric()):
                x2 = int(input_2)
            else:
                x2 = self.state[input_2]
            x1 = self.state[input_1]

 
            result = func_dict[operation](x1, x2)
  
            self.state[input_1] = result
    
    def run_operation(self, row):
        
        func_dict = {
            'add': lambda a, b: a + b,
            'mul': lambda a, b: a * b,
            'div': lambda a, b: a // b,
            'mod': lambda a, b: np.mod(a, b),
            'eql': lambda a, b: int(a == b),
            'inp': None
        }

        operation = row['operation']
        input_1 = row['input_1']


        if operation == 'inp':
            self.state[input_1] = int(self.input[0])
            self.input = self.input[1:]
        else:
            input_2 = row['input_2']
            if input_2.isnumeric() or (input_2[0] == '-' and input_2[1:].isnumeric()):
                x2 = int(input_2)
            else:
                x2 = self.state[input_2]
            x1 = self.state[input_1]

 
            result = func_dict[operation](x1, x2)
  
            self.state[input_1] = result

    
    def __repr__(self):
        return f"state:{str(self.state)}"
    
    def __print__(self):
        return f"state:{str(self.state)}"
        
        
    @staticmethod
    def read_data(file_name):
        rows = open(file_name).read().split('\n')
        return [Alu.parse_row(row) for row in rows if row != '']
    
    @staticmethod
    def parse_row(row):

        elements = row.split(' ')

        if len(elements) == 3:
            return {'operation': elements[0], 'input_1': elements[1], 'input_2': elements[2]}
        else:
            return {'operation': elements[0], 'input_1': elements[1]}
    
 
    def run_all_instructions(self, input: str, verbose=False):
        
        self.state = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
        
        if input != None:
            self.input = input
         
        for row in self.instructions:
            
            
                
            self.run_operation(row)
            
            if verbose:
                if row['operation'] == 'inp':
                    print('---input---')
                print(self.state)
            
            #print(self.state)


def apply_instruction(state, instruction, input):
    func_dict = {
        'add': lambda a, b: a + b,
        'mul': lambda a, b: a * b,
        'div': lambda a, b: a // b,
        'mod': lambda a, b: np.mod(a, b),
        'eql': lambda a, b: int(a == b),
        'inp': None
    }

    operation = instruction['operation']
    input_1 = instruction['input_1']


    if operation == 'inp':
        state[input_1] = int(input)
    else:
        input_2 = instruction['input_2']

        if input_2.isnumeric() or (input_2[0] == '-' and input_2[1:].isnumeric()):
            x2 = int(input_2)
        else:
            x2 = state[input_2]

        x1 = state[input_1]


        result = func_dict[operation](x1, x2)

        state[input_1] = result
    
    return state

def apply_instruction_block(state, block, input):
    state_copy = dict(state)
    input = input + 'x'
    for instruction in block:

        state_copy = apply_instruction(state_copy, instruction, input[0])
        if instruction['operation'] == 'inp':
            input = input[1:]
    
    return state_copy


def compile(instructions):
    instruction_blocks = []
    current_block = []
    i = 0
    while i < len(instructions):
        ins = instructions[i]
        
        current_block.append(ins)
        
        if i == len(instructions) - 1 or instructions[i+1]['operation'] == 'inp':
            instruction_blocks.append(current_block)
            current_block = []
        i+=1
        
    return instruction_blocks


def recurs(state, instruction_blocks, input_so_far):
    print(input_so_far, end='\r')
    if len(instruction_blocks) == 0:
        if state['z'] == 0:
            return [(input_so_far, state)]
        else:
            return []
        
    this_block = instruction_blocks[0]
    adder = this_block[-13]['input_2']
    #print(adder)
    wish = (state['z'] % 26) + int(adder)
    if wish >= 1 and wish <= 9:
        this_input = str(wish)
        new_state = apply_instruction_block(state, this_block, this_input)
        return recurs(new_state, instruction_blocks[1:], input_so_far + this_input)
        
        return full_input
    elif int(adder) >= -25 and int(adder) <= 9:
        return []
    else:
        possibles = []
        for input in range(1, 10):
            possibles += recurs(
                apply_instruction_block(state, this_block, str(input)),
                instruction_blocks[1:],
                input_so_far + str(input)
            )
        return possibles
