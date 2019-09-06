from mapa import Mapa, classMap
#from PIL import Image

# image = Image.open("mapa.png")
# image.show()

mapa_ejemplo = Mapa([[1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                         [1, 1, 1, 1, 2, 2, 2, 0, 0, 1],
                         [1, 1, 1, 2, 2, 4, 2, 2, 1, 1],
                         [1, 1, 1, 2, 4, 4, 4, 2, 1, 1],
                         [1, 1, 1, 2, 2, 4, 0, 0, 0, 0],
                         [1, 1, 1, 1, 2, 2, 0, 0, 0, 0]])




print("\033[94m")

try:
    elección = int(input(
        "Elija si quiere elegir el mapa de ejemplo (introduzca el valor 1) o introducir uno a mano (introduzca cualquier otro valor)"))
except ValueError:
    print("Se ha introducido un valor erróneo. El proceso va a terminar su ejecución")
    exit()

if(elección == 1):
    fila = []
    mapa = []
    tamHor = int(input("Introduzca el tamaño horizontal del mapa"))
    tamVer = int(input("Introduzca vertical"))
    for _ in range(tamHor):
        for _ in range(tamVer):
            a = input("Introduzca valores")
            b = int(a)
            fila.append(b)
        print(fila)
        mapa.append(fila)
        fila = []

    mapa_ayuda = Mapa(mapa)

    classMap(mapa_ayuda)
else:
    classMap(mapa_ejemplo)

    # classMap(mapa_ejemplo)

# print("Pre coloreado")
# print("\033[0;31;40m Red exception")
# print("\033[0;31;41m Red exception")
# print("\033[0;31;42m Red exception")
# print("\033[0;31;43m Red exception")
# print("\033[0;31;44m Red exception")
# print("\033[0;31;45m Red exception")
# print("\033[0;31;46m Red exception")
# print("\033[0;31;47m Red exception")
# print("\033[94m Color especial")
# print("\033[0m")
# print("Post coloreado")


#