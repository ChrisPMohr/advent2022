from collections import defaultdict, Counter
from itertools import cycle


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
        for y in range(self.max_y, -1, -1):
            print(''.join([self.items.get((x, y), ".") for x in range(0, 7)]))


def main():
    # line = open('example.txt', 'r').readline()
    line = open('input.txt', 'r').readline()

    shapes = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (0, 1), (1, 0), (1, 1)]
    ]

    moves = cycle(line.strip())
    shapes = cycle(shapes)

    grid = Grid()

    num_shapes = 0
    while num_shapes < 2022:
        num_shapes += 1
        new_shape = next(shapes)
        # print(new_shape)
        new_shape_x = 2
        new_shape_y = (grid.max_y if grid.items else -1) + 4

        while True:
            next_move = next(moves)
            possible_new_shape_x = new_shape_x + (1 if next_move == '>' else -1)
            valid = True
            for box_x, box_y in new_shape:
                new_box_x = box_x + possible_new_shape_x
                new_box_y = box_y + new_shape_y
                if new_box_x < 0 or new_box_x > 6 or (new_box_x, new_box_y) in grid.items:
                    valid = False
                    break
            if valid:
                new_shape_x = possible_new_shape_x

            possible_new_shape_y = new_shape_y - 1
            valid = True
            for box_x, box_y in new_shape:
                new_box_x = box_x + new_shape_x
                new_box_y = box_y + possible_new_shape_y
                if new_box_y < 0 or (new_box_x, new_box_y) in grid.items:
                    valid = False
                    break
            if valid:
                new_shape_y = possible_new_shape_y
            else:
                # print("Adding shape")
                for box_x, box_y in new_shape:
                    new_box_x = box_x + new_shape_x
                    new_box_y = box_y + new_shape_y
                    grid.items[(new_box_x, new_box_y)] = '#'
                break
            #
            # for box_x, box_y in new_shape:
            #     new_box_x = box_x + new_shape_x
            #     new_box_y = box_y + new_shape_y
            #     grid.items[(new_box_x, new_box_y)] = '@'
            #
            # grid.print()
            # print('-' * 40)
            #
            # for box_x, box_y in new_shape:
            #     new_box_x = box_x + new_shape_x
            #     new_box_y = box_y + new_shape_y
            #     del grid.items[(new_box_x, new_box_y)]

        # grid.print()
        # print('-' * 40)



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

    print(grid.max_y + 1)


if __name__ == '__main__':
    main()
