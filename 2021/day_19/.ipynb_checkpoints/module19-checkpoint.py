import numpy as np



class fred:
    
    
    def __init__(self, file_name):
        
        self.rotations =  fred.generate_all_proper_rotations()
        self.data = fred.read_data(file_name)
        self.interbeacon_distances = [
            convert_to_interbeacon_distances(self.data[i])
            for i in range(len(self.data))
        ]

    @staticmethod
    def generate_all_proper_rotations():
        base_possible_rotations = [
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
            np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]]),
            np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]]),
            np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
            np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]),
            np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]),
            ]

        modifiers = [
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]]),
            np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]]),
            np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]]),
            np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]]),
            np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),
            np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]),
            np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]]),
        ]

        proper_rotations = [
            np.matmul(mod, bas)
            for mod in modifiers
            for bas in base_possible_rotations
            if np.linalg.det(np.matmul(mod, bas)) == 1
        ]
        return proper_rotations
        
    @staticmethod
    def read_data(file_name):
        data = open(file_name).read().split('\n\n')

        return [fred.parse_scanner(scanner) for scanner in data]

        return data

    @staticmethod
    def parse_scanner(scanner:str):
        output = scanner.split('\n')[1:]
        return np.array([[int(coord) for coord in beacon.split(',')] for beacon in output])

    
    def rotate(self, scanner_index, rotation_index):
        return np.matmul(self.rotations[rotation_index], self.data[scanner_index].transpose()).transpose()

def generate_all_proper_rotations():
    base_possible_rotations = [
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
        np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]]),
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]]),
        np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
        np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]),
        np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]]),
        ]

    modifiers = [
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]]),
        np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]]),
        np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]]),
        np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]]),
        np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),
        np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]),
        np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]]),
    ]

    proper_rotations = [
        np.matmul(mod, bas)
        for mod in modifiers
        for bas in base_possible_rotations
        if np.linalg.det(np.matmul(mod, bas)) == 1
    ]
    return proper_rotations    

def convert_to_interbeacon_distances(scanner_data):

    distances = dict()
    for a in range(len(scanner_data)):
        for b in range(a+1, len(scanner_data)):
            dist = np.sqrt(np.sum((scanner_data[a] - scanner_data[b]) ** 2))
            distances[(a, b)] = dist

    return distances
    
def find_intersection(dist1, dist2):
    
    overlap = set(dist1.values()).intersection(dist2.values())
    matches = []
    if len(overlap) >= 66:
        

        for dist in overlap:
            keys_1 = list(dist1.keys())[list(dist1.values()).index(dist)]
            keys_2 = list(dist2.keys())[list(dist2.values()).index(dist)]
            
            matches.append((keys_1, keys_2))
            
    return matches


def match_beacons(intersection):
    values_1 = set([pair[0][0] for pair in intersection] + [pair[0][1] for pair in intersection])
    values_2 = set([pair[1][0] for pair in intersection] + [pair[1][1] for pair in intersection])
    #print(values_1)
    #print(values_2)
    result_dict = dict()
    for val1 in values_1:
        #print(f"val1={val1}")
        pairs_that_contain_this_value = [x for x in intersection if x[0][0]==val1 or x[0][1]==val1]
        if len(pairs_that_contain_this_value) >= 2:
            pair_1 = pairs_that_contain_this_value[0]
            pair_2 = pairs_that_contain_this_value[1]

            result = list(set([pair_1[1][0], pair_1[1][1]]).intersection(set([pair_2[1][0], pair_2[1][1]])))[0]

            result_dict[val1] = result
    
    return result_dict

def create_match_from_scanner_data(scanner_data_1, scanner_data_2):
    inter = find_intersection(
        convert_to_interbeacon_distances(scanner_data_1),
        convert_to_interbeacon_distances(scanner_data_2)
    )
    
    return match_beacons(inter)

