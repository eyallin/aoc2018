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


def analyze_order(pairs, nodes):
    in_rank = collections.Counter(p[1] for p in pairs if p[1] in nodes and p[0] in nodes)

    # find node with 0 in-rank
    candidates = [n for n in nodes if n not in in_rank]
    return candidates


def part1(pairs):
    nodes = set(p[0] for p in pairs) | set(p[1] for p in pairs)
    output = ''
    while nodes:
        next_task = sorted(analyze_order(pairs, nodes))[0]
        output += next_task
        nodes.remove(next_task)

    return output


def test_part1():
    pairs = test_input()
    order = part1(pairs)
    assert order == 'CABDFE'


def part2(pairs, duration_base, num_workers):
    nodes = set(p[0] for p in pairs) | set(p[1] for p in pairs)
    nodes = {n: duration_base + ord(n)-65+1 for n in nodes}
    time = 0
    workers = {a: -1 for a in range(num_workers)}
    output = ''
    while nodes:
#        print('{} - workers: {}'.format(time, workers))
        for w in workers:
            if workers[w] != -1:
                task = workers[w]
                nodes[task] -= 1
                if nodes[task] == 0:
#                    print('Worker {} done with task {}'.format(w, task))
                    output += task
                    del nodes[task]
                    workers[w] = -1
        
        free_workers = sorted([w for w in workers if workers[w] == -1])

        for worker in free_workers:
            candidate_tasks = sorted(analyze_order(pairs, nodes.keys()))
            # remove in-progress tasks
            for w in workers:
                if workers[w] in candidate_tasks:
                    candidate_tasks.remove(workers[w])
            
            if candidate_tasks:
#                print('Worker {} taking new task {}'.format(worker, candidate_tasks[0]))
                workers[worker] = candidate_tasks[0]

        time += 1

    return time-1


def test_part2():
    pairs = test_input()
    assert part2(pairs, 0, 2) == 15


if __name__ == "__main__":
    with open('day7_input.txt') as f:
        pairs = list(parse_input(f.read()))
    print(part1(pairs))

    print(part2(pairs, 60, 5))