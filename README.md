# pico-pressure
Live visualisation of piezoresistive pressure sensing via a Pico 2 W

# Overview
This repository is a set of tools to support piezoresistive pressure sensing. 

In the full featured version, the Raspberry Pi Pico 2 W creates its own wifi network as an access point and serves a website to any connecting devices that displays the current pressure detected.


## Directory of Resources
| Folder | Filename | Description |
| ----------- | - |----------- |
| `pico-pressure-single` |  | VS Code project for sensing a single pressure sensor |
|                      | | |
| `pico-pressure-matrix` |  | VS Code project for sensing a pressure matrix |
|                      | | |
| `pico-debug-tools` |  | VS Code project with debugging code examples for the Pico |
|    | `blink.py` | Simple blinking example of the on-board LED to verify the Pico is functioning |
|    | `simpleaccesspoint.py` | Simple example of pico acting as an accesspoint, creating a wifi network, and serving a simple webpage |
| `arduino-debug-tools` | | Arduino and Processing sketches for verifying the circuit works |
|    | `general_pressure_arduino.ino` | Arduino sketch to measure the pressure change |
|    | `general_pressure_processing.pde` | Processing sketch to visualise pressure change |

# Set Up
This project is developed for the [Raspberry Pi Pico 2 W](https://www.raspberrypi.com/products/raspberry-pi-pico-2/). It will not work on another board without significant modification.

1. *Install MicroPython on the Pico 2 W -* This project uses MicroPython. You can find the instructions for how to install MicroPython on the Pico 2 W in the [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#what-is-micropython). It recommended that you download the UF2 file for the Pico 2 W from the [MicroPython documentation](https://micropython.org/download/RPI_PICO2_W/) directly.

2. *VS Code Pico Extension -* This project was developed using the development environment [Visual Studio (VS) Code](https://visualstudio.microsoft.com/). This repository contains the full project workspace which can be opened in VS Code. The Raspberry Pi Pico Project Extension directly interacts with the Pico, supporting an interactive terminal (REPL). Other projects and documentation may describe using Thonny, but this project recommends VS Code. The instructions for installing VS Code and the extension can be found in the [Pico documentation](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf).

3. *Pressure Sensing Circuit -* For the single pressure sensor, a voltage divider circuit is connected to an analog pin. For the matrix sensors, rows are connected to analog pins and columns connected to digital pins.

# Running the code
1. Open the Python file to be run in VS Code with the Pico board connected to the laptop. 
2. The bottom status bar VS Code should show that the Pico is Connected. Click on the Run button.
3. Click on the Stop button to stop the code.


# Debugging tools
## Pico Debugging
Code examples to isolate the different aspects of the system for debugging.
* `blink.py` - Blinks the on-boad LED on and off. Code example to determine that the Pico board is working as expected and code can be uploaded from a computer.

* `simpleaccesspoint.py` - Creates a wifi accesspoint from the Pico. From a laptop connect to the network name `Pico2W` using the password `password`. Both the network name and password can be changed in the last two lines of the Python file.

## Arduino Debugging
Code examples for using an Arduino and Processing to visualise the pressure changes.
* `general_pressure_arduino.ino` - Arduino sketch that reads in from a 3 x 4 matrix pressure sensor and prints the values over Serial.
* `general_pressure_processing.pde` - Processing sketch that displays the values from the Arduino in a grid that changes colour according to the pressure applied.