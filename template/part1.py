from collections import defaultdict, Counter


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
    def min_x(self):
        return min(x for x, y in self.items)

    @property
    def max_x(self):
        return max(x for x, y in self.items)

    @property
    def min_y(self):
        return min(y for x, y in self.items)

    @property
    def max_y(self):
        return max(y for x, y in self.items)

    def print(self):
        min_x = self.min_x
        max_x = self.max_x
        for y in range(self.min_y, self.max_y+1):
            print(''.join([self.items.get((x, y), " ") for x in range(min_x, max_x+1)]))


def main():
    lines = open('example.txt', 'r').readlines()
    # lines = open('input.txt', 'r').readlines()
    # line = open('example.txt', 'r').readline()
    # line = open('input.txt', 'r').readline()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))  # Nums on one line
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))  # Nums on one line

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
