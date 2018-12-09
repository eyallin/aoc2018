# https://adventofcode.com/2018/day/5



def react(s):
    while True:
        print(len(s))
        for i, c2 in enumerate(s[1:], 1):
            c1 = s[i-1]
            if c1.lower() == c2.lower() and c1 != c2:
                if i == 1:
                    s = s[2:]
                else:
                    s = s[:i-1] + s[i+1:]
                break
        else:
            return s


def test_react():
    s = 'dabAcCaCBAcCcaDA'
    assert len(react(s)) == 10

if __name__ == "__main__":
    with open('day5_input.txt') as f:
        data = f.read()
    print(react(data))