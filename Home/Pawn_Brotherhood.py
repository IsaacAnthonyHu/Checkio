# You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.
# Input:
# Placed pawns coordinates as a set of strings.
# Output:
# The number of safe pawns as a integer.
# Example:
# safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
# safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
# How it is used:
# For a game AI one of the important tasks is the ability to estimate game state.
# This concept will show how you can do this on the simple chess figures positions.
# Precondition:
# 0 < pawns ≤ 8

# 核心思路:当前位置的下方两个位置是否在初始SET中
# if x in set(safe_pawns)
# len(set(a) & set(b)) != 0


def safe_pawns(pawns) -> int:
	chessboard_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	chessboard_number = ['1', '2', '3', '4', '5', '6', '7', '8']
	new_list = []
	for x in pawns:  # 交换x与y轴，方便x轴的±1（数字方便加减）
		alpha_to_number = chessboard_number[chessboard_alpha.index(x[0])]
		number_to_alpha = chessboard_alpha[chessboard_number.index(x[1])]
		new_list.append(number_to_alpha+alpha_to_number)
	pawns = set(new_list)
	a = 0
	for coordinate in pawns:
		if coordinate[0] == 'a':
			pawns_back = set([])  # type({})是dict，空set应该是set([])
		else:
			back_line = chessboard_alpha[chessboard_alpha.index(coordinate[0])-1]
			b = back_line + str(int(coordinate[1]) + 1)
			c = back_line + str(int(coordinate[1]) - 1)
			pawns_back = {b, c}
		if len(pawns & pawns_back) != 0:
			a += 1

		else:
			pass
	return a

# ---


def safe_pawns_best_solution(pawns):  # 活用ord()与chr()函数
	'''
	chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
	ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
		它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
		如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常
	使用函数名.__doc__或help(函数名)调用函数说明文档
	:param pawns: 棋子位置组成的set
	:return: 返回左右背后方有队友的数量
	'''
	answer = 0
	for pawn in pawns:
		if chr(ord(pawn[0])-1)+str(int(pawn[1])-1) in pawns or chr(ord(pawn[0])+1)+str(int(pawn[1])-1) in pawns:
			answer += 1
	return answer
# ---


if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
	assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
