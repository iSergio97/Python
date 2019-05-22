#!/usr/bin/env python
# coding: utf-8

# Para implementar un problema de planificación se puede hacer uso de las clases de objetos proporcionadas por el módulo `problema_planificación` (**Nota**: es importante tener en cuenta que este módulo asume que todos los símbolos de objetos son cadenas).

 import problema_planificación_pddl as probpl


# En la primera parte de la práctica se mostrará cómo implementar unas instancias de los problemas de la rueda pinchada y del mundo de los bloques cuyo planteamiento general se puede encontrar en las transparencias del tema.

# # Problema de la rueda pinchada

# El problema de la rueda pinchada consiste en determinar los pasos a realizar para cambiar una rueda pinchada por una rueda de repuesto que se encuentra en el maletero, guardando finalmente la rueda pinchada en el maletero, para poder continuar el viaje.

# En primer lugar declaramos los predicados que vamos a utilizar para representar el problema, indicando los conjuntos sobre los cuales se van a construir dichos predicados.

 en = probpl.Predicado({'rueda-pinchada', 'rueda-repuesto'}, {'eje', 'maletero', 'suelo'})


# Un estado es una instancia de la clase `Estado`, creada a partir de una serie de instancias de los predicados declarados previamente.

 estado_inicial_rueda = probpl.Estado(en('rueda-pinchada', 'eje'), en('rueda-repuesto', 'maletero'))
print("estado_inicial_rueda")
print(estado_inicial_rueda)


# Las acciones se implementan como instancias de la clase `AcciónPlanificación`. Los argumentos que se pueden proporcionar son los siguientes:
# * `nombre`: una cadena que representa la acción. Este argumento es obligatorio.
# * `precondicionesP`: una lista de instancias de predicados que forman las precondiciones positivas. Este argumento es opcional.
# * `precondicionesN`: una lista de instancias de predicados que forman las precondiciones negativas. Este argumento es opcional.
# * `efectosP`: una lista de instancias de predicados que forman los efectos positivos. Este argumento es opcional.
# * `efectosN`: una lista de instancias de predicados que forman los efectos negativos. Este argumento es opcional.
# * `coste`: un número entero positivo (esta implementación asume que el coste de aplicar la acción es siempre el mismo,
# independientemente del estado). Este argumento es opcional, en cuyo caso se toma coste 1.
# 
# En el caso de una sola precondición o efecto no es necesario proporcionarlos en una lista.

 # Sacar la rueda de repuesto del maletero
sacar = probpl.AcciónPlanificación(
    nombre='sacar_repuesto',
    precondicionesP=en('rueda-repuesto', 'maletero'),
    efectosP=en('rueda-repuesto', 'suelo'),
    efectosN=en('rueda-repuesto', 'maletero'))

# Quitar la rueda pinchada del eje
quitar = probpl.AcciónPlanificación(
    nombre = 'quitar_pinchada',
    precondicionesP = [en('rueda-pinchada', 'eje')],
    efectosP = [en('rueda-pinchada', 'suelo')],
    efectosN = [en('rueda-pinchada', 'eje')])

# Colocar la rueda de repuesto en el eje
poner = probpl.AcciónPlanificación(
    nombre = 'poner_repuesto',
    precondicionesP = en('rueda-repuesto', 'suelo'),
    precondicionesN = en('rueda-pinchada', 'eje'),
    efectosP = en('rueda-repuesto', 'eje'),
    efectosN = en('rueda-repuesto', 'suelo'))

# Guardar la rueda pinchada en el maletero
guardar = probpl.AcciónPlanificación(
    nombre = 'guardar_pinchada',
    precondicionesP = [en('rueda-pinchada', 'suelo')],
    precondicionesN = [en('rueda-repuesto', 'maletero')],
    efectosP = [en('rueda-pinchada', 'maletero')],
    efectosN = [en('rueda-pinchada', 'suelo')])


# Una vez creadas las acciones, la función `print` nos muestra su estructura.

 print(quitar)


 print(guardar)


