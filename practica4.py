import xlrd

tabla = []
alfabeto = []
states = []
c0 = set()
c1 = set()
cn = set()
c = []
b = []
print("Ingresa el numero de elementos de tu alfabeto\n")
numE = int(input())
print("Ingresa los simbolos de tu alfabeto\n")
for i in range(0, numE):
	alfabeto.append(input())
print("Escribe el numero de estados de tu automata\n")
nstates = int(input())
print("Ingresa los estados de tu automata\n")
for s in range(0, nstates):
	states.append(input())
print("Cuantos estados de aceptacion hay?\n")
nc0 = int(input())
print("Indica cuales son\n")
for s in range(0, nc0):
	c0.add(input())
for j in states:
	if(j not in c0):
		c1.add(j)
ck = list(c0)
cj = list(c1)
c.append(ck)
c.append(cj)
for i in range(0, nstates):
	tabla.append([0]*numE)
print("Introduce la tabla de transicion del AFD")
for f in range(0, nstates):
	for col in range(0, numE):
		print("Estado ",states[f]," simbolo ",alfabeto[col])
		tabla[f][col] = input()


"""while True:
	if(nc0 == 1 and len(cj) > 1):
		for f in range(0, len(cj)):
			for col in range(0, numE):
				if(tabla[f][col] in cj):					
					cn.add(tabla[f][col])
					cj.remove(tabla[f][col])
	elif(nc0 > 1 and len(cj) == 1):
		for f in range(0, len(ck)):
			for col in range(0, numE):
				if(tabla[f][col] in ck):					
					cn.add(tabla[f][col])
					ck.remove(tabla[f][col])
	cm = list(cn)
	c = [ck, cj, cm]
	break"""				
#print(tabla)
print(c)