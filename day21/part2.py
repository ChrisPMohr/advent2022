from collections import defaultdict, Counter


memoizer = {}


def eval_root(monkeys):
    m1 = monkeys['root'][0]
    m2 = monkeys['root'][2]
    return (eval_monkey(monkeys, m1), eval_monkey(monkeys, m2))


def reduce(equation):
    print(equation)
    lhs, rhs = equation
    while isinstance(lhs, tuple):
        print(lhs, rhs)
        v1, op, v2 = lhs
        if op == '/':
            if isinstance(v2, int):
                lhs = v1
                rhs *= v2
            elif isinstance(v1, int):
                lhs = v2
                rhs = v1 / rhs
            else:
                print("What do? /")
                return
        if op == '*':
            if isinstance(v2, int):
                lhs = v1
                rhs /= v2
            elif isinstance(v1, int):
                lhs = v2
                rhs /= v1
            else:
                print("What do? *")
                return
        if op == '+':
            if isinstance(v2, int):
                lhs = v1
                rhs -= v2
            elif isinstance(v1, int):
                lhs = v2
                rhs -= v1
            else:
                print("What do? +")
                return
        if op == '-':
            if isinstance(v2, int):
                lhs = v1
                rhs += v2
            elif isinstance(v1, int):
                lhs = v2
                rhs = v1 - rhs
            else:
                print("What do? -")
                return
    print(lhs, rhs)


def eval_monkey(monkeys, name):
    if name in memoizer:
        return memoizer[name]
    job = monkeys[name]
    ret = None
    if isinstance(job, int):
        ret = job
    elif job is None:
        ret = "x"
    else:
        v1 = eval_monkey(monkeys, job[0])
        v2 = eval_monkey(monkeys, job[2])
        expr = f"({v1} {job[1]} {v2})"
        if "x" not in expr:
            ret = int(eval(expr))
        else:
            ret = (v1, job[1], v2)
    memoizer[name] = ret
    return ret



def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    monkeys = {}

    for line in lines:
        line = line.strip()
        monkey_name, job = line.split(": ")
        if " " in job:
            monkeys[monkey_name] = job.split(" ")
        elif monkey_name == 'humn':
            monkeys[monkey_name] = None
        else:
            monkeys[monkey_name] = int(job)

    equation = eval_root(monkeys)
    print(reduce(equation))


if __name__ == '__main__':
    main()
