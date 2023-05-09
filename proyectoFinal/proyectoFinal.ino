#include <NoDelay.h>
#include <NewPing.h>

const unsigned int PIN_TRIGGER = 32;
const unsigned int PIN_ECHO = 27;
const unsigned int PIN_BOTON = 4;
const unsigned int PIN_ZUM = 16;
const int DISTANCIA_MAX = 200;
const int DISTANCIA_ALERTA = 15;
const unsigned int BAUD_RATE = 115200;
const int FRECUENCIA = 2000;
const int CANAL_PWM = 0;
const int RESOLUCION = 8;
const long PAUSA = 1000;

typedef enum {
  ALARMA_ARMADA,
  ALARMA_SONANDO,
  ALARMA_DESARMADA
} estadoAlarma;

estadoAlarma edoAlarma;
noDelay pausa(PAUSA);
NewPing sonar(PIN_TRIGGER, PIN_ECHO, DISTANCIA_MAX);

int obtenDistancia();
void suenaAlarma();
void IRAM_ATTR desarmaAlarma();

void setup() {
  Serial.begin(BAUD_RATE);

  ledcSetup(CANAL_PWM, FRECUENCIA, RESOLUCION);
  ledcAttachPin(PIN_ZUM, CANAL_PWM);
  ledcWrite(CANAL_PWM, 127);

  pinMode(PIN_BOTON, INPUT);
  attachInterrupt(PIN_BOTON, desarmaAlarma, FALLING);

  edoAlarma = ALARMA_ARMADA;
  ledcWriteTone(CANAL_PWM, 0);
  delay(5000);
}

void loop() {
  if (pausa.update()) {
    int distancia = obtenDistancia();

    switch (edoAlarma) {
      case ALARMA_ARMADA:
        if (distancia <= DISTANCIA_ALERTA) {
          Serial.println("Alarma encendida");
          suenaAlarma();
        }
        break;
      case ALARMA_SONANDO:
        break;
      case ALARMA_DESARMADA:
        edoAlarma = ALARMA_ARMADA;
        break;
    }
  }
}

int obtenDistancia() {
  int uS = sonar.ping_median();
  int distancia = sonar.convert_cm(uS);
  return distancia;
}

void suenaAlarma() {
  edoAlarma = ALARMA_SONANDO;
  ledcWriteTone(CANAL_PWM, 1000);
}

void IRAM_ATTR desarmaAlarma() {
  if (edoAlarma == ALARMA_SONANDO) {
    Serial.println("Alarma desarmada");
    edoAlarma = ALARMA_DESARMADA;
    ledcWriteTone(CANAL_PWM, 0);
    delay(5000);
  }
}
