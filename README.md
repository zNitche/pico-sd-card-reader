### Raspberry Pi Pico SD card reader example

---

#### Driver
MicroPython official `sdcard.py`

```
https://github.com/micropython/micropython/blob/v1.19.1/drivers/sdcard/sdcard.py
```

#### Wiring

| SD card reader Pin |     RPi Pico Pin     |
|--------------------|:--------------------:|
| 5V / 3.3 V         | 40 (VBUS) / 36 (3V3) |
| GND                |       38 (GND)       |
| MISO               |       11 (GP8)       |
| MOSI               |      15 (GP11)       |
| SCK                |      14 (GP10)       |
| CS                 |       12 (GP9)       |
