from point  import Point
from vector import Vector

def main():
    v = Vector(2.0, 3.0)
    p1 = Point(2.0, 3.0)
    p2 = Point(5.0, 6.0)
    p3 = 5

    print(f'El vector {v} tiene la coordenada {v.x} y la coordenada {v.y}')
    print(repr(v))

    print(f'El punto {p1} tiene la coordenada {p1.x} y la coordenada {p1.y}')
    print(repr(p1))

    print(f'Los valores hash de v y p1 son {hash(v)} y {hash(p1)}')
    print(f'La distancia del punto {p1} al punto {p2} es {p1.distance(p2)}')

    print(f'La resta de los puntos {p1} y {p2} es {p1-p2}')
    print(f'La resta de los puntos {p1} y {p3} es {p1-p3}')

if __name__ == "__main__":
    main()