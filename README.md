# pico-pressure
Live visualisation of piezoresistive pressure sensing via a Pico 2 W

# Overview
This repository is a set of tools to support piezoresistive pressure sensing. 

In the full featured version, the Raspberry Pi Pico 2 W creates its own wifi network as an access point and serves a website to any connecting devices that displays the current pressure detected.

It also contains debugging examples to print the raw sensor data via the USB connection without involving wifi. 

## Directory of Resources
| Folder | Filename | Description |
| ----------- | - |----------- |
| pico-pressure-single |  | VS Code project for sensing a single pressure sensor |
|    | blink.py | Simple blinking of the on-board LED to verify the Pico is functioning |
# Set Up
This project is developed for the [Raspberry Pi Pico 2 W](https://www.raspberrypi.com/products/raspberry-pi-pico-2/). It will not work on another board without significant modification.

1. *Install MicroPython on the Pico 2 W -* This project uses MicroPython. You can find the instructions for how to install MicroPython on the Pico 2 W in the [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#what-is-micropython). It recommended that you download the UF2 file for the Pico 2 W from the [MicroPython documentation](https://micropython.org/download/RPI_PICO2_W/) directly.

2. *VS Code Pico Extension -* This project was developed using the development environment [Visual Studio (VS) Code](https://visualstudio.microsoft.com/). This repository contains the full project workspace which can be opened in VS Code. The Raspberry Pi Pico Project Extension directly interacts with the Pico, supporting an interactive terminal (REPL). Other projects and documentation may describe using Thonny, but this project recommends VS Code. The instructions for installing VS Code and the extension can be found in the [Pico documentation](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf).

3. *Pressure Sensing Circuit -* 

# Running the code

# Debugging tools
