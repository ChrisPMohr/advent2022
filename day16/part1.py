from collections import defaultdict, Counter, deque


class Grid(object):

    def __init__(self):
        self.items = {}

    @classmethod
    def build_from_lines(cls, lines, transform=lambda c: c):
        grid = cls()
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                grid.items[(x, y)] = transform(c)

    @property
    def min_x(self):
        return min(x for x, y in self.items)

    @property
    def max_x(self):
        return max(x for x, y in self.items)

    @property
    def min_y(self):
        return min(y for x, y in self.items)

    @property
    def max_y(self):
        return max(y for x, y in self.items)

    def print(self):
        min_x = self.min_x
        max_x = self.max_x
        for y in range(self.min_y, self.max_y+1):
            print(''.join([self.items.get((x, y), " ") for x in range(min_x, max_x+1)]))


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()
    # line = open('example.txt', 'r').readline()
    # line = open('input.txt', 'r').readline()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))  # Nums on one line
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))  # Nums on one line

    valves = {}
    tunnels = {}

    for line in lines:
        valve_part, tunnel_part = line.strip().split("; tunnel")
        tunnel_part = tunnel_part.split(" ", 4)[4]
        valve_name, flow_rate = valve_part.split("Valve ")[1].split(" has flow rate=")
        valves[valve_name] = int(flow_rate)
        new_tunnels = tunnel_part.split(", ")
        tunnels[valve_name] = set(new_tunnels)

    total_time = 30

    q = deque()
    q.append(("AA", set(), total_time, 0))

    max_flow = 0

    seen = set()

    while q:
        pos, opened, time_left, current_flow = q.popleft()
        if (pos, tuple(sorted(opened)), time_left, current_flow) in seen:
            continue
        seen.add((pos, tuple(sorted(opened)), time_left, current_flow))
        # print("Trying", pos, opened, time_left, current_flow)

        if time_left == 0:
            if current_flow > max_flow:
                max_flow = current_flow
            continue

        new_time = time_left - 1
        if pos not in opened and valves[pos] > 0:
            new_opened = set(opened)
            new_opened.add(pos)
            new_flow = current_flow + valves[pos] * new_time
            q.append((pos, new_opened, new_time, new_flow))

        for next_pos in tunnels[pos]:
            q.append((next_pos, opened, new_time, current_flow))

    print(max_flow)


if __name__ == '__main__':
    main()
