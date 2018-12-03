# https://adventofcode.com/2018/day/1


def day1a(data):
    return sum(int(a) for a in data.split())


def test_part1():
    assert day1a("+1 +1 +1") == 3
    assert day1a("+1 +1 -2") == 0
    assert day1a("-1 -2 -3") == -6


if __name__ == '__main__':
    with open('./day1_input.txt') as f:
        print(day1a(f.read()))
