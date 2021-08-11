/*
  ReadAnalogVoltage

  Reads an analog input on pin 0, converts it to voltage, and prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/ReadAnalogVoltage
*/
//#include <string.h>

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

byte buffer[8];
byte cmd[] = {0x10, 0x03, 0x00, 0x01, 0x00, 0x01,0xD6, 0x8B};
byte cmd_1[] = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06,0x07, 0x08};
byte cmd_t[] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x01};
byte cmd_f[] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00};

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  String out = String(voltage) + ";" + String(voltage + 1) + ";" + String(voltage + 2);
  // print out the value you read:
  //  Serial.println(out);
  Serial.readBytes(buffer, 8);
  if(memcmp (buffer, cmd_1, 8)==0)
  {
    Serial.write(cmd_t, sizeof(cmd_t));
  } else Serial.write(cmd_f, sizeof(cmd_f));
  delay(500);
}
