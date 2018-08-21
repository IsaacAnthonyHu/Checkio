# You are given a positive number as a string along with the radix for it.
# Your function should convert it into decimal form.
# The radix is less than 37 and greater than 1.
# The task uses digits and the letters A-Z for the strings.
#
# Watch out for cases when the number cannot be converted.
# For example: "1A" cannot be converted with radix 9.
# For these cases your function should return -1.
#
# Input:
# Two arguments. A number as string and a radix as an integer.
#
# Output:
# The converted number as an integer.
#
# Example:
# checkio("AF", 16) == 175
# checkio("101", 2) == 5
# checkio("101", 5) == 26
# checkio("Z", 36) == 35
# checkio("AB", 10) == -1
#
# How it is used:
# Here you will learn how to work with the various numeral systems and handle exceptions.
#
# Precondition:
# re.match("\A[A-Z0-9]\Z", str_number)
# 0 < len(str_number) ≤ 10
# 2 ≤ radix ≤ 36


def checkio(str_number: str, radix: int) -> int:
	number_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	a = 0
	zip_list = list(zip(str_number, list(range(len(str_number)))[::-1]))
	for x in zip_list:
		true_number = number_str.index(x[0])
		if true_number >= radix:
			a = -1
			break
		else:
			a = a + true_number*(radix**x[1])
	return a


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("AF", 16) == 175, "Hex"
	assert checkio("101", 2) == 5, "Bin"
	assert checkio("101", 5) == 26, "5 base"
	assert checkio("Z", 36) == 35, "Z base"
	assert checkio("AB", 10) == -1, "B > A = 10"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
