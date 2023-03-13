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

    seen = set()

    max_valve_flows = list(sorted(valves.values(), reverse=True))

    def astar(pos, opened, time_left, current_flow, max_flow):
        if (pos, tuple(sorted(opened)), time_left, current_flow) in seen:
            return max_flow
        seen.add((pos, tuple(sorted(opened)), time_left, current_flow))
        print("Trying", pos, opened, time_left, current_flow, max_flow)

        if time_left == 0:
            return max(current_flow, max_flow)

        max_new_flow = 0
        t = time_left - 1
        i = 0
        while t > 0 and i < len(max_valve_flows):
            max_new_flow += t * max_valve_flows[i]
            t -= 2
            i += 1

        if max_new_flow + current_flow < max_flow:
            return max_flow

        new_time = time_left - 1
        if pos not in opened and valves[pos] > 0:
            new_opened = set(opened)
            new_opened.add(pos)
            new_flow = current_flow + valves[pos] * new_time
            option_max_flow = astar(pos, new_opened, new_time, new_flow, max_flow)
            if option_max_flow >= max_flow:
                max_flow = option_max_flow

        for next_pos in tunnels[pos]:
            option_max_flow = astar(next_pos, opened, new_time, current_flow, max_flow)
            if option_max_flow >= max_flow:
                max_flow = option_max_flow

        return max_flow

    print(astar("AA", set(), total_time, 0, 0))


if __name__ == '__main__':
    main()
