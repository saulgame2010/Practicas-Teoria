import xlrd

def equiv(sheet, c):
	"""AQUI DECLARO DOS CLASES QUE ME VAN A AYUDAR A GUARDAR LOS ESTADOS QUE CUMPLAN O NO CIERTAS
	CONDICIONES"""
	c2 = []
	c3 = []		
	"""AQUÍ RECORRO LA LISTA C QUE CONTIENE A C0 (QUE SERÍA EN ESTE CASO C[0])
	Y A C1 (QUE SERÍA C[1]"""
	for i in range(len(c)):
	#AQUÍ EMPIEZO A RECORRER LAS LISTAS INTERNAS DE C, ES DECIR C0 Y C1		
		for j in range(len(c[i])):			
			"""AQUI ESPECIFICO QUE SI CUALQUIERA DE LAS CLASES DENTRO DE C
			TIENEN MAS DE UN ELEMENTO, LAS ANALICE, PORQUE LAS QUE TIENEN SOLO 1 YA NO SE
			SIMPLIFICAN MAS"""
			if(len(c[i])>1):
				"""SI SE CUMPLE LA CONDICION, EMPIEZA A ANALIZAR LOS ESTADOS QUE ESTAN EN LA TABLA
				DE TRANSICIÓN COMENZANDO POR LA FILA 1, ES DECIR, EN DONDE EMPIEZAN LOS ESTADOS,
				SI EMPEZARA EN LA FILA 0, ESTARÍA ANALIZANDO LA FILA EN DONDE SE ENCUENTRAN LOS SIMBOLOS
				CON LOS QUE TRABAJA EL AUTÓMATA, ESPERO QUE ME ENTIENDAS"""				
				for f in range(1, sheet.nrows):					
					"""AQUI VERIFICO SI EL ESTADO DE LA TABLA ESTÁ EN LA CLASE QUE SE ESTÁ ANALIZANDO
					AL RECIBIR CUALQUIERA DE LOS DOS SIMBOLOS DEL ALFABETO, ES DECIR, 
					EN LA CLASE QUE ESTOY ANALIZANDO (POR EJEMPLO C1) ESTÁN LOS ELEMENTOS
					C1 = {Q1, Q3, Q4} ENTONCES ANALIZANDO MI TABLA ME ENCUENTRO CON Q0
					SI Q0 AL METERLE UN 0 ME LLEVA AL ESTADO Q1 Y AL METERLE UN 1 ME LLEVA A Q4, ENTONCES
					SÍ CUMPLE PORQUE TANTO Q1 COMO Q4 ESTÁN EN C1. DE ESTO SE ENCARGA ESTA CONDICIÓN
					(SE SUPONE)"""
					if(sheet.cell_value(f, 1) in c[i] and sheet.cell_value(f, 2) in c[i]):							
						#ESTE PRINT NO LO BORRES O TE DA ERROR DE IDENTACION (NO SÉ POR QUÉ)
						print("",end="-")#el valor ", sheet.cell_value(f, 0), " si esta
					#SI NO SE CUMPLE LA CONDICION ANTERIOR, AHORA CHECO QUE EL ESTADO QUE SE ESTÁ ANALIZANDO
					#VAYA A UN ESTADO CON 0 O CON 1, NO CON LOS DOS COMO EN LA CONDICION ANTERIOR
					#POR EJEMPLO, SI A Q0 CON UN 1 SE VA A Q1 PERO CON UN 0 SE VA A Q2, CUMPLE CON ESTA CONDICION
					#PORQUE Q1 SÍ ESTÁ EN C1 PERO Q2 NO LO ESTA, CUANDO PASA ESTO SACO A Q0 DE LA CLASE DONDE ESTÉ
					#Y LO AGREGO A UNA NUEVA
					elif((sheet.cell_value(f, 1) in c[i] and sheet.cell_value(f, 2) not in c[i]) or (sheet.cell_value(f, 1) not in c[i] and sheet.cell_value(f, 2) in c[i])):							
						#LO MISMO DEL ERROR CON ESTE PRINT, NO LO BORRES
						#el valor ", sheet.cell_value(f, 0), " no esta
						for a in c[i]:								
							if(a == sheet.cell_value(f, 0) and sheet.cell_value(f, 0)):
								c2.append(sheet.cell_value(f, 0))
						for a in c[i]:								
							if(a == sheet.cell_value(f, 0)):
								c[i].remove(a)
					#EN ESTE ELSE ES DONDE SE CHECA CUANDO DE PLANO Q0 CON 0 Y Q0 CON 1 ME LLEVAN A ESTADOS QUE NO ESTAN
					#EN C1 Y HACEN LO MISMO QUE EL ELIF ANTERIOR, CREAN UNA NUEVA CLASE, QUITAN AL ESTADO QUE SE 
					#ESTA ANALIZANDO DE LA CLASE DONDE ESTÁ Y LO PONE EN UNA NUEVA CLASE
					else:
						for a in c[i]:								
							if(a == sheet.cell_value(f, 0) and sheet.cell_value(f, 0)):
								c3.append(sheet.cell_value(f, 0))
						for a in c[i]:								
							if(a == sheet.cell_value(f, 0)):
								c[i].remove(a)
	#ESTOS DE AQUI SOLO SON PARA VER QUÉ HAY EN LAS NUEVAS CLASES
	#print(c2)
	#print(c3)
	#print(c)

