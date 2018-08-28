# You are given a matrix of NxN (4≤N≤10).
# You should check if there is a sequence of 4 or more matching digits.
# The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
#
# Input:
# A matrix as a list of lists with integers.
#
# Output:
# Whether or not a sequence exists as a boolean.
#
# Example:
# checkio([
#     [7, 1, 4, 1],
#     [1, 2, 5, 2],
#     [3, 4, 1, 3],
#     [1, 1, 8, 1]
# ]) == False
# checkio([
#     [2, 1, 1, 6, 1],
#     [1, 3, 2, 1, 1],
#     [4, 1, 1, 3, 1],
#     [5, 5, 5, 5, 5],
#     [1, 1, 3, 1, 1]
# ]) == True
# checkio([
#     [7, 1, 1, 8, 1, 1],
#     [1, 1, 7, 3, 1, 5],
#     [2, 3, 1, 2, 5, 1],
#     [1, 1, 1, 5, 1, 4],
#     [4, 6, 5, 1, 3, 1],
#     [1, 1, 9, 1, 2, 1]
#     ]) == True
#
# How it is used:
# This concept is useful for games where you need to detect various lines of the same elements (3 games for example).
# This algorithm can be used for basic pattern recognition.
#
# Precondition:
# 0 ≤ len(matrix) ≤ 10
# all(all(0 < x < 10 for x in row) for row in matrix)


# 尝试定义函数用于二维数组倾斜遍历（正负倾斜,暂时定义NE-WS为正倾斜，NW-ES为负倾斜）
# 定义以matrix[0][0]为原点(0,0)，横向为Y轴，纵向为X轴，二者皆为正方向
# 正倾斜：第一行元素坐标为(0,0),(0,1),(0,2),(0,3) ------(负倾斜等效于matrix中列表元素全部reverse后的正倾斜结果)
#        第一个元素(0,0)为零直接终止
#        第二个元素(0,1)进行处理，X+1, Y-1, 返回(1,0), 检测到Y轴值为零，结束
#        第三个元素(0,2)进行处理，X+1, Y-1, 返回(1,1), Y不为零, 继续, 返回(2,0), 检测到Y轴值为零,结束
#        第四个元素(0,3)进行处理，X+1, Y-1, 返回(1,2), Y不为零, 继续, 返回(2,1), Y不为零, 继续, 返回(3,0),检测到Y轴值为零,结束

import re


def checkio(matrix):
	def element_process(target_matrix):  # 半个倾斜(half_lean)
		index_matrix = [[(y, x) for x in range(len(target_matrix[0]))] for y in range(len(target_matrix[0]))]
		a = []
		for x in index_matrix[0]:
			position = list(x)
			position_list = [target_matrix[position[0]][position[1]]]
			while position[1] != 0:
				position[0] += 1
				position[1] -= 1
				position_list.append(target_matrix[position[0]][position[1]])
			a.append(position_list)
		return a


	def whole_lean(matrix1):  # 拼接全倾斜(full_lean)

		list1 = element_process(matrix1)
		new = []
		for x in matrix1:
			new.append(list(reversed(x)))
		new = list(reversed(new))
		list2 = element_process(new)
		list3 = list1 + list2
		return  list3


	def full_list(matrix1):
		# 正倾斜列表为
		pos_lean_list = whole_lean(matrix1)
		# 负倾斜列表为
		new1 = []
		for x in matrix1:
			new1.append(list(reversed(x)))
		neg_lean_list = whole_lean(new1)
		# 横向列表为
		hori_list = matrix1
		# 纵向列表为
		vert_list = list(zip(*matrix1))
		# 总列表
		all_list = pos_lean_list + neg_lean_list + hori_list + vert_list

		wa = []
		for x in all_list:
			wa.append(''.join(list(map(str,x))))

		return wa

	a = False

	for x in full_list(matrix):
		if re.findall(r'((\d)\2{3,})', x):
			a = True

	return a


# ---
def checkio_best_solution(matrix):
	N = len(matrix)
	def seq_len(x, y, dx, dy, num):
		if 0 <= x < N and 0 <= y < N and matrix[y][x] == num:
			return 1 + seq_len(x + dx, y + dy, dx, dy, num)
		else:
			return 0

	DIR = [(dx, dy) for dy in range(-1, 2)
	                for dx in range(-1, 2)
	                if dx != 0 or dy != 0]
	for y in range(N):
		for x in range(N):
			for dx, dy in DIR:
				if seq_len(x, y, dx, dy, matrix[y][x]) >= 4:
					return True
	return False
# ---


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio([
	    [1, 2, 1, 1],
	    [1, 1, 4, 1],
	    [1, 3, 1, 6],
	    [1, 7, 2, 5]
	]) == True, "Vertical"
	assert checkio([
	    [7, 1, 4, 1],
	    [1, 2, 5, 2],
	    [3, 4, 1, 3],
	    [1, 1, 8, 1]
	]) == False, "Nothing here"
	assert checkio([
	    [2, 1, 1, 6, 1],
	    [1, 3, 2, 1, 1],
	    [4, 1, 1, 3, 1],
	    [5, 5, 5, 5, 5],
	    [1, 1, 3, 1, 1]
	]) == True, "Long Horizontal"
	assert checkio([
	    [7, 1, 1, 8, 1, 1],
	    [1, 1, 7, 3, 1, 5],
	    [2, 3, 1, 2, 5, 1],
	    [1, 1, 1, 5, 1, 4],
	    [4, 6, 5, 1, 3, 1],
	    [1, 1, 9, 1, 2, 1]
	]) == True, "Diagonal"
