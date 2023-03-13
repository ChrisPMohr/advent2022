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
        elif cmd.startswith("ls"):
            # create files in current_path
            current_dir = file_sys
            for p in current_path:
                current_dir = current_dir.setdefault(p, {})
            while lines and not lines[0].startswith("$"):
                line = lines.pop(0).strip()
                size, name = line.split()
                if size != "dir":
                    current_dir[name] = int(size)
        else:
            print("error", line)
            return

    def get_total_size(d):
        total_size = 0
        for k, v in d.items():
            if isinstance(v, dict):
                size = get_total_size(v)
                total_size += size
            else:
                total_size += v
        return total_size

    unused_space = 70000000 - get_total_size(file_sys)
    needed_space = 30000000 - unused_space

    def find_small_enough_directory(d):
        total_size = 0
        smallest = None
        for k, v in d.items():
            if isinstance(v, dict):
                sub_smallest, size = find_small_enough_directory(v)
                total_size += size
                if sub_smallest:
                    if not smallest or sub_smallest < smallest:
                        smallest = sub_smallest
                else:
                    if size >= needed_space:
                        if not smallest or size <= smallest:
                            smallest = size
            else:
                total_size += v
        return smallest, total_size

    print(find_small_enough_directory(file_sys))


if __name__ == '__main__':
    main()
