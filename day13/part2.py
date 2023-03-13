from collections import defaultdict, Counter
import json
import functools


class Grid(object):

    def __init__(self):
        self.items = {}

    @classmethod
    def build_from_lines(cls, lines, transform=lambda c: c):
        grid = cls()
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                grid.items[(x, y)] = transform(c)

    @property
    def max_x(self):
        return max(x for x, y in self.items)

    @property
    def max_y(self):
        return max(x for x, y in self.items)

    def print(self):
        max_x = self.max_x
        for y in range(self.max_y):
            print(''.join([self.items[(x, y)] for x in range(max_x)]))


def comp(left, right, indent=0):
    print("  " * indent, left, '|',  right)
    # left < right = -1
    # left > right = 1

    if isinstance(left, int) and isinstance(right, int):
        return -1 if left < right else (1 if left > right else 0)
    if isinstance(left, list) and isinstance(right, list):
        l = min(len(left), len(right))
        for i in range(l):
            res = comp(left[i], right[i], indent+1)
            if res != 0:
                return res
        if len(left) < len(right):
            return -1
        if len(left) > len(right):
            return 1
        return 0
    else:
        if isinstance(left, int):
            left = [left]
        else:
            right = [right]
        return comp(left, right, indent+1)


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()
    # line = open('example.txt', 'r').readline()
    # line = open('input.txt', 'r').readline()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))  # Nums on one line
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))  # Nums on one line

    i = 0
    s = 0
    packets = []
    while lines:
        line = lines.pop(0).strip()
        if line:
            packets.append(json.loads(line))

    p1 = json.loads("[[2]]")
    p2 = json.loads("[[6]]")
    packets.append(p1)
    packets.append(p2)

    packets.sort(key=functools.cmp_to_key(comp))

    i1 = 0
    i2 = 0
    for i, p in enumerate(packets):
        if p == p1:
            i1 = i + 1
        if p == p2:
            i2 = i + 1
    print(i1 * i2)
    # print('\n'.join(str(p) for p in packets))

    # for line in lines:
    #     line = line.strip()

    # items = {}
    # for y, line in enumerate(lines):
    #     for x, c in enumerate(line.strip()):
    #         items[(x, y)] = int(c)

    # max_x = max(x for x,y in items)
    # max_y = max(y for x,y in items)
    # for y in range(0, max_y + 1):
    #     print("".join('#' if (x,y) in items else ' ' for x in range(0, max_x+10)))


if __name__ == '__main__':
    main()
