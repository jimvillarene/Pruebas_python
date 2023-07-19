#programa para que el usuario adivine el numero que estoy pensando
import random
print("Hola, cuál es tu nombre")
nombre=input()
print("Hola, "+nombre+". Estoy pensando en un numero entre el 1 y el 10, ¿Puedes adivinar cál es")
numero=input()
magicNum=random.randint(0,11)
while numero != magicNum
	if numero < magicNum:
		print("Tu numero está demasiado bajo. Inténtalo otra vez)
		numero=input()
		continue
	elif numero > magicNum:
		print("Tu número está demasiado alto. Inténtalo otra vez")
		numero=input()
	else:
		break
print("Felicidades, diste en el blanco")
		

