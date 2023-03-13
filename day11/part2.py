class Monkey(object):

    def __init__(self, items, operation, test_val, test_res_true, test_res_false):
        self.items = items
        self.operation = operation
        self.test_val = test_val
        self.test_res_true = test_res_true
        self.test_res_false = test_res_false
        self.inspect_count = 0

    def apply_operation(self, item, mod):
        self.inspect_count += 1
        if self.operation[1] == 'old':
            v2 = item
        else:
            v2 = int(self.operation[1])

        if self.operation[0] == '*':
            item *= v2
        elif self.operation[0] == '+':
            item += v2

        return item % mod


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()

    monkeys = []

    while lines:
        lines.pop(0)
        items = list(map(int, lines.pop(0).strip().split(": ")[1].split(", ")))
        operation = lines.pop(0).strip().split("new = old ")[1].split(" ")
        test_val = int(lines.pop(0).strip().split(" by ")[1])
        test_res_true = int(lines.pop(0).strip().split("monkey ")[1])
        test_res_false = int(lines.pop(0).strip().split("monkey ")[1])
        try:
            lines.pop(0)
        except:
            pass
        monkeys.append(
            Monkey(
                items,
                operation,
                test_val,
                test_res_true,
                test_res_false
            )
        )
        print(items)
        print(operation)
        print(test_val, test_res_true, test_res_false)
        print("-" * 40)

    prod_test_val = 1
    for m in monkeys:
        prod_test_val *= m.test_val

    ROUNDS = 10000
    for i in range(ROUNDS):
        print(i)
        for m in range(len(monkeys)):
            monkey = monkeys[m]
            for item in monkey.items:
                item = monkey.apply_operation(item, prod_test_val)
                if item % monkey.test_val == 0:
                    monkeys[monkey.test_res_true].items.append(item)
                else:
                    monkeys[monkey.test_res_false].items.append(item)
            monkey.items = []

    monkeys.sort(key=lambda m: m.inspect_count, reverse=True)
    print(monkeys[0].inspect_count * monkeys[1].inspect_count)


if __name__ == '__main__':
    main()
