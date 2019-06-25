# Converter.py
# A program to convert temperatures from Fahrenheit to Celsius
# Input(s) a number
# Output(s) a Celsius temp
__author__ = "Sergio Garrido Domínguez"

def converterToCelsius():
    x = eval(input("Write the actual temperature: "))
    # y = 5/9 * (x - 32)
    # print(y)
    print(5/9 * (x - 32))


converterToCelsius()