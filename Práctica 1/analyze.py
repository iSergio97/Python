import pandas
import numpy
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import naive_bayes
from sklearn import neighbors


datos = pandas.read_csv('insulina.csv', header=None, names=['NOC', 'MADR', 'ADES', 'DDES', 'ALM', 'ACOM', 'DCOM', 'MER', 'ACEN', 'DCEN'])

le = preprocessing.LabelEncoder()
le.fit(datos['NOC'])