# Finalmente, un problema de planificación será una instancia de la clase `ProblemaPlanificación` construida a partir de los siguientes argumentos:
# * `operadores`: la lista de acciones del problema.
# * `estado_inicial`: el estado inicial del problema.
# * `objetivosP`: una lista de instancias de predicados que forman los objetivos positivos.
# * `objetivosN`: una lista de instancias de predicados que forman los objetivos negativos.
# 
# En el caso de un solo operador, un solo objetivo positivo o un solo objetivo negativo, no es necesario proporcionarlos en una lista.

 problema_rueda_pinchada = probpl.ProblemaPlanificación(
    operadores=[quitar, guardar, sacar, poner],
    estado_inicial=probpl.Estado(en('rueda-pinchada','eje'),
                                 en('rueda-repuesto','maletero')),
    objetivosP=[en('rueda-pinchada','maletero'), 
                en('rueda-repuesto','eje')])


# Una vez implementado el problema de planificación, para buscar un plan solución basta aplicar algún algoritmo de búsqueda en espacio de estados.

 import búsqueda_espacio_estados as búsqee


 búsqueda_profundidad = búsqee.BúsquedaEnProfundidad()

búsqueda_profundidad.buscar(problema_rueda_pinchada)


 búsqueda_anchura = búsqee.BúsquedaEnAnchura()

búsqueda_anchura.buscar(problema_rueda_pinchada)


# # Problema del mundo de los bloques

# En el problema del mundo de los bloques se dispone de un conjunto de bloques cúbicos dispuestos sobre una mesa. Los bloques se pueden apilar, pero cada bloque solo se puede colocar sobre un único bloque. Un brazo robótico puede coger un bloque y moverlo a otra posición, ya sea sobre la mesa o sobre otro bloque. El brazo robótico solo puede coger un bloque cada vez. El objetivo es construir una determinada pila de bloques.

# En primer lugar declaramos los predicados que vamos a utilizar para representar el problema, indicando los conjuntos sobre los cuales se van a construir dichos predicados. Si un predicado no va a tener argumentos, entonces se debe indicar que se va a construir sobre el conjunto vacío.

 bloques = {'A','B','C'}
despejado = probpl.Predicado(bloques)
brazolibre = probpl.Predicado({})
sobrelamesa = probpl.Predicado(bloques)
sobre = probpl.Predicado(bloques,bloques)
agarrado = probpl.Predicado(bloques)


# Definimos un estado inicial para el problema de los bloques en el que el bloque $A$ está situado sobre la mesa y no tiene nada encima; el bloque $B$ está situado sobre la mesa y tiene encima el bloque $C$, que no tiene nada más encima; y el brazo robótico está libre.

 estado_inicial_bloques = probpl.Estado(
    sobrelamesa('A'),despejado('A'),
    sobrelamesa('B'),sobre('C','B'),despejado('C'),
    brazolibre())


# Se pueden establecer costes distintos para las acciones obtenidas a partir de un mismo esquema. Para ello basta crear una instancia de la clase `CosteEsquema` a partir de una función que establezca ese coste en función de ciertos parámetros. Por ejemplo, supongamos que el coste de mover cada uno de los tres bloques es distinto, ya que tienen pesos distintos.

 coste_bloque = probpl.CosteEsquema(lambda b: {'A': 1, 'B': 2, 'C': 3}[b])


