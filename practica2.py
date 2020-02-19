import random
from posixpath import join

alfabeto=[]
lenguaje1=[]
lenguaje2=[]
def alf(alfa):
	while True:
		print("¿Como quieres ingresar tu alfabeto?\n1.-Por extension\n2.-Por rango")
		op = input("Seleccion: ")
		if(op == "1"):
			print("De cuantos elementos va a ser? (debe tener al menos 3 elementos): ",end="")
			numE = int(input())
			if(numE < 3):
				print("Deben ser al menos 3 elementos\n")			
			else:
				#Lo que hace la función range es es crear una secuencia de números
				#lo hace con los argumentos que recibe, que son (numero de partida, numero hasta donde llegará la secuencia)
				for x in range(0, int(numE)):
					print("Simbolo #", str(x + 1), ": ",end=" ")					
					alfa.append(input())
				print("El alfabeto contiene los siguientes simbolos: " + str(alfa) + "\n")
				break
		elif(op == "2"):
			char1 = input("Ingresa el primer elemento: ")
			char2 = input("Ingresa el ultimo elemento: ")
			#ord() devuelve el unicode del caracter que tenga en su argumento
			#Aquí se verifica que el unicode del primer elemento no sea mayor
			#al del segundo para evitar ingresar un alfabeto no ordenado de forma ascendente
			if (ord(char1) > ord(char2)):
				print("El orden en que ingresaste los elementos es invalido\n")
			#En esta línea hacemos una resta del unicode del primer y segundo elemento para verificar
			#que se estén ingresando 3 o más elementos	
			elif((ord(char2)-ord(char1)) < 2):
				print("El alfabeto debe tener al menos 3 simbolos")			
			else:
				for x in range(ord(char1), ord(char2)+1):
					alfa.append(chr(x)) 
				print("El alfabeto contiene los siguientes simbolos: " + str(alfa) + "\n")
				break
def defleng(lenguaje):
    palabra=[]
    nump=int(input("Cuantos elementos tendra el lenguaje: "))
    lon=int(input("Longitud de los elementos del lenguaje: "))
    for np1 in range(0,nump):
        for lon1 in range(0,lon):
         palabra.append(random.choice(alfabeto))
         aux="".join(palabra)
        lenguaje.append(aux)
        palabra.clear()
    print("El lenguaje contiene los siguientes elementos: ",str(lenguaje))

#1
alf(alfabeto)
#2
print("\t---Lenguaje 1---")
defleng(lenguaje1)
print("\n\t---Lenguaje 2---")
defleng(lenguaje2)