[TOC]

# Elementary Section Note



## 02_Best_Stock

字典型数据可以通过以下方法得到对应的键集和值集

```python
list(dict.keys())
list(dict.value())
```



## 04_Bigger_Price

使用sorted()函数

`sorted(iterable[, cmp[, key[, reverse]]]`

参数说明：

* `iterable` -- 可迭代对象。
* `cmp` -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
* `key` -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
* `reverse` -- 排序规则，`reverse = True` 降序 ， `reverse = False` 升序（默认）。



先不深究cmp函数部分，使用：

`sorted(iterable, key, reverse)`

对可迭代对象中的每一个元素使用key中函数，对结果值进行排序

## 









