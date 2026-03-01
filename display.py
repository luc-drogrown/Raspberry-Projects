from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time

serial = spi(device=0, port=0, gpio_DC=24, gpio_RST=25)

device = ssd1306(serial)

def demo():
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((10,20), "Hello Pi Zero!", fill="white")
        draw.text((10, 40), "SPI is working!", fill="white")

try:
    demo()
    print("display should be on")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
