#Converter.py
#A program to convert temperatures from Celsius to Fahrenheit
#Input(s) a number
#Output(s) a Fahrenheit temp
__author__ = "Sergio Garrido Domínguez"

def converterToFahrenheit():
    x = eval(input("Write the actual temperature: "))
    print(x*9/5 + 32)


converterToFahrenheit()
