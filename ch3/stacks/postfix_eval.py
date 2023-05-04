from stack_class.stack_class import Stack


# helper function
def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = []
    for char in postfix_expr:
        if char != " ":
            token_list.append(char)
    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()


# A postfix input string of "1 2 3 4 5 * + * +" should return an output of 47
print(postfix_eval("1 2 3 4 5 * + * +"))