# Los esquemas de acciones se implementan como instancias de la clase `EsquemaPlanificación`. Los posibles argumentos que se pueden proporcionar son los siguientes:
# * `nombre`: una cadena de la forma $acc(z_1, \dotsc, z_k)$, donde si $z_i$ representa una variable, entonces debe escribirse entre llaves. Este argumento es obligatorio.
# * `precondicionesP`: una lista de instancias de predicados que forman las precondiciones positivas. Este argumento es opcional.
# * `precondicionesN`: una lista de instancias de predicados que forman las precondiciones negativas. Este argumento es opcional.
# * `efectosP`: una lista de instancias de predicados que forman los efectos positivos. Este argumento es opcional.
# * `efectosN`: una lista de instancias de predicados que forman los efectos negativos. Este argumento es opcional.
# * `coste`: una instancia de la clase `costeEsquema` que establece el coste de una acción a partir de los valores de las variables $z_i$. Este argumento es opcional, en cuyo caso se toma coste 1.
# * `dominio`: un conjunto de tuplas del mismo tamaño que el número de variables. Indica el conjunto de situaciones para las tiene sentido instanciar el esquema de acción.
# * `variables`: un diccionario que asocia a cada nombre de variable $z_i$ el conjunto de valores que puede tomar.
# 
# Al menos uno de los argumentos `dominio` o `variables` debe aparecer. En caso de incluir los dos, sólo se tiene en cuenta el argumento `dominio`.
# 
# Las instancias de los predicados en `precondicionesP`, `precondicionesN`, `efectosP` y `efectosN`, pueden hacer referencia a las variables $z_i$, que deben escribirse entre llaves. En el caso de una sola precondición positiva o negativa, o un solo efecto positivo o negativo no es necesario proporcionarlos en una lista.

 # Colocar un bloque sobre otro
apilar = probpl.EsquemaPlanificación('apilar({x},{y})',
    precondicionesP=[despejado('{y}'), agarrado('{x}')],
    efectosN=[despejado('{y}'), agarrado('{x}')],
    efectosP=[despejado('{x}'), brazolibre(), sobre('{x}', '{y}')],
    coste=coste_bloque('{x}'),
    dominio={('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')},
    variables={'x': bloques, 'y': bloques})

# Quitar un bloque que estaba sobre otro
desapilar = probpl.EsquemaPlanificación('desapilar({x},{y})',
    precondicionesP = [sobre('{x}','{y}'),despejado('{x}'),brazolibre()],
    efectosN = [sobre('{x}','{y}'),despejado('{x}'),brazolibre()],
    efectosP = [agarrado('{x}'),despejado('{y}')],
    coste = coste_bloque('{x}'),
    dominio = {('A','B'),('A','C'),('B','A'),('B','C'),('C','A'),('C','B')})

# Agarrar un bloque de la mesa con el robot
agarrar = probpl.EsquemaPlanificación('agarrar({x})',
    precondicionesP = [despejado('{x}'),sobrelamesa('{x}'),brazolibre()],
    efectosN = [despejado('{x}'),sobrelamesa('{x}'),brazolibre()],
    efectosP = [agarrado('{x}')],
    coste = coste_bloque('{x}'),
    dominio = bloques)

# Bajar un bloque hasta la mesa
bajar = probpl.EsquemaPlanificación('bajar({x})',
    precondicionesP = [agarrado('{x}')],
    efectosN = [agarrado('{x}')],
    efectosP = [despejado('{x}'),sobrelamesa('{x}'),brazolibre()],
    coste = coste_bloque('{x}'),
    variables = {'x':bloques})


# La representación como cadena de un esquema de acción muestra las acciones que se generarían a partir de él.

 print("\nagarrar")
print(agarrar)
print("\n")


 print("apilar")
print(apilar)
print("\n")

# Finalmente, para representar el problema de planificación se pasa la lista de esquemas de acción a la clase `ProblemaPlanificación` (en general, se pueden proporcionar tanto acciones como operadores, incluso mezclados). 

 problema_mundo_bloques = probpl.ProblemaPlanificación(
    operadores = [apilar,desapilar,agarrar,bajar],
    estado_inicial = estado_inicial_bloques,
    objetivosP = [sobrelamesa('C'),sobre('B','C'),sobre('A','B')])


# Una vez implementado el problema de planificación, para buscar un plan solución basta aplicar algún algoritmo de búsqueda en espacio de estados.

 print("búsqueda_profundidad.buscar(problema_mundo_bloques)\n")
búsqueda_profundidad.buscar(problema_mundo_bloques)


# # Problema de los buceadores

