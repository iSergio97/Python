import problema_espacio_estados as probee
import búsqueda_espacio_estados as búsqee
import copy


estado1 = [{2}, set(), {1}]
estado2 = [{1}, set(), {2}]


def está_vacía(estado, varilla):
    return not bool(estado[varilla - 1])

def disco_superior(estado, varilla):
    return min(estado[varilla - 1])

def aplicabilidad(estado):
    return (not está_vacía(estado, 1) and
            (está_vacía(estado, 3) or
             disco_superior(estado, 1) < disco_superior(estado, 3)))

def quitar_disco(estado, varilla):
    disco = disco_superior(estado, varilla)
    estado[varilla - 1].remove(disco)
    return disco

def poner_disco(estado, varilla, disco):
    estado[varilla - 1].add(disco)

def aplicación(estado):
    nuevo_estado = copy.deepcopy(estado)
    disco = quitar_disco(nuevo_estado, 1)
    poner_disco(nuevo_estado, 3, disco)
    return nuevo_estado

a13 = probee.Acción('De 1 a 3', aplicabilidad, aplicación)


print(a13.es_aplicable(estado1))

print(a13.es_aplicable(estado2))

print(a13.aplicar(estado2))

#Comienzo de clase
class MoverDisco(probee.Acción):
    def __init__(self, i, j):
        nombre = 'De {} a {}'.format(i, j)
        super().__init__(nombre)
        self.varilla_de = i
        self.varilla_a = j

    def está_vacía(self, estado, varilla):
        return not bool(estado[varilla - 1])

    def disco_superior(self, estado, varilla):
        return min(estado[varilla - 1])

    def es_aplicable(self, estado):
        return (not self.está_vacía(estado, self.varilla_de) and
                (self.está_vacía(estado, self.varilla_a) or
                 self.disco_superior(estado, self.varilla_de) <
                 self.disco_superior(estado, self.varilla_a)))

    def quitar_disco(self, estado, varilla):
        disco = self.disco_superior(estado, varilla)
        estado[varilla - 1].remove(disco)
        return disco

    def poner_disco(self, estado, varilla, disco):
        estado[varilla - 1].add(disco)

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        disco = self.quitar_disco(nuevo_estado, self.varilla_de)
        self.poner_disco(nuevo_estado, self.varilla_a, disco)
        return nuevo_estado
#Fin de la clase

acciones = [MoverDisco(i, j) for i in range(1, 4) for j in range(1, 4) if i != j]
estado_inicial = [{1, 2}, set(), set()]
estado_final = [set(), set(), {1, 2}]
Torres_Hanoi_2_discos = probee.ProblemaEspacioEstados(acciones, estado_inicial, [estado_final])

print(Torres_Hanoi_2_discos.es_estado_final(estado1))

print(Torres_Hanoi_2_discos.es_estado_final(a13.aplicar(estado2)))

for acción in Torres_Hanoi_2_discos.acciones_aplicables(estado1):
    print(acción.nombre)


for acción in Torres_Hanoi_2_discos.acciones_aplicables(estado1):
    print(acción.aplicar(estado1))


b_anchura = búsqee.BúsquedaEnAnchura(detallado=True)

print(b_anchura.buscar(Torres_Hanoi_2_discos))

b_profundidad = búsqee.BúsquedaEnProfundidad(detallado=True)

print(b_profundidad.buscar(Torres_Hanoi_2_discos))

#Comienzo de clase
class TorresHanoi(probee.ProblemaEspacioEstados):
    def __init__(self, n):
        acciones = [MoverDisco(i, j) for i in range(1, 4) for j in range(1, 4) if i != j]
        estado_inicial = [set(range(1, n + 1)), set(), set()]
        super().__init__(acciones, estado_inicial)
        self.n = n

    def es_estado_final(self, estado):
        return estado[2] == set(range(1, self.n + 1))
#Fin de clase

Torres_Hanoi_8_discos = TorresHanoi(8)

b_óptima = búsqee.BúsquedaÓptima()

def h(nodo):
    estado = nodo.estado
    return len(estado[0]) + len(estado[1])

b_a_estrella = búsqee.BúsquedaAEstrella(h)

# %%timeit -n1 -r1
#print(b_a_estrella.buscar(Torres_Hanoi_8_discos))

# %%timeit -n1 -r1
#print(b_óptima.buscar(Torres_Hanoi_8_discos))

