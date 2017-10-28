from threading import Timer
from datetime import datetime
from RPimax7219 import led


def get_number_length(num):
	num = int(num)
	counter = 0
	while num > 0:
		num = int(num / 10)
		counter += 1
	return counter

max_length = 8
blink = False
def show_number(num):
	global blink
	whole_part = int(num)
	length = get_number_length(whole_part)
	fraction_length = max_length - length
	fraction_part = pow(10, fraction_length) * (num - int(num))
	fraction_part = int(fraction_part)
	blink = not blink
	for i in range(0, max_length):
		if i < fraction_length:
			digit = fraction_part % 10
			fraction_part = int(fraction_part / 10)
		else:
			digit = whole_part % 10
			whole_part = int(whole_part / 10)
		display.letter(0, i+1, int(digit), i == fraction_length and blink)


def getHoursLeft():
	delta = datetime(2080, 1, 1) - datetime.now()
	return delta.total_seconds() / 3600

display = led.sevensegment()

def show():
	h = getHoursLeft()
	#display.write_number(deviceId=0, value=h)
	#display.write_text(0, "{:.1f}".format(h))
	show_number(h)
	(Timer(1, show)).start()


show()
#show_number(550512.33)
