import math
from vector import Vector
from typing import Self

class Point():
    def __init__(self, x: float, y:float):
        # _x, _y son atributos privados.
        self._x:float = x
        self._y:float = y

    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value

    def __sub__(self, other: Self) -> Vector:
        """
        Resta de puntos
        """
        if not isinstance(other, Point):
            raise TypeError(f'El objeto {other} no es un punto')
        else:
            return Vector(self.x - other.x, self.y - other.y)
    
    def distance(self, other: Self) -> float:
        """
        Distancia entre dos puntos:

        """
        if not isinstance(other, Point): 
            raise TypeError(f'El objeto {other} no es un punto')
        else: 
            return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self) -> str:
        return f'P({self.x}, {self.y})'

    def __str__(self) -> str:
        return f'({self.x:.4f}, {self.y:.4f})'
 
