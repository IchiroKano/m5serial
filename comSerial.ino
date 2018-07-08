#include <M5Stack.h>

HardwareSerial Serial2(2);

void setup() {
  
  M5.begin();

  // Serial2.begin(unsigned long baud, uint32_t config, int8_t rxPin, int8_t txPin, bool invert)
  Serial2.begin(115200, SERIAL_8N1, 16, 17);

  M5.Lcd.setTextColor(TFT_WHITE,TFT_BLACK);  
  M5.Lcd.setTextSize(2);
  M5.Lcd.setCursor(0, 0, 4);
  M5.Lcd.println("M5 uart start");  
}

void loop() {
  if(Serial2.available() > 0) {
    String strInput = Serial2.readStringUntil('\n');
    M5.Lcd.clear();
    M5.Lcd.setCursor(0, 64, 4);
    M5.Lcd.setTextColor(GREEN);
    M5.Lcd.println( strInput );
  }

  if(M5.BtnA.wasPressed()) {
    printMessage( "IP address" );
  }
  if(M5.BtnB.wasPressed()) {
    printMessage( "Date" );
  } 
  if(M5.BtnC.wasPressed()) {
    printMessage( "Time" );
  } 
  
    M5.update();
}

void printMessage( char *strMsg ){
  M5.Lcd.clear();
  M5.Lcd.setCursor(0, 128, 4);
  M5.Lcd.setTextColor(YELLOW);
  M5.Lcd.println( strMsg );  
  Serial2.write( strMsg );
}
