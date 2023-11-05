import math
from typing import Self

class Vector():
    def __init__(self, x: float, y:float):
        # _x, _y son atributos privados.
        self._x:float = x
        self._y:float = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def mod(self) -> float:
        return math.sqrt(self.x**2 * self.y**2)

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __le__(self, other: Self) -> bool:
        return self.mod <= other.mod

    def __hash__(self):
        return hash((self.x, self.y, self.mod))

    def __add__(self, other: Self) -> Self:
        """
        Suma de vectores
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        """
        Resta de vectores
        """
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self) -> Self:
        """
        Vector inverso
        """
        return Vector(-self.x, -self.y)

    def __rmul__(self, other: float) -> Self:
        """
        Producto de escalar (real) por vector
        """
        return Vector(other * self.x, other * self.y)

    def __mul__(self, other: Self) -> float:
        """
        Producto escalar de vectores
        """
        return self.x * other.x + self.y * other.y

    def __repr__(self) -> str:
        return f'V({self.x}, {self.y})'

    def __str__(self) -> str:
        return f'({self.x:.4f}, {self.y:.4f})'