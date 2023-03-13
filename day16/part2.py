from collections import defaultdict, Counter, deque


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

    total_time = 26
    # total_time = 8

    # manual_estimate = 1720
    # manual_estimate = 1868
    # manual_estimate = 2000
    # manual_estimate = 2046
    # manual_estimate = 2227
    # manual_estimate = 2300
    # manual_estimate = 2500
    manual_estimate = 2550

    seen = set()

    max_valve_flows = list(sorted(valves.items(), key=lambda kv: kv[1]))

    def astar(pos1, pos2, opened, time_left, current_flow, max_flow):
        if (pos1, pos2, tuple(sorted(opened)), time_left, current_flow) in seen:
            # print("-" * time_left, "skipping", pos1, pos2, opened, time_left, max_flow)
            return 0, []
        seen.add((pos1, pos2, tuple(sorted(opened)), time_left, current_flow))
        seen.add((pos2, pos1, tuple(sorted(opened)), time_left, current_flow))

        # print("-"* time_left, "Trying", pos1, pos2, opened, time_left, current_flow, max_flow)

        if time_left == 0:
            print("-"* time_left, "returning from", pos1, pos2, opened, time_left, max_flow)
            return max(current_flow, max_flow), []

        best_solution = []
        max_new_flow = 0
        t = time_left - 1
        if pos1 in opened and pos2 in opened:
            t -= 1
        i = 0
        this_max_valve_flows = list(max_valve_flows)
        while t > 0 and this_max_valve_flows:
            v1 = None
            while this_max_valve_flows and v1 is None or v1 in opened:
                v1, flow1 = this_max_valve_flows.pop()
            v2 = None
            while this_max_valve_flows and v2 is None or v2 in opened:
                v2, flow2 = this_max_valve_flows.pop()
            if not v1 or not v2:
                break
            max_new_flow += t * flow1
            max_new_flow += t * flow2
            t -= 2
            i += 2

        if max_new_flow + current_flow < manual_estimate:
            # print("-" * time_left, "Can't beat estimate", pos1, pos2, opened, time_left, max_new_flow + current_flow, max_flow)
            return 0, []
        if max_new_flow + current_flow < max_flow:
            # print("-" * time_left, "Can't beat best", pos1, pos2, opened, time_left, max_new_flow + current_flow, max_flow)
            return 0, []
        # else:
        #     print("-" * time_left, "Estimate", pos1, pos2, opened, time_left, max_new_flow + current_flow, max_flow)

        new_time = time_left - 1
        if pos1 not in opened and valves[pos1] > 0:
            new_opened = set(opened)
            new_opened.add(pos1)
            new_flow = current_flow + valves[pos1] * new_time

            if pos2 not in new_opened and valves[pos2] > 0:
                new_new_opened = set(new_opened)
                new_new_opened.add(pos2)
                new_new_flow = new_flow + valves[pos2] * new_time
                option_max_flow, solution = astar(pos1, pos2, new_new_opened, new_time, new_new_flow, max_flow)
                if option_max_flow > max_flow:
                    best_solution = [f"{pos1} open, {pos2} open"] + solution
                    print("-"* time_left, "New best", option_max_flow, pos1, pos2, new_new_opened, new_time, best_solution)
                    max_flow = option_max_flow

            for next_pos2 in tunnels[pos2]:
                option_max_flow, solution = astar(pos1, next_pos2, new_opened, new_time, new_flow, max_flow)
                if option_max_flow > max_flow:
                    best_solution = [f"{pos1} open, {pos2}->{next_pos2}"] + solution
                    print("-"* time_left, "New best", option_max_flow, pos1, next_pos2, new_opened, new_time, best_solution)
                    max_flow = option_max_flow

        for next_pos1 in tunnels[pos1]:
            if pos2 not in opened and valves[pos2] > 0:
                new_opened = set(opened)
                new_opened.add(pos2)
                new_flow = current_flow + valves[pos2] * new_time
                option_max_flow, solution = astar(next_pos1, pos2, new_opened, new_time, new_flow, max_flow)
                if option_max_flow > max_flow:
                    best_solution = [f"{pos1}->{next_pos1}, {pos2} open"] + solution
                    print("-"* time_left, "New best", option_max_flow, next_pos1, pos2, new_opened, new_time, best_solution)
                    max_flow = option_max_flow

            for next_pos2 in tunnels[pos2]:
                option_max_flow, solution = astar(next_pos1, next_pos2, opened, new_time, current_flow, max_flow)
                if option_max_flow > max_flow:
                    best_solution = [f"{pos1}->{next_pos1}, {pos2}->{next_pos2}"] + solution
                    print("-"* time_left, "New best", option_max_flow, next_pos1, next_pos2, opened, new_time, best_solution)
                    max_flow = option_max_flow

        # print("-"* time_left, "returning from", pos1, pos2, opened, time_left, max_flow)
        return max_flow, best_solution

    print(astar("AA", "AA", set(), total_time, 0, 0))


if __name__ == '__main__':
    main()
