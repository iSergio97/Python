import problema_espacio_estados as probee
import búsqueda_espacio_estados as búsqee
import math
import datetime

print(datetime.datetime.now())

# Comienzo de clase
class Mapa:
    def __init__(self, paredes_v, paredes_h, estado_inicial):
        self.paredes_v = paredes_v
        self.paredes_h = paredes_h
        self.estado_inicial = estado_inicial

    def tamano_hor(self):
        return len(self.paredes_v)

    def tamano_ver(self):
        return len(self.paredes_h)

    def tipo_celda_arr(self, f, c):
        return 0 if self.paredes_h[f - 1].__contains__(self, c) else 1

    def tipo_celda_aba(self, f, c):
        return 0 if self.paredes_h[f].__contains__(self, c) else 1

    def tipo_celda_izq(self, f, c):
        return 0 if self.paredes_v[c - 1].__contains__(self, f) else 1

    def tipo_celda_der(self, f, c):
        return 0 if self.paredes_v[c].__contains__(self, f) else 1

    def estado_inicial(self):
        return self.estado_inicial
# Fin de clase


paredes_ver = ([],
               [1],
               [1],
               [1],
               [],
               [])

paredes_hor = ([1],
               [],
               [],
               [],
               [],
               [])

# Estados inicial y final:
estadoInicial = (5, 3,
                 2, 1, 0)
estadoFinal = (3, 7)

mapa_ejemplo = Mapa(paredes_ver, paredes_hor, estadoInicial)


# Acciones:
    # Moverse a la derecha:
def aplicabilidad_mov_der(estado):
    return estado[1] + 1 == estadoFinal[1] or \
           (estado[1] < mapa_ejemplo.tamano_hor() - 1
            and mapa_ejemplo.tipo_celda_der(estado[0], estado[1]) != 0)


def aplicar_mov_der(estado):
    return estado[0], estado[1] + 1, estado[2], estado[3] if (estado[0] == estadoFinal[0]
                                                              and estado[1] + 1 == estadoFinal[1]) \
        else estado[0], estado[1], moverMonstruo(estado[0], estado[1] + 1, estado)


# Coste:
# Modificar a coste variable en función de la acción tomada (el movimiento lo mata directamente por trampa o zombie)
def coste(estado):
    coste = 1
    #  W T F ? !
    if aplicar_mov_der(estado[1]) and \
            (posicionZombie(estado[1] + 1) or posicionTrampa(estado[1] + 1) or (math.pow(abs(estado[0] - estado[2]), 2) + math.pow(abs(estado[1] - estado[3]), 2)) < math.sqrt(2)):
        coste = 100000
    return coste


moverDerecha = probee.Acción("Mover a la derecha", aplicabilidad_mov_der, aplicar_mov_der, coste)


# Moverse a la izquierda:
def aplicabilidad_mov_izq(estado):
    return estado[1] - 1 == estadoFinal[1] or \
           (estado[1] > -1
            and mapa_ejemplo.tipo_celda_izq(estado[0], estado[1]) != 0)


def aplicar_mov_izq(estado):
    return estado[0], estado[1] - 1, estado[2], estado[3] if (estado[0] == estadoFinal[0]
                                                              and estado[1] + 1 == estadoFinal[1])\
        else estado[0], estado[1] - 1, moverMonstruo(estado[0], estado[1] - 1, estado)


def coste(estado):
    coste = 1
    if aplicar_mov_izq(estado[0]) and \
            (posicionZombie(estado[0], estado[1] - 1) or posicionTrampa(estado[0], estado[1] - 1) or (math.pow(abs(estado[0] - estado[2]), 2) + math.pow(abs(estado[1] - 1 - estado[3]), 2)) < math.sqrt(2)):
        coste = 100000
    return coste


moverIzquierda = probee.Acción("Mover a la izquierda", aplicabilidad_mov_izq, aplicar_mov_izq, coste)


# Moverse hacia abajo:
def aplicabilidad_mov_aba(estado):
    return estado[0] + 1 == estadoFinal[0] or \
           (estado[0] < mapa_ejemplo.tamano_ver() - 1
            and mapa_ejemplo.tipo_celda_aba(estado[0], estado[1]) != 0)


def aplicar_mov_aba(estado):
    return estado[0] + 1, estado[1], estado[2], estado[3] if (estado[0] + 1 == estadoFinal[0]
                                                              and estado[1] == estadoFinal[1]) \
        else estado[0] + 1, estado[1], moverMonstruo(estado[0] + 1, estado[1], estado)


def coste(estado):
    coste = 1
    if aplicar_mov_aba(estado[0]) and (posicionZombie(estado[0] + 1, estado[1]) or posicionTrampa(estado[0] + 1, estado[1]) or (math.pow(abs(estado[0] + 1 - estado[2]), 2) + math.pow(abs(estado[1] - estado[3]), 2)) < math.sqrt(2)):
        coste = 100000
    return coste


moverAbajo = probee.Acción("Mover hacia abajo", aplicabilidad_mov_aba, aplicar_mov_aba, coste)


