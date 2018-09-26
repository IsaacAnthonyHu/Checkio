# Input: Time in a 12-hour format (as a string)
# Output: Time in a 24-hour format (as a string)

# Example:

# time_converter('12:30 p.m.') == '12:30'
# time_converter('9:00 a.m.') == '09:00'
# time_converter('11:15 p.m.') == '23:15'

# How it is used: For work with the different time formats.

# Precondition:
# '00:00' <= time <= '23:59'

from datetime import datetime
def time_converter(time):
	# real_time = time[:05]
	if time[-5:] == ' p.m.':
		real_time_format = time[:-5] + ' pm'
	else:
		real_time_format = time[:-5] + ' am'
	print('real_time_format:-->',real_time_format)
	# meridium = time[-5:]
	struct_time = datetime.strptime(real_time_format,'%I:%M %p') # 解析时小时为12小时制，应用%I而非%H
	print('struct_time:-->',struct_time)
	converted_time = struct_time.strftime('%H:%M')
	return converted_time

print(time_converter('11:15 p.m.'))