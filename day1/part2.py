from collections import defaultdict, Counter


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))

    elves = []
    cur_elf = []
    for line in lines:
        line = line.strip()
        if line:
            cur_elf.append(int(line))
        else:
            elves.append(cur_elf)
            cur_elf = []
    elves.append(cur_elf)
    sums = [sum(elf) for elf in elves]
    sums.sort(reverse=True)

    print(sum(sums[:3]))

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