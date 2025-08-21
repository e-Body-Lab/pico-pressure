/*
 general_pressure_arduino

 To be used with the Processing sketch 
 general_pressure_processing.pde.

 Sends over Serial the sensor values for the 
 intersection of each row and column. Rows are 
 connected to analog pins and columns connected to 
 digital pins. 
*/

#define NUM_ROWS 3
#define NUM_COLS 4
#define SENSOR_POINTS NUM_ROWS* NUM_COLS

int rows[] = { A0, A1, A2 };
int cols[] = { 2, 3, 4, 5 };
int incomingValues[SENSOR_POINTS] = {};

void setup() {
  // set all columns to INPUT:
  for (int i = 0; i < NUM_COLS; i++) {
    pinMode(cols[i], INPUT);
  }
  // begin Serial communication
  Serial.begin(9600);
}

void loop() {
  // go through each column pin
  for (int colCount = 0; colCount < NUM_COLS; colCount++) {
    // set pin to OUTPUT
    pinMode(cols[colCount], OUTPUT);

    // set LOW
    digitalWrite(cols[colCount], HIGH);

    // read the input from each analog pin (row) in that column
    for (int rowCount = 0; rowCount < NUM_ROWS; rowCount++) {
      incomingValues[colCount * NUM_ROWS + rowCount] = analogRead(rows[rowCount]);

    } 
    // set column pint back to INPUT
    pinMode(cols[colCount], INPUT);
  } 

  // print over Serial the values of the matrix:
  for (int i = 0; i < SENSOR_POINTS; i++) {
    Serial.print(incomingValues[i]);
    if (i < SENSOR_POINTS - 1) Serial.print("\t");
  }
  Serial.println();
  delay(10);
}