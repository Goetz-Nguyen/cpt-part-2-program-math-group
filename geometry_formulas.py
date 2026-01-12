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
        Method for solving the perimeter of a rectangle
        """
        r_perimeter = 2 * (self._length + self._width)
        print(f"The perimeter of the rectangle is {r_perimeter} units.")
    def rectangle_area(self):
        """
        Method for solving the area of a rectangle
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
        """
        Method for solving the perimeter of a square
        """
        sq_perimeter = 4 * self._s
        print(f"The perimeter of the square is {sq_perimeter} units.")
    def square_area(self):
        """
        Method for solving the area of a square
        """
        sq_area = self._s**2
        print(f"The area of the square is {sq_area} units.")

class Triangle:
    """
    A class that handles on solving the perimeter and area of a triangle

    Attributes:
        a (int): Side 'a' value
        b (int): Side 'b' value
        c (int): Side 'c' value

    Invariants:
        - Cannot have an empty input 
        - Cannot have a negative input
    """ 
    def __init__(self, a: int, b: int, c: int):
        """
        Initializes the value of the side of a square
        """
        self._a = a
        self._b = b
        self._c = c
        self._base = b
        self._height = 2 * (self._a / self._b)
    def triangle_perimeter(self):
        """
        Method for solving the perimeter of a triangle
        """
        t_perimeter = self._a + self._b + self._c
        print(f"The perimeter of the triangle is {t_perimeter} units")
    def triangle_area(self):
        """
        Method for solving the area of a triangle
        """
        t_area = (self._base * self._height) / 2
        print(f"The area of the triangle is {t_area:.2f} units")
    def get_height(self) -> int:
        """
        Getting the height of the triangle
        """
        return self._height

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
    def __init__(self, radius: int) -> None:
        """
        Initializes the value of values of the diameter, radius, and circumference of a circle
        """
        self._radius = radius
        self.pi = math.pi
        self._diameter = 2 * self._radius
        self._circumference = 2 * self.pi * self._radius
    def get_cicumference(self) -> int:
        """
        Method for returning the circumference 
        """
        print(f"The circumference of the circle is {self._circumference:.2f} units")
    def get_diameter(self) -> int:
        """
        Method for returning the diameter 
        """
        print(f"The diameter of the circle is {self._diameter:.2f} units")
    def circle_area(self):
        """
        Method for solving the area of a circle
        """
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
        Initializes the value of the side of a cube
        """
        super().__init__(s)
    def cube_volume(self):
        """
        Method for solving the volume of a cube
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
        Method of solving the volume of a rectangular prism
        """
        r_prism_volume = self._length * self._width * self._height
        print(f"The volume of the rectangular prism is {r_prism_volume} units.")
    def rect_prism_surface_area(self):
        """
        Method of solving the surface area of a rectangular prism
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
        Initializes the value of the radius and height of a cylinder
        """
        self._radius = radius
        self._height = height
    def cylinder_volume(self):
        """
        Method for solving the volume of a cylinder 
        """
        cy_volume = math.pi * self._radius**2 * self._height
        print(f"The volume of the cylinder is {cy_volume:.2f} units.")
    def cylinder_surface_area(self):
        """
        Method for solving the surface area of a cylinder 
        """
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
        Initializes the value of the radius and height of a cone
        """
        super().__init__(radius, height)
    def cone_volume(self):
        """
        Method for solving the volume of a cone
        """
        cne_volume = math.pi * self._radius**2 * (self._height / 3)
        print(f"The volume of the cone is {cne_volume:.2f} units")
    def cone_surface_area(self):
        """
        Method for solving the surface area of a cone 
        """
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
                    sq1 = int(input("Enter side length: "))
                    if sq1 < 0:
                        print("Cannot input any negative numbers")
                        sq1 = int(input("Enter side length: "))
                    sq_value = Square(sq1)
                    sq_value.square_perimeter()
                    sq_value.square_area()
                except:
                    print("Please enter a valid input")
            case "Rectangle":
                try:
                    rect1 = int(input("Enter length: ")), int(input("Enter width: "))
                    print(rect1)
                    while rect1 < 0:
                        print("Cannot input any negative numbers")
                        rect1 = int(input("Enter length: ")), int(input("Enter width: "))
                    rect_value = Rectangle(rect1)
                    rect_value.rectangle_area()
                    rect_value.rectangle_perimeter()
                except:
                    print("Please enter a valid input")

            case "Triangle":
                try:
                    tri1 = int(input("Enter side a: ")), int(input("Enter side b: ")), int(input("Enter side c: "))
                    while tri1 < 0:
                        print("Cannot input any negative numbers")
                        tri1 = int(input("Enter side a: ")), int(input("Enter side b: ")), int(input("Enter side c: "))
                    tri_value = Triangle(tri1)
                    tri_value.triangle_perimeter()
                    tri_value.triangle_area()
                except:
                    print("Please enter a valid input")

            case "Circle":
                try:
                    cir1 = int(input("Enter radius: "))
                    if cir1 < 0:
                        print("Cannot input any negative numbers")
                        cir1 = int(input("Enter radius: "))
                    cir_value = Circle(cir1)
                    cir_value.get_diameter()
                    cir_value.get_cicumference()
                    cir_value.circle_area()
                except: 
                    print("Please enter a valid input")

            case "Cube":
                try: 
                    cub = int(input("Enter side value: "))
                    if cub < 0:
                        print("Cannot input any negative numbers")
                        cub = int(input("Enter side value: "))
                    cub_value = Cube(cub)
                    cub_value.cube_volume()
                    cub_value.cube_surface_area()
                except:
                    print("Please enter a valid input")

            case "Rectangular Prism":
                try: 
                    rectangular_p = int(input("Enter length: ")), int(input("Enter width: ")), int(input("Enter height: "))
                    while rectangular_p < 0:
                        print("Cannot input any negative numbers")
                        rectangular_p = int(input("Enter length: ")), int(input("Enter width: ")), int(input("Enter height: "))
                    rectangular_p_value = Rectangular_Prism(int(input("Enter length: ")), int(input("Enter width: ")), int(input("Enter height: ")))
                    rectangular_p_value.rect_prism_volume()
                    rectangular_p_value.rect_prism_surface_area()
                except:
                    print("Please enter a valid input")

            case "Circular Cylinder":
                try:
                    cylinder = int(input("Enter radius: ")), int(input("Enter height:  "))
                    while cylinder < 0:
                        print("Cannot input any negative numbers")
                        cylinder = int(input("Enter radius: ")), int(input("Enter height:  "))
                    cylinder_value = Circular_cylinder(int(input("Enter radius: ")), int(input("Enter height:  ")))
                    cylinder_value.cylinder_volume()
                    cylinder_value.cylinder_surface_area()
                except:
                    print("Please enter a valid input")

            case "Cone":
                try:
                    cne = int(input("Enter radius: ")), int(input("Enter height: "))
                    while cne < 0:
                        print("Cannot input any negative numbers")
                        cne = int(input("Enter radius: ")), int(input("Enter height: "))
                    cone_value = Cone(int(input("Enter radius: ")), int(input("Enter height:  ")))
                    cone_value.cylinder_volume()
                    cone_value.cylinder_surface_area()
                except:
                    print("Please enter a valid input")

            case "Exit":
                return

if __name__ == "__main__":
    main()