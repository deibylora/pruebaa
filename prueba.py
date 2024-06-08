a = int(input("Ingresa un numero: "))
b = int(input("Ingresa otro numero: "))
n = [a, b]

while True:
    
    mas_numeros = input("Quiere ingresar mas numeros? yes/no:\n")
    if mas_numeros == "yes":
        x = int(input("Ingresa otro numero: "))
        n.append(x)
    elif mas_numeros == "no":
        break

cantidad_numeros = len(n)
try:
    print ((a + b + x) / cantidad_numeros)
except:
    print ((a + b) / cantidad_numeros)