__author__ = "Sergio Garrido Domínguez"

#  change.py
#  A program to calculate the value of an account of coins in dollars
#  Input(s) an amount of quarters, another of dimes, another of nickels and the last one of pennies
#  Output(s) the amount of dollars you have

def change():
    print("Money change")
    quarters = eval(input("Introduce the amount of Quarters "))
    dimes = eval(input("Introduce the amount of Dimes "))
    nickels = eval(input("Introduce the amount of Nickles "))
    pennies = eval(input("Introduce the amount of Pennies "))

    print("The amount is:", quarters*.25 + dimes*0.1 + nickels*.05 + pennies*.01)


change()
