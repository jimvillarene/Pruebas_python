#programa para que el usuario adivine el numero que estoy pensando
import random
print("Hola, cuál es tu nombre")
nombre=input()
print("Hola, "+nombre+". Estoy pensando en un numero entre el 1 y el 10, ¿Puedes adivinar cuál es")
numero=0
magicNum=random.randint(1,11)
intentos=1
while numero != magicNum and intentos < 7:
    print("Intenta adivinar")
    numero=int(input())
    if numero < magicNum:
        print("Tu numero está demasiado bajo. Inténtalo otra vez")
        intentos+=1
        continue
    elif numero > magicNum:
        print("Tu número está demasiado alto. Inténtalo otra vez")
        intentos+=1
    else:
        break
if numero == magicNum:
    print("Felicidades, diste en el blanco después de "+str(intentos)+" intentos")
else:
	print("Lo siento no diste en el blanco. El número era: "+str(magicNum))		
