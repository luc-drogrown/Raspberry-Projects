import os
import time
from luma.core.render import canvas

# --- HARDWARE DETECTION ---
def get_device():
    try:
        # Check if we are on a Raspberry Pi (ARM architecture)
        if os.uname()[4][:3] == 'arm':
            from luma.core.interface.serial import spi
            from luma.oled.device import ssd1306
            serial = spi(device=0, port=0, gpio_DC=24, gpio_RST=25)
            return ssd1306(serial)
        else:
            # We are on a laptop! Use the Emulator
            from luma.emulator.device import pygame
            return pygame(width=128, height=64)
    except Exception as e:
        print(f"Error loading device: {e}")
        return None

device = get_device()

# --- MAIN LOOP ---
try:
    while True:
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white")
            draw.text((30, 25), "GIT SYNCED!", fill="white")
        time.sleep(1)
except KeyboardInterrupt:
    pass