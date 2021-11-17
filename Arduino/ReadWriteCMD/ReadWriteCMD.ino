/*
  ReadAnalogVoltage

  Reads an analog input on pin 0, converts it to voltage, and prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/ReadAnalogVoltage
*/
//#include <string.h>

// Compute the MODBUS RTU CRC
unsigned int ModRTU_CRC(byte *buf, int len)
{
  unsigned int crc = 0xFFFF;
  
  for (int pos = 0; pos < len; pos++) {
    crc ^= (unsigned int)buf[pos];          // XOR byte into least sig. byte of crc
  
    for (int i = 8; i != 0; i--) {    // Loop over each bit
      if ((crc & 0x0001) != 0) {      // If the LSB is set
        crc >>= 1;                    // Shift right and XOR 0xA001
        crc ^= 0xA001;
      }
      else                            // Else LSB is not set
        crc >>= 1;                    // Just shift right
    }
  }
  // Note, this number has low and high bytes swapped, so use it accordingly (or swap bytes)
  return crc;  
}

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

bool is_equal(byte cmd_1[], byte cmd_2[], int len)
{
  for(int i=0; i<len; i++)
  {
    if(cmd_1[i] !=  cmd_2[i])
      return false;
  }
  return true;
}

byte data[1029];
static unsigned int value = 0;
void prepe(byte x)
{
  data[0] = x;
  data[1] = 0x03;
  data[2] = 0x01;
  byte *d = &data[3];
  for(unsigned int i=0; i<1024; i++)
  {
    if(i%2 == 0)
    {
      d[i] = highByte(value);
      d[i+1] = lowByte(value);
      value++;
    }
  }
  // TODO add crc16
  unsigned int myCrc16 = ModRTU_CRC(data, 1027);
  data[1027] = lowByte(myCrc16);
  data[1028] = highByte(myCrc16);
}

void start_vobromotor(byte highByte, byte lowByte)
{
  value = (highByte << 8) | lowByte ;
}

bool is_ready()
{
  static int n = 1;
  if(n%10 == 0)
  {
    n++;
    return true;
  }
  n++;
  return false;
}

byte buffer[9];

// status
byte status_cmd[] = { 0x30, 0x04, 0x00, 0x00, 0x00, 0x01 };
//the vibromotor data request
byte vib_data[]   = {0x30, 0x03, 0x00, 0x02, 0x00, 0x01, 0x21, 0xEB};
// start vibromotor request 30 06 00 01 00 00 dc 2b
byte vib_start[] = {0x30, 0x06, 0x00, 0x01, 0x00, 0x00, 0xDC, 0x2B};
// get frequency
byte get_freq_cmd[] = {0x30, 0x03, 0x00, 0x01, 0x00, 0x01, 0xD1, 0xEB};
// ready data command 3X 04 00 00 00 02 CS CS
byte ready_data_cmd[] = { 0x30, 0x04, 0x00, 0x00, 0x00, 0x02 };

void serialEvent(){
  Serial.readBytes(buffer, 8);
  serial_flush_buffer();
  if(is_equal(&buffer[3], &vib_data[3], 3)) {
    prepe(buffer[0]);
    Serial.write(data, 1029);
  }
  else if(is_equal(&buffer[1], &vib_start[1], 3))
  {
    start_vobromotor(buffer[4], buffer[5]);
  }
  else if(is_equal(&buffer[1], &get_freq_cmd[1], 5))
  {
    buffer[4] = highByte(value);
    buffer[5] = lowByte(value);
    unsigned int myCrc16 = ModRTU_CRC(buffer, 6);
    buffer[6] = lowByte(myCrc16);
    buffer[7] = highByte(myCrc16);
    Serial.write(buffer, 8);
  }
  else if(is_equal(&buffer[1], &ready_data_cmd[1], 5))
  {
    if(is_ready())
    {
      buffer[3] = 0x01;
    }
    unsigned int myCrc16 = ModRTU_CRC(buffer, 4);
    buffer[4] = lowByte(myCrc16);
    buffer[5] = highByte(myCrc16);
    Serial.write(buffer, 6);
  }
  else if(is_equal(&buffer[1], &status_cmd[1], 5))
  {
    buffer[3] = 0x01;
    unsigned int myCrc16 = ModRTU_CRC(buffer, 4);
    buffer[4] = lowByte(myCrc16);
    buffer[5] = highByte(myCrc16);
    Serial.write(buffer, 6);
  }
  else
    Serial.write(buffer, 9);
}

bool alreadyRun = false;
// the loop routine runs over and over again forever:
void loop() {
//  if(alreadyRun == false)
//  {
//    prepe();
//    alreadyRun = true;
//  }
    
//  if(memcmp (buffer, cmd_1, 8)==0)
//  {
//    cmd_t[7] += 1; 
//    Serial.write(cmd_t, sizeof(cmd_t));
//  } else Serial.write(cmd_f, sizeof(cmd_f));
//  delay(1);
}
