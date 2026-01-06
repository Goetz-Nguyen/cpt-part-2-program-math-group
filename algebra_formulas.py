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
    def __init__(self, a: int, b: int, c: int):
        self._a = a
        self._b = b
        self._c = c
    def quadratic(self):
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
    def __init__(self, a: int, b: int, c: int):
        self._a = a
        self._b = b
        self._c = c
    def pythagorean_theorem(self):
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
    def __init__(self, n: int):
        self.n = n
    def printing_triangle(self):
        for i in range(self.n):
            for j in range(self.n - i + 1):
                print(end=" ")

            for j in range(i+1):
                print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

            # for new line
            print()

class Midpoint:
    def __init__(self, x1: int, x2: int, y1: int, y2: int):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
    def midpoint(self):
        x = ((self._x1 + self._x2) / 2)
        y = ((self._y1 + self._y2) / 2)
        print(f"The midpoint is {x}, {y}")

class Distance(Midpoint):
    def __init__(self, x1, x2, y1, y2):
        super().__init__(x1, x2, y1, y2)
    def distance(self):
        d_ans = math.sqrt((self._x2 - self._x1)**2 + (self._y2 - self._y1)**2)
        print(f"The distance between these 2 points is {d_ans}")

# class Exponent_laws:
#     def __init__(self, base: int, m: int, n: int):
#         self._base = base
#         self._m = m
#         self._n = n
#     def 
        

def main():
    algebralist = ["Quadratics", "Pythagorean", "Pascal's Triangle", "Midpoint", "Distance","Exit"]
    menu = promptinput("Pick a formula: ", algebralist)
    match menu:
        case "Quadratics":
            try:
                variables = Quadratics(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")))
            except:
                print("Enter a valid number.")
            variables.quadratic()
            menu = promptinput("Pick a formula: ", algebralist)
        case "Pythagorean":
            try: 
                sides = Pythagorean(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: ")))
            except: 
                print("Enter valid number.")
            sides.pythagorean_theorem()
            menu = promptinput("Pick a formula: ", algebralist)
        case "Pascal's Triangle":
            try:
                n = Pascals_Triangle(int(input("Enter the value of N: ")))
                n.printing_triangle()
            except:
                print("Enter a valid value for N.")
            menu = promptinput("Pick a formula: ", algebralist)
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