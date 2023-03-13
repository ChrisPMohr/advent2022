from collections import defaultdict, Counter
from itertools import cycle
import numpy as np


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
    # line = open('example.txt', 'r').readline()
    # line = open('example2.txt', 'r').readline()
    line = open('input.txt', 'r').readline()

    shapes = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (0, 1), (1, 0), (1, 1)]
    ]

    base_moves = line.strip()

    max_shapes = 1000000000000
    # max_shapes = 10000
    if len(base_moves) % 5 == 0:
        cycle_size = len(base_moves)
    else:
        cycle_size = len(base_moves) * 5
    print(cycle_size)
    print(max_shapes % cycle_size)

    moves = cycle(base_moves)
    shapes = cycle(shapes)

    num_relevant_rows = 30

    grid = Grid()
    visible_rows = np.zeros(num_relevant_rows * 2 + 4, 7)
    visible_rows_bottom = 0
    max_y = 0

    after_cycle_repeats = False
    lines_at_target_start = 0
    shapes_after_cycles = 0
    result_lines = 0

    top_shapes_cycles = {}
    total_shapes = 0
    cycles = 0

    while True:
        cycles += 1

        print("--", cycles, "--")
        num_shapes = 0
        while num_shapes < cycle_size:
            # adjust array up by slicing
            # if num_shapes % 30:
            #     crop_level = grid.max_y - 30
            #     for x in range(0, 7):
            #         for y in range(grid.min_y, crop_level):
            #             if (x, y) in grid.items:
            #                 del grid.items[(x, y)]

            num_shapes += 1

            if after_cycle_repeats:
                shapes_after_cycles -= 1
                # print("decrementing target_shapes", shapes_after_cycles)
                if shapes_after_cycles < 0:
                    print('-' * 80)
                    print('-' * 80)
                    print('-' * 80)
                    lines_after_cycles = max_y - lines_at_target_start
                    result_lines += lines_after_cycles
                    print("lines after cycles", lines_after_cycles)
                    print("total", result_lines)
                    print('-' * 80)
                    print('-' * 80)
                    print('-' * 80)
                    return

            # print(num_shapes)
            new_shape = next(shapes)
            new_shape_x = 2
            new_shape_y = max_y + 4 if max_y > 0 else 3

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

        if not after_cycle_repeats:
            # calculate top_shapes
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
                print(sorted(list(top_shapes_cycles.values()) + [(cycles, grid.max_y + 1)]))
                repeated_cycle, repeated_lines = top_shapes_cycles[top_shapes]
                lines_in_repeats = max_y + 1 - repeated_lines
                print("Repeated cycles at", repeated_cycle, "and", cycles)
                print(f"{lines_in_repeats} lines in {cycles - repeated_cycle} cycles")

                remaining_shapes = max_shapes - num_shapes
                remaining_cycles = remaining_shapes // cycle_size
                repeats = remaining_cycles // (cycles - repeated_cycle)
                shapes_after_cycles = remaining_shapes - (cycles - repeated_cycle) * cycle_size * repeats

                result_lines += repeated_lines + lines_in_repeats * repeats

                after_cycle_repeats = True
                lines_at_target_start = max_y

                print("Remaining cycles", remaining_cycles)
                print("Number of repeats", repeats, "plus", shapes_after_cycles, "shapes")
                print("Total lines", max_y + repeats * lines_in_repeats, "after cycles")

            else:
                top_shapes_cycles[top_shapes] = (cycles, max_y)
                print((cycles, max_y))


if __name__ == '__main__':
    main()
