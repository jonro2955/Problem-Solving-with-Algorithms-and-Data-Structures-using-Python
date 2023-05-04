from stack_class.stack_class import Stack


def base_converter(decimal_num, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()
    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num = decimal_num // base
    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]
    return new_string


# "166" in base 10 should convert to "A6" in hexadecimal
print(base_converter(166, 16))