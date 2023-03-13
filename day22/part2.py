from collections import defaultdict, Counter

import re


# cube_size = 4
cube_size = 50

# cube_map = [
#     [None, None, 1, None],
#     [2, 3, 4, None],
#     [None, None, 5, 6]
# ]
cube_map = [
    [None, 1    , 2],
    [None, 3    , None],
    [4   , 5    , None],
    [6   ,  None, None]
]
cube_connections = {
    (1, "U"): (6, "L"),
    (1, "R"): (2, "L"),
    (1, "D"): (3, "U"),
    (1, "L"): (4, "L"),
    (2, "U"): (6, "D"),
    (2, "R"): (5, "R"),
    (2, "D"): (3, "R"),
    (2, "L"): (1, "R"),
    (3, "U"): (1, "D"),
    (3, "R"): (2, "D"),
    (3, "D"): (5, "U"),
    (3, "L"): (4, "U"),
    (4, "U"): (3, "L"),
    (4, "R"): (5, "L"),
    (4, "D"): (6, "U"),
    (4, "L"): (1, "L"),
    (5, "U"): (3, "D"),
    (5, "R"): (2, "R"),
    (5, "D"): (6, "R"),
    (5, "L"): (4, "R"),
    (6, "U"): (4, "D"),
    (6, "R"): (5, "D"),
    (6, "D"): (2, "U"),
    (6, "L"): (1, "U"),
}

cube_coords = {}
for y, row in enumerate(cube_map):
    for x, face in enumerate(row):
        if face is not None:
            cube_coords[face] = (x, y)

# cube_connections = {
#     (1, "U"): (2, "U"),
#     (1, "R"): (6, "R"),
#     (1, "D"): (4, "U"),
#     (1, "L"): (3, "U"),
#     (2, "U"): (1, "U"),
#     (2, "R"): (3, "L"),
#     (2, "D"): (5, "D"),
#     (2, "L"): (6, "D"),
#     (3, "U"): (1, "L"),
#     (3, "R"): (4, "L"),
#     (3, "D"): (5, "L"),
#     (3, "L"): (2, "R"),
#     (4, "U"): (1, "D"),
#     (4, "R"): (6, "U"),
#     (4, "D"): (5, "U"),
#     (4, "L"): (3, "R"),
#     (5, "U"): (4, "D"),
#     (5, "R"): (6, "L"),
#     (5, "D"): (2, "D"),
#     (5, "L"): (3, "D"),
#     (6, "U"): (4, "R"),
#     (6, "R"): (1, "R"),
#     (6, "D"): (2, "L"),
#     (6, "L"): (5, "R"),
# }


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
        return self.items[(x,y)] not in {"#", " "}

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

dir_char = {
    "L": "<",
    "R": ">",
    "U": "^",
    "D": "v"
}


def right(dir):
    s = "RDLUR"
    return s[s.index(dir) + 1]


def left(dir):
    s = "LDRUL"
    return s[s.index(dir) + 1]


def reverse(dir):
    return left(left(dir))


def which_face(pos):
    face_x = (pos[0] - 1) // cube_size
    face_y = (pos[1] - 1) // cube_size
    try:
        return cube_map[face_y][face_x]
    except IndexError:
        return None


def wrap(old_pos, old_facing):
    old_face = which_face(old_pos)
    old_cube_coords = cube_coords[old_face]
    new_face, new_edge = cube_connections[(old_face, old_facing)]
    if old_facing == "U":
        face_min_x = old_cube_coords[0] * cube_size + 1
        old_pos_from_left = old_pos[0] - face_min_x
    elif old_facing == "D":
        face_max_x = (old_cube_coords[0] + 1) * cube_size
        old_pos_from_left = face_max_x - old_pos[0]
    elif old_facing == "R":
        face_min_y = old_cube_coords[1] * cube_size + 1
        old_pos_from_left = old_pos[1] - face_min_y
    else:  # if old_facing == "L":
        face_max_y = (old_cube_coords[1] + 1) * cube_size
        old_pos_from_left = face_max_y - old_pos[1]

    new_facing = reverse(new_edge)
    new_cube_coords = cube_coords[new_face]

    if new_edge == "U":
        face_max_x = (new_cube_coords[0] + 1) * cube_size
        face_min_y = new_cube_coords[1] * cube_size + 1
        new_pos = (face_max_x - old_pos_from_left, face_min_y)
    elif new_edge == "D":
        face_min_x = new_cube_coords[0] * cube_size + 1
        face_max_y = (new_cube_coords[1] + 1) * cube_size
        new_pos = (face_min_x + old_pos_from_left, face_max_y)
    elif new_edge == "R":
        face_max_x = (new_cube_coords[0] + 1) * cube_size
        face_max_y = (new_cube_coords[1] + 1) * cube_size
        new_pos = (face_max_x, face_max_y - old_pos_from_left)
    else:  # if new_edge == "L":
        face_min_x = new_cube_coords[0] * cube_size + 1
        face_min_y = new_cube_coords[1] * cube_size + 1
        new_pos = (face_min_x, face_min_y + old_pos_from_left)
    return new_pos, new_facing


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()


    # print(Counter(cube_connections.values()).most_common(1))
    #
    # for c1, c2 in cube_connections.items():
    #     if cube_connections[c2] != c1:
    #         print("mismatch", c1, c2)
    # return

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
            # print("moving space", move)
            d = dirs[facing]
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            new_facing = facing
            old_face = which_face(pos)
            new_face = which_face(new_pos)
            if old_face != new_face:
                new_pos, new_facing = wrap(pos, facing)
                print("Wrapping from", pos, "to", new_pos)
            if grid.is_open(*new_pos):
                pos = new_pos
                facing = new_facing
                grid.items[pos] = dir_char[facing]
        if turn == "R":
            facing = right(facing)
        elif turn == "L":
            facing = left(facing)
        grid.items[pos] = dir_char[facing]
        # print("pos is", pos)
        # grid.print()

    facing_score = {
        "R": 0,
        "D": 1,
        "L": 2,
        "U": 3
    }
    score = pos[1] * 1000 + pos[0] * 4 + facing_score[facing]
    print(score, pos, facing)
    grid.print()


if __name__ == '__main__':
    main()
