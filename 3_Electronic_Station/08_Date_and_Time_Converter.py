# Input: Date and time as a string

# Output: The same date and time, but in a more readable format

# Example:

# date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
# date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
# date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"
# NB: words "hour" and "minute" are used only when time is 01:mm (1 hour) or hh:01 (1 minute).
# In other cases it should be used "hours" and "minutes".

# How it is used: To improve the understanding between computer and humans.

# Precondition:
# 0 < date <= 31
# 0 < month <= 12
# 0 < year <= 3000
# 0 < hours < 24
# 0 < minutes < 60
from datetime import datetime

def date_time(time:str) -> str:
	struct_time = datetime.strptime(time,'%d.%m.%Y %H:%M')
	if struct_time.strftime('%H%M') == '0101':
		return struct_time.strftime('%#d %B %Y year %#H hour %#M minute')
	elif struct_time.strftime('%H') == '01':
		return struct_time.strftime('%#d %B %Y year %#H hour %#M minutes')
	elif struct_time.strftime('%M') == '01':
		return struct_time.strftime('%#d %B %Y year %#H hours %#M minute')
	else:
		return struct_time.strftime('%#d %B %Y year %#H hours %#M minutes')

if __name__ == '__main__':
	print("Example:")
	print(date_time("01.01.2000 00:00"))
	print(date_time("09.05.1945 06:30"))
	print(date_time("20.11.1990 03:55"))
	print(date_time("20.11.1990 01:01"))
	print(date_time("20.11.1990 01:55"))
	print(date_time("20.11.1990 03:01"))
# time = datetime.strptime('01.01.2999 01:59', '%d.%m.%Y %H:%M')
# print(time.strftime('%d %B %Y year %#H hour %#M minutes'))
# print(time.strftime('%H'))
# print(time.strftime('%M'))
# print(time.strftime('%H%M'))
# print(str(int('01')))