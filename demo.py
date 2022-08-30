import time
import vfd_16

def main():
    display = vfd_16.Display(cs=18, clk=19, sdi=21, dimming=100)

    display.write('12345678abcdEFGH')

    time.sleep(1)
    
    display.write('ABCD', position=8)

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

    display.write('MicroPython VFD')
    
    time.sleep(1)

if __name__ == '__main__':
    main()
