from automatas import estado
from automatas import automata

def numeros(estado,destino):
    recorrido=[]
    for x in range(0,9):
        numero=[str(x),destino]
        recorrido.append(numero)
    estado.lis+=recorrido

def caracteres(estado,destino):
    recorrido=[]
    for x in range(65,91):
        if x != 69:
            letra=[chr(x),destino]
            recorrido.append(letra)
    for x in range(97,123):
        if x != 101:
            letra=[chr(x),destino]
            recorrido.append(letra)
    estado.lis+=recorrido

def automata1():
    q0=estado([['+',"q1"],['-',"q1"],['.',"np"]],"q0")
    caracteres(q0,"np")
    numeros(q0,"q2")
    q1=estado([['E',"np"],['e',"np"],['.',"np"],['+',"np"],['-',"np"]],"q1")
    numeros(q1,"q2")
    caracteres(q1,"np")
    q2=estado([['.',"q3"],['E',"q5"],['e',"q5"],['+',"q1"],['-',"q1"]],"q2")
    numeros(q2,"q2")
    caracteres(q2,"np")
    q3=estado([['E',"np"],['e',"np"],['.',"np"],['+',"np"],['-',"np"]],"q3")
    numeros(q3,"q4")
    caracteres(q3,"np")
    q4=estado([['E',"q5"],['e',"q5"],['.',"np"],['+',"q1"],['-',"q1"]],"q4")
    numeros(q4,"q4")
    caracteres(q4,"np")
    q5=estado([['E',"np"],['e',"np"],['.',"np"],['+',"q6"],['-',"q6"]],"q5")
    numeros(q5,"q7")
    caracteres(q5,"np")
    q6=estado([['E',"np"],['e',"np"],['.',"np"],['-',"np"],['+',"np"]],"q6")
    numeros(q6,"q7")
    caracteres(q6,"np")
    q7=estado([['.',"np"],['+',"np"],['-',"np"]],"q7")
    numeros(q7,"q7")
    caracteres(q7,"np")
    listEstados=[q0,q1,q2,q3,q4,q5,q6,q7]
    automata1=automata(listEstados)
    listAceptados=["q2","q4","q7"]
    cadena=input("Escribe un numero real: ")
    for ele in cadena:
        automata1.transicion(ele)
    if automata1.nomEstado in listAceptados:
        print("cadena valida") 
    else:
        print("cadena no valida")
        automata1=automata(listEstados)

def automata2():
    q0=estado([[0,"q1"],[1,"q3"]],"q0")
    q1=estado([[0,"q2"],[1,"q4"]],"q1")
    q2=estado([[0,"q1"],[1,"q5"]],"q2")
    q3=estado([[0,"q1"],[1,"np"]],"q3")
    q4=estado([[0,"q2"],[1,"np"]],"q4")
    q5=estado([[0,"q1"],[1,"np"]],"q5")
    listEstados=[q0,q1,q2,q3,q4,q5]
    automata2=automata(listEstados)
    listAceptados=["q2","q5"]
    cadena=input("Escribe tu secuencia: ")
    for ele in cadena:
        automata2.transicion(int(ele))
    if automata2.nomEstado in listAceptados:
        print("cadena valida") 
    else:
        print("cadena no valida")
        automata2=automata(listEstados)

    
def automata3():
    q0=estado([['a',"q1"],['b',"q2"],['c',"q3"]],"q0") 
    q1=estado([['a',"q4"],['b',"q5"],['c',"q6"]],"q1")
    q2=estado([['a',"q7"],['b',"q8"],['c',"q9"]],"q2")
    q3=estado([['a',"q10"],['b',"q11"],['c',"q12"]],"q3")
    q4=estado([['a',"q13"],['b',"q13"],['c',"q13"]],"q4")
    q5=estado([['a',"np"],['b',"q13"],['c',"np"]],"q5")
    q6=estado([['a',"np"],['b',"np"],['c',"q13"]],"q6")
    q7=estado([['a',"q13"],['b',"np"],['c',"np"]],"q7")
    q8=estado([['a',"q13"],['b',"q13"],['c',"q13"]],"q8")
    q9=estado([['a',"np"],['b',"np"],['c',"q13"]],"q9")
    q10=estado([['a',"q13"],['b',"np"],['c',"np"]],"q10")
    q11=estado([['a',"np"],['b',"q13"],['c',"np"]],"q11")
    q12=estado([['a',"q13"],['b',"q13"],['c',"q13"]],"q12")
    q13=estado([['a',"np"],['b',"np"],['c',"np"]],"q13")
    listEstados=[q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13]
    automata3=automata(listEstados)
    listAceptados=["q13"]
    cadena2=input("Escribe tu cadena: ")
    for ele in cadena2:
        automata3.transicion(ele)
    if automata3.nomEstado in listAceptados:
        print("cadena valida") 
    else:
        print("cadena no valida")
        automata3=automata(listEstados)

def vendingMachine():
    q0 = estado()
    q1 = estado()
    q2 = estado()
    q3 = estado()
    q4 = estado()
    q5 = estado()
    q6 = estado()
    q7 = estado()
    q8 = estado()

while True:
    print("""\n\t Menú
    [1]  Numéro real
    [2]  Número par de 0's sin 1's sucesivos
    [3]  Cadenas de longitud 3 bajo {a,b,c}
    [4]  Aplicación AFD
    [5]  Salir""")
    sel=input("\nSeleccione una operación: ")
    if sel=="1":
        print("\n\tNúmero real")
        automata1()
    if sel=="2":
        print("\n\tCadena con 0's pares y sin 1's seguidos ")
        automata2()
    if sel=="3":
        print("\n\tCadena longitud 3 bajo {a,b,c}")
        automata3()
    if sel=="5":
        break
    if sel<"0" or sel>"5":
        print("No ha elegido una opción valida")
    
        

