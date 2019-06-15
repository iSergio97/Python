import problema_espacio_estados as probee
import búsqueda_espacio_estados as búsqee
import copy

# Comienzo de clase

class Mapa:
    def __init__(self, paredes_v, paredes_h):
        self.paredes_v = paredes_v
        self.paredes_h = paredes_h

    #El len del tamaño horizontal no debería ser tamaño de las paredes - 1 en vez de + 1?
    def tamano_hor(self):
        return len(self.paredes_v) + 1

    #Lo mismo con las paredes verticales
    def tamano_ver(self):
        return len(self.tamano_h) + 1

    def tipo_celda_arr(self, f, c):
        return 0 if paredes_h[f - 1].__contains__(self, c) else 1

    def tipo_celda_aba(self, f, c):
        return 0 if paredes_h[f].__contains__(self, c) else 1

    def tipo_celda_izq(self, f, c):
        return 0 if paredes_v[c - 1].__contains__(self, f) else 1

    def tipo_celda_der(self, f, c):
        return 0 if paredes_v[c].__contains__(self, f) else 1


# Fin de clase

paredes_ver = [[],
               [1],
               [1],
               [1],
               [],
               []]

paredes_hor = [[1],
               [],
               [],
               [],
               [],
               []]

mapa_ejemplo = Mapa(paredes_ver, paredes_hor)

# Estados inicial y final:
# Supongo que esto de estado inicial y final corresponde con el primer nivel, ¿no?
estadoInicial = [[5, 3],
                 [2, 1]]
estadoFinal = [3, 7]


# Coste:
# Aquí no habría que comprobar cuánto debe de ser el coste si avanza hacia el zombie o trampa? Y, si avanza
# hacia delante, sí es de coste 1.
def coste(estado):
    return 1


# Acciones:
    # Moverse a la derecha:
def aplicabilidad_mov_der(estado):
    return estado[0[1]] + 1 == estadoFinal[0[1]] or \
           (estado[0[1]] < mapa_ejemplo.tamano_hor() - 1
            and mapa_ejemplo.tipo_celda_der(estado[0[0]], estado[0[1]]) != 0)


def aplicar_mov_der(estado):
    return estado[0[0]], estado[0[1]] + 1, estado[1[0]], estado[1[1]] if (estado[0[0]] == estadoFinal[0[0]]
                                           and estado[0[1]] + 1 == estadoFinal[0[1]]) \
        else estado[0[0]], estado[0[1]]


moverDerecha = probee.Acción("Mover a la derecha", aplicabilidad_mov_der, aplicar_mov_der, coste)


    # Moverse a la izquierda:
def aplicabilidad_mov_izq(estado):
    return estado[0[1]] - 1 == estadoFinal[0[1]] or \
           (estado[0[1]] > -1
            and mapa_ejemplo.tipo_celda_izq(estado[0[0]], estado[0[1]]) != 0)


def aplicar_mov_izq(estado):
    return estado[0[0]], estado[0[1]] - 1, estado[1[0]], estado[1[1]] if (estado[0[0]] == estadoFinal[0[0]]
                                              and estado[0[1]] + 1 == estadoFinal[0[1]])\
        else estado[0[0]], estado[0[1]] - 1


moverIzquierda = probee.Acción("Mover a la izquierda", aplicabilidad_mov_izq, aplicar_mov_izq, coste)


    # Moverse hacia abajo:
def aplicabilidad_mov_aba(estado):
    return estado[0[0]] + 1 == estadoFinal[0[0]] or \
           (estado[0[0]] < mapa_ejemplo.tamano_ver() - 1
            and mapa_ejemplo.tipo_celda_aba(estado[0[0]], estado[0[1]]) != 0)


def aplicar_mov_aba(estado):
    return estado[0[0]] + 1, estado[0[1]], estado[1[0]], estado[1[1]] if (estado[0[0]] + 1 == estadoFinal[0[0]]
                                           and estado[0[1]] == estadoFinal[0[1]]) \
        else estado[0[0]] + 1, estado[0[1]]


moverAbajo = probee.Acción("Mover hacia abajo", aplicabilidad_mov_aba, aplicar_mov_aba, coste)


    # Moverse hacia arriba:
def aplicabilidad_mov_arr(estado):
    return estado[0[0]] - 1 == estadoFinal[0[0]] or \
           (estado[0[0]] > -1
            and mapa_ejemplo.tipo_celda(estado[0[0]], estado[0[1]]) != 0)


def aplicar_mov_arr(estado):
    return estado[0[0]] - 1, estado[0[1]], estado[1[0]], estado[1[1]] if (estado[0[0]] - 1 == estadoFinal[0[0]]
                                              and estado[0[1]] == estadoFinal[0[1]]) \
        else estado[0[0]] - 1, estado[0[1]], moverMonstruo(estado[0[0]] - 1, estado[0[1]], estado)


