from collections import defaultdict, Counter


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    crates = {}
    i = 0
    instruction_line = None
    for line in lines:
        line = line.rstrip()
        if line[1] == '1':
            instruction_line = i + 2
            break
        for j, cell in enumerate(line[1::4]):
            if cell != " ":
                crates[(j, i)] = cell
        i += 1

    stacks = []
    max_rows = i
    for i in range(len(lines[0])//4 + 1):
        stack = []
        for j in range(max_rows):
            if (i, max_rows - j - 1) in crates:
                stack.append(crates[(i, max_rows - j - 1)])
        stacks.append(stack)

    for line in lines[instruction_line:]:
        words = line.split()
        mini_stack = []
        for i in range(int(words[1])):
            mini_stack.append(stacks[int(words[3]) - 1].pop())
        stacks[int(words[5]) - 1].extend(reversed(mini_stack))

    print(''.join(s[-1] for s in stacks))


if __name__ == '__main__':
    main()
