#include <Arduino.h>
#include <WiFi.h>
#include <FirebaseESP32.h> // Firebase library for ESP32
#include <DHT.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h> // Library for I2C LCD
LiquidCrystal_I2C lcd(0x27,16,2); // Initialize the LCD display

#define DHTPIN 15
#define DHTTYPE    DHT11
DHT_Unified dht(DHTPIN, DHTTYPE); // Initialize DHT sensor

/* Define the WiFi credentials */
#define WIFI_SSID "PROJECT"
#define WIFI_PASSWORD "123456789"

/* Define Firebase configuration */
#define API_KEY "AIzaSyC5Q-66lWOj5kZCl1q7KvYD9ZO9pecFHkw"
#define DATABASE_URL "https://test-d3894-default-rtdb.firebaseio.com"
#define USER_EMAIL "mutants.400@gmail.com"
#define USER_PASSWORD "Ro9710047880"

// Define Firebase objects
FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;

void setup() {
  Serial.begin(115200);
  lcd.init(); // Initialize the LCD display
  lcd.backlight(); // Turn on the backlight

  // Connect to WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());

  // Initialize Firebase configuration
  config.api_key = API_KEY;
  auth.user.email = USER_EMAIL;
  auth.user.password = USER_PASSWORD;
  config.database_url = DATABASE_URL;
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);

  // Initialize DHT sensor
  dht.begin();
}

void loop() {
  delay(1000);

  // Read temperature and humidity from DHT sensor
  sensors_event_t event;
  dht.temperature().getEvent(&event);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("TEMPERATURE");
  lcd.setCursor(0,1);
  lcd.print(event.temperature);
  
  // Send temperature data to Firebase
  Firebase.setFloat(fbdo, F("/weather/temp"), event.temperature);

  delay(1000);

  dht.humidity().getEvent(&event);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("HUMIDITY");
  lcd.setCursor(0,1);
  lcd.print(event.relative_humidity);
  
  // Send humidity data to Firebase
  Firebase.setFloat(fbdo, F("/weather/hum"), event.relative_humidity);

  delay(1000);

  // Read rain sensor data
  int iVal = analogRead(2);
  
  // Send rain sensor data to Firebase
  Firebase.setInt(fbdo, F("/weather/rain"), iVal);
}
