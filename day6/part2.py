from collections import defaultdict, Counter


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    line = lines[0]
    for i in range(len(line) - 14):
        code = line[i:i+14]
        if len(set(line[i:i+14])) == 14:
            print(i + 14)
            break


if __name__ == '__main__':
    main()
