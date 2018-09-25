# Stephan and Sophia forget about security and use simple passwords for everything.
# Help Nikola develop a password security check module.
# Require:
# The password will be considered strong enough if its length is greater than or equal to 10 symbols.
# The password has at least one digit, as well as containing one uppercase letter and one lowercase letter in it.
# The password contains only ASCII latin letters or digits.

import re


def checkio(password):
	a = re.match("[a-zA-Z0-9]+", password)
	b = re.search("[a-z]", password)
	c = re.search("[A-Z]", password)
	d = re.search("[0-9]", password)
	e = len(password)

	if bool(a) and bool(b) and bool(c) and bool(d) and e >= 10:
		return True
	else:
		return False

#-------------------------------
DIGIT_RE = re.compile('\d')
UPPER_CASE_RE = re.compile('[A-Z]')
LOWER_CASE_RE = re.compile('[a-z]')

def checkio_Best_Solution(data):
	"""
	Return True if password strong and False if not

	A password is strong if it contains at least 10 symbols,
	and one digit, one upper case and one lower case letter.
	"""
	if len(data) < 10:
		return False

	if not DIGIT_RE.search(data):
		return False

	if not UPPER_CASE_RE.search(data):
		return False

	if not LOWER_CASE_RE.search(data):
		return False

	return True
#-------------------------------
if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio('A1213pokl') == False, "1st example"
	assert checkio('bAse730onE4') == True, "2nd example"
	assert checkio('asasasasasasasaas') == False, "3rd example"
	assert checkio('QWERTYqwerty') == False, "4th example"
	assert checkio('123456123456') == False, "5th example"
	assert checkio('QwErTy911poqqqq') == True, "6th example"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")