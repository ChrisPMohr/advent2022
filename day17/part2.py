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

    def print(self, min_y=None):
        min_x = self.min_x
        max_x = self.max_x
        min_y = 0 if min_y is None else min_y
        for y in range(self.max_y, min_y - 1, -1):
            print(''.join([self.items.get((x, y), ".") for x in range(0, 7)]))


def main():
    line = open('example.txt', 'r').readline()
    # line = open('input.txt', 'r').readline()

    target_cycle = 1
    target_shapes = 80
    # target_cycle = 121
    # target_shapes = 1022445

    shapes = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (0, 1), (1, 0), (1, 1)]
    ]

    base_moves = line.strip()

    max_shapes = 1000000000000
    if len(base_moves) % 5 == 0:
        cycle_size = len(base_moves)
    else:
        cycle_size = len(base_moves) * 5
    print(cycle_size)
    print(max_shapes % cycle_size)

    moves = cycle(base_moves)
    shapes = cycle(shapes)

    grid = Grid()

    in_target = False
    lines_at_target_start = None


    top_shapes_cycles = {}
    total_shapes = 0
    cycles = 0

    max_y_hundreds = 0

    while True:
        cycles += 1

        if cycles - 1 == target_cycle:
            in_target = True
            print("In target")
            lines_at_target_start = grid.max_y + 100 * max_y_hundreds


        print("--", cycles, "--")
        num_shapes = 0
        while num_shapes < cycle_size:
            if num_shapes % 30:
                crop_level = grid.max_y - 30
                for x in range(0, 7):
                    for y in range(grid.min_y, crop_level):
                        if (x, y) in grid.items:
                            del grid.items[(x, y)]

            if grid.items and grid.max_y > 150:
                new_items = {}
                for (x, y) in list(grid.items.keys()):
                    new_items[(x, y-100)] = grid.items[(x, y)]
                    del grid.items[(x, y)]
                grid.items = new_items
                max_y_hundreds += 1

            num_shapes += 1

            if in_target:
                target_shapes -= 1
                # print("decrementing target_shapes", target_shapes)
                if target_shapes < 0:
                    print('-' * 80)
                    print('-' * 80)
                    print('-' * 80)
                    print(grid.max_y + 100 * max_y_hundreds - lines_at_target_start)
                    print('-' * 80)
                    print('-' * 80)
                    print('-' * 80)
                    in_target = False

            # print(num_shapes)
            new_shape = next(shapes)
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

        total_shapes += num_shapes


        # calculate top_shapes to
        max_y = grid.max_y
        # top_shapes_height = 10
        top_shapes_height = 20
        top_shapes = set()

        grid.print(grid.max_y - top_shapes_height)
        print("-" * 10)

        for x in range(0, 7):
            for y in range(-1 * top_shapes_height, 1):
                pos = (x, max_y + y)
                if pos in grid.items:
                    top_shapes.add((x, y))
        top_shapes = tuple(sorted(top_shapes))
        if top_shapes in top_shapes_cycles:
            repeated_cycle, repeated_lines = top_shapes_cycles[top_shapes]
            lines_in_repeats = (grid.max_y + max_y_hundreds * 100 + 1) - repeated_lines
            print("Repeated cycles at", repeated_cycle, "and", cycles)
            print(f"{lines_in_repeats} lines in {cycles - repeated_cycle} cycles")

            remaining_shapes = max_shapes - num_shapes
            remaining_cycles = remaining_shapes // cycle_size

            print("Remaining cycles", remaining_cycles)
            repeats = remaining_cycles // (cycles - repeated_cycle)
            print("Number of repeats", repeats, "plus", remaining_shapes - (cycles - repeated_cycle) * cycle_size * repeats, "shapes")
            print("Total lines", grid.max_y + max_y_hundreds + 100 + 1 + repeats * lines_in_repeats, "after cycles")

            print(sorted(list(top_shapes_cycles.values()) + [(cycles, grid.max_y + 1)]))
            return
        else:
            top_shapes_cycles[top_shapes] = (cycles, grid.max_y + max_y_hundreds * 100 + 1)
            print((cycles, grid.max_y + max_y_hundreds * 100 + 1))


if __name__ == '__main__':
    main()
