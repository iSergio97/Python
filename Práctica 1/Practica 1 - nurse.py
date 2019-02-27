from builtins import print

import pandas
import numpy
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import naive_bayes
from sklearn import neighbors


print("\nIn 1")
nurse = pandas.read_csv('nurse.csv', header=None, names=['parents', 'has_nurse', 'form', 'children', 'housing', 'fiance', 'social', 'health'])
print(nurse.shape)  # Número de filas y columnas
nurse.head(10)

#
#print("\nIn 2")
#le = preprocessing.LabelEncoder()  # Creamos un codificador de etiquetas
#le.fit(nurse['buying'])  # Calculamos la codificación de cada valor
#print(le.classes_)
#print(le.transform(['vhigh', 'med', 'high', 'low', 'vhigh']))  # Codificamos los valores
#print(le.inverse_transform([3, 2, 0, 1, 3]))  # Descodificamos los códigos


print("\nIn 3")
codificadores = []
nurse_codificado = pandas.DataFrame()
for variable, valores in nurse.iteritems():
    le = preprocessing.LabelEncoder()
    le.fit(valores)
    print('Codificación de valores para {}: {}'.format(variable, le.classes_))
    codificadores.append(le)
    nurse_codificado[variable] = le.transform(valores)

nurse_codificado.head(10)

# Si no es necesario conservar los codificadores, la siguiente es una manera más
# directa de codificar las variables
# le = preprocessing.LabelEncoder()
# nurse_codificado = nurse.apply(le.fit_transform, axis=0)


print("\nIn 4")
print('Codificación:', codificadores[-1].classes_)
print(nurse_codificado.shape[0])  # Cantidad total de ejemplos
print(nurse_codificado['C'].value_counts(
        normalize=True, sort=False))  # Frecuencia total de cada clase de aceptabilidad

nurse_entrenamiento, nurse_prueba = model_selection.train_test_split(
    nurse_codificado, test_size=.33, random_state=12345,
    stratify=nurse_codificado['acceptability'])

# Comprobamos que el conjunto de prueba contiene el 33 % de los datos, en la misma proporción
# con respecto a la variable objetivo
print(nurse_prueba.shape[0], 12960*.2)
print(nurse_prueba['acceptability'].value_counts(
        normalize=True, sort=False))

# Comprobamos que el conjunto de entrenamiento contiene el resto de los datos, en la misma
# proporción con respecto a la variable objetivo
print(nurse_entrenamiento.shape[0], 12960 * (1 - .2))
print(nurse_entrenamiento['acceptability'].value_counts(
        normalize=True, sort=False))

print("\nIn 5")
datos_entrenamiento = nurse_entrenamiento.loc[:, 'buying':'safety']
print("Datos de entrenamiento")
print(datos_entrenamiento)
print("\n")

clases_entrenamiento = nurse_entrenamiento['acceptability']
print("Clases de entrenamiento")
print(clases_entrenamiento)
print("\n")

datos_prueba = nurse_prueba.loc[:, 'buying':'safety']
print("Datos de prueba")
print(datos_prueba)
print("\n")

clases_prueba = nurse_prueba['acceptability']
print("Clases de prueba")
print(clases_prueba)
print("\n")

print("\nIn 6")
clasif_NB = naive_bayes.MultinomialNB(alpha=1.0)  # alpha es el tamaño muestral equivalente
print(clasif_NB)


print("\nIn 7")
ohe = preprocessing.OneHotEncoder(sparse=False)
print(ohe)


print("\nIn 8")
# En las expresiones siguientes, el método values proporciona los datos como un vector de
# numpy y el método reshape lo transforma entonces a una matriz con una columna y tantas
# filas como sea necesario. Esto debe hacerse ya que el preprocesador OneHotEncoder solo
# trabaja con matrices.
print(nurse_codificado['buying'].values)
print(nurse_codificado['buying'].values.reshape(-1, 1))
ohe.fit(nurse_codificado['buying'].values.reshape(-1, 1))
ohe.transform(nurse_codificado['buying'].values.reshape(-1, 1))

print("\nIn 9")
ohe = preprocessing.OneHotEncoder(sparse=False)
# El método fit_transform realiza un ajuste a partir de una matriz de datos seguido de una
# transformación de esos mismos datos.
datos_entrenamiento_nb = ohe.fit_transform(datos_entrenamiento)
datos_prueba_nb = ohe.fit_transform(datos_prueba)

print(datos_entrenamiento)
print(datos_prueba_nb)

print("\nIn 10")
clasif_NB.fit(datos_entrenamiento_nb, clases_entrenamiento)


print("\nIn 11")
print(clasif_NB.class_count_)
print(clasif_NB.class_log_prior_)
print(clasif_NB.feature_count_)
print(clasif_NB.feature_log_prob_)


print("\nIn 12")
nuevo_ejemplo = ['vhigh', 'vhigh', '3', 'more', 'big', 'high']
# Codificamos los valores de los atributos
nuevo_ejemplo_codif = [le.transform([valor])
                       for valor, le in zip(nuevo_ejemplo, codificadores)]
nuevo_ejemplo_codif = numpy.reshape(nuevo_ejemplo_codif, (1, -1))
print(nuevo_ejemplo_codif)
# Transformamos los atributos a codificación binaria
nuevo_ejemplo_nb = ohe.transform(nuevo_ejemplo_codif)
print(nuevo_ejemplo_nb)
# Predecimos la clase
clase_nuevo_ejemplo = clasif_NB.predict(nuevo_ejemplo_nb)
print(codificadores[-1].inverse_transform(clase_nuevo_ejemplo))


print("\nIn 13")
# Calculamos la fracción de clases correctamente predichas para el conjunto de datos de prueba
print(clasif_NB.score(datos_prueba_nb, clases_prueba))

print("\nIn 14")
clasif_kNN = neighbors.KNeighborsClassifier(n_neighbors=5, metric='hamming')
print(clasif_kNN)


print("\nIn 15")
print(clasif_kNN.fit(datos_entrenamiento, clases_entrenamiento))


print("\nIn 16")
distancias, vecinos = clasif_kNN.kneighbors(nuevo_ejemplo_codif)
print(nuevo_ejemplo_codif)
print(datos_entrenamiento.iloc[vecinos[0]])
print(distancias[0])


print("\nIn 17")
clase_nuevo_ejemplo = clasif_kNN.predict(nuevo_ejemplo_codif)
print(codificadores[-1].inverse_transform(clase_nuevo_ejemplo))


print("\nIn 18")
print(clasif_kNN.score(datos_prueba, clases_prueba))


print("\n Ejercicio propuesto")
for i in range(0, 10):
    clasKN = neighbors.KNeighborsClassifier(n_neighbors=i+1, metric="hamming")
    vs = model_selection.cross_val_score(clasKN, nurse, clases_entrenamiento, cv=10)
    print(vs.mean())

