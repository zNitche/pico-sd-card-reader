import machine
from lib import sdcard
import uos
import os


def init_sd_card_reader():
    cs = machine.Pin(9, machine.Pin.OUT)
    spi = machine.SPI(1,
                      baudrate=1000000,
                      polarity=0,
                      phase=0,
                      bits=8,
                      firstbit=machine.SPI.MSB,
                      sck=machine.Pin(10),
                      mosi=machine.Pin(11),
                      miso=machine.Pin(8))

    sd = sdcard.SDCard(spi, cs)

    return sd


def get_file_size(file_path):
    return os.stat(file_path)[6]


def mount_sd_card(sd_card_reader):
    vfs = uos.VfsFat(sd_card_reader)
    uos.mount(vfs, "/sd_card")


def main():
    sd_card_reader = init_sd_card_reader()
    mount_sd_card(sd_card_reader)

    file_path = "/sd_card/test_file.txt"

    with open(file_path, "a+") as file:
        file.write("Hello Pico")
        file.write("\r\n")

    print(f"file '{file_path}' size = {get_file_size(file_path)}")


if __name__ == '__main__':
    main()
