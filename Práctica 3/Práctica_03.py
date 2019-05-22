#!/usr/bin/env python
# coding: utf-8

# # Rompecabezas de las Torres de Hanoi

# El rompecabezas de las Torres de Hanoi consta de tres varillas verticales y un número de discos, que determinará la complejidad del problema, todos de distinto tamaño y apilados de mayor a menor radio en la primera varilla.
# 
# El objetivo del juego es pasar todos los discos de la primera a la última varilla, siguiendo tres simples reglas:
# 1. Se desplaza un disco cada vez.
# 2. Solo se pueden desplazar los discos de arriba de las varillas.
# 3. No se puede colocar un disco sobre otro más pequeño.

# En esta primera parte de la práctica se mostrará cómo implementar el rompecabezas de las Torres de Hanoi como un problema de espacio de estados y se aplicarán distintos algoritmos de búsqueda para resolverlo.

# Para implementar un problema de espacio de estados se pueden hacer uso de las clases de objetos proporcionadas por el módulo `problema_espacio_estados`.

import problema_espacio_estados as probee


# Los algoritmos de búsqueda están implementados en el módulo `búsqueda_espacio_estados`.

 import búsqueda_espacio_estados as búsqee


# El siguiente módulo será de utilidad para copiar un estado en otro estado igual, pero completamente nuevo e independiente.

 import copy


# El primer paso es decidir cómo se van a implementar los estados. Para el rompecabezas de las Torres de Hanoi una opción es hacerlo mediante una lista que guarde para cada varilla el conjunto de los discos que hay en ella.

 estado1 = [{2}, set(), {1}]
estado2 = [{1}, set(), {2}]


# A continuación hay que implementar las acciones como instancias de la clase `Acción`, proporcionando un nombre, una función de aplicabilidad y una función de aplicación para cada acción. Por ejemplo, la acción `De 1 a 3` que mueve un disco de la primera a la tercera varilla se puede implementar de la siguiente manera:

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


 a13.es_aplicable(estado1)


 a13.es_aplicable(estado2)


 a13.aplicar(estado2)


# Normalmente las acciones se pueden agrupar en distintos tipos, cada uno de los cuales puede ser implementado de manera abstracta mediante una clase que herede de la clase `Acción`.

# Para el rompecabezas de las Torres de Hanoi, todas las acciones son del tipo mover un disco de una varilla a otra. En este caso, consideramos que el coste de mover un disco es siempre 1, el valor por defecto. En caso de que fuera distinto, al crear una instancia de la clase `Acción` se puede proporcionar una función `coste`, o bien al heredar de la clase `Acción` se puede redefinir el método `coste_de_aplicar`.

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


# Finalmente, un problema de espacio de estados se implementa como una instancia de la clase `ProblemaEspacioEstados`, proporcionando una lista de acciones, un estado inicial y una lista de estados finales.

 acciones = [MoverDisco(i, j) for i in range(1, 4) for j in range(1, 4) if i != j]
estado_inicial = [{1, 2}, set(), set()]
estado_final = [set(), set(), {1, 2}]
Torres_Hanoi_2_discos = probee.ProblemaEspacioEstados(
    acciones, estado_inicial, [estado_final])


 Torres_Hanoi_2_discos.es_estado_final(estado1)


 Torres_Hanoi_2_discos.es_estado_final(a13.aplicar(estado2))


 for acción in Torres_Hanoi_2_discos.acciones_aplicables(estado1):
    print(acción.nombre)


 for acción in Torres_Hanoi_2_discos.acciones_aplicables(estado1):
    print(acción.aplicar(estado1))


# El procedimiento para realizar una búsqueda en un espacio de estados consiste en crear una instancia de una clase que implemente un algoritmo de búsqueda, proporcionando los argumentos necesarios, y aplicar el método buscar de esa instancia al problema de espacio de estados.
# 
# Las clases correspondientes a los algoritmos de búsqueda más comunes son las siguientes:
# * `BúsquedaEnAnchura`
# * `BúsquedaEnProfundidad`
# * `BúsquedaPrimeroElMejor`: hay que proporcionar la función de evaluación heurística `f`.
# * `BúsquedaÓptima`
# * `BúsquedaAEstrella`: hay que proporcionar la función de estimación del coste `h`.
# 
# Adicionalmente, todas las clases anteriores admiten establecer el argumento `detallado` a `True`, para que al realizar una búsqueda se imprima por pantalla su traza.

 b_anchura = búsqee.BúsquedaEnAnchura(detallado=True)


 b_anchura.buscar(Torres_Hanoi_2_discos)


 b_profundidad = búsqee.BúsquedaEnProfundidad(detallado=True)


 b_profundidad.buscar(Torres_Hanoi_2_discos)


