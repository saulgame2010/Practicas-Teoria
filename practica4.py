tabla = []
alfabeto = []
states = []
c0 = set()
c1 = set()
c = []
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
c.append(c0)
c.append(c1)
for i in range(0, nstates):
	tabla.append([0]*numE)
print(tabla)
print("Introduce la tabla de transicion del AFD")
for f in range(0, nstates):
	for col in range(0, numE):
		print("Estado ",states[f]," simbolo ",alfabeto[col])
		tabla[f][col] = input()

print(tabla)
print(c)