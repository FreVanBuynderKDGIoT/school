#!/usr/bin/env python
"""
info about project
"""

# imports
from guizero import App, PushButton, Box, Text

__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


# functions
def button1_clicked():
    global light1_on
    if light1_on:
        light1_on = False
    else:
        light1_on = True
    color_the_lamps()


def button2_clicked():
    global light2_on
    if light2_on:
        light2_on = False
    else:
        light2_on = True

    color_the_lamps()


def button3_clicked():
    global light3_on
    if light3_on:
        light3_on = False
    else:
        light3_on = True

    color_the_lamps()


def color_the_lamps():
    if light1_on:
        lamp1_text.tk.configure(background="Yellow")
    else:
        lamp1_text.tk.configure(background="Black")

    if light2_on:
        lamp2_text.tk.configure(background="Yellow")
    else:
        lamp2_text.tk.configure(background="Black")

    if light3_on:
        lamp3_text.tk.configure(background="Yellow")
    else:
        lamp3_text.tk.configure(background="Black")


window = App(title="Dashboard oefening", width=380, height=170)
title = Text(window, text="Druk op een knop", size=20)
element_box = Box(window, width="fill", height="fill", layout="grid")

space = Box(element_box, width=20, height=80, grid=[0, 0])
lamp1 = Box(element_box, width=100, height=80, grid=[1, 0], border=True)
space = Box(element_box, width=20, height=80, grid=[2, 0])
lamp2 = Box(element_box, width=100, height=80, grid=[3, 0], border=True)
space = Box(element_box, width=20, height=80, grid=[4, 0])
lamp3 = Box(element_box, width=100, height=80, grid=[5, 0], border=True)

space = Box(element_box, width="fill", height=30, grid=[0, 1, 6, 1])

button1 = Box(element_box, width=100, height=20, grid=[1, 2], border=True)
space = Box(element_box, width=20, height=20, grid=[2, 2])
button2 = Box(element_box, width=100, height=20, grid=[3, 2], border=True)
space = Box(element_box, width=20, height=20, grid=[4, 2])
button3 = Box(element_box, width=100, height=20, grid=[5, 2], border=True)

lamp1_text = Text(lamp1, text="LAMP 1", color=(52, 52, 52), width=100, height=80)
lamp2_text = Text(lamp2, text="LAMP 2", color=(52, 52, 52), width=100, height=80)
lamp3_text = Text(lamp3, text="LAMP 3", color=(52, 52, 52), width=100, height=80)

lamp1_button = PushButton(button1, width=100, height=20, text="OK 1")
lamp2_button = PushButton(button2, width=100, height=20, text="OK 2")
lamp3_button = PushButton(button3, width=100, height=20, text="OK 3")

light1_on = False
light2_on = False
light3_on = False


lamp1_button.when_clicked = button1_clicked
lamp2_button.when_clicked = button2_clicked
lamp3_button.when_clicked = button3_clicked

color_the_lamps()

window.display()
