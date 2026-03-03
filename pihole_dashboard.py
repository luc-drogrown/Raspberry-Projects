from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
import time
import requests
from gpiozero import Button

#initialize display
serial = spi(device=0, port=0, gpio_DC=24, gpio_RST=25)
device = ssd1306(serial)

button = Button(4)

menu = 0

def button_pressed():
    global menu
    if menu<2:
        menu += 1
    else:
        menu = 0

def createSession():
    url = "http://localhost/api/auth"
    apiPayload = {"password": "P6EiId3_"}

    r = requests.post(url, json=apiPayload, timeout = 5)

    if r.status_code == 200:
        data = r.json()

        sid = data['session']['sid']
        print("Login Succesfull! SID: {sid}")
        return sid
    else:
        print("Server rejected login: {r.status_code}")
        return 0
    
def getStats(sid):
    statsUrl = "http://localhost/api/stats/summary"
    infoUrl = "http://localhost/api/info/system"
    
    if sid != 0:
        header = {"X-FTL-SID": sid}
    
    stats_r = requests.get(statsUrl, headers=header)
    info_r = requests.get(infoUrl, headers=header)
    stats = stats_r.json()
    info = info_r.json()

    return stats

try:
    print("Scripts is running!")
    sid = createSession()
    while True:
        stats = getStats(sid)
        with canvas(device) as draw:
            if menu == 0:
                draw.text((5, 5), "Pi-Hole: Ads", fill="white")
                draw.line([(0, 20), (127, 20)], fill="white")
                draw.text((5, 25), f"Ads Today: {stats['queries']['blocked']}", fill="white")
                draw.text((5, 45), f"Percent: {stats['queries']['percent_blocked']}%", fill="white")
            elif menu == 1:
                draw.text((5, 5), "Pi-Hole: Clients", fill="white")
                draw.line([(0, 20), (127, 20)], fill="white")
                draw.text((5, 25), f"Active: {stats['clients']['active']}", fill="white")
                draw.text((5, 45), f"Total: {stats['clients']['total']}", fill="white")
            elif menu == 2:
                draw.text((5, 5), "Pi-Hole: Status", fill="white")
                draw.line([(0, 20), (127, 20)], fill="white")
                draw.text((5, 25), f"Uptime: {info['system']['uptime']} s", fill="white")
                draw.text((5, 45), f"CPU: {info['system']['cpu']['%cpu']} %", fill="white")
        time.sleep(5)
except KeyboardInterrupt:
    device.cleanup()
    print("Clean exit!")