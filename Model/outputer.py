from abc import ABCMeta
from abc import abstractmethod

class Outputer(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, output_path):
        self.output_path = output_path

    @abstractmethod
    def output(self):
        pass
    
    