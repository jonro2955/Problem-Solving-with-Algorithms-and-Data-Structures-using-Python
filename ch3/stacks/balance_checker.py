from stack_class.stack_class import Stack


# helper function
def matches(sym_left, sym_right):
    all_lefts = "([{"
    all_rights = ")]}"
    return all_lefts.index(sym_left) == all_rights.index(sym_right)


def balance_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), symbol):
                    return False
    return s.is_empty()


# test
print(balance_checker('{({([][])}())}'))  # expected: True
print(balance_checker('[{()]'))  # expected: False







