from collections import defaultdict, Counter


def update_tail(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    if abs(dx) == 2 and dy == 0:
        tail[0] += dx/2
    elif abs(dy) == 2 and dx == 0:
        tail[1] += dy/2
    elif abs(dx) == 2:
        tail[0] += dx/2
        tail[1] = head[1]
    elif abs(dy) == 2:
        tail[1] += dy/2
        tail[0] = head[0]

    return tail


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    head_pos = [0, 0]
    tail_pos = [0, 0]
    all_tail_poses = {tuple(tail_pos)}

    for line in lines:
        # print(line)
        dir, num_move = line.strip().split(" ")
        num_move = int(num_move)
        if dir == 'R':
            for _ in range(num_move):
                head_pos[0] += 1
                tail_pos = update_tail(head_pos, tail_pos)
                all_tail_poses.add(tuple(tail_pos))
        if dir == 'L':
            for _ in range(num_move):
                head_pos[0] -= 1
                tail_pos = update_tail(head_pos, tail_pos)
                all_tail_poses.add(tuple(tail_pos))
        if dir == 'U':
            for _ in range(num_move):
                head_pos[1] += 1
                tail_pos = update_tail(head_pos, tail_pos)
                all_tail_poses.add(tuple(tail_pos))
        if dir == 'D':
            for _ in range(num_move):
                head_pos[1] -= 1
                tail_pos = update_tail(head_pos, tail_pos)
                all_tail_poses.add(tuple(tail_pos))

    print(len(all_tail_poses))



if __name__ == '__main__':
    main()
