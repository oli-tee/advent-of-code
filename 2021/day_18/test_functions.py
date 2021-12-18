import module18



def test_explode():
    assert module18.explode(list('[[[[[9,8],1],2],3],4]')) == (list('[[[[0,9],2],3],4]'), True)
    assert module18.explode(list('[7,[6,[5,[4,[3,2]]]]]')) == (list('[7,[6,[5,[7,0]]]]'), True)
    assert module18.explode(list('[[6,[5,[4,[3,2]]]],1]')) == (list('[[6,[5,[7,0]]],3]'), True)
    assert module18.explode(list('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')) == (list('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'), True)
    assert module18.explode(list('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')) == (list('[[3,[2,[8,0]]],[9,[5,[7,0]]]]'), True)
    assert module18.explode(list('[1, [2, 3]]')) == (list('[1, [2, 3]]'), False)
    
def test_spleet():
    assert module18.spleet(['[', '12', ',', '6', ']']) == (['[', '[', '6', ',', '6', ']', ',', '6', ']'], True)
    assert module18.spleet(['[', '9', ',', '6', ']']) == (['[', '9', ',', '6', ']'], False)
    #assert module18.spleet('[[[[0,7],4],[15,[0,13]]],[1,1]]') == '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'
    
def test_reduce():
    input = list('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
    assert module18.reduce(input) == list('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
    

def test_add():
    # [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]]
    assert module18.add(list('[1,2]'), list('[3,4]')) == list("[[1,2],[3,4]]")

def test_magnitude():
    assert module18.get_magnitude(5) == 5
    assert module18.get_magnitude([9,1]) == 29
    assert module18.get_magnitude([[1,2],[[3,4],5]]) == 143
    assert module18.get_magnitude([[1,2],[[3,4],5]]) == 143
    assert module18.get_magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384
    assert module18.get_magnitude([[[[1,1],[2,2]],[3,3]],[4,4]]) == 445
    assert module18.get_magnitude([[[[3,0],[5,3]],[4,4]],[5,5]]) == 791
    assert module18.get_magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]) == 1137
    assert module18.get_magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488
    """
    [[1,2],[[3,4],5]] becomes 143.
[[[[0,7],4],[[7,8],[6,0]]],[8,1]] becomes 1384.
[[[[1,1],[2,2]],[3,3]],[4,4]] becomes 445.
[[[[3,0],[5,3]],[4,4]],[5,5]] becomes 791.
[[[[5,0],[7,4]],[5,5]],[6,6]] becomes 1137.
[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] becomes 3488.
    """
    
    
def test_add_series():
    ''.join(module18.add_list_of_nr([
        list('[1, 1]'),
        list('[2, 2]'),
        list('[3, 3]'),
        list('[4, 4]'),
    ]
    )) == '[[[[1,1],[2,2]],[3,3]],[4,4]]'
    
    """For example, the final sum of this list is [[[[1,1],[2,2]],[3,3]],[4,4]]:

    [1,1]
    [2,2]
    [3,3]
    [4,4]
    The final sum of this list is [[[[3,0],[5,3]],[4,4]],[5,5]]:

    [1,1]
    [2,2]
    [3,3]
    [4,4]
    [5,5]
    The final sum of this list is [[[[5,0],[7,4]],[5,5]],[6,6]]:

    [1,1]
    [2,2]
    [3,3]
    [4,4]
    [5,5]
    [6,6]
    """

def test_solve1():
    list_of_itemized_lists = module18.read_data('test_input.txt')
    assert module18.solve1(list_of_itemized_lists) == 4140
    
def test_solve2():
    list_of_itemized_lists = module18.read_data('test_input.txt')
    assert module18.solve2(list_of_itemized_lists) == 3993
    