#include <SPI.h>
#include <MFRC522.h>

// lcd
#include <LiquidCrystal_I2C.h>  //http://downloads.arduino.cc/libraries/github.com/marcoschwartz/LiquidCrystal_I2C-1.1.2.zip
#include <Wire.h>               // https://www.resistorpark.com/content/Arduino_Libraries/wire.zip

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_1_PIN        10         // Configurable, take a unused pin, only HIGH/LOW required, must be different to SS 2
#define SS_2_PIN        8          // Configurable, take a unused pin, only HIGH/LOW required, must be different to SS 1
#define LED_G         7             //define green LED pin
#define LED_R         6             //define red LED

#define RELAY         2             //relay pin 
#define ACCESS_DELAY 4000
#define DENIED_DELAY 3000

byte ssPins[] = {SS_1_PIN, SS_2_PIN};
MFRC522 mfrc522[RELAY];   // Create MFRC522 instance.
LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display


void setup() 
{
  Serial.begin(9600);   // Initiate a serial communication
  while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();          // Initiate  SPI bus
  
  for (uint8_t reader = 0; reader < RELAY; reader++) {
    mfrc522[reader].PCD_Init(ssPins[reader], RST_PIN); // Init each MFRC522 card
    Serial.print(F("Reader "));
    Serial.print(reader);
    Serial.print(F(": "));
    mfrc522[reader].PCD_DumpVersionToSerial();
  }
  
  // Initiate the LCD:
  lcd.init();
  lcd.backlight();
  pinMode(LED_G, OUTPUT);
  pinMode(LED_R, OUTPUT);
  pinMode(RELAY, OUTPUT);
  digitalWrite(RELAY, LOW);
  
    lcd.setCursor(1, 0); 
    lcd.print("Scan Your Key");
    lcd.setCursor(6, 1); 
    lcd.print("^-^");
      
}

  int counter = 0;

  
void loop() 
{  
String content= "";
for (uint8_t reader = 0; reader < RELAY; reader++) {
    // Look for new cards

    if (mfrc522[reader].PICC_IsNewCardPresent() && mfrc522[reader].PICC_ReadCardSerial()) {
      Serial.print(F("Reader "));
      Serial.print(reader);
      MFRC522::PICC_Type piccType = mfrc522[reader].PICC_GetType(mfrc522[reader].uid.sak);
      Serial.println(mfrc522[reader].PICC_GetTypeName(piccType));

      for (byte i = 0; i < mfrc522[reader].uid.size; i++) 
      {
        Serial.print(mfrc522[reader].uid.uidByte[i] < 0x10 ? " 0" : " ");
        Serial.print(mfrc522[reader].uid.uidByte[i], HEX);
        content.concat(String(mfrc522[reader].uid.uidByte[i] < 0x10 ? " 0" : " "));
        content.concat(String(mfrc522[reader].uid.uidByte[i], HEX));
      }
      content.toUpperCase();
      
      
      
      
      
      if (content.substring(1) == "D7 F0 57 B2") //change here the UID of the card/cards that you want to give access
      {
        if (reader == 0){ counter++; }
        if (reader == 1 && counter > 0){ counter--; }
        
        Serial.println("Authorized access");
        Serial.println();
        delay(500);
        lcd.clear();
        lcd.setCursor(0, 0); 
        lcd.print("Access Authoried");  
        lcd.setCursor(6, 1); 
        lcd.print("^-^");
        digitalWrite(RELAY, HIGH);
        digitalWrite(LED_G, HIGH);
        delay(ACCESS_DELAY);
        digitalWrite(RELAY, LOW);
        digitalWrite(LED_G, LOW);

        lcd.clear();
        lcd.setCursor(1, 0); 
        lcd.print("Scan Your Key");
        lcd.setCursor(6, 1); 
        lcd.print("^-^");
        lcd.setCursor(11, 1); 
        lcd.print(counter);
      }
      else   {
        Serial.println("Access denied");
        lcd.print("Access Denied!");  
        lcd.clear();
        lcd.setCursor(1, 0); 
        lcd.print("Acess Denied!");
        lcd.setCursor(6, 1); 
        lcd.print("*-*");
        digitalWrite(LED_R, HIGH);
        delay(DENIED_DELAY);
        digitalWrite(LED_R, LOW);
        lcd.setCursor(1, 0); 
    
        lcd.clear();
        lcd.setCursor(1, 0); 
        lcd.print("Scan Your Key");
        lcd.setCursor(6, 1); 
        lcd.print("^-^");
        }


        
      // Halt PICC
      mfrc522[reader].PICC_HaltA();
      // Stop encryption on PCD
      mfrc522[reader].PCD_StopCrypto1();
    } //if (mfrc522[reader].PICC_IsNewC
  } //for(uint8_t reader

}


 /**
 * Helper routine to dump a byte array as hex values to Serial.
 */
void dump_byte_array(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i], HEX);
  }
}
