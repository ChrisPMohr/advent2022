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

    @property
    def min_x(self):
        return min(x for x, y in self.items)

    @property
    def max_x(self):
        return max(x for x, y, z in self.items)

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
    lines = open('example.txt', 'r').readlines()
    # lines = open('input.txt', 'r').readlines()
    # line = open('example.txt', 'r').readline()
    # line = open('input.txt', 'r').readline()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))  # Nums on one line
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))  # Nums on one line

    grid = Grid()

    for line in lines:
        pos = tuple(map(int, line.strip().split(",")))
        grid.items[pos] = '#'

    dirs = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1)
    ]

    all_dirs = [ ]
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                all_dirs.append((x, y, z))

    all_dirs.remove((0, 0, 0))

    exterior_pixels = set()
    interior_pixels = set()
    pixel_queue = deque()
    max_x = grid.max_x
    for pos in grid.items.keys():
        if pos[0] == max_x:
            pixel_queue.append(pos)
            exterior_pixels.add(pos)

    while pixel_queue:
        x, y, z = pixel_queue.popleft()
        any_air = False
        for d in dirs:
            new_pos = (d[0] + x, d[1] + y, d[2] + z)
            if new_pos not in grid.items:
                any_air = True
        print(f"Looking at {(x, y, z)}, any_air {any_air}?")
        if not any_air:
            continue

        for d in all_dirs:
            new_pos = (d[0] + x, d[1] + y, d[2] + z)
            if new_pos in grid.items:
                if new_pos not in exterior_pixels:
                    pixel_queue.append(new_pos)
                    exterior_pixels.add(new_pos)
                else:
                    interior_pixels.add(new_pos)

    print(len(exterior_pixels), len(interior_pixels))

    filled_pixels = set()
    pixel_queue = deque()
    if interior_pixels:
        pixel_queue.append(interior_pixels.pop())
        while pixel_queue:
            (x, y, z) = pixel_queue.popleft()
            for d in dirs:
                new_pos = (d[0] + x, d[1] + y, d[2] + z)
                if new_pos not in exterior_pixels and new_pos not in filled_pixels:
                    filled_pixels.add(new_pos)
                    pixel_queue.append(new_pos)

    sides = 0
    for x, y, z in exterior_pixels:
        for d in dirs:
            new_pos = (d[0] + x, d[1] + y, d[2] + z)
            if new_pos not in grid.items and new_pos not in filled_pixels:
                sides += 1
    print(sides)


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
