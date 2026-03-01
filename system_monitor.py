import subprocess
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time
from datetime import datetime as dt
from gpiozero import Button

serial = spi(device=0, port=0, gpio_DC=24, gpio_RST=25)
device = ssd1306(serial)

button = Button(4)

menu=0

def button_pressed():
    global menu
    if menu<2:
        menu = menu + 1
    else:
        menu = 0

def clock():
    now = dt.now()
    nowDate = now.date()
    nowTime = now.time()
    formatedTime =  str(nowTime.hour) + ":" + str(nowTime.minute) + ":" +str(nowTime.second)
    stringDate = nowDate.isoformat()
    with canvas(device) as draw:
        draw.text((70, 0), stringDate, fill="white")
        draw.text((0, 0), formatedTime, fill="white")

def get_cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", "r")as f:
        temp = f.read()
    return f"{float(temp) / 1000:.1f} °C"

def get_ip_address():
    cmd = "hostname -I | cut -d' ' -f1"
    try:
        ip = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
    except:
        ip = "No Network"
    return ip

def get_time():
    now = dt.now()
    nowTime = now.time()
    formattedTime = str(nowTime.hour) + ":" + str(nowTime.minute)#+ ":" + str(nowTime.second)
    return formattedTime

def get_date():
    now = dt.now()
    nowDate = now.date()
    stringDate = nowDate.isoformat()
    return stringDate

try:
    print("System monitor should be working!")
    while True:
        button.when_pressed = button_pressed
        with canvas(device) as draw:
            if menu == 0:
                draw.text((5, 5), "Time and Date:", fill="white")
                draw.line([(0, 20), (127, 20)], fill="white")
                draw.text((5, 25), f"Time: {get_time()}", fill="white")
                draw.text((5, 45), f"Date: {get_date()}", fill="white")
            elif menu == 1:
                draw.text((5, 5), "Network:", fill="white")
                draw.line([(0,20), (127,20)], fill="white")
                draw.text((5, 25), f"IP: {get_ip_address()}", fill="white")
            elif menu == 2:
                draw.text((5, 5), "System Stats:", fill="white")
                draw.line([(0, 20), (127, 20)], fill="white")
                draw.text((5, 25), f"CPU Temp: {get_cpu_temp()}", fill="white")
            
            #draw.text((5, 5), f"IP: {get_ip_address()}", fill="white")
            #draw.text((5, 25), f"CPU Temp: {get_cpu_temp()}", fill="white")
            #draw.text((5, 45), f"Time: {get_time()}", fill="white")
        time.sleep(5)
except KeyboardInterrupt:
    device.cleanup()
    print("Clean exit!")