moverArriba = probee.Acción("Mover hacia arriba", aplicabilidad_mov_arr, aplicar_mov_arr)


def moverMonstruo(f, c, estado):
    # Si estamos en su casilla
    if f == estado[1[0]] and c == estado[1[1]]:
        # No se mueve
        return estado[1[0]], estado[1[1]]
    # Si estamos en su fila
    elif f == estado[1[0]]:
        # Y estamos un paso a su derecha
        if c + 1 == estado[1[1]]:
            # Se mueve un paso a la derecha de ser posible
            return estado[1[0]], estado [1[1]] + 1 \
                if mapa_ejemplo.tipo_celda_der(estado[1[0]], estado[1[1]]) != 0 else estado[1[0]], estado [1[1]]
        # Si estamos dos o más pasos a su derecha
        elif c + 1 < estado[1[1]]:
            # Se mueve dos pasos a su derecha de ser posible
            if mapa_ejemplo.tipo_celda_der(estado[1[0]], estado[1[1]]) != 0 \
                    and mapa_ejemplo.tipo_celda_der(estado[1[0]], estado[1[1]] + 1) != 0:
                return estado[1[0]], estado [1[1]] + 2
            # Si no uno y si no ninguno
            else:
                return estado[1[0]], estado [1[1]] + 1 \
                    if mapa_ejemplo.tipo_celda_der(estado[1[0]], estado[1[1]]) != 0 else estado[1[0]], estado [1[1]]
        # Si por el contrario estamos un paso a su izquierda
        elif c - 1 == estado[1[1]]:
            # Se mueve un paso a la izquierda de ser posible
            return estado[1[0]], estado[1[1]] - 1 \
                if mapa_ejemplo.tipo_celda_izq(estado[1[0]], estado[1[1]]) != 0 else estado[1[0]], estado[1[1]]
        # Si estamos dos o más pasos a su izquierda
        else:
            # Se mueve dos pasos a su izquierda de ser posible
            if mapa_ejemplo.tipo_celda_izq(estado[1[0]], estado[1[1]]) != 0 \
                    and mapa_ejemplo.tipo_celda_izq(estado[1[0]], estado[1[1]] - 1) != 0:
                return estado[1[0]], estado[1[1]] - 2
            # Si no uno y si no ninguno
            else:
                return estado[1[0]], estado[1[1]] + - 1 \
                    if mapa_ejemplo.tipo_celda_izq(estado[1[0]], estado[1[1]]) != 0 else estado[1[0]], estado[1[1]]
    # Si estamos en su columna
    elif c == estado[1[1]]:
        # Y estamos un paso debajo de él
        if f + 1 == estado[1[0]]:
            # Se mueve hacia abajo de ser posible
            return estado[1[0]] + 1, estado[1[1]] \
                if mapa_ejemplo.tipo_celda_aba(estado[1[0]], estado[1[1]]) != 0 else estado[1[0]], estado[1[1]]
        # Si estamos dos o más pasos debajo de él
        elif f + 1 < estado[1[0]]:
            # Se mueve dos pasos hacia abajo de ser posible
            if mapa_ejemplo.tipo_celda_aba(estado[1[0]], estado[1[1]]) != 0 \
                    and mapa_ejemplo.tipo_celda_aba(estado[1[0]], estado[1[1]] + 1) != 0:
                return estado[1[0]] + 2, estado[1[1]]
            # Si no uno y si no ninguno
            else:
                return estado[1[0]] + 1, estado[1[1]] \
                    if mapa_ejemplo.tipo_celda_aba(estado[1[0]], estado[1[1]]) != 0 else estado[1[0]], estado[1[1]]
        # Si por el contrario estamos un paso encima de él
        elif f - 1 < estado[1[0]]:
            # Se mueve un paso hacia arriba de ser posible
            return estado[1[0]] - 1, estado[1[1]] \
                if mapa_ejemplo.tipo_celda_arr(estado[1[0]], estado[1[1]]) != 0 else estado[1[0]], estado[1[1]]
        # Si estamos dos o más pasos encima de él
        else:
            # Se mueve dos pasos hacia arriba de ser posible
            if mapa_ejemplo.tipo_celda_arr(estado[1[0]], estado[1[1]]) != 0 \
                    and mapa_ejemplo.tipo_celda_arr(estado[1[0]], estado[1[1]] - 1) != 0:
                return estado[1[0]] - 2, estado[1[1]]
            # Si no uno y si no ninguno
            else:
                return estado[1[0]] - 1, estado[1[1]] \
                    if mapa_ejemplo.tipo_celda_arr(estado[1[0]], estado[1[1]]) != 0 else estado[1[0]], estado[1[1]]
    # Si no estamos ni en su fila ni en su columna
    else:
        # Si estamos a su derecha
        # Como sabes si estamos a su derecha?
        # Lo mismo con el resto de movimientos que no son directos (filas o columnas iguales a la del muñeco)
        if f < estado[1[0]]:
            # Se mueve dos pasos a su derecha de ser posible
            # Aquí no sería mejor comprobar cualquier combinación y que se tome la que más cerca le deje?
            if mapa_ejemplo.tipo_celda_der(estado[1[0]], estado[1[1]]) != 0 \
                    and mapa_ejemplo.tipo_celda_der(estado[1[0]], estado[1[1]] + 1) != 0:
                return estado[1[0]], estado[1[1]] + 2
            # Si no uno
            elif mapa_ejemplo.tipo_celda_der(estado[1[0]], estado[1[1]]) != 0:
                return estado[1[0]], estado[1[1]] + 1
            # Y si no, se mueve verticalmente
            else:
                # Si estamos debajo de él
                if c < estado[1[1]]:
                    # Se mueve dos pasos hacia abajo de ser posible
                    if mapa_ejemplo.tipo_celda_aba(estado[1[0]], estado[1[1]]) != 0 \
                            and mapa_ejemplo.tipo_celda_aba(estado[1[0]], estado[1[1]] + 1) != 0:
                        return estado[1[0]] + 2, estado[1[1]]
                    # Si no uno y si no ninguno
                    else:
                        return estado[1[0]] + 1, estado[1[1]] \
                            if mapa_ejemplo.tipo_celda_aba(estado[1[0]], estado[1[1]]) != 0 \
                            else estado[1[0]], estado[1[1]]
                # Si estamos encima de él
                else:
                    # Se mueve dos pasos hacia arriba de ser posible
                    if mapa_ejemplo.tipo_celda_arr(estado[1[0]], estado[1[1]]) != 0 \
                            and mapa_ejemplo.tipo_celda_arr(estado[1[0]], estado[1[1]] - 1) != 0:
                        return estado[1[0]] - 2, estado[1[1]]
                    # Si no uno y si no ninguno
                    else:
                        return estado[1[0]] - 1, estado[1[1]] \
                            if mapa_ejemplo.tipo_celda_arr(estado[1[0]], estado[1[1]]) != 0\
                            else estado[1[0]], estado[1[1]]
        # Si por el contrario estamos a su izquierda
        else:
            # Se mueve dos pasos a su izquierda de ser posible
            if mapa_ejemplo.tipo_celda_izq(estado[1[0]], estado[1[1]]) != 0 \
                    and mapa_ejemplo.tipo_celda_izq(estado[1[0]], estado[1[1]] - 1) != 0:
                return estado[1[0]], estado[1[1]] - 2
            # Si no uno y si no ninguno
            elif mapa_ejemplo.tipo_celda_izq(estado[1[0]], estado[1[1]]) != 0:
                return estado[1[0]], estado[1[1]] + - 1
            # Y si no, se mueve verticalmente
            else:
                # Si estamos debajo de él
                if c < estado[1[1]]:
                    # Se mueve dos pasos hacia abajo de ser posible
                    if mapa_ejemplo.tipo_celda_aba(estado[1[0]], estado[1[1]]) != 0 \
                            and mapa_ejemplo.tipo_celda_aba(estado[1[0]], estado[1[1]] + 1) != 0:
                        return estado[1[0]] + 2, estado[1[1]]
                    # Si no uno y si no ninguno
                    else:
                        return estado[1[0]] + 1, estado[1[1]] \
                            if mapa_ejemplo.tipo_celda_aba(estado[1[0]], estado[1[1]]) != 0 \
                            else estado[1[0]], estado[1[1]]
                # Si estamos encima de él
                else:
                    # Se mueve dos pasos hacia arriba de ser posible
                    if mapa_ejemplo.tipo_celda_arr(estado[1[0]], estado[1[1]]) != 0 \
                            and mapa_ejemplo.tipo_celda_arr(estado[1[0]], estado[1[1]] - 1) != 0:
                        return estado[1[0]] - 2, estado[1[1]]
                    # Si no uno y si no ninguno
                    else:
                        return estado[1[0]] - 1, estado[1[1]] \
                            if mapa_ejemplo.tipo_celda_arr(estado[1[0]], estado[1[1]]) != 0 \
                            else estado[1[0]], estado[1[1]]


# Definir el problema

problema = probee.ProblemaEspacioEstados([moverDerecha, moverIzquierda, moverAbajo, moverArriba],
                                         estadoInicial, [estadoFinal])

# bOptima = búsqee.BúsquedaÓptima()
# print(bOptima.buscar(problema))

# Este es la heurística, ¿verdad?
# Si es, ¿qué compruebas? ¿Qué esté más cerca de la meta (primer abs) y el segundo abs?
def h(nodo):
    estado = nodo.estado
    return abs(estado[0[0]] - estadoFinal[0]) + abs(estado[0[1]] + estadoFinal[1])


b_a_estrella = búsqee.BúsquedaAEstrella(h)

# %%timeit -n1 -r1
print(b_a_estrella.buscar(mapa_ejemplo))
