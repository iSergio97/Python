import problema_espacio_estados as probee
import búsqueda_espacio_estados as búsqee
import math
import datetime

print(datetime.datetime.now())


# Comienzo de clase
class Mapa:
    def __init__(self, paredes_v, paredes_h, trampas, estado_inicial):
        self.paredes_v = paredes_v
        self.paredes_h = paredes_h
        self.trampas = trampas
        self.estado_inicial = estado_inicial

    def tamano_hor(self):
        return len(self.trampas[0]) - 1

    def tamano_ver(self):
        return len(self.trampas) - 1

    def tipo_celda_arr(self, f, c):
        return self.trampas[f][c]

    def tipo_celda_aba(self, f, c):
        return self.trampas[f][c]

    def tipo_celda_izq(self, f, c):
        return self.trampas[f][c]

    def tipo_celda_der(self, f, c):
        return self.trampas[f][c]

    def trampa(self, f, c):
        return self.trampas[f][c]
# Fin de clase


paredes_ver = [[],
               [],
               [],
               [],
               []]

paredes_hor = [[],
               [],
               [],
               [],
               []]

# ¿Y si en vez de un mapa de trampas ponemos directamente las coordenadas?
mapa_trampas = [[0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]
#print("Posición del mapa de trampas en la posición (0, 0): " + str(mapa_trampas[0][5]))

# Estados inicial y final:
estadoInicial = (0, 0,
                 4, 4, 0)
estadoFinal = (0, 1)

mapa_ejemplo = Mapa(paredes_ver, paredes_hor, mapa_trampas, estadoInicial)

print("Mapa de ejemplo tipo celda derecha")

# Este print devuelve el valor de la posición actual del tipo derecha
print(mapa_ejemplo.tipo_celda_der((estadoInicial[0]), (estadoInicial[1])))



def coste(estado):
    return 1000000 if 0 == mapa_trampas(estado[0], estado[1]) or (estado[0] == estado[2] and estado[1] == estado[3]) or mapa_ejemplo.tipo_celda_der((estadoInicial[0]), (estadoInicial[1])) != 0 else 1
# Acciones:
    # Moverse a la derecha:
def aplicabilidad_mov_der(estado):
    return estado[1] < mapa_ejemplo.tamano_hor() - 1 and mapa_ejemplo.tipo_celda_der((estadoInicial[0]), (estadoInicial[1])) == 0 and mapa_trampas(estado[0], estado[1 + 1]) == 0


def aplicar_mov_der(estado):
    return estado[0], estado[1]+1, moverMonstruo(estado[0], estado[1]+1, estado[4])


moverDerecha = probee.Acción("Mover a la derecha", aplicabilidad_mov_der, aplicar_mov_der, coste)


# Moverse a la izquierda:
def aplicabilidad_mov_izq(estado):
    return estado[1] > - 1 and mapa_ejemplo.tipo_celda_izq((estadoInicial[0]), (estadoInicial[1])) == 0 and mapa_trampas([estado[0]][(estado[1] - 1)]) == 0


def aplicar_mov_izq(estado):
    return estado[0], estado[1]-1, moverMonstruo(estado[0], estado[1]-1, estado[4])


moverIzquierda = probee.Acción("Mover a la izquierda", aplicabilidad_mov_izq, aplicar_mov_izq, coste)


# Moverse hacia abajo:
def aplicabilidad_mov_aba(estado):
    return estado[0] < mapa_ejemplo.tamano_ver() - 1 \
            and mapa_ejemplo.tipo_celda_aba((estadoInicial[0]), (estadoInicial[1])) == 0 and mapa_trampas([(estado[0] + 1)][estado[1]]) == 0


def aplicar_mov_aba(estado):
    return estado[0] + 1, estado[1], moverMonstruo(estado[0] + 1, estado[1], estado[4])


moverAbajo = probee.Acción("Mover hacia abajo", aplicabilidad_mov_aba, aplicar_mov_aba, coste)


# Moverse hacia arriba:
def aplicabilidad_mov_arr(estado):
    return estado[0] > - 1 and mapa_ejemplo.tipo_celda_arr((estadoInicial[0]), (estadoInicial[1])) == 0 and mapa_trampas([(estado[0] - 1)], [estado[1]]) == 0


def aplicar_mov_arr(estado):
    return estado[0] - 1, estado[1], moverMonstruo(estado[0]-1, estado[1], estado[4])


moverArriba = probee.Acción("Mover hacia arriba", aplicabilidad_mov_arr, aplicar_mov_arr, coste)


# TODO: Échale un vistazo a esto y cambia el acceso al mapa de trampas, bloqueos y demás
# TODO: mapa_ejemplo.tipo_celda_der((estadoInicial[0]), (estadoInicial[1]))
# TODO: La línea de arriba accede de forma correcta a las posiciones
def moverMonstruo(f, c, estado):
    if estado[4] > 0 or (f == estado[2] and c == estado[3]):
        return estado[2], estado[3]
    else:
        f_monstruo = estado[2]
        c_monstruo = estado[3]
        for _ in range(1):
            # Si estamos a la derecha del monstruo y nos podemos mover a la derecha
            if c > c_monstruo and mapa_ejemplo.tipo_celda_der(f_monstruo, c_monstruo + 1) != 0:
                # El monstruo se mueve 1 paso a la derecha
                f_monstruo = f_monstruo
                c_monstruo = c_monstruo + 1
                # Si el monstruo cae en una trampa o nos alcanza
                if mapa_trampas(f_monstruo, c_monstruo) == 1 or (f_monstruo == f and c_monstruo == c):
                    # Termina el movimiento
                    break
            # Si estamos a la izquierda del monstruo y nos podemos mover a la izquierda
            elif c < c_monstruo and mapa_ejemplo.tipo_celda_izq(f_monstruo, c_monstruo - 1) != 0:
                f_monstruo = f_monstruo
                c_monstruo = c_monstruo - 1
                # Si el monstruo cae en una trampa o nos alcanza
                if mapa_trampas(f_monstruo, c_monstruo) == 1 or (f_monstruo == f and c_monstruo == c):
                    # Termina el movimiento
                    break
            elif f > f_monstruo and mapa_ejemplo.tipo_celda_aba(f_monstruo + 1, c_monstruo) != 0:
                f_monstruo = f_monstruo + 1
                c_monstruo = c_monstruo
                # Si el monstruo cae en una trampa o nos alcanza
                if mapa_trampas(f_monstruo, c_monstruo) == 1 or (f_monstruo == f and c_monstruo == c):
                    # Termina el movimiento
                    break
            elif f < f_monstruo and mapa_ejemplo.tipo_celda_arr(f_monstruo - 1, c_monstruo) != 0:
                f_monstruo = f_monstruo - 1
                c_monstruo = c_monstruo
                # Si el monstruo cae en una trampa o nos alcanza
                if mapa_trampas(f_monstruo, c_monstruo) == 1 or (f_monstruo == f and c_monstruo == c):
                    # Termina el movimiento
                    break
    return f_monstruo, c_monstruo


def turnos(f, c, estado):
    if estado[4] > 0:
        return estado[4] - 1
    else:
        return 3 if mapa_trampas([f], [c]) == 1 else 0


# Definir el problema
print("\nEntra a probee.")
problema = probee.ProblemaEspacioEstados([moverDerecha, moverIzquierda, moverAbajo, moverArriba],
                                         estadoInicial, estadoFinal)
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
