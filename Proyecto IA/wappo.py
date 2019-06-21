import problema_espacio_estados as probee
import búsqueda_espacio_estados as búsqee
import datetime

print(datetime.datetime.now())


# Comienzo de clase
class Mapa:
    def __init__(self, paredes_v, paredes_h, trampas, estado_inicial, estado_final):
        self.paredes_v = paredes_v
        self.paredes_h = paredes_h
        self.trampas = trampas
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final

    def tamano_hor(self):
        return len(self.trampas[0])

    def tamano_ver(self):
        return len(self.trampas)

    def tipo_celda_arr(self, f, c):
        return 0 if self.paredes_v[f - 1][c] == 1 or f - 1 < -1 else 1

    def tipo_celda_aba(self, f, c):
        return 0 if self.paredes_v[f][c] == 1 or f + 1 > self.tamano_ver() else 1

    def tipo_celda_izq(self, f, c):
        return 0 if self.paredes_h[f][c - 1] == 1 or c - 1 < -1 else 1

    def tipo_celda_der(self, f, c):
        return 0 if self.paredes_h[f][c] == 1 or c + 1 > self.tamano_hor() else 1

    def es_estado_final(self, estado):
        return estado[0] == self.estado_final[0] and estado[1] == self.estado_final[1]
# Fin de clase


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
# print("Posición del mapa de trampas en la posición (0, 0): " + str(mapa_trampas[0][5]))

# Estados inicial y final:
estadoInicial = (4, 2,
                 1, 0, 0)
estadoFinal = (4, 1)

mapa_ejemplo = Mapa(paredes_ver, paredes_hor, mapa_trampas, estadoInicial, estadoFinal)

# print("mapa_ejemplo.tipo_celda_izq(0, 0")
# print(mapa_ejemplo.tipo_celda_izq(0, 0))

print("mapa_ejemplo.tipo_celda_der(0, 0, ¿0?")
print(mapa_ejemplo.tipo_celda_der(0, 0))


# print("mapa_ejemplo.tipo_celda_izq(7, 7)")
# print(mapa_ejemplo.tipo_celda_izq(7, 7))
# print("mapa_ejemplo.tipo_celda_aba(-1, -1)")
# print(mapa_ejemplo.tipo_celda_aba(-1, -1))

def coste(estado):
    return 1000000 if mapa_trampas[estado[0]][estado[1]] != 0 \
                      or (estado[0] == estado[2] and estado[1] == estado[3]) else 1


print("estado[1] < mapa_ejemplo.tamano_hor()-1")
print(estadoInicial[1] < mapa_ejemplo.tamano_hor() - 1)

print("Mapa ejemplo celda derecha en 1, 1")
print(mapa_ejemplo.tipo_celda_der(2, 4))


# Acciones:
# Moverse a la derecha:
def aplicabilidad_mov_der(estado):
    f = estado[0]
    c = estado[1]
    return mapa_ejemplo.tipo_celda_der(f, c) != 0 or mapa_ejemplo.trampas[f][c + 1] != 1


def aplicar_mov_der(estado):
    f = estado[0]
    c = estado[1] + 1
    return movimiento(f, c, estado)


moverDerecha = probee.Acción("Mover a la derecha", aplicabilidad_mov_der, aplicar_mov_der, coste)


# Moverse a la izquierda:
def aplicabilidad_mov_izq(estado):
    f = estado[0]
    c = estado[1]
    return mapa_ejemplo.tipo_celda_izq(f, c) != 0 or mapa_ejemplo.trampas[f][c - 1] != 1


def aplicar_mov_izq(estado):
    f = estado[0]
    c = estado[1] - 1
    return movimiento(f, c, estado)


moverIzquierda = probee.Acción("Mover a la izquierda", aplicabilidad_mov_izq, aplicar_mov_izq, coste)


# Moverse hacia abajo:
def aplicabilidad_mov_aba(estado):
    f = estado[0]
    c = estado[1]
    return mapa_ejemplo.tipo_celda_aba(f, c) != 0 or mapa_ejemplo.trampas[f + 1][c] != 1


