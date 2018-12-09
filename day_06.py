# https://adventofcode.com/2018/day/6

import collections
import itertools

def distance_from_point(coord, point):
    return abs(point[0] - coord[0]) + abs(point[1] - coord[1])


def calc_grid_distances(points, grid_size):
    grid = {}    
    for g in itertools.product(range(grid_size[0]), range(grid_size[1])):
        distance_from_points = {i: distance_from_point(g, p) for i, p in enumerate(points)}
        min_distance = min(distance_from_points.items(), key=lambda i: distance_from_points[i[0]])

        if list(distance_from_points.values()).count(min_distance[1]) > 1:
            min_distance = None, None
        grid[g] = min_distance[0]

    return grid


def remove_infinite_areas(grid, size):
    counts = collections.Counter(grid.values())

    # remove outermost elements (since they're infinite areas)
    for y in range(size[1]):
        del counts[grid[(0, y)]]
        del counts[grid[(size[0]-1, y)]]

    for x in range(size[0]):
        del counts[grid[(x, 0)]]
        del counts[grid[(x, size[1]-1)]]
    
    return counts


def test_point_distances():
    points = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9),
    ]
    grid_size = max(p[0] for p in points), max(p[1] for p in points)

    distances = calc_grid_distances(points, grid_size)
    assert distances[(0, 0)] == 0
    assert distances[(0, 5)] == 1
    assert distances[(0, 4)] == None
    assert distances[(4, 4)] == 3
    assert distances[(5, 4)] == 4


def print_grid(grid, grid_size):
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            p = grid[(x, y)]
            if p is not None:
                print(p, end='')
            else:
                print('.', end='')
        print('')


def parse_input(data):
    for line in data.splitlines():
        if not line.strip(): 
            continue
        x, y = line.split(',')
        yield (int(x), int(y))


def part1(points):
    grid_size = max(p[0] for p in points)+1, max(p[1] for p in points)+1
    distances = calc_grid_distances(points, grid_size)
    counts = remove_infinite_areas(distances, grid_size)
    return counts



def calc_safe_area(points, grid_size, size_threshold):
    grid = {}    
    for g in itertools.product(range(grid_size[0]), range(grid_size[1])):
        distance_from_points = {i: distance_from_point(g, p) for i, p in enumerate(points)}
        total_distances = sum(distance_from_points.values())

        if total_distances < size_threshold:
            grid[g] = 1

    return sum(grid.values())


def test_safe_area():
    points = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9),
    ]
    grid_size = max(p[0] for p in points), max(p[1] for p in points)
    safe_area = calc_safe_area(points, grid_size, 32)
    assert safe_area == 16


def part2(points):
    grid_size = max(p[0] for p in points), max(p[1] for p in points)
    safe_area = calc_safe_area(points, grid_size, 10000)
    return safe_area


if __name__ == "__main__":
    points = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9),
    ]
    print(part1(points))

    with open('day6_input.txt') as f:
        data = f.read()
    points = list(parse_input(data))
    print(part1(points).most_common(1))
    print(part2(points))
