from collections import defaultdict, Counter


class Grid(object):

    def __init__(self):
        self.items = {}
        self.start_pos = None
        self.end_pos = None

    @classmethod
    def build_from_lines(cls, lines, transform=lambda c: c):
        grid = cls()
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                grid.items[(x, y)] = transform(c)
                if c == 'S':
                    grid.start_pos = (x, y)
                    grid.items[grid.start_pos] = transform('a')
                if c == 'E':
                    grid.end_pos = (x, y)
                    print("end_pos", (x, y))
                    grid.items[grid.end_pos] = transform('z')
        return grid

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


dirs = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def bfs(grid):
    poses = [(grid.start_pos, 0)]
    seen = set()

    while True:
        pos, distance = poses.pop(0)
        if pos in seen:
            continue
        seen.add(pos)
        print(pos, grid.items[pos], distance)
        for d in dirs:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            print("checking new_pos", new_pos, grid.items.get(new_pos))
            if new_pos in seen:
                continue
            if new_pos not in grid.items:
                continue
            height = grid.items[pos]
            new_height = grid.items[new_pos]
            if new_height - height > 1:
                continue
            if new_pos == grid.end_pos:
                return distance + 1
            poses.append((new_pos, distance+1))


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()
    # line = open('example.txt', 'r').readline()
    # line = open('input.txt', 'r').readline()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))  # Nums on one line
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))  # Nums on one line

    grid = Grid.build_from_lines(lines, transform=ord)
    print(bfs(grid))



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
