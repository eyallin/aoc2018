# https://adventofcode.com/2018/day/10


import collections
import re


Point = collections.namedtuple('Point', 'x y dx dy')

regex = re.compile(r'position=<(.*)> velocity=<(.*)>')

def parse_points(data):
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        m = regex.match(line)
        assert m
        x, y = m.group(1).split(',')
        dx, dy = m.group(2).split(',')
        p = Point(int(x), int(y), int(dx), int(dy))
        yield p


def point_at_time(p, t):
    return Point(p.x + p.dx * t, p.y + p.dy * t, p.dx, p.dy)


def get_bbox(points):
    return (min(p.x for p in points),
            min(p.y for p in points),
            max(p.x for p in points),
            max(p.y for p in points),
    )

def bbox_size(bb):
    return bb[2] - bb[0] + 1, bb[3] - bb[1] + 1

def print_message(points):
    bbox = get_bbox(points)
    arr = []
    sizex, sizey = bbox_size(bbox)
    for y in range(sizey):
        arr.append([' '] * sizex)
    
    for p in points:
        arr[p.y - bbox[1]][p.x - bbox[0]] = '#'
    
    for line in arr:
        print(''.join(line))
    print('')


def part1(data):
    orig_points = list(parse_points(data))
    
    bboxes = []
    for t in range(20000):
        if t % 1000 == 0:
            print('At time {}'.format(t))
        points = [point_at_time(p, t) for p in orig_points]
        bboxes.append((t, get_bbox(points)))
    
    min_t, min_bbox_size = min(bboxes, key=lambda b: bbox_size(b[1]))
    print (min_t, min_bbox_size)

    print_message([point_at_time(p, min_t) for p in orig_points])


if __name__ == "__main__":
    input = """
position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
"""
    part1(input)

    with open('day10_input.txt') as f:
        data = f.read()
    part1(data)