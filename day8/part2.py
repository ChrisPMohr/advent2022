from collections import defaultdict, Counter


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    trees = []

    for line in lines:
        line = line.strip()
        trees.append([int(c) for c in line])

    max_y = len(lines)
    max_x = len(lines[0]) - 1

    max_vd = 0

    for y in range(max_y):
        for x in range(max_x):
            vd = 1

            direction_vd = 0
            for x2 in range(x-1, -1, -1):
                direction_vd += 1
                if trees[y][x2] >= trees[y][x]:
                    break
            vd *= direction_vd

            direction_vd = 0
            for x2 in range(x + 1, max_x):
                direction_vd += 1
                if trees[y][x2] >= trees[y][x]:
                    break
            vd *= direction_vd

            direction_vd = 0
            for y2 in range(y-1, -1, -1):
                direction_vd += 1
                if trees[y2][x] >= trees[y][x]:
                    break
            vd *= direction_vd

            direction_vd = 0
            for y2 in range(y + 1, max_y):
                direction_vd += 1
                if trees[y2][x] >= trees[y][x]:
                    break
            vd *= direction_vd

            if vd >= max_vd:
                max_vd = vd
    print(max_vd)



if __name__ == '__main__':
    main()
