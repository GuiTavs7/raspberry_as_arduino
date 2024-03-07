# Bibliotecas utilizadas

import RPi.GPIO as GPIO # Para utilizar os pinos de GPIO
import time # Para usar o time.sleep

GPIO.setmode(GPIO.BOARD)

pinoLED_1 = 12 # Vamos utilizar o pino 12 da placa

# Define o pino do LED como saída
GPIO.setup(pinoLED_1, GPIO.OUT)

while(1): #Repete esta secao sempre
    GPIO.output(pinoLED_1, True) # Acende o LED
    time.sleep(0.5) # Aguarda meio segundo
    GPIO.output(pinoLED_1, False) # Apaga o LED
    time.sleep(0.5) # Aguarda meio segundo
