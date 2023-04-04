import abc


class Flyweight(metaclass=abc.ABCMeta):
    """
    Declare an interface through which flyweights can receive and act on
    extrinsic state.
    """

    def __init__(self):
        self.intrinsic_state = None

    @abc.abstractmethod
    def set_color(self, color):
        pass

    @abc.abstractmethod
    def set_shape(self, shape):
        pass