def combine_scanners(scanner_data_1, scanner_data_2, matches):
    # matches: an intersection dictionary indicating the mapping between 
    # beacons in scanner1 and scanner 2
    vector1 = scanner_data_1[list(matches.keys())[1]] - scanner_data_1[list(matches.keys())[0]]
    vector2 = scanner_data_2[list(matches.values())[1]] - scanner_data_2[list(matches.values())[0]]
    
    
    rotations = generate_all_proper_rotations()
    for rot in rotations:
        if (np.matmul(rot, vector2.transpose()) == vector1).all():
            correct_rotation = rot

    rotated_2 = np.matmul(correct_rotation, scanner_data_2.transpose()).transpose()
    
    offset = scanner_data_1[list(matches.keys())[0]] - rotated_2[list(matches.values())[0]]
    #print(f"offset={offset}")
    
    realigned_2 = rotated_2 + offset
    
    #print(f"intersection size: {len(set(list(realigned_2)).intersection(set(list(scanner_data_1))))}")
    common = [pair for pair in realigned_2 if pair in scanner_data_1]
    addish = array_list_diff(realigned_2, scanner_data_1)# [pair for pair in realigned_2 if pair not in scanner_data_1]
    #print('---new items;')
    #print(addish)
    #print('---overlapping items;')
    #print(common)
    #print(f"{len(common)} common elements, {len(addish)} new elements")
    return  np.array(list(scanner_data_1) + addish), offset

def combine_all(data):
    
   
    interbeacon_distances = [
        convert_to_interbeacon_distances(data[i])
        for i in range(len(data))
    ]
    scanners_not_combined = data[1:]
    distances_not_combined = interbeacon_distances[1:]
    original_index_not_combined = list(range(1,len(data)))
    
    scanners = [[0, 0, 0]]
    
    combined = data[0]
    #print(f"{len(combined)} beacons in space")
    #print(f"{len(scanners_not_combined)} scanner not combined")

    #print(f">>> is my boi here? {my_boi in combined}")
    while len(scanners_not_combined) > 0:
        main_distance = convert_to_interbeacon_distances(combined)
        i = 0
        match_found = False
        while i<len(scanners_not_combined) and not match_found:
            inter = find_intersection(main_distance, distances_not_combined[i])
            if len(inter) >= 66:
                #print(f"adding set {original_index_not_combined[i]}")
                
                combined, scanner_position = combine_scanners(combined, scanners_not_combined[i], match_beacons(inter))
                scanners.append(scanner_position)
                match_found = True
                scanners_not_combined.pop(i)
                distances_not_combined.pop(i)
                original_index_not_combined.pop(i)
                
                #print(f"{len(combined)} beacons in space")
                #print(f"{len(scanners_not_combined)} scanner not combined")

                #print(f">>> is my boi here? {my_boi in combined}")
            i += 1
    return combined, scanners


def solve1(data):
    beacons, scanners = combine_all(data)
    return len(beacons)
    
    
def read_data(file_name):
        data = open(file_name).read().split('\n\n')

        return [fred.parse_scanner(scanner) for scanner in data if scanner != '']

        return data
    
    
def parse_scanner(scanner:str):
        output = scanner.split('\n')[1:]
        return np.array([[int(coord) for coord in beacon.split(',')] for beacon in output if beacon != ''])
    
def array_list_diff(array_list_1, array_list_2):
    list_list_1 = [list(x) for x in array_list_1]
    list_list_2 = [list(x) for x in array_list_2]
    diff = [np.array(x) for x in list_list_1 if x not in list_list_2]
    return diff

def find_max_distance_between_scanners(scanners):
    max_distance = -np.inf
    for i in range(len(scanners)):
        for j in range(i+1, len(scanners)):
            dist = np.sum(np.abs(scanners[i] - scanners[j]))
            max_distance = max(max_distance, dist)
            
            
    return max_distance

def solve2(data):
    beacons, scanners = combine_all(data)
    return find_max_distance_between_scanners(scanners)