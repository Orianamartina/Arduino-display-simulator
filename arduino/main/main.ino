#include "Arduino.h"
#include "rdr2.h"

void setup() {
  Serial.begin(9600);

}

void loop() {
  Serial.write("IMGSTART", 8);
  for (int i = 0; i < sizeof(bitmap_data); i++)
  {
    Serial.write(bitmap_data[i]);
  }

}
