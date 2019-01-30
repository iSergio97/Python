#futVal.py
#A program to calculate the value of an investment
#Input(s) a number
#Output(s) a Fahrenheit temp
__author__ = "Sergio Garrido Domínguez"

def futVal():
    actualVal = eval(input("Introduce the amount you will investment: "))
    temp = eval(input("Now, introduce the life-year of this investment: "))
    intRate = eval(input("Finally, introduce the annual interest rate in %: "))

    for i in range(temp):
        actualVal = actualVal*(1 + intRate/100)
        print("Year", str(i + 1) + ":", "Actual ammount: " + str(actualVal))


futVal()