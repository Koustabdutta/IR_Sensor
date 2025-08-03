#define S1 32
#define S2 33
#define S3 25
#define S4 26
#define S5 27

void setup() {
  Serial.begin(115200);
  pinMode(S1, INPUT);
  pinMode(S2, INPUT);
  pinMode(S3, INPUT);
  pinMode(S4, INPUT);
  pinMode(S5, INPUT);
}

void loop() {
  int v1 = digitalRead(S1);
  int v2 = digitalRead(S2);
  int v3 = digitalRead(S3);
  int v4 = digitalRead(S4);
  int v5 = digitalRead(S5);

  // Print values in a CSV format for plotting
  Serial.print(v1); Serial.print(",");
  Serial.print(v2); Serial.print(",");
  Serial.print(v3); Serial.print(",");
  Serial.print(v4); Serial.print(",");
  Serial.println(v5);

  delay(1000);
}