# En el marco de la _Conferencia Internacional sobre Planificación Automática y Planificación Temporal_ ([International Conference on Automated Planning and Scheduling, ICAPS](http://www.icaps-conference.org/)) se celebra, con periodicidad aproximadamente trienal, la _Competición Internacional de Planificación_ (http://www.icaps-conference.org/index.php/Main/Competitions).
# 
# Esta competición tiene diferentes objetivos: realizar una comparación empírica del estado del arte de los sistemas de planificación; destacar desafíos para la comunidad de Planificación Automática; proponer nuevas direcciones para la investigación y nuevos vínculos con otros campos de la Inteligencia Artificial; y proporcionar nuevos conjuntos de datos que puedan ser utilizados por la comunidad científica como puntos de referencia.

# Uno de los problemas incluidos en la competición es el _problema de los buceadores_, propuesto por Nathan Robinson,Christian Muise y Charles Gretton.

# El problema consiste en lo siguiente: hay una serie de buceadores, cada uno de los cuales puede acarrear 4 tanques de aire. A estos buceadores hay que contratarlos para que entren en un sistema cavernoso inundado y, o bien tomen fotografías, o bien preparen el camino para otros buceadores dejando caer tanques llenos de aire. El lugar es demasiado estrecho para que pueda entrar más de un buceador a la vez. El sistema cavernoso está formado por una serie de cuevas, algunas de ellas interconectadas entre sí. La entrada es única. Ciertas cuevas son objetivos que los buceadores deben fotografiar. Tanto nadar de un lugar a otro, como fotografiar una cueva, consume un tanque entero de aire. Los buceadores deben realizar un proceso de descompresión al salir a superficie, por lo que cada uno de ellos solo puede realizar un único viaje. Ciertos buceadores desconfían de algunos de sus compañeros y rechazarán trabajar si alguno de ellos ha recorrido las cuevas previamente. Contratar un buceador tiene un coste diferente para cada uno de ellos.

# Consideremos los siguientes conjuntos de símbolos de objetos (__que no tienen por qué ser los únicos que se usen en el problema__):

 cuevas = {'C{}'.format(i) for i in range(5)}
buceadores = {'B{}'.format(i) for i in range(2)}
cantidades = {str(i) for i in range(9)}


 print("Cuevas: {}".format(cuevas))
print("Buceadores: {}".format(buceadores))
print("Cantidades: {}".format(cantidades))


# y las siguientes relaciones de conexión entre las cuevas:

 conexiones = [('C0', 'C1'),
              ('C1', 'C0'),
              ('C1', 'C2'),
              ('C1', 'C4'),
              ('C2', 'C1'),
              ('C2', 'C3'),
              ('C3', 'C2'),
              ('C4', 'C1')]


# __Ejercicio 1__: implementar los siguientes predicados:
# * `posición_buceador`: para cada buceador indica en qué cueva se encuentra, o si se encuentra en la superficie.
# * `disponible`: para cada buceador indica si está disponible para trabajar.
# * `trabajando`: para cada buceador indica si está contratado y trabajando.
# * `descompresión`: para cada buceador indica si está en el proceso de descompresión.
# * `tanques_llenos`: para cada buceador indica cuantos de sus 4 tanques están llenos de aire; para cada cueva indica cuantos tanques llenos de aire hay en dicha cueva, para que un buceador los pueda coger.
# * `con_foto_de`: para cada lugar de la cueva indica si se le ha realizado o no una fotografía.

 posicion_buceador = probpl.Predicado(buceadores, cuevas | {'superficie'})
disponible = probpl.Predicado(buceadores)
trabajando = probpl.Predicado(buceadores)
descompresion = probpl.Predicado(buceadores)
tanques_llenos = probpl.Predicado(buceadores | cuevas, cantidades)
# Se podría definir dos predicados diferentes, uno para los buceadores con tanques llenos y otro con cuevas con tanques llenos
con_foto_de = probpl.Predicado(buceadores, cuevas)

estado = probpl.Estado(disponible('B0'),
                       disponible('B0'),
                       tanques_llenos('C0','0'),
                       tanques_llenos('C1','0'),
                       tanques_llenos('C2','0'),
                       tanques_llenos('C3','0'),
                       tanques_llenos('C4','0'))


