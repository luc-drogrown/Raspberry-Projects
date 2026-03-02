from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time

serial = spi(device=0, port=0, gpio_DC=24, gpio_RST=25)
device = ssd1306(serial)

def get_x(oldx):
    direction = 1
    if oldx+5+direction == 127:
        direction = -1
    elif oldx-direction == 0:
        direction == 1
    newx = oldx+direction
    return newx

def get_y(oldy):
    direction = 1
    if oldy+5+direction == 63:
        direction = -1
    elif oldy-direction == 0:
        direction = 1
    newy = oldy+direction
    return newy

x = 64
y = 32

try:
    print("Script is running!")
    x += get_x(x)
    y += get_y(y)
    while True:
        with canvas(device) as draw:
            #draw.rectangle([(x,y), (x+5, y+5)], fill="white", width=2)
            draw.rectangle([(64, 32), (69, 37)], fill="white", width=2)
        time.sleep(1)
except KeyboardInterrupt:
    device.cleanup()
    print("Clean Exit!")
