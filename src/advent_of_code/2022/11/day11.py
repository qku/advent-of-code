import yaml
from yaml.loader import SafeLoader

file = 'input.txt'
# file = 'test_input.txt'
with open(file) as f:
    content = f.read()
    # remove indentation before If
    content = content.replace('  If', 'If')
    # add square brackets around starting items
    content = content.replace('items: ', 'items: [')
    content = content.replace('\n  Operation', ']\n  Operation')
    # load data into dictionary
    data = yaml.load(content, Loader=SafeLoader)

dividers = [int(i['Test'].split()[-1]) for i in data.values()]
print(dividers)


def monkey_business(_monkeys):
    counts = []
    for m in _monkeys:
        n = m.inspection_count
        print(n)
        counts.append(n)
    counts.sort()
    return counts[-1] * counts[-2]


class Monkey:
    def __init__(self, info):
        self.items = list(info['Starting items'])
        self.modulos = [{d: i for d in dividers} for i in self.items]

        operation_string = info['Operation'].split('=')[1].strip()
        if operation_string == 'old * old':
            def _operation(x):
                return x ** 2
        else:
            _, op, n = operation_string.split()
            if op == '+':
                def _operation(x):
                    return x + int(n)
            elif op == '*':
                def _operation(x):
                    return x * int(n)
            else:
                raise AssertionError
        self._operation = _operation

        self._div_test = int(info['Test'].split()[-1])
        self._target_true = int(info['If true'].split()[-1])
        self._target_false = int(info['If false'].split()[-1])

        self.inspection_count = 0

    def turn(self):
        targets = {}
        while self.items:
            self.inspection_count += 1
            item = self.items.pop(0)
            item = self._operation(item)
            item = int(item // 3)
            if item % self._div_test == 0:
                target = self._target_true
            else:
                target = self._target_false

            try:
                targets[target].append(item)
            except KeyError:
                targets[target] = [item]
        return targets

    def smart_turn(self):
        targets = {}
        while self.modulos:
            self.inspection_count += 1
            modulo_dict = self.modulos.pop(0)
            for k in modulo_dict:
                modulo_dict[k] = self._operation(modulo_dict[k])
                modulo_dict[k] = modulo_dict[k] % k
            if modulo_dict[self._div_test] == 0:
                target = self._target_true
            else:
                target = self._target_false

            try:
                targets[target].append(modulo_dict)
            except KeyError:
                targets[target] = [modulo_dict]
        return targets


# part I
monkeys = []
for data_dict in data.values():
    monkeys.append(Monkey(data_dict))

for i in range(20):
    for active_monkey in monkeys:
        for target, content in active_monkey.turn().items():
            monkeys[target].items += content

print(f'Monkey business part I: {monkey_business(monkeys)}')

# part II
monkeys = []
for data_dict in data.values():
    monkeys.append(Monkey(data_dict))

for i in range(10000):
    for active_monkey in monkeys:
        for target, content in active_monkey.smart_turn().items():
            monkeys[target].modulos += content

print(f'Monkey business part II: {monkey_business(monkeys)}')
