from collections import defaultdict, Counter


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))  # Nums on one line
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))  # Nums on one line

    count = 0
    for line in lines:
        line = line.strip()
        elf1, elf2 = line.split(',')
        r11, r12 = elf1.split('-')
        r21, r22 = elf2.split('-')
        r11 = int(r11)
        r12 = int(r12)
        r21 = int(r21)
        r22 = int(r22)
        if (r11 >= r21 and r22 >= r11) or (r21 >= r11 and r12 >= r21):
            print("overlap", line)
            count += 1
    print(count)

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
