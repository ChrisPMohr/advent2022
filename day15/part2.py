from collections import defaultdict, Counter


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    sensors = []

    for line in lines:
        line = line.strip()
        sensor, beacon = line.split("Sensor at ")[1].split(": closest beacon is at ")
        x, y = sensor.split(", ")
        x1 = int(x.split("=")[1])
        y1 = int(y.split("=")[1])
        x, y = beacon.split(", ")
        x2 = int(x.split("=")[1])
        y2 = int(y.split("=")[1])
        d = dist(x1, y1, x2, y2)
        sensors.append(((x1, y1), d))

    for row_y in range(0, 4000000+1):
        excluded_ranges = []
        for (x1, y1), d in sensors:
            x_dist = d - abs(y1 - row_y)
            if x_dist > 0:
                excluded_ranges.append((x1-x_dist, x1+x_dist))

        excluded_ranges.sort()

        current_range = None
        for r1, r2 in excluded_ranges:
            if current_range is None:
                current_range = (r1, r2)
            else:
                cr1, cr2 = current_range
                if r1 <= cr2 + 1:
                    current_range = (cr1, max(cr2, r2))
                else:
                    print((cr2+1)*4000000 + row_y)
                    return



if __name__ == '__main__':
    main()
