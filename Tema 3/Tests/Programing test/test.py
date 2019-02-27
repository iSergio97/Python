import math
import random
import networkx as nx
import time
import matplotlib.pyplot as plt

def pobIni(num_p, num_v):
    poblacion=[]
    for i in range (num_p):
        cromosoma=[]
        for j in range (num_v):
            num = random.randint(0,2)
            cromosoma.append(num)
            poblacion.append(cromosoma[:])
    return poblacion