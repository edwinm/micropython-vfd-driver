import time
import vfd_16

def main():
    display = vfd_16.Display(cs=18, clk=19, sdi=21, dimming=100)

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

    display.define_character(1,
"""

  *
   *
*****
   *
  *
""")

    display.define_character(2,
"""
 ***
 ***
  *
*****
  *
 * *
*   *
""")

    display.define_character(3,
"""
 ***
* * *
* * *
*****
*   *
*   *
 ***
""")



    display.write('\x00\x01\x02\x03 VFD Display')

    time.sleep(1)

    display.write('0123456', position=9)

    time.sleep(1)

    display.light_off()

    time.sleep(1)

    display.light_on()

    time.sleep(1)

    display.stand_by_mode()

    time.sleep(1)

    display.normal_mode()

    time.sleep(1)

    display.dim(255)

    time.sleep(1)

    display.dim(100)

    time.sleep(1)

    display.clear()

    display.write('\x01MicroPython VFD')
    
    time.sleep(1)

    display.dim(255)

if __name__ == '__main__':
    main()
