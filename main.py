from segments import cleanup, display_number
import network
import urequests
from utime import sleep
hour, minute, second = 23, 30, 0

# Create a station interface and set your credentials
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect('raspberrypi')

while not station.isconnected():
    continue

print('Network config:', station.ifconfig())
try:
    while True:
        if station.isconnected():
            hour = int(urequests.get('http://10.42.0.1:5000/time/hour').text)
            minute = int(urequests.get('http://10.42.0.1:5000/time/minute').text)
            second = int(urequests.get('http://10.42.0.1:5000/time/second').text)
        else:
            second += 1
            if second == 60:
                second = 0
                minute += 1
                if minute == 60:
                    minute = 0
                    hour += 1
        hour_rem = 24 - hour
        minute_rem = 60 - minute 
        second_rem = 60 - second
        if hour == 23:
            number = (minute_rem - 1)  * 100 + (second_rem - 1)
        else:
            number = (hour_rem - 1) * 100 + (minute_rem - 1)
        display_number(number, 200, 2)
except KeyboardInterrupt:
    cleanup()
