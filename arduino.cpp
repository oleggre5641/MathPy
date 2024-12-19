#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

#define LED_PIN D1  // Пин для управления светодиодом
const char* ssid = "iPhone SHKET";
const char* password = "12345123";
const char* botToken = "7667889910:AAF8e6Ofty1KFUz1rRfKwEvuX5lhBEE6-vs"; // токен вашего бота

WiFiClientSecure client;
UniversalTelegramBot bot(botToken, client);

unsigned long lastTimeBotRan;  // Для проверки новых сообщений
const int botRequestDelay = 1000; // Интервал опроса в миллисекундах

bool ledState = false; // Текущее состояние светодиода

void handleNewMessages(int numNewMessages) {
  for (int i = 0; i < numNewMessages; i++) {
    String chat_id = bot.messages[i].chat_id;
    String text = bot.messages[i].text;

    if (text == "/off") {
      ledState = true;
      digitalWrite(LED_PIN, HIGH);
      bot.sendMessage(chat_id, "Светодиод выключен!", "");
    } else if (text == "/on") {
      ledState = false;
      digitalWrite(LED_PIN, LOW);
      bot.sendMessage(chat_id, "Светодиод включен!", "");
    } else if (text == "/morze"){
      ledState = true;
      digitalWrite(LED_PIN, LOW);
      delay(500);
      digitalWrite(LED_PIN, HIGH);
      delay(500);
      digitalWrite(LED_PIN, LOW);
      delay(500);
      digitalWrite(LED_PIN, HIGH);
      delay(500);
      digitalWrite(LED_PIN, HIGH);
      delay(500);
      digitalWrite(LED_PIN, LOW);
      delay(500);
      digitalWrite(LED_PIN, HIGH);
      delay(500);
      digitalWrite(LED_PIN, HIGH);
      delay(500);
      digitalWrite(LED_PIN, LOW);
      delay(500);
      digitalWrite(LED_PIN, HIGH);
      bot.sendMessage(chat_id, "Светодиод мигает!", "");
    } else {
      bot.sendMessage(chat_id, "Неизвестная команда. Используйте /on или /off.", "");
    }
  }
}

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  Serial.begin(115200);
  WiFi.begin(ssid, password);

  Serial.print("Подключение к Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nПодключено к Wi-Fi!");
  Serial.print("IP-адрес: ");
  Serial.println(WiFi.localIP());

  client.setInsecure(); // Отключение проверки сертификатов
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Потеряно соединение с Wi-Fi. Переподключение...");
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    Serial.println("\nWi-Fi подключено!");
  }

  if (millis() - lastTimeBotRan > botRequestDelay) {
    int numNewMessages = bot.getUpdates(bot.last_message_received + 1);
    while (numNewMessages) {
      handleNewMessages(numNewMessages);
      numNewMessages = bot.getUpdates(bot.last_message_received + 1);
    }
    lastTimeBotRan = millis();
  }
}
