[TOC]
# Home Section Note

## 01_House_Password
re库中re.compile函数旨在直接生成正则表达式对象，  
这样可以避免重复在查找函数中输入正则式
```python
import re

re.search('[A-Z]', 'string')
# Equal To:
Upper_rule = re.compile('[A-Z]')
Upper_rule.search('[A-Z]')
```

另有re库的几个匹配函数中的区别可以区分一下：

```python
re.search()
re.match()
re.findall() #无法用于带有backreference的正则表达式
re.finditer()
```

## 02_The_Most_Wanted_Letter

max(iterable, key, default)求迭代器的最大值  
其中iterable为迭代器，max会for i in 遍历一遍这个迭代器，然后将迭代器的每一个返回值当做参数传给key=func中的func(一般用lambda表达式定义)
然后将func的执行结果传给key，然后以key为标准进行大小的判断。

```python
max(string, key = text.count)
# 以上函数也即是以下函数的效果：
max([text.count(x) for x in string])
```

## 03_Non_Unique_Elements
了解列表生成式中加入if条件
```python
def checkio_best_solution(data):
	return [i for i in data if data.count(i) > 1]
```

## 04_Monkey_Typing
了解bool函数 

```python
bool([])
--> False
bool({})
--> False
bool('')
--> False
book(123)
--> True
```



空对象返回False,其余返回True  
利用了sum函数,可以对列表中布尔值进行加和，True为1，False为0

## 05_Long_Repeat
正则表达式的特殊引用方式'((\w)\2{0,})'  

后向引用：backreference

\2指应用从左往右第二个括号中的正则内容

## 06_All_The_Same
Null

## 07_Caesar_Cipher_Encryptor
将str列表中元素合并，使用
```python
''.join(str_list)
```
chr函数：  
chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符  
ord函数：  
ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。

连续字母对应的ASCII值也连续

## 08_Sun_Angle
函数返回值中也能够加入判断
```python
def sun_angle_best_solution(time):
	h, m = map(int, time.split(':'))
	angle = 15 * h + m / 4 - 90
	return angle if 0 <= angle <= 180 else "I don't see the sun!"
```

## 09_Pawn_Brotherhood
Null

## 10_Xs_And_Os_Referee

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
同时列出数据和数据下标，一般用在 for 循环当中
```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
# >>> [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
```

zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包为一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少内存。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

```python
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 返回一个对象
>>> zipped
<zip object at 0x103abc288>
>>> list(zipped)  # list() 转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> list(zip(a,c))              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
 
>>> a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]
>>>
```



## 11_The_Warriors

对class的理解之后具体再谈