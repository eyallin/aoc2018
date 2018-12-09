# https://adventofcode.com/2018/day/5


def react(s):
    units = list(set(c.lower() for c in s))
    pairs = ['{}{}'.format(c, c.upper()) for c in units] + ['{}{}'.format(c.upper(), c) for c in units]
    
    orig = s
    while True:
        for pair in pairs:
            s = s.replace(pair, '')
        if orig == s:
            return s
        orig = s


def test_react():
    s = 'dabAcCaCBAcCcaDA'
    assert len(react(s)) == 10


def improve_reaction(s):
    s = react(s)
    units = set(c.lower() for c in s)
    unit_results = {}
    for unit in units:
        s2 = s.replace(unit, '').replace(unit.upper(), '')
        s2 = react(s2)
        unit_results[unit] = s2
    return min(unit_results.items(), key=lambda x: len(x[1]))


def test_improvement():
    s = 'dabAcCaCBAcCcaDA'
    c, s = improve_reaction(s)
    assert c == 'c'
    assert s == 'daDA'


if __name__ == "__main__":
    with open('day5_input.txt') as f:
        data = f.read()

    print(len(react(data)))

    c, seq = improve_reaction(data)
    print(len(seq))