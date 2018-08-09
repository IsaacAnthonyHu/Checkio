# This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one which makes it an answer.
# Input: String.
# Output: Int.
# Example:
# long_repeat('sdsffffse') == 4
# long_repeat('ddvvrwwwrggg') == 3
import re


def long_repeat(line):
	"""
	    length the longest substring that consists of the same char
	"""
	repeat_list = re.findall(r'((\w)\2{0,})', line.lower())  # 正则引用写法有点意思
	iter_list_length = [len(x[0]) for x in repeat_list]
	return max(iter_list_length+[0])

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert long_repeat('sdsffffse') == 4, "First"
	assert long_repeat('ddvvrwwwrggg') == 3, "Second"
	assert long_repeat('abababaab') == 2, "Third"
	assert long_repeat('') == 0, "Empty"
	print('"Run" is good. How is "Check"?')
