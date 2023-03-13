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
        return min(x for x, y, z in self.items)

    @property
    def max_x(self):
        return max(x for x, y, z in self.items)

    @property
    def min_y(self):
        return min(y for x, y, z in self.items)

    @property
    def max_y(self):
        return max(y for x, y, z in self.items)

    @property
    def min_z(self):
        return min(z for x, y, z in self.items)

    @property
    def max_z(self):
        return max(z for x, y, z in self.items)

    def print(self):
        min_x = self.min_x
        max_x = self.max_x
        for y in range(self.min_y, self.max_y+1):
            print(''.join([self.items.get((x, y), " ") for x in range(min_x, max_x+1)]))


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()
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

    outside_space = set()
    pixel_queue = deque()

    min_x = grid.min_x
    min_y = grid.min_y
    min_z = grid.min_z
    max_x = grid.max_x
    max_y = grid.max_y
    max_z = grid.max_z
    first_pixel = (min_x - 1, min_y - 1, min_z - 1)
    outside_space.add(first_pixel)
    pixel_queue.append(first_pixel)
    while pixel_queue:
        pos = pixel_queue.popleft()
        x, y, z = pos
        for d in dirs:
            new_x = d[0] + x
            new_y = d[1] + y
            new_z = d[2] + z
            new_pos = (new_x, new_y, new_z)
            if min_x - 1 <= new_x <= max_x + 1 and min_y - 1 <= new_y <= max_y + 1 and min_z - 1 <= new_z <= max_z + 1:
                if new_pos not in grid.items and new_pos not in outside_space:
                    outside_space.add(new_pos)
                    pixel_queue.append(new_pos)

    # print(sorted(list(outside_space)))

    exterior_pixels = set()
    for x, y, z in grid.items.keys():
        is_exterior = False
        for d in dirs:
            new_pos = (d[0] + x, d[1] + y, d[2] + z)
            if new_pos in outside_space:
                is_exterior = True
                break
        if is_exterior:
            exterior_pixels.add((x, y, z))

    print("interior pixels", grid.items.keys()-exterior_pixels)
    print(len(exterior_pixels))

    sides = 0
    for x, y, z in exterior_pixels:
        for d in dirs:
            new_pos = (d[0] + x, d[1] + y, d[2] + z)
            if new_pos in outside_space:
                sides += 1
    print(sides)



if __name__ == '__main__':
    main()