# __Ejercicio 2__: implementar las siguientes acciones:
# * `contratar(B0)`: contrata al buceador `B0`, que inmediatamente se dispone a trabajar; siempre y cuando esté disponible y no haya otro buceador contratado ahora mismo. El buceador `B1` rechazará ser contratado después de él. Contratar al buceador `B0` tiene coste 10.
# * `contratar(B1)`: contrata al buceador `B1`, que inmediatamente se dispone a trabajar; siempre y cuando esté disponible y no haya otro buceador contratado ahora mismo. Contratar al buceador `B1` tiene coste 67.

 contratarB0 = probpl.AcciónPlanificación(nombre='contratar(B0)',
                                         precondicionesP=[disponible('B0')],
                                         precondicionesN=[trabajando('B0'), trabajando('B1')],
                                         efectosP=[trabajando('B0'), tanques_llenos('B0', '4')],
                                         efectosN=[disponible('B0'), disponible('B1')],
                                         coste=10)



# __Ejercicio 3__: implementar los siguientes operadores:
# * `entrar_al_agua`: un buceador contratado entra desde la superficie al sistema cavernoso, lleva sus cuatro tanques de aire llenos.
# * `bucear`: un buceador nada entre dos cuevas conectadas, gastando un tanque completo de aire.
# * `fotografiar`: un buceador fotografía una cueva, gastando un tanque completo de aire.
# * `soltar_tanque`: un buceador suelta un tanque lleno en una de las cuevas.
# * `cargar_tanque`: un buceador carga uno de sus tanques vacíos con uno lleno que se ha soltado previamente en una de las cuevas.
# * `salir_del_agua`: un buceador sale a superficie y pasa al proceso de descompresión.

 bucear2 = probpl.EsquemaPlanificación(nombre='bucear({b}, {t1}, {t2} {c1}, {c2})',
                                     precondicionesP=[tanques_llenos('{b}', '{t1}'),
                                                      trabajando('{b}'),
                                                      posicion_buceador('{b}', '{c1}')],
                                     efectosP=[posicion_buceador('{b}', '{c2}')],
                                     efectosN=[tanques_llenos('{b}', '{t1}'),
                                               posicion_buceador('{b}', '{c1}'),
                                               tanques_llenos('{b}', '{t2}')],
                                     dominio={(b, t1, t2, c1, c2)
                                              for b in buceadores
                                              for (t1, t2) in {('1', '0'),
                                                               ('2', '1'),
                                                               ('3', '2'),
                                                               ('4', '3')}
                                              for c1 in cuevas
                                              for c2 in cuevas
                                              if (c1, c2) in conexiones})


bucear = probpl.EsquemaPlanificación(
    nombre = 'bucear({b}, {t}, {t1}, {c}, {c1})',
    precondicionesP = [tanques_llenos('{b}', '{t}'), trabajando('{b}'), posicion_buceador('{b}', '{c}')],
    efectosP = [posicion_buceador('{b}', '{c1}'), tanques_llenos('{b}', '{t1}')],
    efectosN = [tanques_llenos('{b}', '{t}'), posicion_buceador('{b}', '{c}')],
    dominio={(b, t, t1,  c, c1) for b in buceadores
                           for (t, t1) in [('1', '0'), ('2', '1'), ('3', '2'), ('4', '3')]
                           for c in cuevas
                           for c1 in cuevas if (c, c1) in conexiones}
)


print(("Bucear: \n"))
print(bucear)


# __Ejercicio 4__: implementar la instancia del problema de tal manera que inicialmente los dos buceadores estén en la superficie, disponibles para ser contratados; no haya tanques llenos en las cuevas; y no se haya hecho todavía ninguna foto. El objetivo será fotografiar la cueva `C4` y que los dos buceadores estén en la superficie.

 # __Ejercicio 5__: Aplicar algún algoritmo de búsqueda en espacio de estados para encontrar un plan solución de la instancia del problema (**Nota**: una búsqueda no informada puede requerir un tiempo considerable). ¿Cuántas acciones tiene el plan resultante?. ¿Se puede alcanzar el mismo objetivo pero con una foto de la cueva `C3`?

