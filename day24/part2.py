from collections import defaultdict, Counter, deque


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
    "^": (0, -1),
    "v": (0, 1),
    ">": (1, 0),
    "<": (-1, 0),
}

def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    grid = Grid.build_from_lines(lines, transform=lambda c: "." if c != "#" else "#")
    blizzards = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in dirs.keys():
                blizzards.append(((x, y), c))

    blizzard_poses = {pos for pos, _ in blizzards}
    # grid.print()
    # print(blizzards)

    min_x = grid.min_x
    max_x = grid.max_x
    min_y = grid.min_y
    max_y = grid.max_y

    start_y = grid.min_y
    for start_x in range(grid.min_x, grid.max_x + 1):
        if grid.items[(start_x, start_y)] == ".":
            break
    start_pos = (start_x, start_y)

    end_y = grid.max_y
    for end_x in range(grid.min_x, grid.max_x + 1):
        if grid.items[(end_x, end_y)] == ".":
            break
    end_pos = (end_x, end_y)

    q = deque([(start_pos, 0, 0)])
    last_step = -1
    seen = set()
    while q:
        pos, stage, step = q.popleft()
        if (pos, stage, step) in seen:
            continue
        seen.add((pos, stage, step))
        if pos == end_pos and stage == 2:
            print(step)
            break
        new_stage = stage
        if pos == end_pos and stage == 0:
            new_stage = 1
        if pos == start_pos and stage == 1:
            new_stage = 2
        if step != last_step:
            new_blizzards = []
            for blizz_pos, blizz_dir in blizzards:
                move = dirs[blizz_dir]
                new_pos = (blizz_pos[0] + move[0], blizz_pos[1] + move[1])
                if grid.items[new_pos] == "#":
                    if blizz_dir == "^":
                        new_pos = (new_pos[0], max_y - 1)
                    elif blizz_dir == "v":
                        new_pos = (new_pos[0], min_y + 1)
                    elif blizz_dir == ">":
                        new_pos = (min_x + 1, new_pos[1])
                    else:
                        new_pos = (max_x - 1, new_pos[1])
                new_blizzards.append((new_pos, blizz_dir))
            blizzards = new_blizzards
            last_step = step
            # print(last_step)
            # print(new_blizzards)
            blizzard_poses = {pos for pos, _ in blizzards}
        # generate next steps
        for dx, dy in dirs.values():
            new_pos = (pos[0] + dx, pos[1] + dy)
            if new_pos not in blizzard_poses and grid.items.get(new_pos) == ".":
                q.append((new_pos, new_stage, step + 1))
        new_pos = pos
        if new_pos not in blizzard_poses and grid.items.get(new_pos) == ".":
            q.append((new_pos, new_stage, step + 1))



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
