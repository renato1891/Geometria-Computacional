class Ponto():

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def printa(self):
        print('{0} and {1}'.format(self.getX(), self.getY()))



