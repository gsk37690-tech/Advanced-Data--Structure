def reverse_and_swap(expression):
    result = ""
    for ch in reversed(expression):
        if ch == '(':
            result += ')'
        elif ch == ')':
            result += '('
        else:
            result += ch
    return result

def infix_to_postfix_for_prefix(expression):
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
                   precedence[token] < precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)

    # Pop all the operators from the stack
    while stack:
        output.append(stack.pop())

    return ''.join(output)

def infix_to_prefix(expression):

    reversed_expression = reverse_and_swap(expression)

    postfix = infix_to_postfix_for_prefix(reversed_expression)

    prefix = postfix[::-1]

    return prefix

def runner():
    expression = input("Enter Expression:")
    print("Infix :",expression)
    result = infix_to_prefix(expression)
    #print("Reverse and Swap",result)
    print("Prefix :",result)
runner()

"""
The Reverse → Postfix → Reverse approach is one of the easiest ways to teach Infix → Prefix 
to beginners because it reuses the Infix → Postfix algorithm they already know.

There is one important detail: when we reverse the expression, we must swap ( and ), 
and when processing operators, associativity matters, especially for ^.


INFIX - > REVERSE -> SWAP ( and ) -> POSTFIX  ->  REVERSE -> PREFIX
"""