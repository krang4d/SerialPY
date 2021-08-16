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

void serial_flush_buffer()
{
  while (Serial.read() >= 0)
   ; // do nothing
}

byte buffer[9];
byte cmd[]   = {0x10, 0x03, 0x00, 0x01, 0x00, 0x01, 0xD6, 0x8B};
byte cmd_1[] = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08};
byte cmd_t[] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01};
byte cmd_f[] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};

void serialEvent(){
  Serial.readBytes(buffer, 8);
  serial_flush_buffer();
  Serial.write(buffer, 9);
}

// the loop routine runs over and over again forever:
void loop() {
  
//  if(memcmp (buffer, cmd_1, 8)==0)
//  {
//    cmd_t[7] += 1; 
//    Serial.write(cmd_t, sizeof(cmd_t));
//  } else Serial.write(cmd_f, sizeof(cmd_f));
//  delay(1);
}