def aplicar_mov_aba(estado):
    f = estado[0] + 1
    c = estado[1]
    return movimiento(f, c, estado)


moverAbajo = probee.Acción("Mover hacia abajo", aplicabilidad_mov_aba, aplicar_mov_aba, coste)


# Moverse hacia arriba:
def aplicabilidad_mov_arr(estado):
    f = estado[0]
    c = estado[1]
    return mapa_ejemplo.tipo_celda_arr(f, c) != 0 or mapa_ejemplo.trampas[f - 1][c] != 1


def aplicar_mov_arr(estado):
    f = estado[0] - 1
    c = estado[1]
    return movimiento(f, c, estado)


moverArriba = probee.Acción("Mover hacia arriba", aplicabilidad_mov_arr, aplicar_mov_arr, coste)


def movimiento(f, c, estado):
    f_monstruo = estado[2]
    c_monstruo = estado[3]
    if not (estado[4] > 0 or (f == f_monstruo and c == c_monstruo)):
        for _ in range(2):
            # Si estamos a la derecha del monstruo y se puede mover a la derecha
            if c > c_monstruo and mapa_ejemplo.tipo_celda_der(f_monstruo, c_monstruo) == 0:
                # El monstruo se mueve 1 paso a la derecha
                f_monstruo = f_monstruo
                c_monstruo = c_monstruo + 1
                # Si el monstruo cae en una trampa o nos alcanza
                if mapa_trampas[f_monstruo][c_monstruo] == 1 or (f_monstruo == f and c_monstruo == c):
                    # Termina el movimiento
                    estado[4] = 3
                    break
            # Si estamos a la izquierda del monstruo y se puede mover a la izquierda
            elif c < c_monstruo and mapa_ejemplo.tipo_celda_izq(f_monstruo, c_monstruo) == 0:
                f_monstruo = f_monstruo
                c_monstruo = c_monstruo - 1
                # Si el monstruo cae en una trampa o nos alcanza
                if mapa_trampas[f_monstruo][c_monstruo] == 1 or (f_monstruo == f and c_monstruo == c):
                    # Termina el movimiento
                    estado[4] = 3
                    break
            # Si estamos debajo del monstruo y se puede mover hacia abajo
            elif f > f_monstruo and mapa_ejemplo.tipo_celda_aba(f_monstruo, c_monstruo) == 0:
                f_monstruo = f_monstruo + 1
                c_monstruo = c_monstruo
                # Si el monstruo cae en una trampa o nos alcanza
                if mapa_trampas[f_monstruo][c_monstruo] == 1 or (f_monstruo == f and c_monstruo == c):
                    # Termina el movimiento
                    estado[4] = 3
                    break
            # Si estamos encima del monstruo y se puede mover hacia arriba
            elif f < f_monstruo and mapa_ejemplo.tipo_celda_arr(f_monstruo, c_monstruo) == 0:
                f_monstruo = f_monstruo - 1
                c_monstruo = c_monstruo
                # Si el monstruo cae en una trampa o nos alcanza
                if mapa_trampas[f_monstruo][c_monstruo] == 1 or (f_monstruo == f and c_monstruo == c):
                    # Termina el movimiento
                    estado[4] = 3
                    break
        return f, c, f_monstruo, c_monstruo, estado[4]
    else:
        return f, c, f_monstruo, c_monstruo, estado[4] - 1


# Definir el problema
print("\nEntra a probee.")
problema = probee.ProblemaEspacioEstados([moverDerecha, moverIzquierda, moverAbajo, moverArriba],
                                         estadoInicial, [estadoFinal])
# problema.es_estado_final(estadoFinal)
print("\nSale de probee.")
bOptima = búsqee.BúsquedaÓptima()
print("\nSale de asignación bOptima")
print(bOptima.buscar(problema))
print("\nSale de bOptima.buscar(problema)")

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
