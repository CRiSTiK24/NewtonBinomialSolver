import sympy
import math
print("Benvinguts al Calculador De Binomis De Newton Suprem By CRiSTiK V.2! per respresentar potencies feu-ho aixis: \"x**3\"(x elevat a tres), per representar multiplicacions feu-ho aixis: \"3*x\"(tres per x). Finalment un exemple de polinomi: \"2*x**4\", les incognites acceptades son: \"a,b,c,x,y,z\". Gracies per utilitzar aquest sacre programa, el qual te una mica de utilitat, no com els teoremes de funcions.")
sympy.init_printing()
a,b,c,x,y,z = sympy.symbols('a,b,c,x,y,z')
P1 = input("Inserta Polinomi 1: ")
P2 = input("Inserta Polinomi 2: ")
Pot = int(input("Digues la potencia del binomi: "))
Polinomi_1 = sympy.Poly(P1)
Polinomi_2 = sympy.Poly(P2)
def mult(p1, p2):
    return p1 * p2
def suma(p1, p2):
    return p1 + p2
def res(p1, p2):
    return p1 - p2
def div(p1, p2):
    return p1 / p2
def Resposta():
	while True:
		pregunta = input("Suma o Resta?")
		if pregunta == "Suma":
			return suma(Polinomi_1,Polinomi_2)
			break
		elif pregunta == "Resta":
			return res(Polinomi_1,Polinomi_2)
			break
		else:
			print("Torna i escriu be \"Suma\" o \"Resta\"!")
def fer_la_potencia(base, potencia):
	pr1 = base
	pr2 = base
	for x in range(potencia):
		pr1 = mult(pr1,pr2)
	return pr1

print(fer_la_potencia(Resposta(),Pot))


