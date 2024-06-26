# MicroPython VFD driver

>Micropython driver for the 8-MD-06INKM Futaba VFD display with 16 segments

## Vacuum fluorescent display (VFD)

Futaba Vacuum fluorescent displays are very bright displays and together with
a LGL VFD Studio backplate, very easy to control using SPI.
Including power, only five connections are needed (GND, VSS, CS, CLK and SDI/MOSI).


<img src="img/vfd.jpg" alt="Photo of VFD connected to an ESP32" width="800" height="528">

## Install

1) Copy the file [`vfd_16.py`](vfd_16.py) to your microcontroller.

2) Connect the five pins as follows:

<img src="img/vfd-pins.jpg" alt="Photo of VFD pins" width="800" height="600">


| VFD | ESP32   |
|-----|---------|
| GND | GND     |
| VCC | 3V3     |
| C S | GPIO 18 |
| CLK | GPIO 19 |
| SDI | GPIO 21 |

To connect the VFD to a breadboard, you need to solder a 5 pin header to the VFD display first.

3) Then use this code to show some text on the display:

```python
import vfd_16

display = vfd_16.Display(cs=18, clk=19, sdi=21, dimming=100)

display.write('12345678abcdEFGH')
```

With an ESP32, you can use any free GPIO pins. On other microcontrollers, you might want to
connect the VFD pins to the corresponding SPI pins on the microcontroller.
In that case, connect the VFD SDI pin to the microcontroller MOSI pin.

## API

### `display = vfd_16.Display(cs=18, clk=19, sdi=21, dimming=100, baudrate=20000000)`

Initialise the display.

| Parameter |          |                 |
|-----------|----------|-----------------|
| `cs`        |          | GPIO pin number |
| `clk`       |          | GPIO pin number |
| `sdi`       |          | GPIO pin number |
| `dimming`   | Optional | Dimming (0-240) |
| `baudrate`  | Optional | SPI Baudrate    |

### `display.write('12345678ABCDEFGH')`

Write a string of up to 16 characters to the display.

### `display.write('XYZ', position=6)`

Write a string at the specified position.

### `display.light_off()`

Turn the lights off.

### `display.light_on()`

Turn the lights on. In combination with `light_off()`, this can be used to blink text.

### `display.stand_by_mode()`

Put the display in standby mode to conserve energy. The display will be off.

### `display.normal_mode()`

Get the display out of standby mode.

### `display.dim(120)`

Dim the display. Values go from 0 (dark) until 240 (full brightness).

### `display.clear()`

Clears the display from any text.

### `display.ticker(text, fps, callback)`

Show the text scrolling on the display.
The `text` parameter is the text, which can be larger than 16 characters.
Set the speed with the `fps` parameter. 5 is the default value.
A higher value results in faster scrolling.
The last optional parameter is a callback function.
When this callback function returns `True`, the `ticker` function stops and returns.

### `display.define_character(num, data)`

Define your own character. `num` is a number 0-7 and `data` is a multiline string, see below.
On the VFD display, you can define eight custom characters.

You can provide the character with a multiline string of
7 lines of 5 characters wide. Every nonspace character will be
a bit that will light up.

```python
    display.define_character(0,
"""
 * *
*****
*****
*****
 ***
 ***
  *
""")
```

You can include the custom characters in your text with hex codes:
`"\x00"` for the custom character 0, `"\x01"` for the custom character 1,
up till `"\x07"` for the custom character 7.
See [demo.py](demo.py) for more examples.

<img src="img/vfd-custom-characters.jpg" alt="Photo of VFD with custom characters" width="800" height="600">

## Hardware

This code is tested with an ESP32 microcontroller, but should work with other microcontrollers that can run Micropython as well.
Let me know your experiences, so I can update this documentation.

## Where to buy?

There are several places where you can buy this VFD display. For example:

[Ali Express/Hi IE Store](https://www.aliexpress.com/item/1005001498957894.html)

When buying the display, make sure that:
- It has 16 segments (digits)
- It has only one row of text
- It has a backplate PCB with five connections (GND, VSS, CS, CLK and SDI).

It should look just like the photos in this document.

## What about 8 segment displays?

This driver is for the 16 segment (digits) VFD display only.
If you have a 8 segment display, I recommend to take a look at
[MicroPython 8MD-06INKM display driver](https://github.com/Reboot93/MicroPython-8MD-06INKM-display-driver) from Reboot93.

## Specification

The specification below applies to the 8 segment version. Most of the API is similar, though.

[Futaba 8-MD-06INKM specification](https://davll.me/posts/2021/05/22/futaba-vfd-1/data/008MD006INKM_A.pdf)

## License

Copyright 2022 [Edwin Martin](https://bitstorm.org/) and released under the [MIT license](LICENSE).
