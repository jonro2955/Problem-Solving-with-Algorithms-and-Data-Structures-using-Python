from stack_class.stack_class import Stack


def infix_to_postfix(infix_expr):
    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    op_stack = Stack()
    postfix_list = []
    token_list = []
    for char in infix_expr:
        if char != " ":
            token_list.append(char)
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


# An infix string input of "A + ((B + C) * (D + E))" should result in
# a postfix output of "A B C + D E + * +"
print(infix_to_postfix("A + ((B + C) * (D + E))"))