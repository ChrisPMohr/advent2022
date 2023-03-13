from collections import defaultdict, Counter


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    num_stacks = len(lines[0])//4 + 1
    stacks = [list() for _ in range(num_stacks)]
    for i, line in enumerate(lines):
        line = line.rstrip()
        if line[1] == '1':
            break
        for j, cell in enumerate(line[1::4]):
            if cell != " ":
                stacks[j].append(cell)

    instruction_line = i + 2

    for stack in stacks:
        stack.reverse()

    for line in lines[instruction_line:]:
        words = line.split()
        for i in range(int(words[1])):
            stacks[int(words[5]) - 1].append(stacks[int(words[3]) - 1].pop())

    print(''.join(s[-1] for s in stacks))


if __name__ == '__main__':
    main()
