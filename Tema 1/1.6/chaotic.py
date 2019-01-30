__author__ = "Sergio Garrido Domínguez"

def main():
    print("Testing the chaotic behaviour")
    x = eval(input("Enter a number between 0 and 1: "))
    if x < 0 or x > 1:
        pass
        print("The number is less than 0 or higher than 1")
    else:
        for i in range(10):
            x = 3.9 * x * (1 - x)
            print(x)


#Note: Leave to blank lines between the end function and the next instruction
#main()