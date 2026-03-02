from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time

serial = spi(device=0, port=0, gpio_DC=24, gpio_RST=25)
device = ssd1306(serial)

xdirection = 1
ydirection = 1

def get_x(oldx):
    global xdirection
    if oldx+5+xdirection == 127:
        xdirection = -1
    elif oldx-xdirection == 0:
        xdirection = 1
    newx = oldx+xdirection
    return newx

def get_y(oldy):
    global ydirection
    if oldy+5+ydirection == 63:
        ydirection = -1
    elif oldy-ydirection == 0:
        ydirection = 1
    newy = oldy+ydirection
    return newy

x = 64
y = 32

try:
    print("Script is running!")
    while True:
        with canvas(device) as draw:
            x = get_x(x)
            y = get_y(y)
            draw.rectangle([(x,y), (x+5, y+5)], fill="white", width=2)
            #draw.rectangle([(64, 32), (69, 37)], fill="white", width=2)
        time.sleep(0.05)
except KeyboardInterrupt:
    device.cleanup()
    print("Clean Exit!")