# %%timeit -n1 -r1
#print(b_a_estrella.buscar(Torres_Hanoi_8_discos))

#Comienzo de clase

class Mapa:
    def __init__(self, celdas):
        self.celdas = celdas

    def tamaño_hor(self):
        return len(self.celdas[0])

    def tamaño_ver(self):
        return len(self.celdas)

    def tipo_celda(self, f, c):
        return self.celdas[f][c]

#Fin de clase

mapa_ejemplo = Mapa([[1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                     [1, 1, 1, 1, 2, 2, 2, 0, 0, 1],
                     [1, 1, 1, 2, 2, 4, 2, 2, 1, 1],
                     [1, 1, 1, 2, 4, 4, 4, 2, 1, 1],
                     [1, 1, 1, 2, 2, 4, 0, 0, 0, 0],
                     [1, 1, 1, 1, 2, 2, 0, 0, 0, 0]])

# Ejercicio 1: implementar como un problema de espacio de estados el problema de encontrar en el mapa anterior
# el camino de menor coste entre la posición `A` y la posición `B`. El coste de salir de una celda de llanura es 1,
# de una celda de bosque es 2 y de una celda de montaña es 4. El camino no puede pasar por ninguna celda de agua.


# Estados inicial y final:
estadoInicial = (5, 0)    # [5,0]
estadoFinal = (0, 9)      # [0,9]


# Coste:
def coste(estado):
    return mapa_ejemplo.tipo_celda(estado[0], estado[1])


# Acciones:
    # Moverse a la derecha:
def aplicabilidad_mov_der(estado):
    return estado[1] < mapa_ejemplo.tamaño_hor()-1 and mapa_ejemplo.tipo_celda(estado[0], estado[1]+1) != 0


def aplicar_mov_der(estado):
    return estado[0], estado[1]+1


moverDerecha = probee.Acción("Mover a la derecha", aplicabilidad_mov_der, aplicar_mov_der, coste)


    # Moverse a la izquierda:
def aplicabilidad_mov_izq(estado):
    return estado[1] > -1 and mapa_ejemplo.tipo_celda(estado[0], estado[1]-1) != 0


def aplicar_mov_izq(estado):
    return estado[0], estado[1]-1


moverIzquierda = probee.Acción("Mover a la izquierda", aplicabilidad_mov_izq, aplicar_mov_izq, coste)


 # Moverse hacia abajo:
def aplicabilidad_mov_aba(estado):
    return estado[0] < mapa_ejemplo.tamaño_ver()-1 and mapa_ejemplo.tipo_celda(estado[0]+1, estado[1]) != 0


def aplicar_mov_aba(estado):
    return estado[0]+1, estado[1]


moverAbajo = probee.Acción("Mover hacia abajo", aplicabilidad_mov_aba, aplicar_mov_aba, coste)


    # Moverse hacia arriba:
def aplicabilidad_mov_arr(estado):
    return estado[0] > -1 and mapa_ejemplo.tipo_celda(estado[0]-1, estado[1]) != 0


def aplicar_mov_arr(estado):
    return estado[0]-1, estado[1]


moverArriba = probee.Acción("Mover hacia arriba", aplicabilidad_mov_arr, aplicar_mov_arr)


# Definir el problema

problema = probee.ProblemaEspacioEstados([moverDerecha, moverIzquierda, moverAbajo, moverArriba],
                                         estadoInicial, [estadoFinal])

# Ejercicio 2: aplicar el algoritmo A* para encontrar una solución del problema anterior.

bOptima = búsqee.BúsquedaÓptima()
print(bOptima.buscar(problema))

def h(nodo):
    estado = nodo.estado
    return estado[0]+9-estado[1]

# Supongamos que además de ir desde la posición A hasta la posición B, una unidad del juego tiene que pasar antes
# por otros puntos de encuentro especificados. Este problema puede resolverse buscando y concatenando
# los caminos intermedios entre los puntos de encuentro (incluyendo también los caminos desde el origen al primer
# punto de encuentro y desde el último punto de encuentro al destino final).

# Ejercicio 3: definir una función `búsqueda_camino_con_puntos` que, dada una lista de puntos del camino (*waypoints*)
# devuelva el camino de menor coste desde la posición A hasta la posición B, pasando en orden
# por esos puntos del camino. Usar esta función para encontrar un camino de coste mínimo desde A hasta B,
# pasando por las posiciones `(1, 6)` y `(5, 5)`, en ese orden.


