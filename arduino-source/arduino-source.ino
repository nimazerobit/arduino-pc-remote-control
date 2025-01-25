#include <IRremote.h>
#define RECEIVER_PIN 4
IRrecv receiver(RECEIVER_PIN);
decode_results results;

void setup() {
  receiver.enableIRIn();
  receiver.blink13(true);
  Serial.begin(9600);
}

void loop() {
  if (receiver.decode(&results)) {
    Serial.println(results.value, HEX);
    receiver.resume();
  }

  delay(50);
}