import math
# Geometry
class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self._length = length
        self._width = width
    def rectangle_perimeter(self):
        r_perimeter = 2 * (self._length + self._width)
        print(r_perimeter)
    def rectangle_area(self):
        r_area = self._length * self._width
        print(r_area)
rect1 = Rectangle(4,2)
rect1.rectangle_area()
rect1.rectangle_perimeter()
class Square:
    def __init__(self, s: int):
        self._s = s
    def square_perimeter(self):
        sq_perimeter = 4 * self._s
        print(sq_perimeter)
    def square_area(self):
        sq_area = self._s**2
        print(sq_area)
sq1 = Square(6)
sq1.square_perimeter()
sq1.square_area()
class Triangle:
    def __init__(self, a: int, b: int, c: int, base:int , height: int,):
        self._a = a
        self._b = b
        self._c = c
        self._base = base
        self._height = height
    def triangle_perimeter(self):
        t_perimeter = self._a + self._b + self._c
        print(t_perimeter)
    def triangle_area(self):
        t_area = (self._base * self._height) / 2
        print(f"{t_area:.2f}")
tri1 = Triangle(1, 2, 3, 4, 5)
tri1.triangle_perimeter()
tri1.triangle_area()
class Circle:
    def __init__(self, diameter: int, radius: int, circumference: int) -> None:
        self._diameter = diameter
        self._radius = radius
        self._circumference = circumference
        self.pi = math.pi
    def diameter(self):
        cir_diameter = 2 * self._radius
        print(f"{cir_diameter:.2f}")
    def circumference(self):
        cir_circumference = 2 * self.pi * self._radius
        print(f"{cir_circumference:.2f}")
    def circle_area(self):
        cir_area = self.pi * self._radius**2
        print(f"{cir_area:.2f}")
cir1 = Circle(2, 6, 9)
cir1.diameter()
cir1.circumference()
cir1.circle_area()
# 3D Shapes
class Cube(Square):
    def __init__(self, s: int):
        super().__init__(s)
    def cube_volume(self):
        c_volume = self._s**3
        print(c_volume)
    def cube_surface_area(self):
        c_surface_area = 6*self._s**2
        print(c_surface_area)
cub = Cube(2)
cub.cube_volume()
cub.cube_surface_area()
class Rectangular_Prism(Rectangle):
    def __init__(self, length: int, width: int, height: int):
        super().__init__(length, width)
        self._height = height
    def rect_prism_volume(self):
        r_prism_volume = self._length * self._width * self._height
        print(r_prism_volume)
    def rect_prism_surface_area(self):
        r_prism_surface_area = 2(self._length * self._width) + 2(self._length * self._height) + 2(self._width * self._height)
        print(r_prism_surface_area)
class Pyramid(Triangle):
    def __init__(self, base: int, height: int, length: int, width: int):
        super().__init__(base, height)
        self._length = length
        self._width = width
    def pyramid_volume(self):
        p_volume = (self._length * self._base * self._height) / 3
        print(p_volume)
    def pyramid_surface_area(self):
        p_surface_area = (self._length * self._width) * math.sqrt(self.)