# https://adventofcode.com/2018/day/3

import collections
import re

Claim = collections.namedtuple('Claim', 'id x y xs ys')


claim_re = re.compile(r'^#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<xs>\d+)x(?P<ys>\d+)$')
def parse_claim(line):
    m = claim_re.match(line)
    return Claim(*(int(a) for a in m.groups()))


def pixels_in_claim(c):
    return ((a, b) for a in range(c.x, c.x + c.xs) for b in range(c.y, c.y + c.ys))


def test_parse_claim():
    assert parse_claim('#1 @ 1,3: 4x4') == Claim(1, 1, 3, 4, 4)
    assert parse_claim('#2 @ 3,1: 4x4') == Claim(2, 3, 1, 4, 4)
    assert parse_claim('#3 @ 5,5: 2x2') == Claim(3, 5, 5, 2, 2)


def test_pixels_in_claim():
    c = Claim('', 1, 3, 4, 4)
    assert set(pixels_in_claim(c)) == set((a, b) for a in range(c.x, c.x + c.xs) for b in range(c.y, c.y + c.ys))


def day3a(data):
    pixels = collections.Counter()
    for line in data.splitlines():
        if not line: continue
        claim = parse_claim(line)
        pixels.update(pixels_in_claim(claim))
    return len([a for a in pixels.values() if a>1])


def test_day3a():
    data = """
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""    
    assert day3a(data) == 4


if __name__ == "__main__":
    with open('day3_input.txt') as f:
        data = f.read()
    print(day3a(data))