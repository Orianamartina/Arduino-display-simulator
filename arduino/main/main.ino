#include "Arduino.h"
// #include "rdr2.h"
#include "recortes/recorte_1.h"
#include "recortes/recorte_2.h"
#include "recortes/recorte_3.h"
#include "recortes/recorte_4.h"
#include "recortes/recorte_5.h"
#include "recortes/recorte_6.h"
#include "recortes/recorte_7.h"
#include "recortes/recorte_8.h"
#include "recortes/recorte_9.h"
#include "recortes/recorte_10.h"
#include "recortes/recorte_11.h"
#include "recortes/recorte_12.h"

void setup() {
  Serial.begin(9600);

}
const unsigned char* const images[] PROGMEM = { bitmap_data_1, bitmap_data_2, bitmap_data_3, bitmap_data_4, bitmap_data_5, bitmap_data_6, bitmap_data_7, bitmap_data_8, bitmap_data_9, bitmap_data_10, bitmap_data_11, bitmap_data_12};
const size_t image_sizes[] = { sizeof(bitmap_data_1), sizeof(bitmap_data_2), sizeof(bitmap_data_3), sizeof(bitmap_data_4), sizeof(bitmap_data_5), sizeof(bitmap_data_6), sizeof(bitmap_data_7), sizeof(bitmap_data_8), sizeof(bitmap_data_9), sizeof(bitmap_data_10), sizeof(bitmap_data_11), sizeof(bitmap_data_12)};
void loop() {
  for (int image = 0; image < 4; image++) {
    Serial.print("IMGSTART");
    const unsigned char* bitmap_ptr = (const unsigned char*)pgm_read_ptr(&images[image]);
    for (size_t i = 0; i < image_sizes[image]; i++) {
        Serial.write(pgm_read_byte(bitmap_ptr + i));
    }

  }
    // Serial.print("IMGSTART");
    // Serial.print(sizeof(bitmap_data_1));
    // for (int i = 0; i < sizeof(images[0]); i++)
    // {
    //   Serial.write(pgm_read_byte(&(images[0])[i]));
    // }
    // delay(40);

  

}
