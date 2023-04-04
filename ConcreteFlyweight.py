from Flyweight import Flyweight


class ConcreteFlyweight(Flyweight):

    def __int__(self):
        super().__init__()
        self.color = None
        self.shape = ""

    def set_color(self, color):
        if color == "white":
            self.color = (255, 255, 255)
        elif color == "black":
            self.color = (0, 0, 0)
        elif color == "red":
            self.color = (247, 21, 45)

    def set_shape(self, shape):
        self.shape = shape
