## Programa para controlar la mini TV
# Inicia apagada. Presionar boton cambia entre encendido y apagado
# (solo activa y descativa retroiluminacion de pantalla y salida de sonido)
# Deberia tener funcion para apagar rasp

#libs
import RPi.GPIO as GPIO
import time
import os
#import subprocess as sp

#pins
BOTON = 26
LUZ = 16

os.system('raspi-gpio set 19 ip')
GPIO.setmode(GPIO.BCM)
GPIO.setup(BOTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LUZ, GPIO.OUT)

def turnOnScreen():
  os.system('raspi-gpio set 19 op a5')
  #os.system('raspi-gpio set 13 op a0')
  GPIO.output(LUZ, GPIO.HIGH)


def turnOffScreen():
  os.system('raspi-gpio set 19 ip')
  #os.system('raspi-gpio set 13 ip')
  GPIO.output(LUZ, GPIO.LOW)

turnOffScreen()
screen_on = False #estado de la pantalla
input_prev = GPIO.input(BOTON) #True cuando no esta presionado el boton
#cont = 0 #contador de ciclos
#N = 20

while (True):
  # If you are having and issue with the button doing the opposite of what you want
  # IE Turns on when it should be off, change this line to:
  # input = not GPIO.input(26)

  input = GPIO.input(BOTON)

  #si boton presionado
  if input == GPIO.LOW and input_prev == GPIO.HIGH:
    screen_on = not screen_on

    if screen_on:
      turnOnScreen()
    else:
      turnOffScreen()

  input_prev = input
  time.sleep(0.2)
