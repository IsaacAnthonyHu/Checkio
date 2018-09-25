# You are given two positive numbers (N, M) in decimal form.
# You should calculate the Hamming distance between these two numbers in binary form.
#
# Input:
# Two arguments as integers.
#
# Output:
# The Hamming distance as an integer.
#
# Example:
# checkio(117, 17) == 3
# checkio(1, 2) == 2
# checkio(16, 15) == 5
#
# How it is used:
# This is a basis for Hamming code and other linear error-correcting programs.
# The Hamming distance is used in systematics as a measure of genetic distance.
# On a grid (ie: a chessboard,) the Hamming distance is the minimum number of moves it would take a rook
# to move from one cell to the other.
#
# Precondition:
# 0 < n < 106
# 0 < m < 106


def checkio(n, m):
	if m > n:
		m_bin = bin(m)[2:]
		n_bin = (len(bin(m))-len(bin(n)))*'0' + bin(n)[2:]
	else:
		n_bin = bin(n)[2:]
		m_bin = (len(bin(n)) - len(bin(m))) * '0' + bin(m)[2:]
	a = 0
	for x in zip(m_bin, n_bin):
		if x[0] != x[1]:
			a += 1
	return a

# ---


def checkio_best_solution(n, m):
	'''
	这个方法太秀了，使用了二进制的异或运算，对比了两个数字对应的每一位，相同返回0，不同返回1，所以只要对返回值中的'1'计数即可，十分机智
	:param n:
	:param m:
	:return:
	'''
	return bin(n ^ m).count('1')

#---


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio(117, 17) == 3, "First example"
	assert checkio(1, 2) == 2, "Second example"
	assert checkio(16, 15) == 5, "Third example"
