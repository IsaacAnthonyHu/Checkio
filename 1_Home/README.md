[TOC]
# Home Section Note

## 1_House_Password
re库中re.compile函数旨在直接生成正则表达式对象，  
这样可以避免重复在查找函数中输入正则式
```python
import re

re.search('[A-Z]', 'string')
# Equal To:
Upper_rule = re.compile('[A-Z]')
Upper_rule.search('[A-Z]')
```

## 2_The_Most_Wanted_Letter
max(iterable, key, default)求迭代器的最大值  
其中iterable为迭代器，max会for i in 遍历一遍这个迭代器，然后将迭代器的每一个返回值当做参数传给key=func中的func(一般用lambda表达式定义)
然后将func的执行结果传给key，然后以key为标准进行大小的判断。

## 3_Non_Unique_Elements
了解列表生成式
```python
def checkio_best_solution(data):
	return [i for i in data if data.count(i) > 1]
```

## 4_Monkey_Typing
了解bool函数  
空对象返回False,其余返回True  
利用了sum函数,可以对列表中布尔值进行加和，True为1，False为0

## 5_Long_Repeat
正则表达式的特殊引用方式'((\w)\2{0,})'  
\2指应用从左往右第二个括号中的正则内容

## 6_All_The_Same
Null

## 7_Caesar_Cipher_Encryptor
将str列表中元素合并，使用
```python
''.join(str_list)
```
chr函数：  
chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符  
ord函数：  
ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。

## 8_Sun_Angle
函数返回值中也能够加入判断
```python
def sun_angle_best_solution(time):
	h, m = map(int, time.split(':'))
	angle = 15 * h + m / 4 - 90
	return angle if 0 <= angle <= 180 else "I don't see the sun!"
```

## 9_Pawn_Brotherhood
Null

## 10_Xs_And_Os_Referee
  
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
同时列出数据和数据下标，一般用在 for 循环当中
```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
# >>> [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
```

## 11_The_Warriors
对class的理解之后具体再谈