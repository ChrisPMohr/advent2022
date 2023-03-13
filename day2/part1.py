from collections import defaultdict, Counter


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))  # Nums on one line
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))  # Nums on one line

    me_score = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    game_score = {
        ('A', 'Y'): 6,
        ('B', 'Z'): 6,
        ('C', 'X'): 6,
        ('A', 'X'): 3,
        ('B', 'Y'): 3,
        ('C', 'Z'): 3,
    }

    score = 0
    for line in lines:
        opp, me = line.strip().split()
        score += me_score.get(me)
        score += game_score.get((opp, me), 0)
    print(score)


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
