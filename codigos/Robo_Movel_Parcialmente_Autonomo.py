#-*-coding:utf-8-*-
import RPi.GPIO as GPIO
import time
import cv2
import cv2.cv as cv

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

def CalculaDistancia():
	# Variáveis para auxiliar no controle do loop principal
	# sampling_rate: taxa de amostragem em Hz, isto é, em média,
	#   quantas leituras do sonar serão feitas por segundo
	# speed_of_sound: velocidade do som no ar a 30ºC em m/s
	# max_distance: máxima distância permitida para medição
	# max_delta_t: um valor máximo para a variável delta_t,
	#   baseado na distância máxima max_distance
	sampling_rate = 20.0
	speed_of_sound = 349.10
	max_distance = 4.0
	max_delta_t = max_distance / speed_of_sound

	# Define TRIG como saída digital
	# Define ECHO como entrada digital
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

	# Inicializa TRIG em nível lógico baixo
	GPIO.output(TRIG, False)
	time.sleep(1)

	# Gera um pulso de 10ms em TRIG.
	# Essa ação vai resultar na transmissão de ondas ultrassônicas pelo
	# transmissor do módulo sonar.
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	# Atualiza a variável start_t enquanto ECHO está em nível lógico baixo.
	# Quando ECHO trocar de estado, start_t manterá seu valor, marcando
	# o momento da borda de subida de ECHO. Este é o momento em que as ondas
	# sonoras acabaram de ser enviadas pelo transmissor.
	while GPIO.input(ECHO) == 0:
		start_t = time.time()

	# Atualiza a variável end_t enquando ECHO está em alto. Quando ECHO
	# voltar ao nível baixo, end_t vai manter seu valor, marcando o tempo
	# da borda de descida de ECHO, ou o momento em que as ondas refletidas
	# por um objeto foram captadas pelo receptor. Caso o intervalo de tempo
	# seja maior que max_delta_t, o loop de espera também será interrompido.
	while GPIO.input(ECHO) == 1 and time.time() - start_t < max_delta_t:
		end_t = time.time()

	# Se a diferença entre end_t e start_t estiver dentro dos limites impostos,
	# atualizamos a variável delta_t e calculamos a distância até um obstáculo.
	# Caso o valor de delta_t não esteja nos limites determinados definimos a
	# distância como -1, sinalizando uma medida mal-sucedida.
	if end_t - start_t < max_delta_t:
		delta_t = end_t - start_t
		distance = 100*(0.5 * delta_t * speed_of_sound)
	else:
		distance = -1

	# Imprime o valor da distância arredondado para duas casas decimais
	print (round(distance, 2))

	# Um pequeno delay para manter a média da taxa de amostragem
	time.sleep(1/sampling_rate)
	
	return distance
	

#Configuração das variáveis nos pinos GPIO

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

#pinos do sensor de distancia
ECHO = 16
TRIG = 18

# Velocidade do som 340,29 m/s -&gt; 34029 cm/s
SPEED_OF_SOUND = 34029

#Configuração do GPIO

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

#inicia a captura de video
captura = cv2.VideoCapture(1)


while(1):
	
	ret, frame = captura.read()
	
	cv2.imshow('Visao frontal do robô',frame)
	
	tecla = cv2.waitKey(15) & 0xff
	
	if tecla == 27: #tecla ESC = sair
		break
	
	print ('DISTANCIA INICIAL:')
	distancia = CalculaDistancia()
	
	if distancia >= 20:
		Mover_Frente()
		time.sleep(2)
		Parar()
	
	elif distancia < 20:
		Mover_Tras()
		time.sleep(1)
		Parar()
		
		Mover_Direita()
		time.sleep(1)
		Parar()
		print ('DISTANCIA DIREITA:')
		distanciaDireita = CalculaDistancia()
		
		Mover_Esquerda()
		time.sleep(2)
		Parar()
		print ('DISTANCIA ESQUERDA:')
		distanciaEsquerda = CalculaDistancia()
		
		if distanciaDireita >= 20 and distanciaEsquerda >= 20:
			if distanciaDireita > distanciaEsquerda:
				Mover_Direita()
				time.sleep(2)
				Parar()
				
				Mover_Frente()
				time.sleep(2)
				Parar()
				
			else:
				Mover_Tras()
				time.sleep(2)
				Parar()
				
		elif distanciaDireita >= 20 and distanciaEsquerda < 20:
			Mover_Direita()
			time.sleep(2)
			Parar()
				
			Mover_Frente()
			time.sleep(2)
			Parar()
			
		elif distanciaEsquerda >= 20 and distanciaDireita < 20:	
			Mover_Frente()
			time.sleep(2)
			Parar()
			
		elif distanciaDireita < 20 and distanciaEsquerda < 20:
			Mover_Esquerda()
			time.sleep(1)
			Parar()
				
			Mover_Frente()
			time.sleep(2)
			Parar()
	
GPIO.cleanup()
captura.release()
cv2.destroyAllWindows() 
