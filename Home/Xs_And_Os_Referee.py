# Tic-Tac-Toe, sometimes also known as Xs and Os,
# is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid.
# The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows wins the game.
#
# But we will not be playing this game.
# You will be the referee for this games results.
# You are given a result of a game and you must determine if the game ends in a win or a draw as well,
# as who will be the winner.
# Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
# A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.
# Input:
# A game result as a list of strings (unicode).
# Output:
# "X", "O" or "D" as a string.
# Example:
# checkio([
#     "X.O",
#     "XX.",
#     "XOO"]) == "X"
# checkio([
#     "OO.",
#     "XOX",
#     "XOX"]) == "O"
# checkio([
#     "OOX",
#     "XXO",
#     "OXX"]) == "D"
# How it is used:
# The concepts in this task will help you when iterating data types.
# They can also be used in game algorithms, allowing you to know how to check results.
# Precondition:
# There is either one winner or a draw.
# len(game_result) == 3
# all(len(row) == 3 for row in game_result)


# 核心思路，set()当前行或列的存在唯一值，也即len(set(target_list)) == 1


from typing import List


def checkio(game_result: List[str]) -> str:
	judge_list = game_result + [''.join([x[0] for x in game_result])] + [''.join([x[1] for x in game_result])] + [''.join([x[2] for x in game_result])] + [''.join([game_result[0][0],game_result[1][1],game_result[2][2]])]+ [''.join([game_result[0][2],game_result[1][1],game_result[2][0]])]
	for x in judge_list:
		if len(set(x)) == 1 and list(set(x))[0] != '.':
			ass = list(set(x))[0]
			break
		else:
			ass = 'D'
	return ass

#--


def checkio_best_solution(result):  # 和我的思路基本一样，只是我的方法太粗暴了一点
	'''
zip(*)为解压缩函数，将本身的列表解压为矩阵式
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
	'''
	rows = result
	cols = map(''.join, zip(*rows))
	diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))  # 这一条太pythonic了，优雅
	lines = rows + list(cols) + list(diags)
	return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'
#--

if __name__ == '__main__':
	print("Example:")
	print(checkio(["X.O",
	               "XX.",
	                "XOO"]))

	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio([
	    "X.O",
	    "XX.",
	    "XOO"]) == "X", "Xs wins"
	assert checkio([
	    "OO.",
	    "XOX",
	    "XOX"]) == "O", "Os wins"
	assert checkio([
	    "OOX",
	    "XXO",
	    "OXX"]) == "D", "Draw"
	assert checkio([
	    "O.X",
	    "XX.",
	    "XOO"]) == "X", "Xs wins again"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
