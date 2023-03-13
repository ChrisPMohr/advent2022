from collections import defaultdict, Counter
from math import floor


def main():
    # lines = list(open('example.txt', 'r').readlines())
    lines = open('input.txt', 'r').readlines()

    badges = []
    for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
        l1 = set(l1.strip())
        l2 = set(l2.strip())
        l3 = set(l3.strip())
        i = list(l1.intersection(l2).intersection(l3))[0]
        badges.append(i)

    s = 0
    for i in badges:
        if ord(i) >= ord('a'):
            s += 1 + ord(i) - ord('a')
        else:
            s += 27 + ord(i) - ord('A')
    print(s)


if __name__ == '__main__':
    main()
