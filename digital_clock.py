from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time
from datetime import datetime as dt

serial = spi(device=0, port=0, gpio_DC=24, gpio_RST=25)
device = ssd1306(serial)

def clock():
	now = dt.now()
	nowDate = now.date()
	nowTime = now.time()
	formatedTime =  str(nowTime.hour) + ":" + str(nowTime.minute) + ":" +str(nowTime.second)
	stringDate = nowDate.isoformat()
	with canvas(device) as draw:
		draw.text((70, 0), stringDate, fill="white")
		draw.text((0, 0), formatedTime, fill="white")

try:
	print("Clock should be working")
	while True:
		clock()
		time.sleep(1)
except KeyboardInterrupt:
	device.cleanup()
	print("Clean exit")
