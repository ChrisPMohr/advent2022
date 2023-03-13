from collections import defaultdict, Counter

import re


class Grid(object):

    def __init__(self):
        self.items = {}

    @classmethod
    def build_from_lines(cls, lines, transform=lambda c: c):
        grid = cls()
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                grid.items[(x, y)] = transform(c)

    def is_open(self, x, y):
        return self.items[(x,y)] == "."

    def exists(self, x, y):
        return self.items.get((x,y), " ") != " "

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

dirs = {
    "L": (-1, 0),
    "R": (1, 0),
    "D": (0, 1),
    "U": (0, -1)
}


def right(dir):
    s = "RDLUR"
    return s[s.index(dir) + 1]


def left(dir):
    s = "LDRUL"
    return s[s.index(dir) + 1]


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()


    grid = Grid()

    for y, line in enumerate(lines):
        line = line[:-1]
        if line == "":
            break
        for x, c in enumerate(line):
            grid.items[(x + 1, y + 1)] = c

    grid.print()

    instruction_line = lines.pop().strip()
    print(instruction_line)
    instructions = []
    current_instruction = None
    for c in instruction_line:
        if c in "LR":
            instructions.append((current_instruction, c))
            current_instruction = None
        else:
            if current_instruction is None:
                current_instruction = int(c)
            else:
                current_instruction = current_instruction * 10 + int(c)
    instructions.append((current_instruction, None))
    print(instructions)

    x = grid.min_x
    y = grid.min_y
    while True:
        if grid.is_open(x, y):
            break
        x += 1
    pos = (x, y)
    facing = "R"

    for num_moves, turn in instructions:
        print("Doing move", num_moves, turn)
        for move in range(num_moves):
            print("moving space", move)
            d = dirs[facing]
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            while not grid.exists(*new_pos):
                print(new_pos, "wraps around")
                new_pos = ((new_pos[0] + d[0]) % grid.max_x, (new_pos[1] + d[1]) % grid.max_y)
            if grid.is_open(*new_pos):
                pos = new_pos
        if turn == "R":
            facing = right(facing)
        elif turn == "L":
            facing = left(facing)

    facing_score = {
        "R": 0,
        "D": 1,
        "L": 2,
        "U": 3
    }
    score = pos[1] * 1000 + pos[0] * 4 + facing_score[facing]
    print(score, pos, facing)




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
