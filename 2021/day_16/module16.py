from typing import Tuple, List, Dict
import numpy as np

PACKET_TYPE_ID__LITERAL = 4
LENGTH_TYPE_ID__LENGTH = 0
LENGTH_TYPE_ID__COUNT = 1


def read_data(file_name: str) -> str:
    return open(file_name).read().replace('\n', '')


def solve1(hex_string:str, verbose: str = False) -> int:
    bin_string = hex_to_bin(hex_string)
    return parse_first_packet(bin_string, verbose)['sum_version_nr']


def solve2(hex_string:str, verbose: str = False) -> int:
    bin_string = hex_to_bin(hex_string)
    return  parse_first_packet(bin_string, verbose)['value']


def hex_to_bin(hexa_string: str) -> str:
    map = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    
    result = ''.join([map[char] for char in hexa_string])
    return result


def parse_first_packet(string, verbose=False) -> Dict:
    """
    this is the key function. It is essentially recursive (via helper functions).
    From the input string, it extracts the complete first packet starting at the beginning of the string.
    It also calculates:
    - the sum of all the version number for this packet and its sub-packets
    - the value of this packet
    """
    
    packet_type = get_type(string)
    
    if packet_type == PACKET_TYPE_ID__LITERAL:
        return parse_literal_packet(string, verbose)
    else:        
        return parse_container_generic(string, verbose)


def parse_literal_packet(string, verbose) -> Dict:
    
    packet_version_nr = get_version_number(string)

    if verbose:
        print('literal packet')
    stop_after_this_one = False
    position = 6
    value_as_bin_string = '' 
    while not stop_after_this_one:
        group = string[position: position+5]
        stop_after_this_one = (group[0] == '0')
        value_as_bin_string += group[1:]
        position += 5

    value = int(value_as_bin_string, 2)
    return {
        'packet': string[:position],
        'sum_version_nr': packet_version_nr,
        'value': value
    }



def parse_container_generic(string, verbose) -> Dict:

    packet_type = get_type(string)
    length_type_id = get_length_type_id(string)
    
    if length_type_id == LENGTH_TYPE_ID__LENGTH:
        size_of_length_definition = 15
        packets_total_length = int(string[7:7+size_of_length_definition], 2)
    
    elif length_type_id == LENGTH_TYPE_ID__COUNT:
        size_of_length_definition = 11
        number_of_subpackets = int(string[7:7 + size_of_length_definition], 2)
        packet_counter = 0
        

    main_packet_version_nr = get_version_number(string)    
    position = 7 + size_of_length_definition
    sum_version_nr = main_packet_version_nr
    sub_packets_value_list = []
    condition = True
    
    while condition:
        sub_packet = parse_first_packet(string[position:])
        len_first_packet = len(sub_packet['packet'])
        sub_packet_version_nr_sum = sub_packet['sum_version_nr']
        if verbose:
            print(sub_packet)
        value = sub_packet['value']
        sub_packets_value_list.append(value)
        if verbose:
            print(f"sub-packet: {sub_packet['packet']}, version {sub_packet_version_nr_sum}")
        position += len_first_packet
        sum_version_nr += sub_packet_version_nr_sum
        
        if length_type_id == LENGTH_TYPE_ID__LENGTH:
            condition = position - (7+size_of_length_definition) < packets_total_length
        elif length_type_id == LENGTH_TYPE_ID__COUNT:
            packet_counter += 1
            condition = packet_counter < number_of_subpackets
        
    value = apply_operator(packet_type, sub_packets_value_list)

    return {
        'packet': string[:position],
        'sum_version_nr': sum_version_nr,
        'value': value
    }
  

def get_version_number(packet):
    return int(packet[0:3], 2)


def get_type(packet):
    return int(packet[3:6], 2)


def get_length_type_id(packet):
    return int(packet[6:7])


def apply_operator(type_id: int, sub_packets_values: List[int]) -> int:
    """
    Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. 
    Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets.
    Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
    Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
    Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
    Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
    Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
    """
    operator_def = {
        0: lambda values: np.sum(values),
        1: lambda values: np.product(values),
        2: lambda values: np.min(values),
        3: lambda values: np.max(values),
        5: lambda values: int(values[0] > values[1]),
        6: lambda values: int(values[0] < values[1]),
        7: lambda values: int(values[0] == values[1]),
    }
    
    result = operator_def[type_id](sub_packets_values)
    return result

