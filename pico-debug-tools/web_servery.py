'''
    web_server.py

    Simple example to demonstrate two-way communication with a Pico 2W running as 
    as access point. 

    Start running this file on the Pico 2W and then join the created network. The 
    on-board LED should blink when the network is being set up and stay on when the 
    set up is complete. The joining instructions will be printed in the REPL.

    Once joining the network and going to the IP address in a browser, a web page 
    displaying the state of the LED and a series of buttons to control the LED and 
    shut down the server will be shown.

    The network ssid and password can be modified at the bottom of this file.
'''

import network
import socket
from time import sleep
from machine import Pin
import rp2
import sys

# global variable for the pin with the on-board LED
pin = Pin("LED", Pin.OUT)

def webpage(led_state, square_color):
    #Template HTML
    html = f"""<!DOCTYPE html>
<html>
<body>
<h1>Pressure Sensor Debug</h1>
<p>You should see a square that changes color when the below buttons are pressed. The LED on the Pico should also turn on and off.</p>
<canvas id="myCanvas" width="500" height="500" style="border:1px solid black;">
Sorry, your browser does not support canvas.
</canvas>

<script>
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
ctx.fillStyle = {square_color};
ctx.fillRect(10,10,480,480);
</script>
<form action="./lighton">
            <input type="submit" value="Light on" />
            </form>
            <form action="./lightoff">
            <input type="submit" value="Light off" />
            </form>
            <form action="./close">
            <input type="submit" value="Shut down server" />
            </form>
<p>LED is {led_state}</p>
</body>
</html>
         """
    return str(html)

def serve(connection):
    '''
    Starts up the server for serving the webpage.
    '''
    # keep track of LED state
    state = 'ON'
    # displayed color in the webpage
    color = '\"green\"'
    # start with turning the LED on
    pin.on()

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
        if request == '/lighton?':
            pin.on()
            state = 'ON'
            color = '\"green\"'
        elif request =='/lightoff?':
            pin.off()
            state = 'OFF'
            color = '\"black\"'
        elif request == '/close?':
            sys.exit()
        html = webpage(state, color)
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
    print('IP address to connect to:: ' + ap.ifconfig()[0])
    # turn on LED
    pin.on()
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

# can change the network name and password below
ip = connect('Pico2W', 'password')
connection = open_socket(ip)
serve(connection)
