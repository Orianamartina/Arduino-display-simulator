#include "Arduino.h"
#include "rdr2.h"

void setup() {
  Serial.begin(9600);

}

void loop() {
  Serial.print("IMGSTART");
  for (int i = 0; i < sizeof(bitmap_data); i++)
  {
    Serial.write(pgm_read_byte(&bitmap_data[i]));
  }

}
