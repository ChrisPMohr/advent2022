import re

memoizer = dict()


def most_geodes(costs, ore_bot, clay_bot, obsidian_bot, geode_bot, ore, clay, obsidian, geode, time):
    # Here is the secret efficiency sauce
    # First, skip any state we've seen before
    state = (costs, ore_bot, clay_bot, obsidian_bot, geode_bot, ore, clay, obsidian, geode, time)
    if state in memoizer:
        return memoizer[state]

    # Second, calculate an overly optimistic best value from this state. Either making:
    # 1. a geode bot if you can afford it or,
    # 2. a clay bot, plus an obsidian bot if you can afford it
    # If this still isn't good enough to beat the best so far, prune this branch of DFS
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
            # I forgot the following line, which techinically still works, but maxes this estimate way too big
            possible_obsidian -= costs[5]
        else:
            if possible_clay >= costs[3]:
                possible_obsidian_bot += 1
                possible_clay -= costs[3]
            possible_clay_bot += 1
        possible_clay += possible_clay_bot
        possible_obsidian += possible_obsidian_bot
    if 'max' in memoizer and possible_max <= memoizer['max']:
        return

    # Main section of most_geodes just does DFS, calculating which moves we can take, updating all
    # of the values, call each child method and calculating the best one
    options = [ore >= costs[0], ore >= costs[1], ore >= costs[2] and clay >= costs[3], ore >= costs[4] and obsidian >= costs[5]]

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
        option_outputs.append(
            most_geodes(costs, ore_bot + 1, clay_bot, obsidian_bot, geode_bot, ore - costs[0], clay, obsidian, geode, time))
    if options[1]:
        option_outputs.append(
            most_geodes(costs, ore_bot, clay_bot + 1, obsidian_bot, geode_bot, ore - costs[1], clay, obsidian, geode, time))
    if options[2]:
        option_outputs.append(
            most_geodes(costs, ore_bot, clay_bot, obsidian_bot + 1, geode_bot, ore - costs[2], clay - costs[3], obsidian, geode, time))
    if options[3]:
        option_outputs.append(
            most_geodes(costs, ore_bot, clay_bot, obsidian_bot, geode_bot + 1, ore - costs[4], clay, obsidian - costs[5], geode, time))
    option_outputs = [o for o in option_outputs if o is not None]
    if not option_outputs:
        return None
    result = max(option_outputs)
    if 'max' not in memoizer or result > memoizer['max']:
        memoizer['max'] = result
    memoizer[state] = result
    return result


def main():
    # Main method is very simple. After seeing your `parse_cost_str`, I like the regex method better
    # because every string is exactly the same this time.

    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    pattern = "Blueprint .*: Each ore robot costs (.*) ore. Each clay robot costs (.*) ore. Each obsidian robot costs (.*) ore and (.*) clay. Each geode robot costs (.*) ore and (.*) obsidian."
    p = re.compile(pattern)

    total_time = 24

    s = 0

    for i, line in enumerate(lines):
        i += 1
        line = line.strip()
        cost = tuple(map(int, p.match(line).group(1, 2, 3, 4, 5, 6)))

        global memoizer
        memoizer = {}
        geodes = most_geodes(cost, 1, 0, 0, 0, 0, 0, 0, 0, total_time)
        s += i * geodes
        print("blueprint", i, "geodes", geodes)

    print(s)


if __name__ == '__main__':
    main()
