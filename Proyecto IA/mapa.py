import problema_espacio_estados as probee
import búsqueda_espacio_estados as búsqee
from PIL import Image

#Inicio de clase
def classMap():
    class Mapa:
        def __init__(self, celdas):
            self.celdas = celdas

        def tamaño_hor(self):
            return len(self.celdas[0])

        def tamaño_ver(self):
            return len(self.celdas)

        def tipo_celda(self, f, c):
            return self.celdas[f][c]

    # Fin de clase

    mapa_ejemplo = Mapa([[1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                         [1, 1, 1, 1, 2, 2, 2, 0, 0, 1],
                         [1, 1, 1, 2, 2, 4, 2, 2, 1, 1],
                         [1, 1, 1, 2, 4, 4, 4, 2, 1, 1],
                         [1, 1, 1, 2, 2, 4, 0, 0, 0, 0],
                         [1, 1, 1, 1, 2, 2, 0, 0, 0, 0]])

    #Al seleccionar la casilla inicial, se lee de arriba hacia abajo y de izquierda a derecha.
    #einicial = (5,0) # Casilla 5-0
    #efinal = (5,0)
    print("\033[94m")
    xinicial = input("Introduce the x value (your position to begin)")
    yinicial = input("Introduce the y value (your position to begin)")
    xfinal = input("Introduce the x value (the x goal position)")
    yfinal = input("Introduce the x value (the y goal position)")
    inicial = False
    final = False
    try:
        xinicialn = int(xinicial)
        yinicialn = int(yinicial)
        xfinaln = int(xfinal)
        yfinaln = int(yfinal)
        inicial = True
        final = True
        einicial = (int(xinicial), int(yinicial))
        efinal = (int(xfinal), int(yfinal))

    except ValueError:
        print("\x1b[1;31;41m")
        print("\x1b[1;31;48m Wops! Se ha encontrado una excepción en la introducción de valores. Se le va a pedir introducir los números de nuevo")
        print("\x1b[1;31;41m")
        print("\033[0m")


    if(inicial and final):
        # Acción "Moverse a la derecha"
        def aplicabilidadMoveRight(estado):
            return estado[1] < mapa_ejemplo.tamaño_hor() - 1 and mapa_ejemplo.tipo_celda(estado[0], estado[1] + 1) != 0

        def aplicarMRight(estado):
            return estado[0], estado[1] + 1

        def coste(estado):
            return mapa_ejemplo.tipo_celda(estado[0], estado[1])

        moverDerecha = probee.Acción("Mover a la derecha", aplicabilidadMoveRight, aplicarMRight, coste)

        # Acción "Moverse a la izquierda"
        def aplicabilidadMoveLeft(estado):
            # Como se hace a la izquierda, se cambia el + por el -
            return estado[1] > 0 and mapa_ejemplo.tipo_celda(estado[0], estado[1] - 1) != 0

        def aplicarMLeft(estado):
            return estado[0], estado[1] - 1

        moverIzquierda = probee.Acción("Mover a la izquierda", aplicabilidadMoveLeft, aplicarMLeft, coste)

        # Acción "Moverse hacia abajo"
        def aplicabilidadMoveDown(estado):
            return estado[0] < mapa_ejemplo.tamaño_ver() - 1 and mapa_ejemplo.tipo_celda(estado[0] + 1, estado[1]) != 0

        def aplicarMDown(estado):
            return estado[0] + 1, estado[1]

        moverAbajo = probee.Acción("Mover hacia abajo", aplicabilidadMoveDown, aplicarMDown, coste)

        # Acción "Moverse hacia arriba"
        def aplicabilidadMoveUp(estado):
            return estado[0] > 0 and mapa_ejemplo.tipo_celda(estado[0] - 1, estado[1]) != 0

        def aplicarMUp(estado):
            return estado[0] - 1, estado[1]

        moverArriba = probee.Acción("Mover hacia arriba", aplicabilidadMoveUp, aplicarMUp, coste)

        # Definir el problema de espacio de estados

        problema = probee.ProblemaEspacioEstados([moverDerecha, moverIzquierda, moverArriba, moverAbajo], einicial,
                                                 [efinal])

        print("b_optima_nueva.buscar[problema]")
        b_optima_nueva = búsqee.BúsquedaÓptima()
        print("\n")
        print("b_optima_nueva.buscar[problema]")
        print(b_optima_nueva.buscar(problema))
        print("\n")


bool = True
i = 0
while bool:
    if i == 0:
        i= i + 1
        image = Image.open("mapa.png")
        image.show()
        classMap()
    else:
        continuar = input("¿Desea probar otras posiciones para la resolución del mapa? (S/N)")
        if continuar == "S":
            classMap()
        elif continuar == "N":
            bool = False
            break