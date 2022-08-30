# MicroPython VFD driver for 16 segments only
# 2022, Edwin Martin
# License: MIT

from micropython import const
from machine import Pin, SPI

DIGITS = const(16)

SPACE = const(0x20)
NOT_RELEVANT = const(0x00)

DCRAM_DATA_WRITE = const(0x20)
DIGIT_SET_OF_DISPLAY_TIMING = const(0xE0)
DIMMING_SET = const(0xE4)
DISPLAY_LIGHT_ON = const(0xE8)
DISPLAY_LIGHT_OFF = const(0xEA)
STAND_BY_MODE_SET = const(0xEC)
NORMAL_MODE = const(0x00)
STAND_BY_MODE = const(0x01)


class Display():

    def __init__(self, cs, clk, sdi, spi_id=2, dimming=255, baudrate=20000000):
        self.baudrate = baudrate
        self.spi = SPI(spi_id, sck=Pin(clk), mosi=Pin(sdi))
        self.cs = Pin(cs, Pin.OUT, value=1)

        self.__command((DIGIT_SET_OF_DISPLAY_TIMING, DIGITS - 1))
        self.dim(dimming)
        self.light_on()

    def write(self, string, position=0):
        for char in string:
            self.__command((DCRAM_DATA_WRITE | position, ord(char)))
            position = position + 1

    def clear(self):
        for digit in range(DIGITS):
            self.__command((DCRAM_DATA_WRITE | digit, SPACE))

    def dim(self, dimming: int):
        self.__command((DIMMING_SET, dimming))

    def normal_mode(self):
        self.__command([STAND_BY_MODE_SET | NORMAL_MODE, NOT_RELEVANT])

    def stand_by_mode(self):
        self.__command([STAND_BY_MODE_SET | STAND_BY_MODE, NOT_RELEVANT])

    def light_on(self):
        self.__command((DISPLAY_LIGHT_ON, NOT_RELEVANT))

    def light_off(self):
        self.__command((DISPLAY_LIGHT_OFF, NOT_RELEVANT))

    def __command(self, commands):
        self.spi.init(baudrate=self.baudrate, polarity=0, phase=0, firstbit=self.spi.LSB)
        self.cs(0)
        for command in commands:
            self.spi.write(bytearray([command]))
        self.cs(1)
