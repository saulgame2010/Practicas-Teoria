import random
from posixpath import join
import itertools
import re

alfabeto=[]
lenguaje1=[]
lenguaje2=[]
nombresh=["Ulises","Saul","Rafael","Jaime","Gabriel","Armando","Martin","Daniel"]
nombresm=["Alejandra","Dalila","Mariela","Gabriela","Blanca","Carolina","Monserrat"]
apellidosp=["Juarez","Garcia","Medina","Palacios","Alvarez","Hernandez","Esquivel","Lara","Chavez","Angel"]
apellidosm=["Espinoza","Pantoja","Doroteo","Castrejon","Lujan","Martinez","Rueda","Martinez","Gutierrez"]
estados= ["AS","BC","BS","CC","CS","CH","CL","CM","DF","DG","GT","GR","HG","JC","MC","MN","MS","NT","NL","OC","PL","QO","QR","SP","SL","SR","TC","TS","TL","VZ","YN","ZS"]
dia=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
mes=["01","02","03","04","05","06","07","08","09","10","11","12"]
digitos=["0","1","2","3","4","5","6","7","8","9"]
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
	num=1
	nump=int(input("Cuantos elementos tendra el lenguaje: "))
	lon=int(input("Longitud de los elementos del lenguaje: "))
	while num<=nump:
		for lon1 in range(0,lon):
			palabra.append(random.choice(alfabeto))
			aux="".join(palabra)
		if aux not in lenguaje:
			lenguaje.append(aux)
			num+=1
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
def elevarlen(n,lenguaje,base):
	if n<0:
		lenguaje=lenguaje[::-1]
		n=n*-1
	if n==0:
		print("")
	if n>1:
		for palabra in lenguaje:
			elevarlen((n-1),lenguaje,palabra +str(base))
	else:
		for palabra in lenguaje:
			print(base + str(palabra),end=" ")

def eleselec():
	print("""\n\t---Elevando lenguaje---
\t   Menú
\t1.- Primer lenguaje
\t2.- Segundo lenguaje""")
	while True:
		numero=(input("Seleccion: "))
		try:
			numero=int(numero)
			if numero==1 or numero==2:
				break
		except ValueError:
			print("No ha seleccionado ningún lenguaje")
	while True:
		potencia = input("Ingresar el valor de la potencia: ")
		try:
			potencia=int(potencia)
			if potencia>=-5 and potencia<=5:
				break
		except ValueError:
			print("Entrada incorrecta")
	if(numero==1):
			elevarlen(potencia,lenguaje1,"")
	if(numero==2):
			elevarlen(potencia,lenguaje2,"")
def curp_ale(): 
	regexVocal = re.compile('a|e|i|o|u|A|E|I|O|U')
	regexConsonante=re.compile('B|C|D|F|G|H|J|K|L|M|N|Ñ|P|Q|R|S|T|V|W|X|Y|Z|b|c|d|f|g|h|j|k|l|m|n|ñ|p|q|r|s|t|v|w|x|y|z')
	nom=random.choice(nombresh)
	nomm=random.choice(nombresm)
	ap=random.choice(apellidosp)
	am=random.choice(apellidosm)
	conap=regexConsonante.findall(ap[1::])[0]
	conam=regexConsonante.findall(am[1::])[0]
	connom=regexConsonante.findall(nom[1::])[0]
	apm=random.choice(apellidosp)
	amm=random.choice(apellidosm)
	conapm=regexConsonante.findall(apm[1::])[0]
	conamm=regexConsonante.findall(amm[1::])[0]
	connomm=regexConsonante.findall(nomm[1::])[0]
	auxaño=[]
	for año in range(1900,2019):
		auxaño.append(str(año))
	curph=ap[0]+regexVocal.findall(ap)[0]+am[0]+nom[0]+random.choice(auxaño)[::-1][0:2][::-1] +random.choice(mes) +random.choice(dia)+"H"+random.choice(estados)+conap+conam+connom+random.choice(digitos)+random.choice(digitos)
	curpm=apm[0]+regexVocal.findall(apm)[0]+amm[0]+nomm[0]+random.choice(auxaño)[::-1][0:2][::-1] +random.choice(mes) +random.choice(dia)+"M"+random.choice(estados)+conapm+conamm+connomm+random.choice(digitos)+random.choice(digitos)
	print("Curp de hombre: ",str(curph.upper()))
	print("Curp de mujer: ",str(curpm.upper()))
	print(str(auxaño))

def java_key_words(palabra):
	regexJava = re.compile('(\\W|^)(abstract|assert|boolean|break|byte|case|catch|char|class|const|continue|default|'+
		'do|double|else|enum|extends|final|finally|float|for|goto|if|implements|import|instanceof|int|interface|long|'+
		'native|new|package|private|protected|public|return|short|static|strictfp|super|switch|synchronized|this|throw|'+
		'throws|transient|try|void|volatile|while|String)(\\W|$)')
	aceptada = regexJava.findall(palabra)
	if aceptada:
		return True
	else:
		return False

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
#f
eleselec()
print("""\nDesea repetir?
	1.-Si
	2.-No""")
validar=int(input("Selección: "))
while validar!=2:
	eleselec()
	print("""\n\nDesea repetir?
	1.-Si
	2.-No""")
	validar=int(input("Selección: "))
#g
	
print("\nGenerando 2 curp aleatorias: ")
curp_ale()
#h
print("\nIngresa una cadena que contenga los identificadores de palabras reservadas de Java")
palabra = input()
x = True
while x:
	if java_key_words(palabra):
		print("Cadena aceptada")
		x = False
	else:
		print("Cadena no aceptada")
		palabra = input("Ingresa de nuevo tu cadena\n")
		java_key_words(palabra)