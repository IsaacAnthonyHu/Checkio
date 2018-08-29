# For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
#
# Numeral	Value
# I	1 (unus)
# V	5 (quinque)
# X	10 (decem)
# L	50 (quinquaginta)
# C	100 (centum)
# D	500 (quingenti)
# M	1,000 (mille)

# Input:
# A number as an integer.
#
# Output:
# The Roman numeral as a string.
#
# Example:
# checkio(6) == 'VI'
# checkio(76) == 'LXXVI'
# checkio(13) == 'XIII'
# checkio(44) == 'XLIV'
# checkio(3999) == 'MMMCMXCIX'
#
# How it is used:
# This is an educational task that allows you to explore different numbering systems.
# Since roman numerals are often used in the typography, it can alternatively be used for text generation.
# The year of construction on building faces and cornerstones is most often written by Roman numerals.
# These numerals have many other uses in the modern world and you read about it here...
# Or maybe you will have a customer from Ancient Rome ;-)
#
# Precondition:
# 0 < number < 4000


def checkio(one_num):
    '''
    将阿拉伯数字转化为罗马数字
    '''
    num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res=''
    for i in range(len(num_list)):
        while one_num>=num_list[i]:
            one_num-=num_list[i]
            res+=str_list[i]
    return res



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
