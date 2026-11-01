from smbus2 import SMBus
import time

ARDUINO_ADDRESS = 0xa;

def send_text_to_arduino(text):
    try:
        data = [ord(char) for char in text]
        with SMBus(1) as bus:
            bus.write_i2c_block_data(ARDUINO_ADDRESS, data[0], data[1:])
        print(f"Sent text to Arduino: {text}")
    except Exception as e:
        print(f"Error sending text to Arduino: {e}")

if __name__ == "__main__":
    send_text_to_arduino("ERROR")
    time.sleep(5)
    send_text_to_arduino("ALL GOOD")