input_string = input('Enter to check for Palindrome:\n')

def is_palindrome(input_string):
	new_string = ""
	reverse_string = ""

	for i in input_string.lower().strip():
		if i != ' ':
			new_string = new_string+i
			reverse_string = i+reverse_string

	if new_string==reverse_string:
		return "A True Work of Symmetry"
	return "Not Good Enough"

print(is_palindrome(input_string))