from typing import Tuple, List
import numpy as np

PACKET_TYPE_ID__LITERAL = 4
LENGTH_TYPE_ID__LENGTH = 0
LENGTH_TYPE_ID__COUNT = 1

def apply_operator(type_id: int, sub_packets_values: List[int]) -> int:
    """
    Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
    Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
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


def read_data(file_name):
    return open(file_name).read().replace('\n', '')

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





def solve1(hex_string:str, verbose: str = False) -> int:
    bin_string = hex_to_bin(hex_string)
    sum_version_numbers = extract_first_packet_and_sum_versions(bin_string, verbose)[1]
    return sum_version_numbers


def solve2(hex_string:str, verbose: str = False) -> int:
    bin_string = hex_to_bin(hex_string)
    sum_version_numbers = extract_first_packet_and_sum_versions(bin_string, verbose)[2]
    return sum_version_numbers


def extract_first_packet_and_sum_versions(string, verbose=False) -> Tuple[str, int, int]:
    "return first packet, its sum version, and its value"
    
    packet_type = get_type(string)
    
    if packet_type == PACKET_TYPE_ID__LITERAL:
        return parse_literal_packet(string, verbose)
    else:
        length_type_id = get_length_type_id(string)
        if length_type_id == LENGTH_TYPE_ID__LENGTH:
            return parse_container_by_length(string, verbose)
        elif length_type_id == LENGTH_TYPE_ID__COUNT:
            return parse_container_by_count(string, verbose)
        else:
            raise ValueError

def parse_literal_packet(string, verbose) -> Tuple[str, int, int]:
    
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
    return (string[:position], packet_version_nr, value)

def parse_container_by_count(string, verbose) -> Tuple[str, int, int]:
    value = None
    main_packet_version_nr = get_version_number(string)
    packet_type = get_type(string)
    
    size_of_length_definition = 11
    sub_packets_value_list = []
    number_of_subpackets = int(string[7:7 + size_of_length_definition], 2)
    if verbose:
        print(f'sub-packets defined by count: {number_of_subpackets}')
    position = 7 + size_of_length_definition
    sum_version_nr = main_packet_version_nr
    for i in range(number_of_subpackets):
        sub_packet = extract_first_packet_and_sum_versions(string[position:])
        len_first_packet = len(sub_packet[0])
        sub_packet_version_nr_sum = sub_packet[1]
        if verbose:
            print(sub_packet)
        value = sub_packet[2]
        sub_packets_value_list.append(value)
        if verbose:
            print(f"sub-packet: {sub_packet[0]}, version {sub_packet_version_nr_sum}")
        position += len_first_packet
        sum_version_nr += sub_packet_version_nr_sum
        
    value = apply_operator(packet_type, sub_packets_value_list)
    return (string[:position], sum_version_nr, value)

def parse_container_by_length(string, verbose) -> Tuple[str, int, int]:
    value = None
    main_packet_version_nr = get_version_number(string)
    packet_type = get_type(string)
    
    sub_packets_value_list = []
    size_of_length_definition = 15
    packets_total_length = int(string[7:7+size_of_length_definition], 2)
    if verbose:
        print(f'sub-packets defined by length: {packets_total_length}')
                
                
    position = 7+size_of_length_definition
    sum_version_nr = main_packet_version_nr

    while position - (7+size_of_length_definition) < packets_total_length:
        sub_packet = extract_first_packet_and_sum_versions(string[position:])
        if verbose:
            print(sub_packet)
            
        len_first_packet = len(sub_packet[0])
        sub_packet_version_nr_sum = sub_packet[1]
        value = sub_packet[2]
        sub_packets_value_list.append(value)
        
        if verbose:
            print(f"sub-packet: {sub_packet[0]}, version {sub_packet_version_nr_sum}")
        position += len_first_packet
        sum_version_nr += sub_packet_version_nr_sum
        
    value = apply_operator(packet_type, sub_packets_value_list)
    return (string[:position], sum_version_nr, value)  
        

def get_version_number(packet):
    return int(packet[0:3], 2)

def get_type(packet):
    return int(packet[3:6], 2)

def get_length_type_id(packet):
    return int(packet[6:7])

"""
def parse_literal_value(literal_value: str) -> int:
    stop_after_this_one = False
    position = 0
    value = ''
    while not stop_after_this_one:
        group = literal_value[position: position+5]
        stop_after_this_one = (group[0] == '0')
        value += group[1:]
        position += 5

    return int(value, 2)
"""

"""
def get_sum_of_version_nr(packet):
    version_nr = get_version_number(packet)
    packet_type = get_type(packet)
    if packet_type == 4:
        return version_nr
    else:
        packets = parse_sub_packets(packet)
        return sum([get_sum_of_version_nr(packet) for packet in packets])

def parse_sub_packets(container_packet):
    length_type_id = get_length_type_id(packet)
    if length_type_id == 0:
        packets_total_length = int(container_packet[7:7+15])
    else:
        number_of_subpackets = int(container_packet[7:7+11])

def parse_literal_packet(packet: str) -> Tuple[int, int]:
    "return (version number, value)"
    return (
        get_version_number(packet),
        parse_literal_value(packet[6:])
    )
    
def parse_container_packet(packet:str) -> Tuple[int, List[str]]:
    version_nr = get_version_number(packet)
    
    type_id = get_length_type_id(packet)
    
    if length_type_id == 0:
        packets_total_length = int(container_packet[7:7+15])
    else:
        number_of_subpackets = int(container_packet[7:7+11])
        
def extract_first_packet(string, verbose=False):
    packet_type = get_type(string)
    if packet_type == 4:
        if verbose:
            print('literal packet')
        stop_after_this_one = False
        position = 6
        while not stop_after_this_one:
            group = string[position: position+5]
            stop_after_this_one = (group[0] == '0')
            position += 5
        
        # the packet must be encoded in hex, so the nr of bytes is multiple of 4
        full_hex_byte_end = position + (4 - ((position) % 4))
        
        #return string[:full_hex_byte_end]
        return string[:position]
    
    else:
        if verbose:
            print('container packet')
        length_type_id = get_length_type_id(string)
        if length_type_id == 0:
            
            packets_total_length = int(string[7:7+15], 2)
            if verbose:
                print(f'sub-packets defined by length: {packets_total_length}')
            return string[:7+15+packets_total_length]
        else:
            
            number_of_subpackets = int(string[7:7+11], 2)
            if verbose:
                print(f'sub-packets defined by count: {number_of_subpackets}')
            position = 7+11
            for i in range(number_of_subpackets):
                len_first_packet = len(extract_first_packet(string[position:]))
                if verbose:
                    print(f"sub-packet: {extract_first_packet(string[position:])}")
                position += len_first_packet
            return string[:position]
"""