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
        return grid

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
    "N": (0, -1),
    "S": (0, 1),
    "E": (1, 0),
    "W": (-1, 0),
    "NW": (-1, -1),
    "NE": (1, -1),
    "SW": (-1, 1),
    "SE": (1, 1),
}

move_frees = {
    "N": ["NE", "N", "NW"],
    "S": ["SE", "S", "SW"],
    "E": ["NE", "E", "SE"],
    "W": ["NW", "W", "SW"]
}

def proposed_move(pos, grid, move_order):
    all_free = True
    for move in dirs.values():
        new_pos = (pos[0] + move[0], pos[1] + move[1])
        if grid.items.get(new_pos, ".") != ".":
            all_free = False
            break
    if all_free:
        return None
    for move in move_order:
        free_dirs = move_frees[move]
        all_free = True
        for free_dirs in free_dirs:
            free_move = dirs[free_dirs]
            new_pos = (pos[0] + free_move[0], pos[1] + free_move[1])
            if grid.items.get(new_pos, ".") != ".":
                all_free = False
                break
        if all_free:
            return move
    return None


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    grid = Grid.build_from_lines(lines)
    grid.print()
    print("-" * 30)

    move_order = ["N", "S", "W", "E"]
    round = 0
    while True:
        round += 1
        proposed_new_positions = dict()
        any_move = False
        for pos, c in grid.items.items():
            if c == ".":
                continue
            move_dir = proposed_move(pos, grid, move_order)
            # print(pos, "proposed", move_dir)
            if move_dir is None:
                continue
            move = dirs[move_dir]
            new_pos = (pos[0] + move[0], pos[1] + move[1])
            if new_pos not in proposed_new_positions:
                proposed_new_positions[new_pos] = pos
            else:
                proposed_new_positions[new_pos] = None
        move_order.append(move_order.pop(0))

        for new_pos, old_pos in proposed_new_positions.items():
            if old_pos is not None:
                any_move = True
                grid.items[new_pos] = grid.items[old_pos]
                grid.items[old_pos] = "."
        if not any_move:
            print(round)
            return
        # print("Round", round+1)
        # grid.print()
        # print("-" * 30)

    count = 0
    max_x = grid.max_x
    min_x = grid.min_x
    for y in range(grid.min_y, grid.max_y+1):
        for x in range(min_x, max_x + 1):
            if grid.items.get((x, y)) != "#":
                count += 1
    print(count)




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
