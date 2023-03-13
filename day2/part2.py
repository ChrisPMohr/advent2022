from collections import defaultdict, Counter


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))  # Nums on one line
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))  # Nums on one line

    me_score = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    me_move = {
        ('A', 'Y'): 'A',
        ('B', 'Y'): 'B',
        ('C', 'Y'): 'C',
        ('A', 'X'): 'C',
        ('B', 'X'): 'A',
        ('C', 'X'): 'B',
        ('A', 'Z'): 'B',
        ('B', 'Z'): 'C',
        ('C', 'Z'): 'A'}

    game_score = {
        ('A', 'B'): 6,
        ('B', 'C'): 6,
        ('C', 'A'): 6,
        ('A', 'A'): 3,
        ('B', 'B'): 3,
        ('C', 'C'): 3,
    }

    score = 0
    for line in lines:
        opp, result = line.strip().split()
        me = me_move.get((opp, result))
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
