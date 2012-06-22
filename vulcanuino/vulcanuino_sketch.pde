#define COMMENCE_FIRING '1'
#define CEASE_FIRE '0'
#define COMMAND_PAUSE '.'

#define FIRING_PIN 11
#define LIGHT_PIN 13

void setup() {
  Serial.begin(9600);
  pinMode(LIGHT_PIN, OUTPUT);
  pinMode(FIRING_PIN, OUTPUT);
  digitalWrite(LIGHT_PIN, HIGH);
  delay(1000);
  digitalWrite(LIGHT_PIN, LOW);
}

void loop() {
    int command = Serial.read();
    if (command >= 0) {
      switch(command) {
        case COMMENCE_FIRING:
          digitalWrite(FIRING_PIN, HIGH);
          break;
        case CEASE_FIRE:
          digitalWrite(FIRING_PIN, LOW);
          break;
        case COMMAND_PAUSE:
          delay(50);
          break;
      }
    } else {
      delay(25);
    }
}
