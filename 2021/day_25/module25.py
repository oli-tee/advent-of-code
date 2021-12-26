import numpy as np

def read_data(file_name):
    rows = [row for row in open(file_name).read().split('\n') if row != '']
    return np.array([list(row) for row in rows])

def is_next_space_free(matrix, coord, axis):
    row = coord[0]
    col = coord[1]
    # axis = 0: one down. Axis = 1: one right
    if axis == 1:
        next_value = matrix[row, (col + 1) % matrix.shape[1]]
    elif axis == 0:
        next_value = matrix[(row + 1) % matrix.shape[0], col]

    else:
        raise ValueError
    
    return next_value == '.'

class Trench():
    
    def __init__(self, data):
        self.cucs = data
    
    def __print__(self):
        return self.cucs.__repr__()
    
    def __repr__(self):
        return self.cucs.__repr__()

    def move_right(self) -> int:
    
        unzipped_right_cuc = np.where(self.cucs == '>')

        right_cuc = [(unzipped_right_cuc[0][i], unzipped_right_cuc[1][i]) for i in range(len(unzipped_right_cuc[0]))]

        mobile_right_cuc = [cuc for cuc in right_cuc if is_next_space_free(self.cucs, cuc, 1)]

        for cuc in mobile_right_cuc:
            self.cucs[cuc[0], (cuc[1] + 1) % self.cucs.shape[1]] = '>'
            self.cucs[cuc[0], cuc[1]] = '.'
            
        return len(mobile_right_cuc)
            
    def move_down(self) -> int:
        unzipped_down_cuc = np.where(self.cucs == 'v')

        down_cuc = [(unzipped_down_cuc[0][i], unzipped_down_cuc[1][i]) for i in range(len(unzipped_down_cuc[0]))]

        mobile_down_cuc = [cuc for cuc in down_cuc if is_next_space_free(self.cucs, cuc, axis=0)]

        for cuc in mobile_down_cuc:
            self.cucs[(cuc[0] + 1) % self.cucs.shape[0], cuc[1]] = 'v'
            self.cucs[cuc[0], cuc[1]] = '.'
        
        return len(mobile_down_cuc)
            
            
    def step(self):
        right_moves = self.move_right()
        down_moves = self.move_down()
        return right_moves + down_moves
    
    def run_n_steps(self, n):
        for i in range(n):
            #print(i)
            self.step()
            #print(self.cucs)
    
    def run_until_blocked(self, max_steps):
        fuse = max_steps
        moves = 1
        step_counter = 0
        while fuse > 0 and moves != 0:
            if step_counter % (max_steps / 10) == 0:
                print(f"{step_counter} steps done")
            #print(step_counter)
            fuse -= 1
            
            moves = self.step()
 
            step_counter += 1
    
        if fuse == 0:
            print("FUSED!")
            return None
            
        return step_counter
        
        
            