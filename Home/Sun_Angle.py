# Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees. If the input will be the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".
# Input:
# The time of the day.
# Output:
# The angle of the sun, rounded to 2 decimal places.
# Example:
# sun_angle("07:00") == 15
# sun_angle("12:15") == 93.75
# sun_angle("01:23") == "I don't see the sun!"
# How it is used:
# One day it can save your life, if you'll be lost far away from civilization.
# Precondition:
# 00:00 <= time <= 23:59

def sun_angle(time):
	time_list = time.split(":")
	minute = (int(time_list[0])*60) + int(time_list[1])
	if minute > 1080 or minute < 360:
		a = "I don't see the sun!"
	else:
		a = ((minute-360)/(12*60))*180
	return a

# -----

def sun_angle_best_solution(time):
	h, m = map(int, time.split(':'))
	angle = 15 * h + m / 4 - 90
	return angle if 0 <= angle <= 180 else "I don't see the sun!"

# -----

if __name__ == '__main__':
	print("Example:")
	print(sun_angle("07:00"))

	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert sun_angle("07:00") == 15
	assert sun_angle("01:23") == "I don't see the sun!"
	print("Coding complete? Click 'Check' to earn cool rewards!")
