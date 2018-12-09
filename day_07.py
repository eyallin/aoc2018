# https://adventofcode.com/2018/day/7

import collections
import re


regex = re.compile(r'Step (?P<from>.) must be finished before step (?P<to>.) can begin.')
def parse_input(data):
    for line in data.splitlines():
        if not line.strip():
            continue
        m = regex.match(line)
        assert m
        yield m.groups()


def test_input():
    data = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""
    return list(parse_input(data))


def analyze_order(pairs):
    nodes = set(p[0] for p in pairs) | set(p[1] for p in pairs)

    output = ''
    while nodes:
        in_rank = collections.Counter(p[1] for p in pairs if p[1] in nodes and p[0] in nodes)

        # find node with 0 in-rank
        candidates = [n for n in nodes if n not in in_rank]
        node = sorted(candidates)[0]
        
        output += node
        
        nodes.remove(node)

    return output


def test_dummy():
    pairs = test_input()
    order = analyze_order(pairs)
    assert order == 'CABDFE'


if __name__ == "__main__":
    with open('day7_input.txt') as f:
        pairs = list(parse_input(f.read()))
    print(analyze_order(pairs))
