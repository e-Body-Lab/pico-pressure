/*
 general_pressure_processing
 
 To be paired with general_pressure_arduino.ino
 
 Visualizes values sent by Arduino by drawing a grid using 
 grayscale shading of each square to represent sensor value.
 
 Expects sensor values to be between 0 and 1023, decreasing as 
 pressure is applied. The sensor values first sent are expected 
 to be the the maximum values (the sensor under no pressure).
 */

import processing.serial.*;

// The serial port
Serial myPort;
int numRows = 3;
int numCols = 4;
int maxNumberOfSensors = numRows * numCols;

// global variable for storing mapped sensor values
float[] sensorValue = new float[maxNumberOfSensors];

// array of previous values
float[] previousValue = new float[maxNumberOfSensors];
int rectWidth;
int rectHeight;
int calibrationValue=-1;

void setup () {
  // set window size, can be changed
  size(600, 600);
  rectWidth = width/numCols;
  rectHeight =height/numRows;

  // List all the available serial ports
  println(Serial.list());
  String portName = Serial.list()[2];
  myPort = new Serial(this, portName, 9600);
  myPort.clear();
  // don't generate a serialEvent() until you get a newline (\n) byte
  myPort.bufferUntil('\n');

  // set inital background
  background(255);
  // turn on antialiasing
  smooth();
  rectMode(CORNER);
}

void draw () {
  // for each column
  for (int i=0; i<numCols; i++) {
    // for each row
    for (int j = 0; j<numRows; j++) {
      // update the fill colour according to the sensor value
      fill(sensorValue[i * numRows + j]);
      // draw the rectangle
      rect(rectWidth * i, rectHeight*j, rectWidth, rectHeight);
    }
  }
}

void serialEvent (Serial myPort) {
  String inString = myPort.readStringUntil('\n');
  // get the ASCII string
  // if it's not empty
  if (inString != null) {
    // trim off any whitespace
    inString = trim(inString);
    // convert to an array of ints
    int incomingValues[] = int(split(inString, "\t"));

    // if first time reading in data
    if (calibrationValue == -1) {
      // calibrate
      calibrationValue = incomingValues[numRows*numCols/2];
    }

    if (incomingValues.length <= maxNumberOfSensors && incomingValues.length > 0) {
      for (int i = 0; i < incomingValues.length; i++) {
        // map the incoming values (0 to 1023) to an appropriate gray-scale range (0-255):
        sensorValue[i] = map(incomingValues[i], 0, 1023, 0, calibrationValue);
        //println(sensorValue[i]);
      }
    }
  }
}
