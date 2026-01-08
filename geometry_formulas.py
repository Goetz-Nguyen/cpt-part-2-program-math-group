import math
from InquirerPy import prompt
# Prompt Input
def promptinput(message,choices):
    """Creates a prompt of choices

    Args:
        message(str): Message to ask
        choices(list): Choices to make
    Return:
        (str): Choice made by user
    """
    user_input = [
        {
            "type": "list",
            "message": message,
            "choices": choices
        }
    ] 
    return prompt(user_input)[0] # Return chosen answer
# Geometry
class Rectangle:
    """
    A class that handles on solving the perimeter and area of a rectangle

    Attributes:
        length (int): Length of the rectangle 
        width (int): Width of the rectangle

    Invariants:
        - Cannot have an empty input 
        - Cannot have a negative input
    """       
    def __init__(self, length: int, width: int) -> None:
        """
        Initializes the value of length and width of the rectangle
        """
        self._length = length
        self._width = width
    def rectangle_perimeter(self):
        """
        Method for solving the perimeter of the rectangle
        """
        r_perimeter = 2 * (self._length + self._width)
        print(f"The perimeter of the rectangle is {r_perimeter} units.")
    def rectangle_area(self):
        """
        Method for solving the area of the rectangle
        """
        r_area = self._length * self._width
        print(f"The area pf the rectangle is {r_area} units.")


class Square:
    """
    A class that handles on solving the perimeter and area of a square

    Attributes:
        s (int): Side of the square

    Invariants:
        - Cannot have an empty input 
        - Cannot have a negative input
    """    
    def __init__(self, s: int):
        """
        Initializes the value of the side of a square
        """
        self._s = s
    def square_perimeter(self):
        sq_perimeter = 4 * self._s
        print(f"The perimeter of the square is {sq_perimeter} units.")
    def square_area(self):
        sq_area = self._s**2
        print(f"The area of the square is {sq_area} units.")

class Triangle:
    """
    A class that handles on solving the perimeter and area of a triangle

    Attributes:
        a (int): Side 'a' value
        b (int): Side 'b' value
        c (int): Side 'c' value
        base (int): Base of the triangle
        height (int): Height of the triangle

    Invariants:
        - Cannot have an empty input 
        - Cannot have a negative input
    """ 
    def __init__(self, a: int, b: int, c: int, base:int , height: int):
        """
        Initializes the value of the side of a square
        """
        self._a = a
        self._b = b
        self._c = c
        self._base = base
        self._height = height
    def triangle_perimeter(self):
        t_perimeter = self._a + self._b + self._c
        print(f"The perimeter of the triangle is {t_perimeter} units")
    def triangle_area(self):
        t_area = (self._base * self._height) / 2
        print(f"The area of the triangle is {t_area:.2f} units")

class Circle:
    """
    A class that handles on solving the diameter, radius, and circumference of a circle

    Attributes:
        length (int): Length of the rectangle 
        width (int): Width of the rectangle

    Invariants:
        - Cannot have an empty input 
        - Cannot have a negative input
    """ 
    def __init__(self, diameter: int, radius: int, circumference: int) -> None:
        """
        Initializes the value of values of the diameter, radius, and circumference of a circle
        """
        self._diameter = diameter
        self._radius = radius
        self._circumference = circumference
        self.pi = math.pi
    def diameter(self):
        cir_diameter = 2 * self._radius
        print(f"The diameter of the circle is {cir_diameter:.2f} units.")
    def circumference(self):
        cir_circumference = 2 * self.pi * self._radius
        print(f"The circumference of the circle is {cir_circumference:.2f} units.")
    def radius(self):
        cir_radius = self._circumference / (2 * self.pi)
        print(f"The circumference of the circle is {cir_radius:.2f} units.")
    def circle_area(self):
        cir_area = self.pi * self._radius**2
        print(f"The area of the circle is {cir_area:.2f} units.")


# 3D Shapes
class Cube(Square):
    """
    A class that handles on solving the volume and surface area of the cube

    Attributes:
        s (int): Side of the cube

    Invariants:
        - Cannot have an empty input 
        - Cannot have a negative input
    """ 
    def __init__(self, s: int):
        """
        Initializes the value of the side of the cube
        """
        super().__init__(s)
    def cube_volume(self):
        """
        Method for solving the colume of the cube
        """
        c_volume = self._s**3
        print(f"The volume of the cube is {c_volume} units.")
    def cube_surface_area(self):
        """
        Method for solving the surface area of the cube 
        """
        c_surface_area = 6*self._s**2
        print(f"The surface area of the cube is {c_surface_area} units.")

