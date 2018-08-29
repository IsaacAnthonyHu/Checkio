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
## The_Most_Wanted_Letter
max(iterable, key, default)求迭代器的最大值
其中iterable为迭代器，max会for i in 遍历一遍这个迭代器，然后将迭代器的每一个返回值当做参数传给key=func中的func(一般用lambda表达式定义)
然后将func的执行结果传给key，然后以key为标准进行大小的判断。