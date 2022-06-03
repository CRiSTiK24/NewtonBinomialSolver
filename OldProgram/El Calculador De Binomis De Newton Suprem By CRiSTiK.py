from math import *
def combinacio(n,k):
	return int(factorial(n)/(factorial(k)*factorial(n-k)))

potencia = int(input("Inserta la potencia de el binomi: "))
yo = int(input("Inserta el primer terme: "))
xo =  int(input("Inserta el segon terme: "))
fila_preguntada = potencia

def pascal(files):
	resultat = []
	#aquí es on es la llista on es guarda el resultat
	for count in range(files):
		#conta les integres de 0 fins a files-1 i per cada loop dona el valor de count, ex:nº files = 3, fa un loop pel num 0, i pel 1 i el 2
		fila = []
		#una altra llista
		for element in range(count+1):
		#conta les integres de 0 fins a count+1 i ho guarda com a valor de element, ex: files = 3, 1r loop on count és 0, aqui li suma 1, llavors li dona que element és 0, pel 2n loop, element es 1, 3r loop 2
			fila.append(combinacio(count,element))
			#li afageix a la fila la combinacio de count i element, ex: count= 0, element = 0, count = 1, element = 1,count= 2, element = 2, llavors fila seria [1,2,1]
	resultat.append(fila)
	#afageix el resultat de fila a resultat
	return resultat

def agafar_la_llista():
	for fila in pascal(fila_preguntada):
	#busca la variable fila fent la variable pascal amb l'argument fila_preguntada.
		return fila

def fer_la_potencia_de_X():
	llista_x = []
	for x in range(potencia):
		xp = xo**x
		llista_x.append(xp)
	return llista_x

def fer_la_potencia_de_Y():
	llista_y = []
	for y in range((potencia-1),-1,-1 ):
		yp = yo**y
		llista_y.append(yp)
	return llista_y

def resposta_final():
	pascal = agafar_la_llista()
	X = fer_la_potencia_de_X()
	Y = fer_la_potencia_de_Y()
	resultat_final = []
	for m in range(potencia):
		k = pascal[m] * X[m] * Y[m]
		resultat_final.append(k)
	print (resultat_final)



resposta_final()
	
