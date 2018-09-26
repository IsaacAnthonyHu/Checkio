def reverse_roman(roman_string):

    # num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


    # print(reverse_numerial)
    # return reverse_numerial
	a = []
	num_list_1 = [1000,500,100,50,10,5,1]
	str_list_1 = ['M','D','C','L','X','V','I']
	roman_char = ['CM','CD','XC','XL','IX','IV']
	num_char = [900,400,90,40,9,4]
	for x in roman_char:
		if roman_string.find(x) != -1:
			a.append(num_char[roman_char.index(x)])
			roman_string = roman_string.replace(x,'')
		print('Roman String:',roman_string)
	
	if roman_string == '':
		reverse_numerial = []
	else:
		reverse_numerial = [num_list_1[str_list_1.index(w)] for w in roman_string]
    	
	return sum(a)+sum(reverse_numerial)


print(reverse_roman('CDXCIX'))
