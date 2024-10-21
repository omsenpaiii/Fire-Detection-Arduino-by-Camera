// Include necessary libraries
#define BUZZER_PIN 12  // Define the pin where the buzzer is connected

String inputString;

void setup()
{
  pinMode(BUZZER_PIN, OUTPUT);  // Set buzzer pin as output
  Serial.begin(9600);
}

void loop()
{
  while (Serial.available())
  {
    inputString = Serial.readStringUntil('\r');
    Serial.println(inputString);

    // Check if the received signal is '1' for face detected
    if (inputString == "1") {
      digitalWrite(BUZZER_PIN, HIGH);  // Turn on the buzzer
      delay(1000);                      // Buzzer duration (1 second)
      digitalWrite(BUZZER_PIN, LOW);   // Turn off the buzzer
    }

    // Additional parsing for coordinates can be ignored
    // if you no longer need to control servos
  }
}
