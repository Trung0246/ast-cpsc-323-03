parsing_table = {
	"E": {
		"a": ["T", "Q"],
		"(": ["T", "Q"],

		")": ["ɛ"],
		"$": ["ɛ"]
	},
	"Q": {
		"+": ["+", "T", "Q"],
		"-": ["-", "T", "Q"],

		")": ["ɛ"],
		"$": ["ɛ"]
	},
	"T": {
		"a": ["F", "R"],
		"(": ["F", "R"],

		"+": ["ɛ"],
		"-": ["ɛ"],
		")": ["ɛ"],
		"$": ["ɛ"]
	},
	"R": {
		"*": ["*", "F", "R"],
		"/": ["/", "F", "R"],

		"+": ["ɛ"],
		"-": ["ɛ"],
		")": ["ɛ"],
		"$": ["ɛ"]
	},
	"F": {
		"a": ["a"],
		"(": ["(", "E", ")"],
		
		"*": ["ɛ"],
		"/": ["ɛ"],
		"+": ["ɛ"],
		"-": ["ɛ"],
		")": ["ɛ"],
		"$": ["ɛ"]
	}
}

def parse_string(input_string, parsing_table):
	stack = ["$", "E"]
	input_string += "$"
	pointer = 0

	while len(stack) > 0:
		print(stack)
		top = stack[-1]
		current_char = input_string[pointer]

		if top == current_char:
			stack.pop()
			pointer += 1
		elif top in parsing_table and current_char in parsing_table[top]:
			rule = parsing_table[top][current_char]
			stack.pop()
			if "ɛ" not in rule:
				stack.extend(reversed(rule))
		else:
			break

	if pointer == len(input_string) - 1 and len(stack) == 0:
		return True, stack
	else:
		return False, stack

input_strings = [
	"(a+a)$",
	"(a+a)e$",
	"(a+a)*a$",
	"a*(a/a)$",
	"a(a+a)$"
]

for i, input_string in enumerate(input_strings):
	is_valid, stack = parse_string(input_string, parsing_table)
	print(f"Input {i+1}: {input_string}")
	print("Stack:", stack)
	if is_valid:
		print("Output: String is accepted / Valid.\n")
	else:
		print("Output: String is not accepted / Invalid.\n")
