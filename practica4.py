import xlrd

c0 = []
c1 = []
#print("Ingresa la ruta de tu tabla de transición en excel")
fileP = "C:\\Users\\saulg\\Desktop\\ESCOM\\4° semestre\\Teoría Computacional\\prueba.xlsx" #input()
openFile = xlrd.open_workbook(fileP)
sheet = openFile.sheet_by_name("Hoja1")
print("Tu tabla de transición es: \n")
for i in range(sheet.nrows):
	print(sheet.cell_value(i, 0), "   ", sheet.cell_value(i, 1), "   ", sheet.cell_value(i, 2))
print("Indica los estados de aceptacion")
c0.append(input())
for i in range(sheet.nrows):
	if(sheet.cell_value(i, 0) not in c0):
		c1.append(sheet.cell_value(i, 0))
print(c0)
print(c1)