import problema_espacio_estados as probee
import búsqueda_espacio_estados as búsqee
import copy


# Comienzo de clase
class Mapa:
    def __init__(self, paredes_v, paredes_h, trampas):
        self.paredes_v = paredes_v
        self.paredes_h = paredes_h
        self.trampas = trampas

    def tamano_hor(self):
        return len(self.trampas[0])

    def tamano_ver(self):
        return len(self.trampas)

    def tipo_celda_der(self, f, c):
        if c + 1 > self.tamano_hor() - 1 or self.paredes_h[f][c] == 1:
            return 0
        else:
            return 1

    def tipo_celda_izq(self, f, c):
        if c - 1 < 0 or self.paredes_h[f][c - 1] == 1:
            return 0
        else:
            return 1

    def tipo_celda_aba(self, f, c):
        if f + 1 > self.tamano_ver() - 1 or self.paredes_v[f][c] == 1:
            return 0
        else:
            return 1

    def tipo_celda_arr(self, f, c):
        if f - 1 < 0 or self.paredes_v[f - 1][c] == 1:
            return 0
        else:
            return 1
#  Fin de clase


# 1 si hay pared debajo de la casilla, 0 si no
paredes_ver = ([[1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]])

# 1 si hay pared a la derecha de la casilla, 0 si no
paredes_hor = ([[0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]])

# 1 si hay trampa en la casilla, 0 si no
mapa_trampas = ([[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]])

mapa_ejemplo = Mapa(paredes_ver, paredes_hor, mapa_trampas)

# Estados inicial y final:
estadoInicial = (4, 2,
                 0, 1, 0)
estadoFinal = (2, 0,
               0, 0, 0)


# Coste
def coste(estado):
    if mapa_trampas[estado[0]][estado[1]] != 0 or (estado[0] == estado[2] and estado[1] == estado[3]):
        return 1000000
    else:
        return 1


# Acciones:
    # Moverse a la derecha:
def aplicabilidad_mov_der(estado):
    f = estado[0]
    c = estado[1]
    if (f == estadoFinal[0] and c + 1 == estadoFinal[1]) \
            or mapa_ejemplo.tipo_celda_der(f, c) == 1 \
            or mapa_ejemplo.trampas[f][c + 1] == 0:
        return True
    else:
        return False


def aplicar_mov_der(estado):
    nuevo_estado = copy.deepcopy(estado)
    f = estado[0]
    c = estado[1] + 1
    return movimiento(f, c, nuevo_estado)


moverDerecha = probee.Acción("Mover a la derecha", aplicabilidad_mov_der, aplicar_mov_der, coste)

print(moverDerecha.es_aplicable(estadoInicial))


    # Moverse a la izquierda:
def aplicabilidad_mov_izq(estado):
    f = estado[0]
    c = estado[1]
    if (f == estadoFinal[0] and c - 1 == estadoFinal[1]) \
            or mapa_ejemplo.tipo_celda_izq(f, c) == 1 \
            or mapa_ejemplo.trampas[f][c - 1] == 0:
        return True
    else:
        return False


def aplicar_mov_izq(estado):
    nuevo_estado = copy.deepcopy(estado)
    f = estado[0]
    c = estado[1] - 1
    return movimiento(f, c, nuevo_estado)


moverIzquierda = probee.Acción("Mover a la izquierda", aplicabilidad_mov_izq, aplicar_mov_izq, coste)

print(moverIzquierda.es_aplicable(estadoInicial))


    # Moverse hacia abajo:
def aplicabilidad_mov_aba(estado):
    f = estado[0]
    c = estado[1]
    x = f + 1 == estadoFinal[0] and c == estadoFinal[1]
    y = mapa_ejemplo.tipo_celda_aba(f, c) == 1
    z = mapa_ejemplo.trampas[f + 1][c] == 0
    if (f + 1 == estadoFinal[0] and c == estadoFinal[1]) \
            or mapa_ejemplo.tipo_celda_aba(f, c) == 1 \
            or mapa_ejemplo.trampas[f + 1][c] == 0:
        return True
    else:
        return False


def aplicar_mov_aba(estado):
    nuevo_estado = copy.deepcopy(estado)
    f = estado[0] + 1
    c = estado[1]
    return movimiento(f, c, nuevo_estado)


moverAbajo = probee.Acción("Mover hacia abajo", aplicabilidad_mov_aba, aplicar_mov_aba, coste)

print(moverAbajo.es_aplicable(estadoInicial))


    # Moverse hacia arriba:
