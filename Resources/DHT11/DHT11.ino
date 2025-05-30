#include <DHT.h>

#define DHTPIN 2       // Pin donde está conectado el sensor DHT11
#define DHTTYPE DHT11  // Tipo de sensor (DHT11)
#define PIN_MOTOR 8    // Pin del relay del motor de ventilación
#define SWITCH_PIN 7   // Pin de interruptor para activar la ventilación manualmente
#define PIN_UMBRAL_TEMP A0
#define PIN_UMBRAL_HUMEDAD A1

float umbral_humedad = 75;  // Umbral de humedad por defecto
float umbral_temp = 25;     // Umbral de temperatura por defecto

DHT dht(DHTPIN, DHTTYPE);

// Variables para el control del tiempo
unsigned long previousMillis = 0;  // Almacena el último tiempo de lectura
const long interval = 2000;  // Intervalo de tiempo de 2 segundos (sin delay)

void setup() {
  Serial.begin(9600);  // Inicia la comunicación serial a 9600 baudios
  dht.begin();         // Inicia el sensor DHT11
  pinMode(PIN_MOTOR, OUTPUT);
  pinMode(SWITCH_PIN, INPUT_PULLUP);  // Configura el interruptor con resistencia pull-up interna
  digitalWrite(PIN_MOTOR, LOW);  // Asegurarse de que el motor esté apagado al principio
}

void loop() {
  // Comprobar si el interruptor está activado (LOW cuando presionado)
  if (digitalRead(SWITCH_PIN) == LOW) {
    digitalWrite(PIN_MOTOR, HIGH);  // Enciende el motor si el interruptor está presionado
    return;  // Salir de la función loop() si el interruptor está activado
  }

  // Lectura analogica umbral de sensores
  float umbral_temp = map(analogRead(PIN_UMBRAL_TEMP),0,1023,0,100);
  float umbral_humedad = map(analogRead(PIN_UMBRAL_HUMEDAD),0,1023,0,100);
  
  
  // Verifica si el tiempo transcurrido ha pasado el intervalo
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    // Guarda el tiempo actual
    previousMillis = currentMillis;

    float humidity = dht.readHumidity();    // Lee la humedad
    float temperature = dht.readTemperature();  // Lee la temperatura

    // Verifica si la lectura fue exitosa
    if (isnan(humidity) || isnan(temperature)) {
      Serial.println("Fallo al leer el sensor DHT!");
      return;
    }

    // Controla el motor en función de los umbrales de temperatura y humedad
    if (humidity > umbral_humedad || temperature > umbral_temp) {
      digitalWrite(PIN_MOTOR, HIGH);  // Enciende el motor
    } else {
      digitalWrite(PIN_MOTOR, LOW);   // Apaga el motor
    }

    // Envía los datos al puerto serial en formato CSV
    Serial.print(temperature);
    Serial.print(",");
    Serial.print(humidity);
    Serial.print(",");
    Serial.print(umbral_temp);
    Serial.print(",");
    Serial.print(umbral_humedad);
    
  }
}
