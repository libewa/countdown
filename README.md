# countdown
This repository houses code for a MicroPython New Years countdown, which displays the time until midnight on a connected 7 segment display.

## Installing

To run this project, copy `segments.py` and `main.py` to your Pico using Thonny or the recommended VS Code extension (click "Toggle Pico-W-FS" in the status bar).

Then run `gettime.py` on another computer with a set clock, enable an unencrypted AP with SSID `raspberrypi`, and reset your Pico. You also probably need to change the `hostip` variable in `main.py` to your host computer's IP address.

Pull requests for improvement are welcome.