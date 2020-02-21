import random
from posixpath import join
import itertools

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
def union_len(leng1,leng2):
	aux=leng1+leng2
	resultado=[]
	for aux2 in aux:
		if aux2 not in resultado:
			resultado.append(aux2)
	print("Lu es: ",str(resultado))
def concalen(len1,len2):
	conca = []
	for aux1 in len1:
		for aux2 in len2:
			aux3=aux1+aux2
			if aux3 not in conca:
				conca.append(aux3)
	print("Lc es: ",str(conca))
def restalen(len1,len2):
	resta = []
	resta2 = []
	for palabra in len1:
		if palabra not in len2:
			resta.append(palabra)
	for palabra in len2:
		if palabra not in len1:
			resta2.append(palabra)
	print("Ld1 es: ",str(resta))
	print("Ld2 es: ",str(resta2))

#a
alf(alfabeto)
#b
print("\t---Lenguaje 1---")
defleng(lenguaje1)
print("\n\t---Lenguaje 2---")
defleng(lenguaje2)
#c
print("\n\t---Union de L1 y L2---")
union_len(lenguaje1,lenguaje2)
#d
print("\n\t---Concatenación de L1 y L2---")
concalen(lenguaje1,lenguaje2)
#e
print("\n\t---Diferencia de lenguajes---")
restalen(lenguaje1,lenguaje2)
