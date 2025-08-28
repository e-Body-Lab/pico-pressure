'''
    pico-pressure-single.py

    Reads and displays a single analog channel of data from sensor on Pin 26. 

    Start running this file on the Pico 2W and then join the created network. The 
    on-board LED should blink when the network is being set up and stay on when the 
    set up is complete. The joining instructions will be printed in the REPL.

    Once joining the network and going to the IP address in a browser, a web page 
    displaying the relative value of the pressure sensor and a button to 
    shut down the server will be shown.

    The network ssid and password can be modified at the bottom of this file.
'''

import network
import socket
from time import sleep
from machine import ADC, Pin
import rp2
import sys
import json

# global variables for the pin with the on-board LED and sensor pin
led_pin = Pin("LED", Pin.OUT)
pressure_pin = ADC(Pin(26))
pressure_max = 65535

def webpage():
    '''
    Returns webpage to be served.
    '''
    html = """<!DOCTYPE html>
<html>
<head>
<title>Pico Pressure Single Channel</title>
</head>
<body>
<canvas id="myCanvas" width="900" height="500" style="border:1px solid black;">
Sorry, your browser does not support canvas.
</canvas>
<script>
let sensorData = "/sensors?";
fetch (sensorData)
.then(response => response.json())
.then(sensors => myDisplay(sensors));

function myDisplay(data) {
    const j = JSON.parse(data);
    document.getElementById("description").innerHTML = "test";
}

const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
ctx.fillStyle = "rgb(60 255 0 / 50%)";
ctx.fillRect(10,10,880,480);
</script>


<h1>Single Channel Pressure Sensor</h1>
<p id="description">Pressure sensor is X</p>
<form action="./close">
    <input type="submit" value="Shut down server" />
</form>
</body>
</html>
         """
    return str(html)

def start_sensing():
    '''
    Starts up the sensing and calibrates the sensor reading. The 
    sensor reading at start is taken to be the maximum value.
    '''
    return pressure_pin.read_u16()

def get_sensors():
    '''
    Returns json object of most recent sensor readings.
    '''
    # get current sensor value
    pressure_value = pressure_pin.read_u16()/pressure_max
    # create json serialisation
    sensors_json = json.dumps([{"sensor1": pressure_value }])
    return sensors_json

def serve(connection):
    '''
    Starts up the server for serving the webpage.
    '''
    # start with turning the LED on
    led_pin.on()

    # start a continous loop
    while True:
        # when a request is received
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        # print for debugging
        print(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/sensors?':
            data = get_sensors()
            client.send(data)
            client.close()
        elif request == '/close?':
            sys.exit()
        else:
            html = webpage()
            client.send(html)
            client.close()


def connect(ssid, password):
    '''
    Create access point.
    '''
    # set up the access with the given ssid and password
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)

    while ap.active() == False:
        print('Setting up connection...')
        time.sleep(0.5)
    print('AP mode is active, You can now connect')
    print('IP address to connect to: ' + ap.ifconfig()[0])
    # turn on LED
    led_pin.on()
    ap_ip = ap.ifconfig()[0]
    return ap_ip

def open_socket(ip):
    '''
    Opens a socket.
    '''
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    # start listening to incoming on socket
    connection.listen(1)
    return connection


# set up LED and sensing
pressure_max = start_sensing()
# set up web server
# can change the network name and password below
ip = connect('Pico2W', 'password')
connection = open_socket(ip)
serve(connection)
