CONST_CHAR_ID = 26


def analyze_rules(rule: str) -> list:
    start = rule[:3]
    count = 0
    rules = []
    cur_rule = start
    for i in range(3, len(rule)):
        if rule[i] == ' ' or rule[i] == '\n':
            continue
        else:
            cur_rule += rule[i]
    rules.append(cur_rule)
    count += 1
    return rules


def is_valid_rule(rule: str) -> bool:
    valid = len(rule) > 3 and is_non_terminal(rule[0]) and rule[1] == '-' and rule[2] == '>'
    if not valid:
        return False
    analyze_rules(rule)
    return True


def is_non_terminal(c: str) -> bool:
    return 'A' <= c <= 'Z'


class Grammar:
    _max_char_id = CONST_CHAR_ID
    _size = int()
    _start = str()
    _rules = list()

    class _Iterator:
        char_id = int()
        rule_id = int()
        rules = list()
        _max_char_id = CONST_CHAR_ID

        def get_rule(self):
            return self.rules[self.char_id][self.rule_id]

        def is_valid(self):
            return self._max_char_id > self.char_id >= 0 and \
                0 <= self.rule_id < len(self.rules[self.char_id])

        def __init__(self, rules, c='A'):
            self.char_id = ord(c) - ord('A')
            self.rule_id = 0
            self.rules = rules

        def __iter__(self):
            return self

        def __next__(self):
            self.rule_id += 1
            if self.rule_id >= len(self.rules[self.char_id]):
                self.rule_id = 0
                self.char_id += 1
                while self.char_id < self._max_char_id and len(self.rules[self.char_id]) == 0:
                    self.char_id += 1
            if not self.is_valid():
                raise StopIteration
            return self.get_rule()

    def __init__(self, start: str = 'S'):
        self._start = start
        self._rules = [[] for _ in range(self._max_char_id)]
        self._size = 0
        self._iter = self.__iter__

    def get_start(self):
        return self._start

    def input_init(self):
        self._size = int(input())
        for i in range(self._size):
            rule = input()
            self.add_rule(rule)

    def add_rule(self, rule: str) -> bool:
        if is_valid_rule(rule):
            rules_pack = analyze_rules(rule)
            for single_rule in rules_pack:
                self._rules[ord(single_rule[0]) - ord('A')].append(single_rule)
                self._size += 1
            return True
        return False

    def __len__(self, c: str = '') -> int:
        if c == '':
            return self._size
        else:
            if is_non_terminal(c):
                return len(self._rules[ord(c) - ord('A')])
        return 0

    def __iter__(self):
        self._iter = self._Iterator(self._rules)
        return self._iter.__iter__()

    def __str__(self):
        sz = self._size
        output = str(sz) + '\n'
        iterator = self._Iterator(self._rules)
        for i in range(sz):
            if i + 1 != sz:
                output = output + next(iterator) + '\n'
            else:
                output = output + next(iterator)
        return output

    def __repr__(self):
        output = str(self._size) + '\n'
        iterator = self._Iterator(self._rules)
        for i in range(self._size):
            if i + 1 != self._size:
                output = output + iterator.get_rule() + '\n'
            else:
                output = output + iterator.get_rule()
        return output
