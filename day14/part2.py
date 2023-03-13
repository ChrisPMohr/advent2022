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
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()
    # line = open('example.txt', 'r').readline()
    # line = open('input.txt', 'r').readline()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))  # Nums on one line
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))  # Nums on one line

    grid = Grid()

    for line in lines:
        line = line.strip()
        segments = [tuple(map(int, s.split(","))) for s in line.split(" -> ")]
        for s1, s2 in zip(segments[:-1], segments[1:]):
            grid.items[s1] = '#'
            grid.items[s2] = '#'
            if s1[0] == s2[0]:
                for y in range(min(s1[1], s2[1]), max(s1[1], s2[1])):
                    grid.items[(s1[0], y)] = '#'
            elif s1[1] == s2[1]:
                for x in range(min(s1[0], s2[0]), max(s1[0], s2[0])):
                    grid.items[(x, s1[1])] = '#'

    orig_max_y = grid.max_y
    new_max_y = orig_max_y + 2
    for x in range(500 - new_max_y - 1, 500 + new_max_y + 2):
        grid.items[(x, new_max_y)] = '#'
    # grid.print()
    # print("-" * 40)

    orig_max_y = grid.max_y

    dirs = [(0, 1), (-1, 1), (1, 1)]

    sand_count = 0
    sand_origin = (500, 0)
    while True:
        new_sand = sand_origin

        while True:
            updated = False
            for d in dirs:
                new_pos = (new_sand[0] + d[0], new_sand[1] + d[1])
                if new_pos not in grid.items:
                    new_sand = new_pos
                    updated = True
                    break
            if not updated:
                if new_sand == sand_origin:
                    sand_count += 1
                    print(sand_count)
                    return
                grid.items[new_sand] = 'o'
                # grid.print()
                # print("-" * 40)
                sand_count += 1
                break








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