# Moverse hacia arriba:
def aplicabilidad_mov_arr(estado):
    return estado[0] - 1 == estadoFinal[0] or \
           (estado[0] > -1
            and mapa_ejemplo.tipo_celda_arr(estado[0], estado[1]) != 0)


def aplicar_mov_arr(estado):
    return estado[0] - 1, estado[1], estado[2], estado[3] if (estado[0] - 1 == estadoFinal[0]
                                                              and estado[1] == estadoFinal[1]) \
        else estado[0] - 1, estado[1], moverMonstruo(estado[0] - 1, estado[1], estado)


def coste(estado):
    coste = 1
    if aplicar_mov_aba(estado[0]) and (posicionZombie(estado[0] - 1, estado[1]) or posicionTrampa(estado[0] - 1, estado[1]) or (math.pow(abs(estado[0] - 1 - estado[2]), 2) + math.pow(abs(estado[1] - estado[3]), 2)) < math.sqrt(2)):
        coste = 100000
    return coste


moverArriba = probee.Acción("Mover hacia arriba", aplicabilidad_mov_arr, aplicar_mov_arr, coste)

# La parte de si está en su fila o en su columna se puede dejar como está


# Falta por comprobar en cada movimiento si está bloqueado por pared o por trampa y si el movimiento + 1 o + 2 lo mete en una trampa
def moverMonstruo(f, c, estado):
    # Si estamos en su casilla
    if f == estado[2] and c == estado[3]:
        # No se mueve
        return estado[2], estado[3]
    # Si estamos en su fila
    elif f == estado[2]:
        # Y estamos un paso a su derecha
        if c + 1 == estado[3]:
            # Se mueve un paso a la derecha de ser posible
            return estado[2], estado[3] + 1 \
                if mapa_ejemplo.tipo_celda_der(estado[2], estado[3] + 1) != 0 else estado[2], estado[3]
        # Si estamos dos o más pasos a su derecha
        elif c + 1 < estado[3]:
            # Se mueve dos pasos a su derecha de ser posible
            if mapa_ejemplo.tipo_celda_der(estado[2], estado[3] + 2) != 0 \
                    and mapa_ejemplo.tipo_celda_der(estado[2], estado[3] + 2) != 0:
                return estado[2], estado[3]
            # Si no uno y si no ninguno
            else:
                return estado[2], estado[3] + 1 \
                    if mapa_ejemplo.tipo_celda_der(estado[2], estado[3]) != 0 else estado[2], estado[3]
        # Si por el contrario estamos un paso a su izquierda
        elif c - 1 == estado[3]:
            # Se mueve un paso a la izquierda de ser posible
            return estado[2], estado[3] - 1 \
                if mapa_ejemplo.tipo_celda_izq(estado[2], estado[3] - 1) != 0 else estado[2], estado[3]
        # Si estamos dos o más pasos a su izquierda
        else:
            # Se mueve dos pasos a su izquierda de ser posible
            if mapa_ejemplo.tipo_celda_izq(estado[2], estado[3] - 2) != 0 \
                    and mapa_ejemplo.tipo_celda_izq(estado[2], estado[3] - 1) != 0:
                return estado[2], estado[3]
            # Si no uno y si no ninguno
            else:
                return estado[2], estado[3] - 1 \
                    if mapa_ejemplo.tipo_celda_izq(estado[2], estado[3] - 1) != 0 else estado[2], estado[3]
    # Si estamos en su columna
    elif c == estado[3]:
        # Y estamos un paso debajo de él
        if f + 1 == estado[2]:
            # Se mueve hacia abajo de ser posible
            return estado[2] + 1, estado[3] \
                if mapa_ejemplo.tipo_celda_aba(estado[2], estado[3]) != 0 else estado[2], estado[3]
        # Si estamos dos o más pasos debajo de él
        elif f + 1 < estado[2]:
            # Se mueve dos pasos hacia abajo de ser posible
            if mapa_ejemplo.tipo_celda_aba(estado[2] + 1, estado[3]) != 0 \
                    and mapa_ejemplo.tipo_celda_aba(estado[2] + 2, estado[3]) != 0:
                return estado[2] + 2, estado[3]
            # Si no uno y si no ninguno
            else:
                return estado[2] + 1, estado[3] \
                    if mapa_ejemplo.tipo_celda_aba(estado[2], estado[3]) != 0 else estado[2], estado[3]
        # Si por el contrario estamos un paso encima de él
        elif f - 1 < estado[2]:
            # Se mueve un paso hacia arriba de ser posible
            return estado[2] - 1, estado[3] \
                if mapa_ejemplo.tipo_celda_arr(estado[2] - 1, estado[3]) != 0 else estado[2], estado[3]
        # Si estamos dos o más pasos encima de él
        else:
            # Se mueve dos pasos hacia arriba de ser posible
            if mapa_ejemplo.tipo_celda_arr(estado[2] - 2, estado[3]) != 0 \
                    and mapa_ejemplo.tipo_celda_arr(estado[2], estado[3] - 1) != 0:
                return estado[2] - 2, estado[3]
            # Si no uno y si no ninguno
            else:
                return estado[2] - 1, estado[3] \
                    if mapa_ejemplo.tipo_celda_arr(estado[2], estado[3]) != 0 else estado[2], estado[3]
    # Si no estamos ni en su fila ni en su columna
    else:
        # Si estamos a su derecha
        if f < estado[2]:
            # Se mueve dos pasos a su derecha de ser posible
            if mapa_ejemplo.tipo_celda_der(estado[2], estado[3] + 2) != 0 \
                    and mapa_ejemplo.tipo_celda_der(estado[2], estado[3] + 1) != 0:
                return estado[2], estado[3] + 2
            # Si no uno
            elif mapa_ejemplo.tipo_celda_der(estado[2], estado[3] + 1) != 0:
                return estado[2], estado[3] + 1
            # Y si no, se mueve verticalmente
            else:
                # Si estamos debajo de él
                if c < estado[3]:
                    # Se mueve dos pasos hacia abajo de ser posible
                    if mapa_ejemplo.tipo_celda_aba(estado[2] + 2, estado[3]) != 0 \
                            and mapa_ejemplo.tipo_celda_aba(estado[2] + 2, estado[3]) != 0:
                        return estado[2] + 2, estado[3]
                    # Si no uno y si no ninguno
                    else:
                        return estado[2] + 1, estado[3] \
                            if mapa_ejemplo.tipo_celda_aba(estado[2] + 1, estado[3]) != 0 \
                            else estado[2], estado[3]
                # Si estamos encima de él
                else:
                    # Se mueve dos pasos hacia arriba de ser posible
                    if mapa_ejemplo.tipo_celda_arr(estado[2] - 2, estado[3]) != 0 \
                            and mapa_ejemplo.tipo_celda_arr(estado[2] - 2, estado[3] - 1) != 0:
                        return estado[2] - 2, estado[3]
                    # Si no uno y si no ninguno
                    else:
                        return estado[2] - 1, estado[3] \
                            if mapa_ejemplo.tipo_celda_arr(estado[2] - 1, estado[3]) != 0\
                            else estado[2], estado[3]
        # Si por el contrario estamos a su izquierda
        else:
            # Se mueve dos pasos a su izquierda de ser posible
            if mapa_ejemplo.tipo_celda_izq(estado[2], estado[3] - 2) != 0 \
                    and mapa_ejemplo.tipo_celda_izq(estado[2], estado[3] - 2) != 0:
                return estado[2], estado[3] - 2
            # Si no uno y si no ninguno
            elif mapa_ejemplo.tipo_celda_izq(estado[2], estado[3] - 1) != 0:
                return estado[2], estado[3]
            # Y si no, se mueve verticalmente
            else:
                # Si estamos debajo de él
                if c < estado[3]:
                    # Se mueve dos pasos hacia abajo de ser posible
                    if mapa_ejemplo.tipo_celda_aba(estado[2] + 2, estado[3]) != 0 \
                            and mapa_ejemplo.tipo_celda_aba(estado[2] + 2, estado[3]) != 0:
                        return estado[2] + 2, estado[3]
                    # Si no uno y si no ninguno
                    else:
                        return estado[2] + 1, estado[3] \
                            if mapa_ejemplo.tipo_celda_aba(estado[2] + 1, estado[3]) != 0 \
                            else estado[2], estado[3]
                # Si estamos encima de él
                else:
                    # Se mueve dos pasos hacia arriba de ser posible
                    if mapa_ejemplo.tipo_celda_arr(estado[2] - 2, estado[3]) != 0 \
                            and mapa_ejemplo.tipo_celda_arr(estado[2] - 2, estado[3] - 1) != 0:
                        return estado[2] - 2, estado[3]
                    # Si no uno y si no ninguno
                    else:
                        return estado[2] - 1, estado[3] \
                            if mapa_ejemplo.tipo_celda_arr(estado[2] - 1, estado[3]) != 0 \
                            else estado[2], estado[3]


# Definir el problema

print("\nEntra a probee.")
problema = probee.ProblemaEspacioEstados([moverDerecha, moverIzquierda, moverAbajo, moverArriba],
                                         estadoInicial, estadoFinal)
print("\nSale de probee.")
bOptima = búsqee.BúsquedaÓptima()
print("\nSale de asignación bOptima")
print(bOptima.buscar(problema))


print("\nCarga la heurística")


def h(nodo):
    estado = nodo.estado
    return abs(estado[0] - estadoFinal[0]) + abs(estado[1] - estadoFinal[1])


print('\nSale de la heurística')
print('\nEntra a b_a_estrella')
b_a_estrella = búsqee.BúsquedaAEstrella(h)
print("\nSale de b_a_estrella")

print("\nEntra el print b_a_estrella.buscar")
print(b_a_estrella.buscar(mapa_ejemplo))
print("\nSale del print de b_a_estrella.buscar")
