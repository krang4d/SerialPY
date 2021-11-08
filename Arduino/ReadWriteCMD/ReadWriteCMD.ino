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

bool is_equal(byte cmd[], int len)
{
  //ffffffffffff019400
  byte tmp[]   = {0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x01, 0x94, 0x00};
  for(int i=0; i<len; i++)
  {
    if(cmd[i] !=  tmp[i])
      return false;
  }
  return true;
}

byte data[1024];
void prepe()
{
  byte b = 0;
  for(int i=0; i<1024; i++)
  {
    data[i] = b;
    b++;
  }
}

byte buffer[9];
byte cmd_0[]   = {0x10, 0x03, 0x00, 0x01, 0x00, 0x01, 0xD6, 0x8B};
byte cmd_1[] = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08};
byte cmd_t[] = {0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01};
byte cmd_f[] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};

void serialEvent(){
  Serial.readBytes(buffer, 8);
  serial_flush_buffer();
  if(is_equal(buffer, 8)) {
    Serial.write(data, 1024);
  }
  else 
    Serial.write(buffer, 9);
}

bool alreadyRun = false;
// the loop routine runs over and over again forever:
void loop() {
  if(alreadyRun == false)
  {
    prepe();
    alreadyRun = true;
  }
    
//  if(memcmp (buffer, cmd_1, 8)==0)
//  {
//    cmd_t[7] += 1; 
//    Serial.write(cmd_t, sizeof(cmd_t));
//  } else Serial.write(cmd_f, sizeof(cmd_f));
//  delay(1);
}
