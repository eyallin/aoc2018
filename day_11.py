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


def find_largest_subgrid(grid_size, serial_number):
    grid = []
    for y in range(grid_size[1]):
        grid.append([0] * grid_size[0])

    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            grid[y][x] = power_level((x, y), serial_number)
    
    subgrid_size = 3
    res = {}
    for y in range(grid_size[1] - subgrid_size):
        for x in range(grid_size[0] - subgrid_size):
            res[(x, y)] = sum(grid[yy][xx] 
                for yy in range(y, y+subgrid_size)
                for xx in range(x, x+subgrid_size)
            )
    
    return max(res, key=lambda x: res[x])


def test_find_largest_subgrid():
    assert find_largest_subgrid((300, 300), 18) == (33, 45)
    assert find_largest_subgrid((300, 300), 42) == (21, 61)


if __name__ == "__main__":
    grid = (300, 30)
    serial_number = 8141
    print('Largest total power is at grid point {}'.format(find_largest_subgrid(grid, serial_number)))