# Write a function that finds the longest palindromic substring of a given string. Try to be as efficient as possible!
# If you find more than one substring you should return the one which is closer to the beginning.

# Input: A text as string
# Output: The longest palindromic substring

# Example:
# longestPalindromic("artrartrt") == "rtrartr"

# Precondition: 1 < |text| < 20
# The text contains only ASCII characters.

# 尝试使用Regex实现，鉴于以下正则使用困难'^(.?)(.?)(.?)(.?)(.?)(.?)(.?)(.?)(.?).?\9\8\7\6\5\4\3\2\1$'，
# 设想构建一个函数生成当前字符串对应所有子串的以下格式的正则式'(.)(.)(.)(.)(.)(.)(.)(.)(.).?\9\8\7\6\5\4\3\2\1'
# re.findall('artrartrt','(.)(.)(.)(.)(.)(.)(.)(.)(.).?\9\8\7\6\5\4\3\2\1')

import re

def regex_list(text):
	text_length = len(text)
	backreference_length = text_length//2
	regex_create_range = range(1,backreference_length+1)
	# print(regex_create_range)
	a = []
	for x in regex_create_range:
		b = [("\\"+ str(w)) for w in list(range(1,x+1))]
		b.reverse()
		c = ''.join(b)
		regex_target = '(.)'*x + '.?' + c
		a.append(regex_target)
	return a


def longest_palindromic(test):
	regexlist = regex_list(test)
	regexlist.reverse()
	# print(regexlist)
	regex_result_list = [list(re.finditer(x,test)) for x in regexlist]
	# for x in regex_result_list:
		# print(list(x))
	# print(regex_result_list)
	while True:
		try:
			regex_result_list.remove([])
		except ValueError:
			break 
	if regex_result_list == []:
		return test[0]
	else:# print(regex_result_list)
		target = regex_result_list[0]
		return target[0].group()
	# for x in regexlist:
	# 	rule = re.compile(x)
	# 	result = rule.finditer(test)
	# 	print(list(result))

print(longest_palindromic('artrartrt'))

# print(regex_list('artrartrt'))