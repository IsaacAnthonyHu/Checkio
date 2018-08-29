# Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.).
# Using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance.
# For example ("a b c", 3) == "d e f"
# Input:
# A secret message as a string (lowercase letters only and white spaces)
# Output:
# The same string, but encrypted
# Example:
# to_encrypt("a b c", 3) == "d e f"
# to_encrypt("a b c", -3) == "x y z"
# to_encrypt("simple text", 16) == "iycfbu junj"
# to_encrypt("important text", 10) == "swzybdkxd dohd"
# to_encrypt("state secret", -13) == "fgngr frperg"
# How it is used:
# For cryptography and to save important information.
# Precondition:
# 0 < len(text) < 50
# -26 < delta < 26


def to_encrypt(text, delta):
	alpha_list = list('abcdefghijklmnopqrstuvwxyz')
	output_list = []
	for charactor in text:
		if charactor == ' ':
			output_list.append(' ')
		else:
			index_number = alpha_list.index(charactor)+delta
			if index_number > 25:
				index_number = index_number-26
			output_list.append(alpha_list[index_number])
	return ''.join(output_list)


# -----


def encrypt(char, delta):
	if char == " ":
		return " "
	else:
		return chr(((ord(char) - 97 + delta) % 26) + 97)

def to_encrypt_solution(text, delta):
	return ("").join([encrypt(x, delta) for x in text])
# -----

if __name__ == '__main__':
	print("Example:")
	print(to_encrypt('abc', 10))

	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert to_encrypt("a b c", 3) == "d e f"
	assert to_encrypt("a b c", -3) == "x y z"
	assert to_encrypt("simple text", 16) == "iycfbu junj"
	assert to_encrypt("important text", 10) == "swzybdkxd dohd"
	assert to_encrypt("state secret", -13) == "fgngr frperg"
	print("Coding complete? Click 'Check' to earn cool rewards!")
