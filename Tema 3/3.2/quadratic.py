__author__ = "Sergio Garrido Domínguez"

#  quadratic.py
#  A program to compute the real roots of a quadratic equation
#  Input(s) the values of the numbers of the equation
#  Output(s) the roots of the equation
#  Note: This .py only solve equations with real solutions

import math

def quadratic():
    a,b,c = eval(input("Enter the coefficients like (a, b, c) : "))

    discRoot = math.sqrt(b ^ 2 - 4 * a * c)
    root1 = (-b + discRoot) / (2*a)
    root2 = (-b + discRoot) / (2*a)

    print("The roots are", root1, root2)


quadratic()