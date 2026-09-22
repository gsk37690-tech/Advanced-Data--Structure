OPERATORS = {"+", "-", "*", "/", "%", "^"}


def convert_postfix_to_prefix(expression):
	"""Convert a postfix expression to prefix notation using a stack.

	Compact expressions use one-character operands, for example ``ab+c*``.
	Whitespace-separated expressions may contain multi-character operands, for
	example ``value 10 + result *``.
	"""
	if not isinstance(expression, str) or not expression.strip():
		raise ValueError("Postfix expression cannot be empty")

	tokens = expression.split() if any(char.isspace() for char in expression) else list(expression)
	stack = []

	for token in tokens:
		if token not in OPERATORS:
			stack.append(token)
			continue

		if len(stack) < 2:
			raise ValueError(f"Not enough operands for operator '{token}'")

		right_operand = stack.pop()
		left_operand = stack.pop()
		stack.append(f"{token} {left_operand} {right_operand}")

	if len(stack) != 1:
		raise ValueError("Invalid postfix expression: unused operands remain")

	return stack[0]


def runner():
	expression = input("Enter Postfix Expression: ")
	try:
		print("Prefix Expression:", convert_postfix_to_prefix(expression))
	except ValueError as error:
		print("Error:", error)


if __name__ == "__main__":
	runner()
