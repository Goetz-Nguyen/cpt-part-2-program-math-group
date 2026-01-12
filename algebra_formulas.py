import math
from math import factorial
from InquirerPy import prompt
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

class Quadratics:
    """
    A class that handles the quadratic formula

    Attributes:
        a (int): Value of a
        b (int): Value of b
        c (int): Value of c

    Invariants:
        - Cannot have an empty input 
 
    """
    def __init__(self, a: int, b: int, c: int) -> None:
        """
        Initializes the values of A, B, and C
        """
        self._a = a
        self._b = b
        self._c = c
    def quadratic(self):
        """
        Method for the quadratic formula
        """
        discriminant = (self._b**2) - (4*self._a*self._c)
        if discriminant < 0:
            print("It has 0 solutions")

        elif discriminant == 0:
            print("It has 1 solution.")
        else:
            print("It has 2 solutions.")
        
            quad_1 = ((-1 *self._b)+math.sqrt(discriminant))/(2*self._a)
            quad_2 = ((-1 * self._b)-math.sqrt(discriminant))/(2*self._a)
            sol = (f"The solutions are {round(quad_1, 2)} and {round(quad_2,2)}")
            print(sol)

class Pythagorean:
    """
    A class that handles the Pythagorean Theorem

    Attributes:
        a (int): Value of a
        b (int): Value of b
        c (int): Value of c

    Invariants:
        - Cannot have an empty input 
 
    """    
    def __init__(self, a: int, b: int, c: int) -> None:
        """
        Initializes the values of A, B, and C
        """
        self._a = a
        self._b = b
        self._c = c
    def pythagorean_theorem(self):
        """
        Method for solving the Pythagorean Theorem
        """
        side = input("Which side to solve?: [a,b,c] ")
        if side.lower() == "c":
            py_theorem = math.sqrt(self._a**2 + self._b**2)
            print(f"The length of C is {py_theorem:.2f}")
        elif side.lower() == "a":
            py_theorem = math.sqrt(self._c**2 - self._b**2)
            print(f"The length of A is {py_theorem:.2f}")
        elif side.lower() == "b":
            py_theorem = math.sqrt(self._c**2 - self._a**2)
            print(f"The length of B is {py_theorem:.2f}")

class Pascals_Triangle:
    """
    A class that handles on printing the Pascal's Triangle

    Attributes:
        n(int): The number of rows 

    Invariants:
        - Cannot have an empty input 
        - Cannot have a negative input

    """    
    #https://www.geeksforgeeks.org/python/python-program-to-print-pascals-triangle/
    def __init__(self, n: int):
        """
        Initializes the value of n
        """
        self.n = n
    def printing_triangle(self):
        """
        Method for printing the Pascal's Triangle
        """
        for i in range(self.n):
            for j in range(self.n - i + 1):
                print(end=" ")

            for j in range(i+1):
                print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

            # for new line
            print()

class Midpoint:
    """
    A class that handles on solving the Midpoint of linear graph

    Attributes:
       x1 (int): The value of the first x coordinate
       x2 (int): The value of the second x coordinate
       y1 (int): The value of the first y coordinate
       y2 (int): The value of the first y coordinate

    Invariants:
        - Cannot have an empty input 

    """    
    def __init__(self, x1: int, x2: int, y1: int, y2: int):
        """
        Initializes the value of x1, x2, y1, and y2
        """
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
    def midpoint(self):
        """
        Method for the formula of the Midpoint of a graph
        """
        x = ((self._x1 + self._x2) / 2)
        y = ((self._y1 + self._y2) / 2)
        print(f"The midpoint is {x}, {y}")

class Distance(Midpoint):
    """
    A class that handles on solving the Distance of two points on a graph

    Attributes:
       x1 (int): The value of the first x coordinate
       x2 (int): The value of the second x coordinate
       y1 (int): The value of the first y coordinate
       y2 (int): The value of the first y coordinate

    Invariants:
        - Cannot have an empty input 
    """    
    def __init__(self, x1, x2, y1, y2):
        """
        Initializes the values of x1, x2, y1, and y2 
        """
        super().__init__(x1, x2, y1, y2)
    def distance(self):
        """
        Method for the forumla of the distance of two points
        """
        d_ans = math.sqrt((self._x2 - self._x1)**2 + (self._y2 - self._y1)**2)
        print(f"The distance between these 2 points is {d_ans}")


        

def main():
    # Menu list
    while True:
        algebralist = ["Quadratics", "Pythagorean", "Pascal's Triangle", "Midpoint", "Distance", "Exponent Laws","Exit"]
        menu = promptinput("Pick a formula: ", algebralist)
        match menu:
            case "Quadratics":
                try:
                    variables = Quadratics(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")))
                except:
                    print("Enter a valid number.")
                variables.quadratic()
            case "Pythagorean":
                try: 
                    sides = Pythagorean(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")))
                except: 
                    print("Enter valid number.")
                sides.pythagorean_theorem()
            case "Pascal's Triangle":
                try:
                    n = int(input("Enter the value of N: "))
                    while n < 0:
                        print("Cannot input any negative numbers")
                        n = int(input("Enter the value of N: "))
                    new_n_value = Pascals_Triangle(n)
                    new_n_value.printing_triangle()
                except:
                    print("Enter a valid input for N.")

            case "Midpoint":
                try:
                    m = Midpoint(int(input("Enter first x coord: ")), int(input("Enter second x coord: ")), int(input("Enter first y coord: ")), int(input("Enter second y coord: ")))
                    m.midpoint()
                except:
                    print("Enter valid coordinates.")
            case "Distance":
                try:
                    d = Distance(int(input("Enter second x coord: ")), int(input("Enter first x coord: ")), int(input("Enter second y coord: ")), int(input("Enter first y coord: ")))
                    d.distance()
                except:
                    print("Enter valid coordinates.")
            case "Exit":
                return
                
if __name__ == "__main__":
    main()