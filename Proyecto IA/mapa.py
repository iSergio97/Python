import problema_espacio_estados as probee
import búsqueda_espacio_estados as búsqee
from PIL import Image

#Inicio de clase
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

print("\nTamaño horizontal")
print(mapa_ejemplo.tamaño_hor())

print("\nTamaño vertical")
print(mapa_ejemplo.tamaño_ver())

def classMap(mapa):
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
    einicial = []
    efinal = []
    try:
        xinicial = int(xinicial)
        yinicial = int(yinicial)
        xfinal = int(xfinal)
        yfinal = int(yfinal)
        inicial = True
        final = True
        einicial = (int(xinicial), int(yinicial))
        efinal = (int(xfinal), int(yfinal))

        if (xinicial > int(mapa_ejemplo.tamaño_hor())) or (xinicial < 0) or (xfinal > mapa_ejemplo.tamaño_hor()) or (
                xfinal < 0) or (yinicial > mapa_ejemplo.tamaño_hor()) or (yinicial < 0) or (
                yfinal > mapa_ejemplo.tamaño_hor()) or (yfinal < 0):
            print("\x1b[1;31;41m")
            print("\x1b[1;31;48m Se han introducido valores que se encuentran fuera del mapa y se va a terminar la ejecución")
            print("\x1b[1;31;41m")
            exit()

    except ValueError:
        print("\x1b[1;31;41m")
        print("\x1b[1;31;48m Wops! Se ha encontrado una excepción en la introducción de valores. El proceso ha cancelado la ejecución")
        print("\x1b[1;31;41m")
        print("\033[0m")
        # exit()


    if(inicial and final):
        # Acción "Moverse a la derecha"
        def aplicabilidadMoveRight(estado):
            return estado[1] < mapa.tamaño_hor() - 1 and mapa_ejemplo.tipo_celda(estado[0], estado[1] + 1) != 0

        def aplicarMRight(estado):
            return estado[0], estado[1] + 1

        def coste(estado):
            return mapa.tipo_celda(estado[0], estado[1])

        moverDerecha = probee.Acción("Mover a la derecha", aplicabilidadMoveRight, aplicarMRight, coste)

        # Acción "Moverse a la izquierda"
        def aplicabilidadMoveLeft(estado):
            # Como se hace a la izquierda, se cambia el + por el -
            return estado[1] > 0 and mapa.tipo_celda(estado[0], estado[1] - 1) != 0

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
