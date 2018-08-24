# You are given an expression with numbers, brackets and operators.
# For this task only the brackets matter.
# Brackets come in three flavors: "{}" "()" or "[]".
# Brackets are used to determine scope or to restrict some expression.
# If a bracket is open, then it must be closed with a closing bracket of the same type.
# The scope of a bracket must not intersected by another bracket.
# In this task you should make a decision, whether to correct an expression or not based on the brackets.
# Do not worry about operators and operands.
#
# Input:
# An expression with different of types brackets as a string (unicode).
#
# Output:
# A verdict on the correctness of the expression in boolean (True or False).
#
# Example:
# checkio("((5+3)*2+1)") == True
# checkio("{[(3+1)+2]+}") == True
# checkio("(3+{1-1)}") == False
# checkio("[1+1]+(2*2)-{3/3}") == True
# checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
# checkio("2+3") == True
#
# How it is used:
# When you write code or complex expressions in a mathematical package, you can get a huge headache when it comes to excess or missing brackets. This concept can be useful for your own IDE.
#
# Precondition:
# There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
# 0 < len(expression) < 103



# 使用正则匹配最内侧的括号"\([0-9\+\-\*\/]*\)|\[[0-9\+\-\*\/]*\]|\{[0-9\+\-\*\/]*\}"然后删除该括号
import re


def checkio(expression):
	# '(({[(({1}-{1}+2)+3)-3]/3}-3)'
	prog = re.compile('\([0-9+\-*/]*\)|\[[0-9+\-*/]*\]|{[0-9+\-*/]*}')
	while True:
		result = prog.findall(expression)
		for x in result:
			expression = expression.replace(x, x[1:-1], 1)
		if prog.findall(expression) == []:
			break
	if re.findall('[(){}\[\]]', expression):
		return False
	else:
		return True


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("((5+3)*2+1)") == True, "Simple"
	assert checkio("{[(3+1)+2]+}") == True, "Different types"
	assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
	assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
	assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
	assert checkio("2+3") == True, "No brackets, no problem"