class Rectangular_Prism(Rectangle):
    """
    A class that handles on solving the volume and surface area of the rectangular prism

    Attributes:
        length (int): Length of the rectangular prism
        width (int): Width of the rectangular prism
        height (int): Height of the rectangular prism

    Invariants:
        - Cannot have an empty input 
        - Cannot have a negative input
    """ 
    def __init__(self, length: int, width: int, height: int):
        """
        Initializes the value of the length, width, and height of the rectangular prism
        """
        super().__init__(length, width)
        self._height = height
    def rect_prism_volume(self):
        """
        Method of solving the volume of the rectangular prism
        """
        r_prism_volume = self._length * self._width * self._height
        print(f"The volume of the rectangular prism is {r_prism_volume} units.")
    def rect_prism_surface_area(self):
        """
        Method of solving the surface area of the rectangular prism
        """
        r_prism_surface_area = 2*(self._length * self._width) + 2*(self._length * self._height) + 2*(self._width * self._height)
        print(f"The surface area of the rectangle is {r_prism_surface_area} units. ")

class Circular_cylinder:
    """
    A class that handles on solving the volume and surface area of a circular cylinder

    Attributes:
        radius (int): Radius of the circular cylinder
        height (int): Height of the circular cylinder

    Invariants:
        - Cannot have an empty input 
        - Cannot have a negative input
    """ 
    def __init__(self, radius: int, height:int):
        """
        Initializes the value of the radius and height of the cylinder
        """
        self._radius = radius
        self._height = height
    def cylinder_volume(self):
        cy_volume = math.pi * self._radius**2 * self._height
        print(f"The volume of the cylinder is {cy_volume:.2f} units.")
    def cylinder_surface_area(self):
        cy_surface_area = (2 *  math.pi * self._radius * self._height) + (2 * math.pi * self._radius**2)
        print(f"The surface area of the cylinder is {cy_surface_area:.2f} units.")

class Cone(Circular_cylinder):
    """
    A class that handles on solving the volume and surface area of a cone

    Attributes:
        radius (int): Radius of the circular cylinder
        height (int): Height of the circular cylinder

    Invariants:
        - Cannot have an empty input 
        - Cannot have a negative input
    """ 
    def __init__(self, radius: int, height: int):
        """
        Initializes the value of the radius and height of the cone
        """
        super().__init__(radius, height)
    def cone_volume(self):
        cne_volume = math.pi * self._radius**2 * (self._height / 3)
        print(f"The volume of the cone is {cne_volume:.2f} units")
    def cone_surface_area(self):
        cne_surface_area = math.pi * self._radius * math.sqrt(self._height**2 + self._radius**2)
        print(f"The surface area of the cone is {cne_surface_area:.2f} units.")


def main():
    while True:
        shapeslist = ["Square", "Rectangle", "Triangle", "Circle", "Cube", "Rectangular Prism",
                    "Circular Cylinder", "Cone", "Exit"]
        menu = promptinput("Pick shape:", shapeslist)
        match menu:
            case "Square":
                try: 
                    sq1 = Square(int(input("Enter side length: ")))
                except:
                    print("Enter valid numbers")
                sq1.square_perimeter()
                sq1.square_area()
            case "Rectangle":
                try:
                    rect1 = Rectangle(int(input("Enter length: ")), int(input("Enter width: ")))
                except:
                    print("Enter valid numbers")
                rect1.rectangle_area()
                rect1.rectangle_perimeter()
            case "Triangle":
                try:
                    tri1 = Triangle(int(input("Enter side a: ")), int(input("Enter side b: ")), int(input("Enter side c: ")), int(input("Enter base: ")), int(input("Enter height: ")))
                except:
                    print("Enter valid numbers")
                tri1.triangle_perimeter()
                tri1.triangle_area()
            case "Circle":
                try:
                    cir1 = Circle(int(input("Enter diameter: ")), int(input("Enter radius: ")), int(input("Enter circumference: ")))
                except: 
                    print("Enter valid numbers")
                cir1.diameter()
                cir1.circumference()
                cir1.radius()
                cir1.circle_area()
            case "Cube":
                try: 
                    cub = Cube(int(input("Enter side value: ")))
                except:
                    print("Invalid Value")
                cub.cube_volume()
                cub.cube_surface_area()
            case "Rectangular Prism":
                try: 
                    rectangular_p = Rectangular_Prism(int(input("Enter length: ")), int(input("Enter width: ")), int(input("Enter height: ")))
                except:
                    print("Invalid value")
                rectangular_p.rect_prism_volume()
                rectangular_p.rect_prism_surface_area()
            case "Circular Cylinder":
                try:
                    cylinder = Circular_cylinder(int(input("Enter radius: ")), int(input("Enter height:  ")))
                except:
                    print("Enter valid number")
                cylinder.cylinder_volume()
                cylinder.cylinder_surface_area()
            case "Cone":
                try:
                    cne = Cone(int(input("Enter radius: ")), int(input("Enter height: ")))
                except:
                    print("Enter valid values")
                cne.cone_volume()
                cne.cone_surface_area()
            case "Exit":
                return

if __name__ == "__main__":
    main()