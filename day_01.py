# https://adventofcode.com/2018/day/1


def day1a(data):
    return sum(int(a) for a in data.split())


def test_part1():
    assert day1a("+1 +1 +1") == 3
    assert day1a("+1 +1 -2") == 0
    assert day1a("-1 -2 -3") == -6


def day1b(data):
    seen_values = set([0])
    current_sum = 0
    while True:
        for v in (int(a) for a in data.split()):
            current_sum += v
            if current_sum in seen_values:
                return current_sum
            seen_values.add(current_sum)


def test_part2():
    assert day1b("+1 -1") == 0
    assert day1b("+3 +3 +4 -2 -4") == 10
    assert day1b("-6 +3 +8 +5 -6") == 5
    assert day1b("+7 +7 -2 -7 -4") == 14


if __name__ == '__main__':
    with open('./day1_input.txt') as f:
        data = f.read()
    
    print(day1a(data))
    print(day1b(data))
