#include <ESP8266WiFi.h>
#include "ThingSpeak.h"

// Defina as informações da sua rede Wi-Fi
const char* ssid = "NOME_DO_WIFI";
const char* password = "SENHA_DO_WIFI";

// Defina o número do canal ThingSpeak e a sua chave API de gravação
unsigned long myChannelNumber = YOUR_CHANNEL_ID;
const char* myWriteAPIKey = "YOUR_WRITE_API_KEY";

WiFiClient  client;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  // Aguarda a conexão
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }

  // Conecta ao ThingSpeak
  ThingSpeak.begin(client);
}

void loop() {
  // Simulação de valores de temperatura e umidade
  float temperatura = random(20, 30);
  float umidade = random(50, 80);

  // Envia os dados para o ThingSpeak
  ThingSpeak.setField(1, temperatura);
  ThingSpeak.setField(2, umidade); 2
  
  int resposta = ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey);
  
  if (resposta == 200) {
    Serial.println("Dados enviados com sucesso");
  } else {
    Serial.println("Erro ao enviar os dados: " + String(resposta));
  }
  
  delay(15000);
}
