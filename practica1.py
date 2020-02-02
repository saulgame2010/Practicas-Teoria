import re
alfabeto1 = []
alfabeto2 = []

def alf(alfa):	
	while True:
		print("Como quieres ingresar tu alfabeto?\n1.-Por extension\n2.-Por rango")
		op = input()
		if(op == "1"):
			print("De cuantos elementos va a ser? (debe tener al menos 3 elementos)\n")
			numE = int(input())
			if(numE < 3):
				print("Deben ser al menos 3 elementos\n")			
			else:
				for x in range(0, int(numE)):
					print("Simbolo #", str(x + 1), ": ")
					alfa.append(input())
				print("El alfabeto contiene los siguientes simbolos: " + str(alfa) + "\n")
				break
		elif(op == "2"):
			char1 = input("Ingresa el primer elemento\n")
			char2 = input("Ingresa el ultimo elemento\n")
			if (ord(char1) > ord(char2)):
				print("El orden en que ingresaste los elementos es invalido\n")
			elif((ord(char2)-ord(char1)) < 2):
				print("El alfabeto debe tener al menos 3 simbolos")			
			else:
				for x in range(ord(char1), ord(char2)+1):
					alfa.append(chr(x)) 
				print("El alfabeto contiene los siguientes simbolos: " + str(alfa) + "\n")
				break
def leer_cadena(alfabeto, cadena):
	cont = 0
	for x in alfabeto:		
		if(str(x) in str(cadena)):			
			cont = cont + cadena.count(x)	
	if cont == len(cadena):
		return True
	else: 
		return False

def elevar_cadena(n, cadena1, cadena2):
	if n == 0:
		return ""
	cadena3 = (cadena1+cadena2)*(abs(n))
	if n < 0:
		return cadena3[::-1]	
	else:
		return cadena3
def letra(x, cadena1):
	if(x in cadena1):
		return "El numero de veces que aparece la letra " + str(x) + "es de " + str(cadena1.count(x)) + " veces"
	else:
		return "Esa letra no se encuentra en la cadena"
#(a)
print("Ingresa el alfabeto Σ1:\n")
alf(alfabeto1)
#(b)
print("Ingresa el alfabeto Σ2\n")
alf(alfabeto2)		
#(c)
while True:
	cadena1 = input("Ingresa la cadena w1 con caracteres validos para el alfabeto Σ1\n")
	if(leer_cadena(alfabeto1, cadena1)):
		break
	else:
		print("La cadena es invalida")
while True:		
	cadena2 = input("Ingresa la cadena w2 con caracteres calidos para el alfabeto Σ1\n")
	if(leer_cadena(alfabeto1, cadena2)):
		break
	else:
		print("La cadena es invalida")
#(d)
print("Para (w1w2)^n elija un exponente entero positivo o negativo para n")
n = int(input())
print(elevar_cadena(n, cadena1, cadena2))
#(e)
while True:	
	print("Para |w1|x elija un simbolo para x")
	x = input()
	print(letra(x, cadena1))