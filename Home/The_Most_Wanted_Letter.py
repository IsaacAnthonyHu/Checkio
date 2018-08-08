# You are given a text, which contains different english letters and punctuation symbols.
# You should find the most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
# Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
# If you have two or more letters with the same frequency, then return the letter which comes first in latin alphabet.
# For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
# Input: A text for analysis as a string.
# Output: The most frequent letter in lower case as a string.
# Example:
# checkio("Hello World!") == "l"
# checkio("How do you do?") == "o"
# checkio("One") == "e"
# checkio("Oops!") == "o"
# checkio("AAaooo!!!!") == "a"
# checkio("abe") == "a"
# Precondition:
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 105

import re


def checkio(text):
	relist = re.findall(r'[a-zA-Z]', text)
	lowercasetext = ''.join(relist)
	lower_case = set(list(lowercasetext.lower()))
	a = {}
	for x in lower_case:
		a[x] = list(text.lower()).count(x)
	# sorted(a, key = lambda x:a[x])
	index = max(a.items(), key=lambda w: w[1])[1]
	www = []
	for x in a:
		if a[x] == index:
			www.append(x)
	return sorted(www)[0]
# ----------
import string


def checkio_best_solution(text):
	"""
	We iterate through latyn alphabet and count each letter in the text.
	Then 'max' selects the most frequent letter.
	For the case when we have several equal letter,
	'max' selects the first from they.
	"""
	text = text.lower()
	return max(string.ascii_lowercase, key=text.count)
# ----------


if __name__ == '__main__':
	print("Example:")
	print(checkio("Hello World!"))

	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio("Hello World!") == "l", "Hello test"
	assert checkio("How do you do?") == "o", "O is most wanted"
	assert checkio("One") == "e", "All letter only once."
	assert checkio("Oops!") == "o", "Don't forget about lower case."
	assert checkio("AAaooo!!!!") == "a", "Only letters."
	assert checkio("abe") == "a", "The First."
	print("Start the long test")
	assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
	print("The local tests are done.")
