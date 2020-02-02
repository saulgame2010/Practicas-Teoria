import re
import random
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
	break
#(g)
cadena3=input("Escribir W3: ")
palindromo(cadena3)
#(h)
print("Para Σ1^n elija un exponente entero positivo mayor a 0")
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
print("\nGenerando 3 palabras aleatorias")
num1=int(input("Caracteres palabra 1 de Σ1: "))
num2=int(input("Caracteres palabra 2 de Σ1: "))
num3=int(input("Caracteres palabra 3 de Σ1: "))
num4=int(input("Caracteres palabra 1 de Σ2: "))
num5=int(input("Caracteres palabra 2 de Σ2: "))
num6=int(input("Caracteres palabra 3 de Σ2: "))
palabrasal(num1,num2,num3,num4,num5,num6)