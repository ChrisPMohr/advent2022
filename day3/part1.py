from collections import defaultdict, Counter
from math import floor


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    common = []
    for line in lines:
        line = line.strip()
        part1 = set(line[:floor(len(line)/2)])
        part2 = set(line[floor(len(line)/2):])
        common.extend(list(part1.intersection(part2)))

    s = 0
    for i in common:
        if ord(i) >= ord('a'):
            s += 1 + ord(i) - ord('a')
        else:
            s += 27 + ord(i) - ord('A')
    print(s)


if __name__ == '__main__':
    main()
