# https://adventofcode.com/2018/day/11


def power_level(cell, serial_number):
    rack_id = cell[0] + 10
    power = rack_id * cell[1]
    power += serial_number
    power *= rack_id
    power = (power // 100) % 10
    power -= 5
    return power


def test_power_level():
    assert power_level((3, 5), 8) == 4
    assert power_level((122, 79), 57) == -5
    assert power_level((217, 196), 39) ==  0
    assert power_level((101, 153), 71) ==  4


def create_grid(grid_size, serial_number):
    grid = []
    for y in range(grid_size[1]):
        grid.append([0] * grid_size[0])

    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            grid[y][x] = power_level((x, y), serial_number)
    return grid


def calc_partial_sums(grid):
    grid_size = len(grid[0]), len(grid)
    sums = []
    for y in range(grid_size[1]):
        sums.append([0] * grid_size[0])

    # top-left element
    sums[0][0] = grid[0][0]

    # first row
    for x in range(1, grid_size[0]):
        sums[0][x] = sums[0][x-1] + grid[0][x]

    # all other rows
    for y in range(1, grid_size[1]):
        sums[y][0] = sums[y-1][0] + grid[y][0]
        for x in range(1, grid_size[0]):
            sums[y][x] = sums[y][x-1] + sums[y-1][x] - sums[y-1][x-1] + grid[y][x]
    
    # sanity check
    assert sums[grid_size[1]-1][grid_size[0]-1] == sum(sum(line) for line in grid)

    return sums


def get_sum_from_partials(partial_sums, coord, size):
    x, y = coord
    res = (partial_sums[y+size-1][x+size-1]
        - (partial_sums[y-1][x+size-1] if y>0 else 0)
        - (partial_sums[y+size-1][x-1] if x>0 else 0)
        + (partial_sums[y-1][x-1] if x>0 and y>0 else 0)
    )
    return res


def find_largest_subgrid(grid, subgrid_size, partial_sums=None):
    curr_max = None
    if partial_sums is None:
        partial_sums = calc_partial_sums(grid)
    
    for y in range(len(grid) - subgrid_size + 1):
        for x in range(len(grid[0]) - subgrid_size + 1):
            res = get_sum_from_partials(partial_sums, (x, y), subgrid_size)
            if curr_max is None or res > curr_max:
                curr_max = res
                best_coord = (x, y)
    
    return best_coord, curr_max, subgrid_size


def test_find_largest_subgrid():
    grid = create_grid((300, 300), 18)
    assert find_largest_subgrid(grid, 3) == ((33, 45), 29, 3)
    grid = create_grid((300, 300), 42)
    assert find_largest_subgrid(grid, 3) == ((21, 61), 30, 3)


def find_largest_subgrid_any_size(grid_size, serial_number):
    grid = create_grid(grid_size, serial_number)
    partial_sums = calc_partial_sums(grid)

    curr_max = None
    for subgrid_size in range(1, 301):
        coord, res, size = find_largest_subgrid(grid, subgrid_size, partial_sums)
        if curr_max is None or res > curr_max[1]:
            curr_max = (coord, res, size)
    return curr_max


def test_find_largest_subgrid_any_size():
    assert find_largest_subgrid_any_size((300, 300), 18) == ((90, 269), 113, 16)
    assert find_largest_subgrid_any_size((300, 300), 42) == ((232, 251), 119, 12)


if __name__ == "__main__":
    grid_size = (300, 300)
    serial_number = 8141

    grid = create_grid(grid_size, serial_number)
    print('Largest total power is at grid point {}'.format(find_largest_subgrid(grid, 3)))

    print('Largest total power for any subgrid size is at grid point {}'.format(find_largest_subgrid_any_size(grid_size, serial_number)))
