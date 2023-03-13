from collections import defaultdict, Counter


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    line = lines[0]
    for i in range(len(line) - 4):
        if len(set(line[i:i+4])) == 4:
            print(i + 4)
            break


if __name__ == '__main__':
    main()
