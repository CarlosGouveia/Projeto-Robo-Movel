#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time
import cv2

#Função para mover o robô para frente
def Mover_Frente():
	
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor3A,GPIO.HIGH)
    GPIO.output(Motor3B,GPIO.LOW)
    
    GPIO.output(Motor2,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor4A,GPIO.HIGH)
    GPIO.output(Motor4B,GPIO.LOW)

#Função para mover o robô para trás
def Mover_Tras():
	
    GPIO.output(Motor1,GPIO.HIGH)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    
    GPIO.output(Motor3,GPIO.HIGH)
    GPIO.output(Motor3A,GPIO.LOW)
    GPIO.output(Motor3B,GPIO.HIGH)
	
    GPIO.output(Motor2,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    
    GPIO.output(Motor4,GPIO.HIGH)
    GPIO.output(Motor4A,GPIO.LOW)
    GPIO.output(Motor4B,GPIO.HIGH)

def Mover_Esquerda():
	
	GPIO.output(Motor1,GPIO.HIGH)
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	
	GPIO.output(Motor3,GPIO.HIGH)
	GPIO.output(Motor3A,GPIO.HIGH)
	GPIO.output(Motor3B,GPIO.LOW)
	
	GPIO.output(Motor2,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	
	GPIO.output(Motor4,GPIO.HIGH)
	GPIO.output(Motor4A,GPIO.LOW)
	GPIO.output(Motor4B,GPIO.HIGH)

def Mover_Direita():
	
	GPIO.output(Motor1,GPIO.HIGH)
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	
	GPIO.output(Motor3,GPIO.HIGH)
	GPIO.output(Motor3A,GPIO.LOW)
	GPIO.output(Motor3B,GPIO.HIGH)
	
	GPIO.output(Motor2,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	
	GPIO.output(Motor4,GPIO.HIGH)
	GPIO.output(Motor4A,GPIO.HIGH)
	GPIO.output(Motor4B,GPIO.LOW)

def Parar():
	GPIO.output(Motor1,GPIO.LOW)
	GPIO.output(Motor3,GPIO.LOW)
	GPIO.output(Motor2,GPIO.LOW)
	GPIO.output(Motor4,GPIO.LOW)

#Configuração das variáveis nos pinos do GPIO

Motor1 = 36
Motor1A = 38
Motor1B = 40

Motor3 = 33
Motor3A = 35
Motor3B = 37

Motor2 = 11
Motor2A = 13
Motor2B = 15

Motor4 = 29
Motor4A = 31
Motor4B = 32

#Configuração GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)

GPIO.setup(Motor3,GPIO.OUT)
GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)

GPIO.setup(Motor2,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)

GPIO.setup(Motor4,GPIO.OUT)
GPIO.setup(Motor4A,GPIO.OUT)
GPIO.setup(Motor4B,GPIO.OUT)

#Inicia a captura de vídeo
captura = cv2.VideoCapture(0)
 
while(1):
	ret, frame = captura.read()
       
	cv2.imshow('Visao frontal do robô',frame)

	tecla = cv2.waitKey(30) & 0xff
	
	if tecla == 82: #tecla 'seta cima' = para frente
		Mover_Frente()
		
	elif tecla == 84: #tecla 'seta abaixo' = para trás
		Mover_Tras()

	elif tecla == 83: #tecla 'seta direita' = para direita
		Mover_Direita()
		time.sleep(0.3)
		Parar()

	elif tecla == 81: #tecla 'seta esquerda' = para esquerda
		Mover_Esquerda()
		time.sleep(0.3)
		Parar()

	elif tecla == 80: #tecla P = parar
		Parar()

	elif tecla == 27: #tecla ESC = sair
		Parar()
		break

GPIO.cleanup() 
captura.release()
cv2.destroyAllWindows()