# Podemos parametrizar la implementación del rompecabezas de las Torres de Hanoi para que dependa del número `n` de discos. Para ello basta implementar una clase que herede de la clase `ProblemaEspacioEstados`. Aprovechamos también para, en lugar de enumerar los estados finales, realizar una descripción declarativa de los mismos redefiniendo el método `es_estado_final`.

 class TorresHanoi(probee.ProblemaEspacioEstados):
    def __init__(self, n):
        acciones = [MoverDisco(i, j) for i in range(1, 4) for j in range(1, 4) if i != j]
        estado_inicial = [set(range(1, n + 1)), set(), set()]
        super().__init__(acciones, estado_inicial)
        self.n = n
    
    def es_estado_final(self, estado):
        return estado[2] == set(range(1, self.n + 1))


# Con un número de discos igual a 8, el coste en tiempo de los algoritmos de búsqueda en anchura y profundidad comienza a no ser asumible, por lo que debemos pasar a realizar una búsqueda informada.

 Torres_Hanoi_8_discos = TorresHanoi(8)


 b_óptima = búsqee.BúsquedaÓptima()


# Para poder aplicar la búsqueda $A^*$, es un requisito necesario definir una función que para cada nodo estime el coste de una solución óptima desde el estado de ese nodo (que en nuestra implementación está guardado en el atributo `estado` de la clase que implementa a estos últimos).

 def h(nodo):
    estado = nodo.estado
    return len(estado[0]) + len(estado[1])
b_a_estrella = búsqee.BúsquedaAEstrella(h)


# `timeit` es una «función mágica» de *Jupyter* que proporciona el promedio de tiempo que tarda un bucle que se repite un cierto número de pasos, ejecutando en cada paso el código de la celda un cierto número de veces (en los ejemplos de abajo se ha establecido un único paso del bucle y una única ejecución del código en cada paso).

 get_ipython().run_cell_magic('timeit', '-n1 -r1', '\nb_óptima.buscar(Torres_Hanoi_8_discos)')


 get_ipython().run_cell_magic('timeit', '-n1 -r1', '\nb_a_estrella.buscar(Torres_Hanoi_8_discos)')


# # Búsqueda de caminos en juegos de ordenador

# Una de las aplicaciones de los problemas de espacio de estados la encontramos en los juegos de ordenador, en los que ciertos elementos deben desplazarse entre dos puntos del mapa de juego. La idea es que los estados representen la posición del elemento y las acciones los posibles movimientos (cuatro si solo se permite en vertical u horizontal, ocho si también se permite en diagonal, etcétera). Se aplica entonces un algoritmo de búsqueda en espacio de estados, generalmente $A*$, para encontrar el *mejor* (sea lo que sea que signifique eso) camino entre una posición inicial y una final.

# La siguiente clase `Mapa` representa un mapa rectangular en el que las celdas puedan ser de distinto tipo.

 class Mapa:
    def __init__(self, celdas):
        self.celdas = celdas
    
    def tamaño_hor(self):
        return len(self.celdas[0])
    
    def tamaño_ver(self):
        return len(self.celdas)
    
    def tipo_celda(self, f, c):
        return self.celdas[f][c]


# En la siguiente imagen las celdas marrón claro representan zonas de llanura, las verdes zonas
# boscosas, las marrón oscuro zonas montañosas y las azules zonas con agua:
# 
# <img src="mapa.png"/>
# 
# Este mapa se puede implementar con la siguiente instancia de la clase `Mapa`:

# mapa_ejemplo = Mapa([[1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
#                      [1, 1, 1, 1, 2, 2, 2, 0, 0, 1],
#                      [1, 1, 1, 2, 2, 4, 2, 2, 1, 1],
#                      [1, 1, 1, 2, 4, 4, 4, 2, 1, 1],
#                      [1, 1, 1, 2, 2, 4, 0, 0, 0, 0],
#                      [1, 1, 1, 1, 2, 2, 0, 0, 0, 0]])

# **Ejercicio 1**: implementar como un problema de espacio de estados el problema de encontrar en el mapa anterior el camino de menor coste entre la posición `A` y la posición `B`. El coste de salir de una celda de llanura es 1, de una celda de bosque es 2 y de una celda de montaña es 4. El camino no puede pasar por ninguna celda de agua.

 # **Ejercicio 2**: aplicar el algoritmo $A^*$ para encontrar una solución del problema anterior.

 # Supongamos que además de ir desde la posición `A` hasta la posición `B`, una unidad del juego tiene que pasar antes por otros puntos de encuentro especificados. Este problema puede resolverse buscando y concatenando los caminos intermedios entre los puntos de encuentro (incluyendo también los caminos desde el origen al primer punto de encuentro y desde el último punto de encuentro al destino final).

# **Ejercicio 3**: definir una función `búsqueda_camino_con_puntos` que, dada una lista de puntos del camino (*waypoints*) devuelva el camino de menor coste desde la posición `A` hasta la posición `B`, pasando en orden por esos puntos del camino. Usar esta función para encontrar un camino de coste mínimo desde `A` hasta `B`, pasando por las posiciones `(1, 6)` y `(5, 5)`, en ese orden.