#AQUI HAGO UNA LISTA C QUE VA A GUARDAR A LAS CLASES C0 Y C1 QUE TAMBIEN SON LISTAS
c = []
c0 = []
c1 = []
#ESTA LINEA LEE UN ARCHIVO DE EXCEL EN LA RUTA ESPECIFICADA, LA CUAL SE PUEDE INGRESAR CON UN INPUT()
#PERO YO LA DEJE ESTABLECIDA POR COMODIDAD
#EN GITHUB YA ESTÁ EL ARCHIVO DE PRUEBA, PERO PUEDES HACER MAS PARA PROBAR OTROS AUTOMATAS
#print("Ingresa la ruta de tu tabla de transición en excel")
#fileP = "C:\\Users\\saulg\\Desktop\\ESCOM\\4° semestre\\Teoría Computacional\\prueba.xlsx" #input()
fileP="C:\\Users\\UlisesJ.000\\Documents\\GitHub\\Practicas-Teoria\\prueba.xlsx"
#ESTA LINEA ABRE EL ARCHIVO EXCEL EN PYTHON PARA PODER LEERLO
openFile = xlrd.open_workbook(fileP)
#ESTA VARIABLE ES LA MAS IMPORTANTE PORQUE ES LA HOJA DE EXCEL QUE VAMOS A ESTAR TRABAJANDO
#ES IMPORTANTE QUE SE PONGA EL NOMBRE DE LA HOJA TAL COMO ESTÁ EN EXCEL
sheet = openFile.sheet_by_name("Hoja1")
#EN ESTE FOR SOLO IMPRIMO LA TABLA
#NROWS ES UNA FUNCION DE LA LIBRERIA XLRD QUE CUENTA LAS FILAS DE LA TABLA QUE TIENE LA HOJA
#EL EQUIVALENTE DE NROWS PARA CONTAR LAS COLUMNAS ES NCOLS
print("Tu tabla de transición es: \n")
for i in range(sheet.nrows):
	#CELL_VALUES RECOGE EL VALOR DE LA CELDA (X, Y) DONDE X ES LA FILA & Y ES LA COLUMNA
	print(sheet.cell_value(i, 0), "   ", sheet.cell_value(i, 1), "   ", sheet.cell_value(i, 2))
print("Cuantos estados de aceptacion hay?: ",end=" ")
nc0 = int(input())
print("\nIndica cuales son: ")
#LOS ESTADOS DE ACEPTACION SE GUARDAN EN LA CLASE C0 Y LOS DEMÁS ESTADOS EN C1
#DE ESO SE ENCARGAN ESTOS DOS FOR
for s in range(0, nc0):
	c0.append(input())
for i in range(sheet.nrows):
	if(sheet.cell_value(i, 0) not in c0):
		if(sheet.cell_value(i, 0) != ''):
			c1.append(sheet.cell_value(i, 0))
#AQUI IMPRIMO LAS CLASES C0 Y C1 PARA VERIFICAR QUE SE GUARDARON BIEN
print("\nC0 = ", c0)
print("C1 = ", c1)
#AQUI GUARDO LAS LISTAS C0 Y C1 EN C
c.append(c0)
c.append(c1)
print("C = ", c)
"""AQUI MANDO A LLAMAR A LA FUNCION EQUIV QUE HACE LA MINIMIZACION
EL PROBLEMA CON ESTA FUNCION ES QUE ESTA PUEDE IR GENERANDO TANTAS CLASES COMO SEAN NECESARIAS
POR LO QUE NO SUPE COMO HACERLA RECURSIVA Y QUE SEPA CUANDO PARAR DE HACER CLASES Y CONCLUIR LA FUNCION
AQUI RECOMIENDO QUE YA SEPAS BIEN QUE ONDA CON LA MINIMIZACIÓN DE LOS AFD, POR LO MISMO DE QUE NO SÉ
CUANDO HACER QUE PARE, LA MANDO A LLAMAR DOS VECES PARA QUE HAGA SU TRABAJO DOS VECES Y GENERE LAS CLASES
EN DOS VUELTAS, PERO ESO NO SIGNIFICA QUE HAYA GENERADO LAS SUFICIENTES"""
equiv(sheet, c)	
equiv(sheet, c)
"""EN LAS SIGUIENTES LINEAS IMPRIMO LAS CLASES RESULTANTES"""
print("\nLas clases resultantes del automata minimizado son:")
for i in range(len(c)):
	if c[i]:
		print("C",i, "= ", c[i], "\n")