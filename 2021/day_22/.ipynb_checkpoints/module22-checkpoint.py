import re
from collections import defaultdict
from typing import Dict, List, Tuple
import numpy as np
from collections import defaultdict

class Cube():
    def __init__(self, ranges):
        self.xlim = ranges[0]
        self.ylim = ranges[1]
        self.zlim = ranges[2]

    def is_subset(self, supercube):
        return (
            self.xlim[0] >= supercube.xlim[0] and
            self.xlim[1] <= supercube.xlim[1] and
            self.ylim[0] >= supercube.ylim[0] and
            self.ylim[1] <= supercube.ylim[1] and
            self.zlim[0] >= supercube.zlim[0] and
            self.zlim[1] <= supercube.zlim[1]
        )
    
    def as_tuple(self):
        return (self.xlim, self.ylim, self.zlim)
        
    def is_valid(self):
        return (
            self.xlim[0] >= -50 and
            self.xlim[1] <= 50 and
            self.ylim[0] >= -50 and
            self.ylim[1] <= 50 and
            self.zlim[0] >= -50 and
            self.zlim[1] <= 50 
        
        )
        
        
    def intersect_and_split(self, cube2):
        
        #x_splits = sorted(list(set([self.xlim[0], self.xlim[1]+1, cube2.xlim[0], cube2.xlim[1]+1])))
        #y_splits = sorted(list(set([self.ylim[0], self.ylim[1]+1, cube2.ylim[0], cube2.ylim[1]+1])))
        #z_splits = sorted(list(set([self.zlim[0], self.zlim[1]+1, cube2.zlim[0], cube2.zlim[1]+1])))
        
        subranges_x = create_subranges(self.xlim, cube2.xlim)
        subranges_y = create_subranges(self.ylim, cube2.ylim)
        subranges_z = create_subranges(self.zlim, cube2.zlim)
        
        sub_cubes = [
            Cube((range_x, range_y, range_z))
            for range_x in subranges_x 
            for range_y in subranges_y 
            for range_z in subranges_z
        ]
        
        result = dict()
        result['intersection'] = []
        result['self_only'] = []
        result['other_only'] = []
        
        
        for sc in sub_cubes:
            if sc.is_subset(self) and sc.is_subset(cube2):
                result['intersection'].append(sc)
            elif sc.is_subset(self):
                result['self_only'].append(sc)
            elif sc.is_subset(cube2):
                result['other_only'].append(sc)

                
        
        return result
    
    def is_intersecting_with_any(self, list_of_cubes):
        if len(list_of_cubes) == 0:
            return False
        else:
            return max([self.is_intersecting_with(cube) for cube in list_of_cubes])
       
    def find_intersecting_cubes(self, list_of_cubes):
        return [cube for cube in list_of_cubes if self.is_intersecting_with(cube)]
        
        
    def is_intersecting_with(self, cube):
        result = (
            do_ranges_intersect(self.xlim, cube.xlim) and
            do_ranges_intersect(self.ylim, cube.ylim) and
            do_ranges_intersect(self.zlim, cube.zlim) 
        )
        return result
    
    def __repr__(self):
        return f"Cube(({str(self.as_tuple())})"
    
    def __str__(self):
        return f"Cube(({str(self.as_tuple())})"
    
    def get_volume(self):
        return (
            (self.xlim[1] - self.xlim[0] + 1) *
            (self.ylim[1] - self.ylim[0] + 1) *
            (self.zlim[1] - self.zlim[0] + 1)
        )
        
def create_subranges(range1, range2):
    splits = sorted(list(set([range1[0], range1[1]+1, range2[0], range2[1]+1])))
    subranges = [(splits[i], splits[i+1]-1) for i in range(len(splits)-1)]
    
    return subranges


def read_data(file_name):
    return [parse_line(row) for row in open(file_name).read().split('\n') if row != '']
    

def parse_line(s: str):
    pattern = "(on|off) x=([-\d]*)\.\.([-\d]*),y=([-\d]*)\.\.([-\d]*),z=([-\d]*)\.\.([-\d]*)"
    numbers = [int(x) for x in re.match(pattern, s).groups()[1:]]
    
    requested_status = re.match(pattern, s).groups()[0]
    
    value_mapping = {'on': 1, 'off': 0}
    
    return {
        'target_value': value_mapping[requested_status],
        'coord_range': (
            Cube((
                (numbers[0], numbers[1]),
                (numbers[2], numbers[3]),
                (numbers[4], numbers[5])
            ))
        )
    }



            


def update_matrix(list_of_on_cubes: Dict, coord_range, value, max_abs_value=np.inf):
    for x in range(apply_threshold(coord_range[0][0]), apply_threshold(coord_range[0][1]) + 1):
        for y in range(apply_threshold(coord_range[1][0]), apply_threshold(coord_range[1][1]) + 1):
            for z in range(apply_threshold(coord_range[2][0]), apply_threshold(coord_range[2][1]) + 1):
                cube = (x, y, z)

                if value == 0 and cube in list_of_on_cubes:
                    list_of_on_cubes.remove(cube)  
                elif value == 1 and cube not in list_of_on_cubes:
                    if abs(x) <= max_abs_value and abs(y) <= max_abs_value and abs(z) <= max_abs_value:
                        list_of_on_cubes.append(cube)
                
    
    return list_of_on_cubes


def update_matrix_v2(list_of_on_cubes: List[Tuple[Tuple[int]]], coord_range, value, max_abs_value=np.inf):
    for cube in list_of_on_cubes:
        pass
    
    



def do_ranges_intersect(range1: Tuple, range2: Tuple) -> bool:
    
    return range1[0] <= range2[1] and range1[1] >= range2[0]




def apply_threshold(coord, max_abs_value=50):
    return min(max(-max_abs_value, coord), max_abs_value)
    
    
def solve1(data):
    return None
    list_of_on_cubes = []
    for row in data:
        list_of_on_cubes = update_matrix(list_of_on_cubes, row['coord_range'], row['target_value'])
    
    return len(list_of_on_cubes)
        

def merge_all(data, fuse=100000):
    items_to_merge = data           
                                         
    cubes_on = []    

    
    while len(items_to_merge) > 0 and fuse > 0:

        fuse -= 1

        new_item = items_to_merge[0]

        if new_item['target_value'] == 1:
            intersecting_cubes = new_item['coord_range'].find_intersecting_cubes(cubes_on)
            if len(intersecting_cubes) == 0:
                cubes_on.append(new_item['coord_range'])
                #print(f">> Adding to cubes_on: {new_item['coord_range']}")
                items_to_merge = items_to_merge[1:]

            else:

                cube_2 = intersecting_cubes[0]
                inter = new_item['coord_range'].intersect_and_split(cube_2)
                cubes_to_queue = inter['self_only']
                items_to_merge = [{'target_value': 1, 'coord_range': x} for x in cubes_to_queue] + items_to_merge[1:]

        elif new_item['target_value'] == 0:
            sub_cubes_to_add = []
            i = 0
            while i < len(cubes_on):
                inter = new_item['coord_range'].intersect_and_split(cubes_on[i])
                if len(inter['intersection']) > 0:
                    cubes_on.pop(i)
                    sub_cubes_to_add += inter['other_only']
                else:
                    i += 1
            cubes_on += sub_cubes_to_add
            items_to_merge = items_to_merge[1:]

        else:
            raise ValueError

    if fuse == 0:
        raise ValueError
        
    return cubes_on

def solve1(data):
    cubes_on = merge_all(data)
    return get_total_volume(cubes_on)


def get_total_volume(cubes):
    return sum([cube.get_volume() for cube in cubes])