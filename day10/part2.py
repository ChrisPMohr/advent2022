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
    def max_x(self):
        return max(x for x, y in self.items)

    @property
    def max_y(self):
        return max(x for x, y in self.items)

    def print(self):
        max_x = self.max_x
        for y in range(self.max_y):
            print(''.join([self.items[(x, y)] for x in range(max_x)]))


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()
    # line = open('example.txt', 'r').readline()
    # line = open('input.txt', 'r').readline()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))  # Nums on one line
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))  # Nums on one line

    x = 1
    cycles = 1
    s = 0

    screen = set()

    for line in lines:
        row = (cycles - 1) % 240 // 40
        col = (cycles - 1) % 40
        line = line.strip()
        print(f"Start cycle   {cycles}: begin executing {line}")
        if line == "noop":
            if x + 1 >= col >= x - 1:
                screen.add((col, row))
            print(f"During cycle   {cycles}: CRT draws pixel at position {col}")
            for y in range(cycles // 40 + 1):
                print(''.join(['#' if (x, y) in screen else '.' for x in range(40)]))
            print()
            cycles += 1
        else:
            # print(line)
            v = int(line.split(" ")[1])
            # print(cycles, "going to add", v)
            if x + 1 >= col >= x - 1:
                screen.add((col, row))

            print(f"During cycle   {cycles}: CRT draws pixel at position {col}")
            for y in range(cycles // 40 + 1):
                print(''.join(['#' if (x, y) in screen else '.' for x in range(40)]))
            print()

            cycles += 1
            row = (cycles - 1) % 240 // 40
            col = (cycles - 1) % 40
            if x + 1 >= col >= x - 1:
                screen.add((col, row))
            print(f"During cycle   {cycles}: CRT draws pixel at position {col}")
            for y in range(cycles // 40 + 1):
                print(''.join(['#' if (x, y) in screen else '.' for x in range(40)]))
            print()

            cycles += 1
            x += v
        print(f"End of cycle   {cycles-1}: finish executing {line} (Register X is now {x})")


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
