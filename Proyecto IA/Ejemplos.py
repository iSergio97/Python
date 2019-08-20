tamHor = int(input("Introduzca el tamaño horizontal: "))
tamVer = int(input("Introduzca el tamaño vertical: "))
fila = []
mapa = []
for i in range(tamHor):
    for j in range(tamVer):
        a = input("El coste de la posición (" + str(i) + ", " + str(j) + "):")
        b = int(a)
        fila.append(b)
    mapa.append(fila)
    fila = []


for i in range(tamHor):
    for j in range(tamVer):
        print(mapa[i][j])
