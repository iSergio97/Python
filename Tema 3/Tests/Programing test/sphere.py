__author__ = "Sergio Garrido Domínguez"


# factorial.py
# A program to compute factorial of a number
# Input(s) the radius
# Output(s) the area and volume of the sphere
import math

def areaAndVolume():
    radius = eval(input("Introduce the radius of the sphere "))
    pi = math.pi
    volume = 4/3 * pi * radius*radius*radius
    area = 4 * pi * math.sqrt(radius)
    print("Area is", area)
    print("Volume is", volume)


areaAndVolume()