from stack_class.stack_class import Stack


def paren_checker(string):
    s = Stack()
    for char in string:
        if char == "(":
            s.push(char)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()
    return s.is_empty()


# test
print(paren_checker("((()))"))  # True
print(paren_checker("((()()))"))  # True
print(paren_checker("(()"))  # False
print(paren_checker(")("))  # False