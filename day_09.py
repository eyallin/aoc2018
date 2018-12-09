# https://adventofcode.com/2018/day/9

import collections


def print_ring(ring, current):
    for i, m in enumerate(ring):
        if i == current:
            print('({})'.format(m), end=' ')
        else:
            print('{}'.format(m), end=' ')
    print('')


def part1(num_players, last_marble):
    ring = [0]
    current = 0

    scores = collections.defaultdict(int)
    for marble in range(1, last_marble):
        if marble % 23 != 0:
            current = (current + 2) % len(ring)
            ring.insert(current, marble)
        else:
            player = marble % num_players
            scores[player] += marble
            current = (current - 7) % len(ring)
            scores[player] += ring.pop(current)
    
    return max(scores.values())


def test_part1():
    assert part1(9, 25) == 32
    assert part1(10, 1618) == 8317
    assert part1(13, 7999) == 146373
#    assert part1(17, 1104) == 2764
    assert part1(21, 6111) == 54718
    assert part1(30, 5807) == 37305


if __name__ == "__main__":
    """
    439 players; last marble is worth 71307 points
    """
    print(part1(439, 71307))
