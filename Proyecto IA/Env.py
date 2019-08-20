import numpy as np

class Env():
    def __init__(self):
        # self.height = int(input("Introduzca la altura "))
        self.height = 3
        # self.width = int(input("Introduzca la anchura "))
        self.width = 3
        self.posX = 0
        self.posY = 0
        # self.endX = int(input("Introduzca el valor de la posición final X "))
        self.endX = 2
        # self.endY = int(input("Introduzca el valor de la posición final Y "))
        self.endY = 2
        self.actions = [0, 1, 2, 3]
        self.stateCount = self.height*self.width
        self.actionCount = len(self.actions)
        fila = []
        self.mapa = []
        for i in range(self.height):
            for j in range(self.width):
                a = input("El coste de la posición (" + str(i) + ", " + str(j) + "):")
                b = int(a)
                fila.append(b)
            self.mapa.append(fila)
            fila = []

        self.cost = self.mapa[self.posX][self.posY]

    def reset(self):
        # self.posX = int(input("Introduzca el valor de la posición inicial X "))
        self.posX = 0
        # self.posY = int(input("Introduzca el valor de la posición inicial Y "))
        self.posY = 0
        self.done = False
        self.cost = 0
        # posx, posy, done
        return 0, 0, False, 0

    # take action
    def step(self, action):
        if action == 0:  # left
            self.posX = self.posX - 1 if self.posX > 0 else self.posX
        if action == 1:  # right
            self.posX = self.posX + 1 if self.posX < self.width-1 else self.posX
        if action == 2:  # up
            self.posY = self.posY - 1 if self.posY > 0 else self.posY
        if action == 3:  # down
            self.posY = self.posY + 1 if self.posY < self.height-1 else self.posY

        done = self.posX == self.endX and self.posY == self.endY
        # mapping (x,y) position to number between 0 and 5x5-1=24
        nextState = self.width*self.posY + self.posX
        reward = 1 if done else 0
        cost = self.cost + self.mapa[self.posX][self.posY]
        return nextState, reward, done, cost

    # return a random action
    def randomAction(self):
        return np.random.choice(self.actions)

    # display environment
    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.posY == i and self.posX == j:
                    print("O", end='')
                elif self.endY == i and self.endX == j:
                    print("T", end='')
                else:
                    print(".", end='')
            print("")