def aplicabilidad_mov_arr(estado):
    f = estado[0]
    c = estado[1]
    if (f - 1 == estadoFinal[0] and c == estadoFinal[1]) \
            or mapa_ejemplo.tipo_celda_aba(f, c) == 1 \
            or mapa_ejemplo.trampas[f - 1][c] == 0:
        return True
    else:
        return False


def aplicar_mov_arr(estado):
    nuevo_estado = copy.deepcopy(estado)
    f = estado[0] - 1
    c = estado[1]
    return movimiento(f, c, nuevo_estado)


moverArriba = probee.Acción("Mover hacia arriba", aplicabilidad_mov_arr, aplicar_mov_arr, coste)

print(moverArriba.es_aplicable(estadoInicial))


def movimiento(f, c, estado):
    f_monstruo = estado[2]
    c_monstruo = estado[3]
    turnos = estado[4]
    if not turnos > 0:
        # or (f == f_monstruo and c == c_monstruo)
        for _ in range(2):
            # Si estamos a la derecha del monstruo y se puede mover a la derecha
            if c > c_monstruo and mapa_ejemplo.tipo_celda_der(f_monstruo, c_monstruo) == 0:
                #  El monstruo se mueve 1 paso a la derecha
                f_monstruo = f_monstruo
                c_monstruo = c_monstruo + 1
                # Si el monstruo nos alcanza
                if f_monstruo == f and c_monstruo == c:
                    # Termina el movimiento
                    break
                # Si el monstruo cae en una trampa
                if mapa_trampas[f_monstruo][c_monstruo] == 1:
                    # Tiene 3 turnos de penalización y termina el movimiento
                    turnos = 3
                    break
            # Si estamos a la izquierda del monstruo y se puede mover a la izquierda
            elif c < c_monstruo and mapa_ejemplo.tipo_celda_izq(f_monstruo, c_monstruo) != 0:
                f_monstruo = f_monstruo
                c_monstruo = c_monstruo - 1
                # Si el monstruo nos alcanza
                if f_monstruo == f and c_monstruo == c:
                    # Termina el movimiento
                    break
                # Si el monstruo cae en una trampa
                if mapa_trampas[f_monstruo][c_monstruo] == 1:
                    # Tiene 3 turnos de penalización y termina el movimiento
                    turnos = 3
                    break
            # Si estamos debajo del monstruo y se puede mover hacia abajo
            elif f > f_monstruo and mapa_ejemplo.tipo_celda_aba(f_monstruo, c_monstruo) != 0:
                f_monstruo = f_monstruo + 1
                c_monstruo = c_monstruo
                # Si el monstruo nos alcanza
                if f_monstruo == f and c_monstruo == c:
                    # Termina el movimiento
                    break
                # Si el monstruo cae en una trampa
                if mapa_trampas[f_monstruo][c_monstruo] == 1:
                    # Tiene 3 turnos de penalización y termina el movimiento
                    turnos = 3
                    break
            # Si estamos encima del monstruo y se puede mover hacia arriba
            elif f < f_monstruo and mapa_ejemplo.tipo_celda_arr(f_monstruo, c_monstruo) != 0:
                f_monstruo = f_monstruo - 1
                c_monstruo = c_monstruo
                # Si el monstruo nos alcanza
                if f_monstruo == f and c_monstruo == c:
                    # Termina el movimiento
                    break
                # Si el monstruo cae en una trampa
                if mapa_trampas[f_monstruo][c_monstruo] == 1:
                    # Tiene 3 turnos de penalización y termina el movimiento
                    turnos = 3
                    break
        return f, c, f_monstruo, c_monstruo, turnos
    else:
        return f, c, f_monstruo, c_monstruo, turnos - 1


# Comienzo de clase
class Wappo(probee.ProblemaEspacioEstados):
    def __init__(self):
        acciones = [moverDerecha, moverIzquierda, moverAbajo, moverArriba]
        estado_inicial = estadoInicial
        super().__init__(acciones, estado_inicial)

    def es_estado_final(self, estado):
        return estado[0] == estadoFinal[0] and estado[1] == estadoFinal[1]
# Fin de clase


problema = Wappo()

b_óptima = búsqee.BúsquedaÓptima()


def h(nodo):
    estado = nodo.estado
    return abs(estado[0] - estadoFinal[0]) + abs(estado[1] - estadoFinal[1])


b_a_estrella = búsqee.BúsquedaAEstrella(h)

print(b_a_estrella.buscar(problema))
