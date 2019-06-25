__author__ = "Sergio Garrido Domínguez"


#  factorial.py
#  A program to compute factorial of a number
#  Input(s) a number
#  Output(s) the solution of the factorial of this number

def factorial():
    number = eval(input("Introduce the number: "))
    #  for fact in range(fact, 1, 1): In this case, we first need to ifelse if the fact is > 0
    fact = 1
    for factor in range(number, 1, -1):
        fact = fact * factor
    print("The factorial of", number, "is", fact)


factorial()
