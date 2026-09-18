def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for token in expression:

        if token.isalnum():  # If the token is an operand (number/variable)
            output.append(token)

        elif token == '(':  # If the token is '(', push it to the stack
            stack.append(token)

        elif token == ')':  # If the token is ')', pop and output from the stack until '(' is found
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '(' from the stack

        else:  # The token is an operator
            while (stack and stack[-1] != '(' and
                   precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)

    # Pop all the operators from the stack
    while stack:
        output.append(stack.pop())

    return ''.join(output)


def runner():
    expression = input("Enter Infix Expression: ")
    postfix_expression = infix_to_postfix(expression)
    print("Postfix Expression:", postfix_expression)

runner()