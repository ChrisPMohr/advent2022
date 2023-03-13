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
                    # print("end_pos", (x, y))
                    grid.items[grid.end_pos] = transform('z')
        return grid


dirs = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


def bfs(grid, start, best_distance):
    poses = [(start, 0)]
    seen = set()

    while poses:
        pos, distance = poses.pop(0)
        # if distance > best_distance:
        #     return best_distance
        if pos in seen:
            continue
        seen.add(pos)
        for d in dirs:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
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

    grid = Grid.build_from_lines(lines, transform=ord)
    all_as = []
    for pos, v in grid.items.items():
        if v == ord('a'):
            all_as.append(pos)

    best_distance = 10000000
    for pos in all_as:
        dist = bfs(grid, pos, best_distance)
        if dist and dist < best_distance:
            best_distance = dist
    print(best_distance)


if __name__ == '__main__':
    main()
