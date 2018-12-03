# https://adventofcode.com/2018/day/2

import collections


def analyze_entry(entry):
    counts = collections.Counter(entry)
    return (2 in counts.values(), 3 in counts.values())


def day2a(data):
    overall = [0, 0]
    for entry in data.split():
        tmp = analyze_entry(entry)
        overall[0] += tmp[0]
        overall[1] += tmp[1]
    return overall[0] * overall[1]


def test_day2a():
    input = """
abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
"""
    assert day2a(input) == 12

def test_analyze_entry():
    assert analyze_entry("abcdef") == (0, 0)
    assert analyze_entry("bababc") == (1, 1)
    assert analyze_entry("abbcde") == (1, 0)
    assert analyze_entry("abcccd") == (0, 1)
    assert analyze_entry("aabcdd") == (1, 0)
    assert analyze_entry("abcdee") == (1, 0)
    assert analyze_entry("ababab") == (0, 1)


if __name__ == "__main__":
    with open('day2_input.txt') as f:
        data = f.read()
    print(day2a(data))