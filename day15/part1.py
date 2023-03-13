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

def dist(x1,y1, x2,y2):
    return abs(x1 - x2) + abs(y1 - y2)

def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    # row_y = 10
    row_y = 2000000

    grid = Grid()

    sensors = []
    beacons = set()

    excluded_ranges = []

    for line in lines:
        line = line.strip()
        sensor, beacon = line.split("Sensor at ")[1].split(": closest beacon is at ")
        x, y = sensor.split(", ")
        x1 = int(x.split("=")[1])
        y1 = int(y.split("=")[1])
        x, y = beacon.split(", ")
        x2 = int(x.split("=")[1])
        y2 = int(y.split("=")[1])
        beacons.add((x2, y2))

        d = dist(x1,y1,x2,y2)
        sensors.append(((x1,y1), d))

        x_dist = d - abs(y1 - row_y)
        if x_dist > 0:
            # print(dist(x1-x_dist, row_y, x1, y1), d)
            excluded_ranges.append((x1-x_dist, x1+x_dist))

        # for x in range(x1 - d, x1 + d + 1):
        #     for y in range(y1 - d, y1 + d + 1):
        #         # print("trying", x, y)
        #         if dist(x1, y1, x, y) <= d and (x,y) not in grid.items:
        #             grid.items[(x,y)] = '#'

        grid.items[(x1, y1)] = "S"
        grid.items[(x2, y2)] = "B"

    excluded_ranges.sort()
    print(excluded_ranges)

    current_range = None
    count = 0
    for r1, r2 in excluded_ranges:
        print(r1, r2)
        if current_range == None:
            current_range = (r1, r2)
        else:
            cr1, cr2 = current_range
            if r1 <= cr2:
                print("merging with", current_range)
                current_range = (cr1, max(cr2, r2))
                print("new range", current_range)
            else:
                count += cr2 - cr1 + 1
                current_range = (r1, r2)
                print("starting new range", current_range)

    cr1, cr2 = current_range
    count += cr2 - cr1 + 1
    print(count - sum([1 for (x, y) in beacons if y == row_y]))


    # for x in range(-5, 30):
    #     if (x, row_y) in beacons:
    #         continue
    #
    #     included = False
    #     for x1, x2 in excluded_ranges:
    #         if x1 <= x <= x2:
    #             included = True
    #             break
    #     if included:
    #         count += 1
    # print(count)
    # print(excluded_ranges)

    # grid.print()
    # print(sum([1 for x in range(grid.min_x, grid.max_x+1) if not (x, y) in beacons and any([dist(x, y, sx, sy) <= d for (sx,sy), d in sensors])]))

    # print(sum([1 for x in range(grid.min_x, grid.max_x+1) if not (x, y) in beacons and any([dist(x, y, sx, sy) <= d for (sx,sy), d in sensors])]))


    # for pos, c in grid.items():
    #     if c == "B"
    # for x in range()

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
