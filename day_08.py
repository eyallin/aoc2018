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


def test_dummy():
    data = '0 3 10 11 12'
    assert part1(data) == 33

    data = '1 1 0 1 99 2 1 1 2'
    assert part1(data) == 101

    data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    assert part1(data) == 138


if __name__ == "__main__":
    with open('day8_input.txt') as f:
        data = f.read()
    print(part1(data))