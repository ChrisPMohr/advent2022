from collections import defaultdict, Counter


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    file_sys = {'/': {}}
    current_path = ['/']

    while lines:
        line = lines.pop(0).strip()
        cmd = line[2:]
        if cmd.startswith("cd "):
            new_dir = line[5:]
            if new_dir == '/':
                current_path = ['/']
            elif new_dir == '..':
                current_path.pop()
            else:
                current_path.append(new_dir)
            print("cd", line)
            print(current_path)
        elif cmd.startswith("ls"):
            # create files in current_path
            current_dir = file_sys
            print("lsing path", current_path)
            for p in current_path:
                current_dir = current_dir.setdefault(p, {})
            while lines and not lines[0].startswith("$"):
                line = lines.pop(0).strip()
                print("creating file", line)
                size, name = line.split()
                if size != "dir":
                    current_dir[name] = int(size)
        else:
            print("error")
            print(line)
            return

    size_limit = 100000

    def get_small_children_size(d):
        total_size = 0
        small_children_sizes = 0
        for k, v in d.items():
            if isinstance(v, dict):
                small_size, all_size = get_small_children_size(v)
                total_size += all_size
                small_children_sizes += small_size
                if all_size <= size_limit:
                    small_children_sizes += all_size
            else:
                total_size += v
        return small_children_sizes, total_size

    print(file_sys)
    print(get_small_children_size(file_sys))

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
