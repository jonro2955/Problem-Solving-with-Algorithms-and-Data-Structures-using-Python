from stack_class.stack_class import Stack


def divide_by_2(decimal_num):
    rem_stack = Stack()
    while decimal_num > 0:
        rem = decimal_num % 2
        rem_stack.push(rem)
        decimal_num = decimal_num // 2
    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())
    return bin_string


# 233(base_10) = 11101001(base_2)
print(divide_by_2(233))