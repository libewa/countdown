from machine import Pin
from utime import sleep
from random import randint

anodes = [
    Pin(18, Pin.OUT),
    Pin(16, Pin.OUT),
    Pin(14, Pin.OUT),
    Pin(12, Pin.OUT),
    Pin(11, Pin.OUT),
    Pin(17, Pin.OUT),
    Pin(15, Pin.OUT)
]

cathodes = [
    Pin(6, Pin.OUT),
    Pin(7, Pin.OUT),
    Pin(8, Pin.OUT),
    Pin(9, Pin.OUT)
]

led_dp = Pin(13, Pin.OUT)

numbers = [
    [1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1]
]

def cleanup():
    for seg in anodes:
        seg.value(0)
    led_dp.value(0)
    for cat in cathodes:
        cat.value(0)

def set_segments(digit: int, positions: [int], decimal: bool = False):
    """
Set individual digits to a given number between 0 and 9.
`digit` is the number to set the digits to.
`positions` is an array of 4 integers which can be either 1 or 0. These specify where to place the `digit`.
`decimal` is a bool that specifies whether to turn on the decimal point for ALL of the `positions`. (To specify the position of the decimal point, use `display_number()`)
    """
    for i in range(4):
        cathodes[i].value(not positions[i])
    if digit != None:
        for i in range(7):
            anodes[i].value(numbers[digit][i])
    
    led_dp.value(decimal)

def set_decimal(decimal_pos: int):
    if decimal_pos != None and decimal_pos != 0:
        if decimal_pos == 1:
            set_segments(None, [1, 0, 0, 0], True)
        elif decimal_pos == 2:
            set_segments(None, [0, 1, 0, 0], True)
        elif decimal_pos == 3:
            set_segments(None, [0, 0, 1, 0], True)
        elif decimal_pos == 4:
            set_segments(None, [0, 0, 0, 1], True)
        
def display_number(number: int, duration: int, decimal_pos: int = 0):
    """
Display a four-digit number on the seven-segment display.

`number` must be a whole number between 0 and 9999.
`duration` defines the number of "cycles" the number is shown. One "cycle" is 5 ms.
`decimal_pos` must be between 0 and 4 or None, a value of either 0, None or a value greater than 4 has no decimal point diplayed.
    """
    if number > 9999:
        raise ValueError("Value must be smaller than 9999")
    if number < 0:
        raise NotImplementedError("Values must be positive as of now")
    
    digits = [int(i) for i in str(number)]
    while len(digits) < 4:
        digits = [0] + digits
    
    for _ in range(duration):
        set_segments(digits[0], [1, 0, 0, 0])
        sleep(0.001)
        cleanup()
        set_segments(digits[1], [0, 1, 0, 0])
        sleep(0.001)
        cleanup()
        set_segments(digits[2], [0, 0, 1, 0])
        sleep(0.001)
        cleanup()
        set_segments(digits[3], [0, 0, 0, 1])
        sleep(0.001)
        cleanup()
        set_decimal(decimal_pos)
        sleep(0.001)
        cleanup()

if __name__ == "__main__":
    try:
        cleanup()
        sleep(0.5)
        display_number(int(input("number: ")), 2000)
        cleanup()
    except KeyboardInterrupt:
        cleanup()
