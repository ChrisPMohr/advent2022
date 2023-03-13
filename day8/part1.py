from collections import defaultdict, Counter


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()
    # line = open('example.txt', 'r').readline()
    # line = open('input.txt', 'r').readline()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))  # Nums on one line
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))  # Nums on one line

    trees = []

    for line in lines:
        line = line.strip()
        trees.append([int(c) for c in line])

    max_y = len(lines)
    max_x = len(lines[0]) - 1

    visible_trees = set()
    for y in range(max_y):
        for x in range(max_x):
            is_visible = True
            for x2 in range(x):
                if trees[y][x2] >= trees[y][x]:
                    is_visible = False
                    break
            if is_visible:
                print((x,y), trees[y][x], "is visible from left")
                visible_trees.add((x,y))

            is_visible = True
            for x2 in range(x+1, max_x):
                if trees[y][x2] >= trees[y][x]:
                    is_visible = False
                    break
            if is_visible:
                print((x,y), trees[y][x], "is visible from right")
                visible_trees.add((x, y))

    for x in range(max_x):
        for y in range(max_y):
            is_visible = True
            for y2 in range(y):
                if trees[y2][x] >= trees[y][x]:
                    is_visible = False
                    break
            if is_visible:
                print((x,y), trees[y][x], "is visible from top")
                visible_trees.add((x, y))

            is_visible = True
            for y2 in range(y + 1, max_y):
                if trees[y2][x] >= trees[y][x]:
                    is_visible = False
                    break
            if is_visible:
                print((x,y), trees[y][x], "is visible from bottom")
                visible_trees.add((x, y))

    print(len(visible_trees))
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
