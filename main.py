#!/usr/bin/env python
"""
Maak een teller.
Je hebt een drukknop die optelt en één die naar beneden telt.
"""

from gpiozero import Button

__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


global counter
counter = 0
IP = "192.168.0.101"
buttonUp = Button(4, pull_up=True, active_state=None, bounce_time=0.5, hold_time=0.5, hold_repeat=False, pin_factory=IP)
buttonDown = \
    Button(5, pull_up=True, active_state=None, bounce_time=0.5, hold_time=0.5, hold_repeat=False, pin_factory=IP)
buttonReset = \
    Button(6, pull_up=True, active_state=None, bounce_time=0.5, hold_time=0.5, hold_repeat=False, pin_factory=IP)

def main():
    while True:
        buttonUp.when_activated = CountUp()
        buttonDown.when_activated = CountDown()
        buttonReset.when_activated = CountReset()


def CountUp():
    counter += 1
    PrintCounter()



def CountDown():
    counter -= 1
    PrintCounter()


def CountReset():
    counter = 0
    print(counter)



def PrintCounter():
    print("de counter staat op: ", counter)


if __name__ == '__main__':
    main()
