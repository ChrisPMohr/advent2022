from collections import defaultdict, Counter

def print_poses(poses):
    print('-' * 40)
    for y in range(-10, 10):
        print(''.join(['X' if [x, y] in poses else '.' for x in range(-10, 10)]))


def update_tail(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    if abs(dx) == 2 and dy == 0:
        tail[0] += dx//2
    elif abs(dy) == 2 and dx == 0:
        tail[1] += dy//2
    elif abs(dx) == 2 and abs(dy) == 2:
        tail[0] += dx//2
        tail[1] += dy// 2
    elif abs(dx) == 2:
        tail[0] += dx//2
        tail[1] = head[1]
    elif abs(dy) == 2:
        tail[1] += dy//2
        tail[0] = head[0]

    return tail


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    poses = [[0, 0] for _ in range(10)]
    all_tail_poses = {tuple(poses[-1])}

    for line in lines:
        # print(line)
        print(poses)
        dir, num_move = line.strip().split(" ")
        num_move = int(num_move)
        if dir == 'R':
            for _ in range(num_move):
                poses[0][0] += 1
                for i in range(9):
                    poses[i+1] = update_tail(poses[i], poses[i+1])
                # print_poses(poses)
                all_tail_poses.add(tuple(poses[-1]))
        if dir == 'L':
            for _ in range(num_move):
                poses[0][0] -= 1
                for i in range(9):
                    poses[i+1] = update_tail(poses[i], poses[i+1])
                # print_poses(poses)
                all_tail_poses.add(tuple(poses[-1]))
        if dir == 'U':
            for _ in range(num_move):
                poses[0][1] += 1
                for i in range(9):
                    poses[i+1] = update_tail(poses[i], poses[i+1])
                # print_poses(poses)
                all_tail_poses.add(tuple(poses[-1]))
        if dir == 'D':
            for _ in range(num_move):
                poses[0][1] -= 1
                for i in range(9):
                    poses[i+1] = update_tail(poses[i], poses[i+1])
                # print_poses(poses)
                all_tail_poses.add(tuple(poses[-1]))
        print_poses(poses)

    print(len(all_tail_poses))




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
