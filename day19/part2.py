from collections import defaultdict, Counter
import re


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


memoizer = dict()


def most_geodes(costs, ore_bot, clay_bot, obsidian_bot, geode_bot, ore, clay, obsidian, geode, time):
    state = (ore_bot, clay_bot, obsidian_bot, geode_bot, ore, clay, obsidian, geode, time)
    if state in memoizer:
        return memoizer[state]

    possible_max = geode
    possible_clay = clay
    possible_clay_bot = clay_bot
    possible_obsidian = obsidian
    possible_obsidian_bot = obsidian_bot
    possible_geode_bot = geode_bot
    for i in range(time):
        possible_max += possible_geode_bot
        if possible_obsidian >= costs[5]:
            possible_geode_bot += 1
            possible_obsidian -= costs[5]
        else:
            # possible_obsidian_bot += 1
            if possible_clay >= costs[3]:
                possible_obsidian_bot += 1
                possible_clay -= costs[3]
            possible_clay_bot += 1
        possible_clay += possible_clay_bot
        possible_obsidian += possible_obsidian_bot
    if 'max' in memoizer and possible_max <= memoizer['max']:
        # print("skipping", state, possible_max, memoizer['max'])
        return

    options = [ore >= costs[0], ore >= costs[1], ore >= costs[2] and clay >= costs[3], ore >= costs[4] and obsidian >= costs[5]]

    # print(state)

    ore += ore_bot
    clay += clay_bot
    obsidian += obsidian_bot
    geode += geode_bot
    time -= 1
    if time == 0:
        return geode

    option_outputs = [
        most_geodes(costs, ore_bot, clay_bot, obsidian_bot, geode_bot, ore, clay, obsidian, geode, time)
    ]
    if options[0]:
        # print("Trying making ore bot")
        option_outputs.append(
            most_geodes(costs, ore_bot + 1, clay_bot, obsidian_bot, geode_bot, ore - costs[0], clay, obsidian, geode, time))
    if options[1]:
        # print("Trying making clay bot")
        option_outputs.append(
            most_geodes(costs, ore_bot, clay_bot + 1, obsidian_bot, geode_bot, ore - costs[1], clay, obsidian, geode, time))
    if options[2]:
        # print("Trying making obsidian bot")
        option_outputs.append(
            most_geodes(costs, ore_bot, clay_bot, obsidian_bot + 1, geode_bot, ore - costs[2], clay - costs[3], obsidian, geode, time))
    if options[3]:
        # print("Trying making geode bot")
        option_outputs.append(
            most_geodes(costs, ore_bot, clay_bot, obsidian_bot, geode_bot + 1, ore - costs[4], clay, obsidian - costs[5], geode, time))
    option_outputs = [o for o in option_outputs if o is not None]
    if not option_outputs:
        return None
    result = max(option_outputs)
    if 'max' not in memoizer or result > memoizer['max']:
        # print("New best", state, result)
        memoizer['max'] = result
    memoizer[state] = result
    return result


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    pattern = "Blueprint .*: Each ore robot costs (.*) ore. Each clay robot costs (.*) ore. Each obsidian robot costs (.*) ore and (.*) clay. Each geode robot costs (.*) ore and (.*) obsidian."
    p = re.compile(pattern)

    total_time = 32

    # product = 1

    i = 0
    line = lines[i].strip()
    cost = tuple(map(int, p.match(line).group(1, 2, 3, 4, 5, 6)))

    global memoizer
    memoizer = {}
    # memoizer['max'] = 30
    geodes = most_geodes(cost, 1, 0, 0, 0, 0, 0, 0, 0, total_time)
    # product *= geodes
    print("blueprint", i + 1, "geodes", geodes)



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
