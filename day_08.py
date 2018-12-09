# https://adventofcode.com/2018/day/8



def tree_reader(data):
    for x in data.split():
        yield int(x)


def process_node(tree):
    num_child_nodes = next(tree)
    num_metadata = next(tree)

    sum_children = sum(process_node(tree) for _ in range(num_child_nodes))
    sum_self = sum(next(tree) for _ in range(num_metadata))
    
    return sum_children + sum_self


def part1(data):
    tree = tree_reader(data)
    return process_node(tree)


def test_part1():
    data = '0 3 10 11 12'
    assert part1(data) == 33

    data = '1 1 0 1 99 2 1 1 2'
    assert part1(data) == 101

    data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    assert part1(data) == 138


def get_from_list(l, idx):
    if idx >= len(l):
        return 0
    return l[idx]


def node_value(tree):
    num_child_nodes = next(tree)
    num_metadata = next(tree)

    if num_child_nodes == 0:
        sum_self = sum(next(tree) for _ in range(num_metadata))
        return sum_self
    else:
        node_values = [node_value(tree) for _ in range(num_child_nodes)]
        nodes_to_pick = [next(tree) for _ in range(num_metadata)]
        return sum(get_from_list(node_values, n-1) for n in nodes_to_pick)
        
    return 9999


def part2(data):
    tree = tree_reader(data)
    return node_value(tree)


def test_part2():
    data = '0 3 10 11 12'
    assert part2(data) == 33
    
    data = '0 1 99'
    assert part2(data) == 99

    data = '1 1 0 1 99 2'
    assert part2(data) == 0
    
    data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    assert part2(data) == 66



if __name__ == "__main__":
    with open('day8_input.txt') as f:
        data = f.read()
    print(part1(data))
    print(part2(data))