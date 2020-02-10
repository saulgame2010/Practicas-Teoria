import re
import random
alfabeto1 = []
alfabeto2 = []

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

def leer_cadena(alfabeto, cadena):	
	#En este ciclo for, x va a tomar como valor todos los elementos del alfabeto
	for x in alfabeto:
		#Aqui se revisa que x esté en la cadena
		#si es así, se va a reemplazar ese caracter por un caracter cualquiera
		#los argumetos de la funcion replace son: el caracter a sustituir, el caracter sustituto y 
		#el numero de veces que se va a reemplazar (este último argumento es opcional)
		if(x in cadena):
			cadena = cadena.replace(x, "")
	if(cadena == ""):
		return True
	else:		
		return False


def elevar_cadena(n, cadena1, cadena2):
	if n == 0:
		return ""
	#La funcion abs nos devuelve el valor absoluto del numero que tiene como parámetro	
	cadena3 = (cadena1+cadena2)*(abs(n))	
	if n < 0:
		return cadena3[::-1]	
	else:
		return cadena3
def letra(x, cadena1):
	#La funcion count() nos devuelve el numero de veces que aparece un caracter o una palabra en una cadena 
	if(x in cadena1):
		return "El numero de veces que aparece la letra " + str(x) + " es de " + str(cadena1.count(x)) + " veces"
	else:
		return "Esa letra no se encuentra en la cadena"
def comparar(cadena1,cadena2):
	if cadena1 in cadena2:
		if cadena1==cadena2 or cadena1=="":
			print(cadena1,"es un prefijo, sufijo y subcadena de",cadena2)
		elif cadena2.startswith(cadena1):
			print(cadena1,"es prefijo propio de",cadena2)
		elif cadena2.endswith(cadena1):
			print(cadena1,"es un sufijo de",cadena2)
		if cadena1 in cadena2 and cadena1!="" and cadena1!=cadena2:
			print(cadena1,"es subcadena propia de",cadena2)
	else:
		verificar=[]
		for leer in cadena1:
			verificar.append(cadena2.find(leer))
		if -1 in verificar:
			print(cadena1,"no es subsecuencia",cadena2)
		else:
			print(cadena1,"es subsecuencia",cadena2)

def palindromo(palabra):
	aux=palabra[::-1]
	if palabra==aux:
		print("W3 al reves es: "+aux+"\nEs un palindromo")
	else:
		print("W3 al reves es: "+aux+"\nNo es un palindromo")
def elevaralf(n,alfabeto,base):
    if n==0:
        print("")
        return
    if n>1:
        for palabra in alfabeto:
            elevaralf((n-1),alfabeto,palabra +str(base))
    
    else:
        for palabra in alfabeto:
            print(base + str(palabra),end=",")
def palabrasal(num1,num2,num3,num4,num5,num6):
	print("Para Σ1")
	for num1 in range(0,num1):
		print(random.choice(alfabeto1),end="")
	print()
	for num2 in range(0,num2):
		print(random.choice(alfabeto1),end="")
	print()
	for num3 in range(0,num3):
		print(random.choice(alfabeto1),end="")
	print("\n\nPara Σ2")
	for num4 in range(0,num4):
		print(random.choice(alfabeto2),end="")
	print()
	for num5 in range(0,num5):
		print(random.choice(alfabeto2),end="")
	print()
	for num6 in range(0,num6):
		print(random.choice(alfabeto2),end="")
#(a)
print("\tIngresa el alfabeto Σ1:")
alf(alfabeto1)
#(b)
print("\tIngresa el alfabeto Σ2")
alf(alfabeto2)		
#(c)
while True:
	cadena1 = input("Ingresa la cadena w1 con caracteres validos para el alfabeto Σ1\n")
	if(leer_cadena(alfabeto1, cadena1)):
		break
	else:
		print("La cadena es invalida")
while True:		
	cadena2 = input("\nIngresa la cadena w2 con caracteres validos para el alfabeto Σ1\n")
	if(leer_cadena(alfabeto1, cadena2)):
		break
	else:
		print("La cadena es invalida")
#(d)
print("\nPara (w1w2)^n elija un exponente entero positivo o negativo para n")
n = int(input())
print(elevar_cadena(n, cadena1, cadena2))
#(e)
while True:	
	print("\nPara |w1|x elija un simbolo para x")
	x = input()
	print(letra(x, cadena1))
	break
#(f)
print("\nComparacion de w1 y w2")
comparar(cadena1,cadena2)
#(g)
cadena3=input("\nEscribir W3: ")
palindromo(cadena3)
#(h)
print("\nPara Σ1^n elija un exponente entero positivo mayor a 0")
while True:
    potencia = input("Ingresar el valor de n: ")
    try:
        potencia=int(potencia)
        if potencia > 0:
            break
    except ValueError:
        print("Entrada incorrecta")
elevaralf(potencia,alfabeto1,"")
#(i)
print("\n\nGenerando 3 palabras aleatorias")
num1=int(input("Caracteres palabra 1 de Σ1: "))
num2=int(input("Caracteres palabra 2 de Σ1: "))
num3=int(input("Caracteres palabra 3 de Σ1: "))
num4=int(input("Caracteres palabra 1 de Σ2: "))
num5=int(input("Caracteres palabra 2 de Σ2: "))
num6=int(input("Caracteres palabra 3 de Σ2: "))
palabrasal(num1,num2,num3,num4,num5,num6)