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


class RingNode:
    __slots__ = ('val', 'prev', 'next')
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Ring:
    def __init__(self, val):
        node = RingNode(val)
        node.next = node
        node.prev = node
        self.current = node
    
    def add(self, val):
        newnode = RingNode(val)
        newnode.next = self.current.next
        newnode.prev = self.current
        newnode.next.prev = newnode
        self.current.next = newnode
        self.current = newnode
#        print('Added {} [p={}, n={}]'.format(val, newnode.prev.val, newnode.next.val))
    
    def remove(self):
        node = self.current
#        print('Removing {} [p={}, n={}]'.format(node.val, node.prev.val, node.next.val))
        node.prev.next = node.next
        node.next.prev = node.prev
        self.current = node.next
        return node.val
    
    def advance(self, n):
        if n > 0:
            for _ in range(n):
                self.current = self.current.next
        else:
            for _ in range(-n):
                self.current = self.current.prev

    def print(self):
        node = self.current
        while True:
            if node == self.current:
                print('({})'.format(node.val), end=' ')
            else:
                print('{}'.format(node.val), end=' ')
            node = node.next
            if node == self.current:
                break
        print('')


def part2(num_players, last_marble):
    ring = Ring(0)

    scores = collections.defaultdict(int)
    for marble in range(1, last_marble):
        if marble % 23 != 0:
            ring.advance(1)
            ring.add(marble)
        else:
            player = marble % num_players
            scores[player] += marble
            ring.advance(-7)
            scores[player] += ring.remove()
    
    return max(scores.values())

def test_part2():
    assert part2(9, 25) == 32
    assert part2(10, 1618) == 8317
    assert part2(13, 7999) == 146373
#    assert part2(17, 1104) == 2764
    assert part2(21, 6111) == 54718
    assert part2(30, 5807) == 37305



if __name__ == "__main__":
    """
    439 players; last marble is worth 71307 points
    """
    print(part1(439, 71307))

    print(part2(439, 71307 * 100))
