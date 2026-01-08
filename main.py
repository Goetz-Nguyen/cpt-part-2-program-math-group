import sympy, random, os, math, matplotlib.pyplot, numpy
from sympy import sympify, SympifyError
from InquirerPy import prompt
from PyDesmos import Graph
from matplotlib.patches import Circle, Rectangle
from math import factorial

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


def geometry_test():
    """
    Prints 10 questions, one at a time for the user, which then is asked for the input of the correct answer.
    It is mainly focused for the unit of Geometry.
    If the answer is the same as the answers listed, it will add a point, which is totaled at the end.
    """
    print("== PRE MADE GEOMETRY TEST QUESTIONS!! ==")
    score = 0
    total = 10

    # 1
    print("#1: In a right triangle, the angle is 37*. The adjacent side is 12.")
    print("Find the hypotenuse. (Round to nearest tenth)")
    ans = input("Your answer: ")
    if ans in ["15.0", "15", "15.1"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    #2
    print("#2:An arc measures 84*. What is the measure of the inscribed angle intercepting it?")
    print("A) 42*   B) 84*   C) 126*   D) 168*")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
    
    #3
    print("#3: A cylinder has a radius 4 and height 10. What is its volume? (Use pi)")
    ans = input("Your answer: ")
    if ans == "160":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
    
    #4
    print("#4: Find the slope between (–3, 5) and (4, –2).")
    ans = input("Your answer: ")
    if ans in ["-1", "-1.0"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
    
    #5
    print("#5: Use the Law of Cosines:")
    print("Given sides a=7, b=9, and angle C=42*, solve for side c (nearest tenth).")
    ans = input("Your answer: ")
    if ans in ["6", "6.0", "6.1"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
    
    #6
    print("#6: A triangle is reflected over the y-axis. What happens to point (x, y)?")
    print("A) (-x, y)   B) (x, -y)   C) (-x, -y)   D) (y, x)")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    #7
    print("#7: Two similar triangles have scale factor 3:5.")
    print("If a side in the smaller triangle is 12, what is the corresponding larger side?")
    ans = input("Your answer: ")
    if ans == "20":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
    # 8
    print("#8: Find the distance between points (2, 3) and (11, 9).")
    ans = input("Your answer: ")
    if ans in ["10.8", "10.819", "11"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
    
    # 9
    print("#9: Find the area of a triangle with sides 8, 9, and 13.")
    ans = input("Your answer: ")
    if ans in ["36", "37"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
    
    # 10
    print("#10: What is the interior angle of a regular 12 sided polygon?")
    ans = input("Your answer: ")
    if ans in ["150", "150*", "150 degrees"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
    print("== GEOMETRY TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")
    return score

def polynomials_test():
    """
    Prints 10 questions, one at a time for the user, which then is asked for the input of the correct answer.
    It is mainly focused for the unit of Polynomials.
    If the answer is the same as the answers listed, it will add a point, which is totaled at the end.
    """

    print("== PRE MADE POLYNOMIALS TEST QUESTIONS!! ==")
    score = 0
    total = 10

    # 1
    print("#1: Factor using the greatest common factor: 18x^5 + 36x^4")
    print("A) 18x^4(x + 2)   B) 18x^5(x + 2)   C) 6x^4(3x + 6)   D) x^4(18x + 36)")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 2
    print("#2: Find the product: (x + 4)(x^2 − 3x − 5)")
    print("A) x^3 + x^2 − 17x − 20")
    print("B) x^3 + 4x^2 − 3x − 20")
    print("C) x^3 + x^2 − 11x − 20")
    print("D) x^3 + 4x^2 − 17x − 20")
    ans = input("Your answer: ")
    if ans == "d":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 3
    print("#3: Factor completely: x^2 − 16")
    print("A) (x − 8)(x + 2)   B) (x − 4)(x + 4)   C) (x − 16)(x + 1)   D) Prime")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 4
    print("#4: Simplify: (5x^3)(2x^2)")
    print("A) 10x^5   B) 7x^6   C) 10x^6   D) x^5")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 5
    print("#5: Factor: x^2 + 9x + 20")
    print("A) (x + 10)(x + 2)   B) (x + 5)(x + 4)   C) (x − 5)(x − 4)   D) Prime")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 6
    print("#6: What is the degree of the polynomial: 7x^3 − 4x + 6?")
    print("A) 1   B) 2   C) 3   D) 6")
    ans = input("Your answer: ")
    if ans == "c":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 7
    print("#7: Simplify: (x^2 − 9) / (x − 3)")
    print("A) x − 3   B) x + 3   C) x^2 − 3   D) Cannot be simplified")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 8
    print("#8: Expand: (x + 5)^2")
    print("A) x^2 + 25   B) x^2 + 10x + 25   C) x^2 − 10x + 25   D) 2x + 10")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 9
    print("#9: Factor by grouping: x^3 − x^2 − 6x + 6")
    print("A) (x − 1)(x^2 − 6)")
    print("B) (x + 1)(x^2 − 6)")
    print("C) (x − 3)(x^2 − 2)")
    print("D) Prime")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 10
    print("#10: Evaluate when x = 3: 2x^2 − 5x + 4")
    print("A) 7   B) 10   C) 5   D) 1")
    ans = input("Your answer: ")
    if ans == "c":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
    print("== POLYNOMIAL TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")

    return score

def algebra_tests():
    """
    Prints 10 questions, one at a time for the user, which then is asked for the input of the correct answer.
    It is mainly focused for the unit on Algebra.
    If the answer is the same as the answers listed, it will add a point, which is totaled at the end.
    """
    print("== PRE MADE ALGEBRA TEST QUESTIONS!! ==")
    score = 0
    total = 5

    # 1
    print("#1: Find all sides of a right triangle whose perimeter is equal to 60 cm and its area is equal to 150 square cm.")
    print("Enter the numbers via the example: '10 20 30'")
    ans = input("Your answer: ")
    if ans in ["25 15 20", "25 20 15", "15 25 20", "15 20 25", "20 15 25", "20 25 15"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    #2
    print("#2: If 200 is added to a positive integer I, the result is a square number. If 276 is added to to the same integer I, another square number is obtained. Find I.")
    print("A) Make sure your answer is writtin in this exact format: 'I=x^z - ? = ?'")
    ans = input("Your answer: ")
    if ans == "I=x^2 − 200 = 124":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
   
    #3
    print("#3: A rock is dropped into a water well and it travels approximately 16t^2 feet in t seconds. If the splash is heard")
    print("3.5 seconds later and the speed of sound is 1087 feet/second, what is the height of the well? (Round to the nearest unit)")
    ans = input("Your answer: ")
    if ans in ["178", "178 Feet", "178ft", "178Ft", "178FT", "178Feet", "178FEET", "178 FEET"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
   
    #4
    print("#4: It takes pump A 2 hours less time than pump B to empty a swimming pool.")
    print("Pump A is started at 8:00 a.m. and pump B is started at 10:00 a.m. At 12:00 p.m.")
    print("60 percent of the pool is empty when pump B broke down. How much time after 12:00 p.m. would it take pump A to empty the pool?")
    ans = input("Your answer: ")
    if ans in ["3.766", "3.7", "3.8","3.766h", "3.7h", "3.8h","3.766hours", "3.7hours", "3.8hhours",]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    #5
    print("#5: Two boats on opposite banks of a river start moving towards each other. They first pass each other")
    print("1400 meters from one bank. They each continue to the opposite bank, immediately turn around and start back to the other bank. When they pass each other a second time, they are")
    print("600 meters from the other bank. We assume that each boat travels at a constant speed all along the journey. Find the width of the river?")
    print("Given sides a=7, b=9, and angle C=42*, solve for side c (nearest tenth).")
    ans = input("Your answer: ")
    if ans in ["3600 meters", "3600 m", "3600m"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    print("")
    print("== ALGEBRA TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")
    return score

def coordinate_planes_test():
    """
    Prints 10 questions, one at a time for the user, which then is asked for the input of the correct answer.
    It is mainly focused for the unit on Coordinate Planes.
    If the answer is the same as the answers listed, it will add a point, which is totaled at the end.
    """
    print("== PRE MADE COORDINATE PLANES TEST QUESTIONS!! ==")
    score = 0
    total = 10

    # 1
    print("#1: What quadrant is the point (4, -7) located in?")
    print("A) Quadrant I   B) Quadrant II   C) Quadrant III   D) Quadrant IV")
    ans = input("Your answer: ")
    if ans == "d":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 2
    print("#2: What is the x-coordinate of the point (-3, 5)?")
    ans = input("Your answer: ")
    if ans == "-3":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 3
    print("#3: Find the slope between the points (2, 4) and (6, 12).")
    ans = input("Your answer: ")
    if ans in ["2", "2.0"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 4
    print("#4: Which point lies on the y-axis?")
    print("A) (5, 0)   B) (0, 6)   C) (3, 3)   D) (-4, 2)")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 5
    print("#5: Find the distance between the points (1, 1) and (4, 5). (Round to nearest tenth)")
    ans = input("Your answer: ")
    if ans in ["5", "5.0", "5.1"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 6
    print("#6: If a point is reflected over the x-axis, what happens to (x, y)?")
    print("A) (x, -y)   B) (-x, y)   C) (-x, -y)   D) (y, x)")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 7
    print("#7: What is the midpoint between the points (2, 6) and (8, 10)?")
    ans = input("Your answer: ")
    if ans in ["5 8", "(5,8)", "(5, 8)", "5,8", "5, 8"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 8
    print("#8: Which point is in Quadrant III?")
    print("A) (3, -4)   B) (-2, 5)   C) (-6, -1)   D) (4, 2)")
    ans = input("Your answer: ")
    if ans == "c":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 9
    print("#9: What is the slope of a horizontal line?")
    ans = input("Your answer: ")
    if ans in ["0", "0.0"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 10
    print("#10: What is the ordered pair of the origin?")
    ans = input("Your answer: ")
    if ans in ["0 0", "(0,0)", "(0, 0)", "0,0", "0, 0"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
    print("== COORDINATE PLANES TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")
    return score

def trigonometry_test():
    """
    Prints 10 questions, one at a time for the user, which then is asked for the input of the correct answer.
    It is mainly focused for the unit on Trigonometry.
    If the answer is the same as the answers listed, it will add a point, which is totaled at the end.
    """
    print("== PRE MADE TRIGONOMETRY TEST QUESTIONS!! ==")
    score = 0
    total = 10

    # 1
    print("#1: In a right triangle, sin(0) = opposite / ?")
    print("A) Adjacent   B) Hypotenuse   C) Tangent   D) Cosine")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 2
    print("#2: cos(0) = ? / hypotenuse")
    print("A) Opposite   B) Adjacent   C) Tangent   D) Sine")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 3
    print("#3: tan(0) =")
    print("A) Opposite / Hypotenuse   B) Adjacent / Hypotenuse")
    print("C) Opposite / Adjacent   D) Hypotenuse / Opposite")
    ans = input("Your answer: ")
    if ans == "c":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 4
    print("#4: Find sin(30*)")
    ans = input("Your answer: ")
    if ans in ["0.5", "1/2"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 5
    print("#5: Find cos(60*)")
    ans = input("Your answer: ")
    if ans in ["0.5", "1/2"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 6
    print("#6: A ladder leans against a wall making a 60* angle with the ground.")
    print("If the ladder is 10m long, how high up the wall does it reach? (Nearest tenth)")
    ans = input("Your answer: ")
    if ans in ["8.7", "8.66", "8.7m"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 7
    print("#7: Which trig ratio is used for Opposite and Adjacent?")
    print("A) Sine   B) Cosine   C) Tangent   D) Secant")
    ans = input("Your answer: ")
    if ans == "c":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 8
    print("#8: Find tan(45*)")
    ans = input("Your answer: ")
    if ans in ["1", "1.0"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 9
    print("#9: An angle of elevation is measured:")
    print("A) Below the horizontal   B) Above the horizontal")
    print("C) From the vertical   D) Inside the triangle")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 10
    print("#10: What is the hypotenuse?")
    print("A) Shortest side   B) Longest side")
    print("C) Side opposite right angle   D) Both B and C")
    ans = input("Your answer: ")
    if ans == "d":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
    print("== TRIGONOMETRY TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")
    return score

def quadratics_test():
    """
    Prints 10 questions, one at a time for the user, which then is asked for the input of the correct answer.
    It is mainly focused for the unit on Quadratics.
    If the answer is the same as the answers listed, it will add a point, which is totaled at the end.
    """
    print("== PRE MADE QUADRATICS TEST QUESTIONS!! ==")
    score = 0
    total = 10

    # 1
    print("#1: What is the standard form of a quadratic?")
    print("A) y = mx + b   B) y = ax^2 + bx + c")
    print("C) y = a(x + h)^2 + k   D) y = x^3")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 2
    print("#2: Factor: x^2 + 5x + 6")
    ans = input("Your answer: ")
    if ans in ["(x+2)(x+3)", "(x + 2)(x + 3)"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 3
    print("#3: Factor: x^2 − 9")
    ans = input("Your answer: ")
    if ans in ["(x-3)(x+3)", "(x + 3)(x - 3)"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 4
    print("#4: What is the vertex of y = (x − 4)^2 + 1?")
    ans = input("Your answer: ")
    if ans in ["(4,1)", "(4, 1)"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 5
    print("#5: How many zeros does a quadratic have?")
    print("A) 1   B) 2   C) 3   D) Depends")
    ans = input("Your answer: ")
    if ans == "d":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 6
    print("#6: Find the axis of symmetry for y = x^2 − 6x + 2")
    ans = input("Your answer: ")
    if ans in ["x=3", "x = 3"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 7
    print("#7: Expand: (x + 4)^2")
    ans = input("Your answer: ")
    if ans in ["x^2+8x+16", "x^2 + 8x + 16"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 8
    print("#8: What is the shape of a quadratic graph?")
    ans = input("Your answer: ")
    if ans.lower() == "parabola":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 9
    print("#9: Solve: x^2 − 4 = 0")
    ans = input("Your answer: ")
    if ans in ["x=2,-2", "2,-2", "-2,2"]:
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")

    # 10
    print("#10: If a > 0 in y = ax^2 + bx + c, the parabola opens:")
    print("A) Down   B) Up")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1 #Adds a 1 to the score variable if it was the right answer

    print("")
    print("== QUADRATICS TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")
    return score

def math_definitions():
    """
    Asks the user to choose which unit they would like to access the definitions for.
    Once a unit is chosen, it will print out key definitions in that unit with short descriptions.
    """
    defintions = ["Geometry", "Trigonometry", "Algebra", "Coordinate Planes", 
                  "Quadratics", "Polynomials", "Back"]
    choice = promptinput("Chose an option: ", defintions)
    print("")

    match choice:
        case "Geometry":
            print("== GEOMETRY VOCABULARY ==:")
            print("Point: An exact location.")
            print("Line: A straight path that goes forever in both directions.")
            print("Angle: Formed by two coordinates connected with a common endpoint.")
            print("Vertex: The point where sides or angles meet.")
            print("Congruent: Same shape and same size.")
            print("Similar: Same shape, different size.")
            print("Line Segment: A line with two end point's.")
            print("Right Angle: An Angle that is exactly 90*.")
            print("Acute Angle: An Angle that is less than 90*.")
            print("Obtuse Angle: An Angle that is greater than 90*, and less than 180*.")
            print("Intersecting Lines: Two lines that cross.")
            print("Parallel Lines: Two lines that do not intersect.")
            print("Vertical Angles: Two Angles that are equal, made by two Intersecting Lines.")

        case "Trigonometry":
            print("== TRIGONOMETRY VOCABULARY ==:")
            print("Hypotenuse: Longest side of a right triangle.")
            print("Opposite: Side across from the angle.")
            print("Adjacent: Side next to the angle.")
            print("Sine (sin): Opposite / Hypotenuse.")
            print("Cosine (cos): Adjacent / Hypotenuse.")
            print("Tangent (tan): Opposite / Adjacent.")
            print("Amplitude: Vertical Stretch of a function.")
            print("Angle of Depression: An Angle which is below the horizontal.")
            print("Angle of Elevation: An Angle that is measured above the horizontal.")
            print("Asymtotes: Lines that represent undefined values for functions.")
            print("Cofunctions: Pairs of functions that have complimentary angles which the trigonmetric ratio's are equal.")
            print("Cosecant: The Reciprocal of Sine.")
            print("Cotangent: The Reciprocal of Tangent.")
            print("Secant: The Reciprocal of Cosine.")

        case "Algebra":
            print("== ALGEBRA VOCABULARY ==:")
            print("Variable: A letter that represents a number.")
            print("Expression: Numbers and variables without an equal sign.")
            print("Equation: A statement showing two expressions are equal.")
            print("Coefficient: Number multiplied by a variable.")
            print("Constant: A number with no variable.")
            print("Solution: A value that makes an equation true.")
            print("Denominator: The lower half of a fraction.")
            print("Numerator: The upper half of a fraction.")
            print("Difference: The answer for a subtraction problem.")
            print("Converse: Opposite.")
            print("Difference of Two squares: A Binomial that the terms are squares, and have a negative sign between them.")
            print("Domain: A set of all of the first coordinates of a relation or function (x).")
            print("Range: A set of all of the second coordinates of a relation or function (y).")
            print("Elmination Method: A solving formula where a variable is removed by adding or subtracting two equations.")
            print("Expand: Multiplying.")
            print("Exponent: The amount of times the base is factored.")
            print("Greatest Common Factor: The largest number that divides into two terms.")

        case "Coordinate Planes":
            print("== COORDINATE PLANE VOCABULARY ==:")
            print("X-axis: The horizontal number line.")
            print("Y-axis: The vertical number line.")
            print("Origin: The point (0, 0).")
            print("Ordered Pair: Coordinates written as (x, y).")
            print("Quadrant: One of the four sections of the plane.")
            print("Slope: Rate of change between two points.")
            print("Coordinate Plane: The plane where a Horizontal line, and a vertical line intersect at their zero's.")
            print("Ordered Pair: (X,Y)")

        case "Quadratics":
            print("== QUADRATICS VOCABULARY == :")
            print("Quadratic Equation: An equation with x^2 as the highest power.")
            print("Parabola: The graph of a quadratic.")
            print("Vertex: The highest or lowest point of a parabola.")
            print("Axis of Symmetry: Vertical line through the vertex.")
            print("Zeros/Roots: X-values where the graph crosses the x-axis.")
            print("Standard Form: ax^2 + bx + c.")
            print("Quadratic Function: y = ax^2 + bx + c")

        case "Polynomials":
            print("== POLYNOMIAL VOCABULARY ==:")
            print("Polynomial: An algebraic expression made up of terms with variables and coefficients.")
            print("Term: A single part of a polynomial separated by addition or subtraction.")
            print("Coefficient: The number multiplied by a variable.")
            print("Constant Term: A term with no variable.")
            print("Monomial: A polynomial with one term.")
            print("Binomial: A polynomial with two terms.")
            print("Trinomial: A polynomial with three terms.")
            print("Degree of a Term: The sum of the exponents of the variables in the term.")
            print("Degree of a Polynomial: The highest degree of any term in the polynomial.")
            print("Expand: To remove brackets by multiplying.")
            print("Factor: To write an expression as a product.")
            print("Factoring Completely: Factoring until no further factoring is possible.")
            print("Greatest Common Factor (GCF): The largest factor shared by all terms.")
            print("Difference of Squares: A binomial of the form a^2 − b^2.")
            print("Perfect Square Trinomial: A trinomial that can be factored into two identical binomials.")
            print("Polynomial Division: Dividing one polynomial by another polynomial.")

        case "Back":
            return

def show_sources():
    """
    Asks the user to pick which unit they want chosen study sources for.
    When a unit is chosen, it will print out many sources under that unit.
    """
    print("== STUDY SOURCES ==")
    units = ["Geometry", "Coordinate Planes", "Polynomials", "Quadratics", "Algebra", "Back"]
    choice = promptinput("Choose an option: ", units)

    match choice:
        case "Geometry":
            print("")
            print("== GEOMETRY SOURCES ==")


            print("Khan Academy High School Trigonometry & Geometry")
            print("A full guide covering geometry and trigonometry with lessons, examples, and practice questions.")
            print("https://www.khanacademy.org/math/geometry/hs-geo-trig")
            print("")


            print("Learn Sin, Cos, and Tan in 5 minutes")
            print("Explains sine, cosine, and tangent using right triangles and examples.")
            print("https://www.youtube.com/watch?v=gSGbYOzjynk")
            print("")


            print("Volume of a Cylinder | MathHelp.com")
            print("Shows how to calculate the volume of a cylinder using the formula.")
            print("https://youtu.be/fxTsG4qkz1U")
            print("")


            print("Volume of a Cube")
            print("Explains how to find the volume of a cube using side length.")
            print("https://youtu.be/bpRsuccb6dI")
            print("")


            print("How to Find Scale Factor with Similar Figures")
            print("Teaches how scale factors work and how to find missing side lengths.")
            print("https://youtu.be/P1f3sJpIYGI")
            print("")


            print("Polygons")
            print("Explains how to find interior and exterior angles of polygons.")
            print("https://youtu.be/E_-3ulbtcLk")
            print("")


            print("How to Find the Area of a Triangle | Calculate the Area of a Triangle")
            print("Teaches how to calculate the area of different types of triangles.")
            print("https://youtu.be/pvMuDPVOm7Y")
            print("")


            print("MathBits Notebook")
            print("A reference site with written notes, examples, and explanations for geometry.")
            print("https://mathbitsnotebook.com/Geometry/Geometry.html")
            print("")


        case "Coordinate Planes":
            print("== COORDINATE PLANES ==")


            print("Reflection Across the X and Y Axis")
            print("Explains reflections over the x-axis, y-axis, and origin.")
            print("https://youtu.be/DerrI1FstO4")
            print("")


            print("Finding the Coordinates of a Point on a Coordinate Plane | Math with Mr. J")
            print("Shows how to identify the coordinates of points on a graph.")
            print("https://youtu.be/a1DXlvwnqUw")
            print("")


            print("How to Plot Points a Coordinate Plane | Positive and Negative Coordinates | Math with Mr. J")
            print("Demonstrates how to plot ordered pairs on a coordinate plane.")
            print("https://youtu.be/5NyuamsbLMo")
            print("")


            print("Coordinate Geometry, Basic Introduction, Practice Problems")
            print("Introduces graphing points, slope, and basic coordinate geometry concepts.")
            print("https://youtu.be/PXnAKcBipKM")
            print("")


            print("Introduction to Coordinate Planes + Vocabulary | Math with Mr. J")
            print("Explains basic coordinate plane terms such as axis, origin, and quadrants.")
            print("https://youtu.be/qcb-mcREIi0")
            print("")


        case "Polynomials":
            print("== POLYNOMIAL SOURCES ==")


            print("Algebra Basics What Are Polynomials")
            print("Explains what polynomials are and their parts.")
            print("https://www.youtube.com/watch?v=ffLLmV4mZwU")
            print("")


            print("Polynomials Adding Subtracting Multiplying and Dividing")
            print("Shows all basic polynomial operations.")
            print("https://www.youtube.com/watch?v=ZvL9aDGNHqA")
            print("")


            print("How to Factor Polynomials the Easy Way")
            print("Teaches how to factor polynomials step by step.")
            print("https://www.youtube.com/watch?v=U6FndtdgpcA&pp=ygUmSG93IHRvIEZhY3RvciBQb2x5bm9taWFscyB0aGUgRWFzeSBXYXnSBwkJTQoBhyohjO8%3D")
            print("")


            print("Solving Word Problems with Polynomials")
            print("Shows how to solve polynomial word problems.")
            print("https://www.youtube.com/watch?v=TenlbkEJGe4")
            print("")


            print("Introduction to Polynomial Functions")
            print("Explains polynomial functions and graphs.")
            print("https://www.youtube.com/watch?v=6Uh3Z6DJ_pI")
            print("")


            print("Khan Academy Polynomials")
            print("Practice and lessons for polynomials.")
            print("https://www.khanacademy.org/math/algebra-home/alg-polynomials")
            print("")


        case "Quadratics":
            print("== QUADRATIC SOURCES ==")


            print("Quadratics Top 10 Must Knows")
            print("Covers key quadratic concepts and solving methods.")
            print("https://www.youtube.com/watch?v=SGUP6BkA870&pp=ygUcUXVhZHJhdGljcyBUb3AgMTAgTXVzdCBLbm93cw%3D%3D")
            print("")


            print("Five Different Ways to Solve a Quadratic Equation")
            print("Shows multiple methods to solve quadratics.")
            print("https://youtu.be/u0mZ8wm-D48?si=0zyb-6ld1nI0fQeJ")
            print("")


            print("Factoring Quadratics as x plus a x plus b")
            print("Teaches how to factor simple quadratic equations.")
            print("https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics-multiplying-factoring/x2f8bb11595b61c86:factor-quadratics-intro/v/factoring-simple-quadratic-expression")
            print("")


            print("Using the Quadratic Formula")
            print("Explains how to solve quadratics using the formula.")
            print("https://www.khanacademy.org/math/algebra/quadratics/solving-quadratics-using-the-quadratic-formula/v/using-the-quadratic-formula")
            print("")


            print("JensenMath Quadratics Unit")
            print("Practice questions and review for quadratics.")
            print("https://www.jensenmath.ca/math10-unit-5")
            print("")


        case "Algebra":
            print("== ALGEBRA SOURCES ==")


            print("Khan Academy Algebra 2")
            print("Full lessons and practice for Algebra topics.")
            print("https://www.khanacademy.org/math/algebra2")
            print("")


            print("What Is a Variable")
            print("Explains what variables are and how they are used.")
            print("https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:foundation-algebra/x2f8bb11595b61c86:intro-variables/v/what-is-a-variable")
            print("")


            print("Intro to Combining Like Terms")
            print("Shows how to combine terms with the same variable.")
            print("https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:foundation-algebra/x2f8bb11595b61c86:combine-like-terms/v/combining-like-terms")
            print("")


            print("Linear Equations")
            print("Teaches how to solve basic linear equations.")
            print("https://www.khanacademy.org/math/algebra-home/alg-basic-eq-ineq/alg-old-school-equations/v/algebra-linear-equations-1")
            print("")


            print("Equation With the Variable in the Denominator")
            print("Shows how to solve equations with fractions.")
            print("https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:solve-equations-inequalities/x2f8bb11595b61c86:linear-equations-variables-both-sides/v/ex-2-multi-step-equation")
            print("")


            print("Learn Fractions in 9 Minutes")
            print("Quick review of fraction rules used in algebra.")
            print("https://youtu.be/GvPB9B9fG04?si=s9bqiPz5DQNJq0aM")
            print("")


            print("Solving Systems of Equations Using Elimination")
            print("Shows how to solve systems using elimination.")
            print("https://youtu.be/cz6UmZLWgEw?si=XcgCsU-KgVLd0tZG")
            print("")


            print("Partial Fraction Decomposition")
            print("Explains how to break rational expressions into parts.")
            print("https://youtu.be/QKkdYW77xNI?si=EeoXuQ9Xeve4dC7j")
            print("")

        case "Back":
            return
    

def save_test(test_name, questions, answers):
    """
    When the function is accessed, it will save a file onto the user's computer under the chosen name with
    their custom made test questions and answers on it.
    """
    file = open(test_name + ".txt", "w")
    for i in range(len(questions)):
        file.write(questions[i] + "\n") # Writes a question to the file
        file.write(answers[i] + "\n") # Writes the corrisponding answer to the question onto the file.
    file.close()


def load_test(filename):
    """
    When the function is accessed, it will search for a file onto the user's computer for the inputted name
    that contains the user's custom questions and answers.

    It will then add it to the program, which can now be accessed and run.
    """
    tests = {}
    try:
        file = open(filename, "r") # Opens the chosen file.
        lines = file.readlines() # Copies all of the line's from the file to the program.
        file.close()
    except:
        print("File could not be loaded.") # If no file under that name exists, it will fail.
        return tests

    questions = []
    answers = []

    i = 0
    while i < len(lines):
        questions.append(lines[i].strip()) # Add's the question from the test into the list.
        answers.append(lines[i + 1].strip()) #Add's the answer from the test into the list.
        i += 2

    test_name = filename.replace(".txt", "")
    tests[test_name] = {"questions": questions, "answers": answers}
    return tests


def create_tests():
    """
    Allows the user to create a custom test with their own question's, and answers.

    The custom test which was made will then be saved onto the user's computer and the program will allow
    the test to be accessed.
    """
    tests = {}

    print("== CREATING A NEW TEST ==")
    test_name = input("Please enter a name for this test: ")

    num = int(input("How many questions do you want to make for this test? "))

    questions = []
    answers = []

    i = 0
    while i < num:
        print("Question", i + 1) # For how many question's the user inputted, it will keep asking the user
                                 # for a question, and its answer.
        question = input("Type your question: ")
        answer = input("Type the correct answer: ")
        questions.append(question) #Appends the question into the list.
        answers.append(answer)     #Appends the answer into the list.
        i += 1

    tests[test_name] = {"questions": questions, "answers": answers}
    save_test(test_name, questions, answers) # Saves the test onto the computer.

    print(f"The test '{test_name}' was created and saved.")
    return tests


def run_test(tests):
    """
    Ask's the user to select which custom test they want to access.
    When a test is selected, that test will run and the user is able to try to answer it.
    """
    print("== AVAILABLE TESTS ==")
    for name in tests:
        print("-", name)

    test_name = input("Which test do you want to open? ")

    if test_name not in tests:
        print("That test does NOT exist.")
        return

    data = tests[test_name]
    questions = data["questions"]
    answers = data["answers"]

    score = 0
    total = len(questions)
    i = 0

    print(f"== STARTING THE TEST: {test_name} ==")

    while i < total:
        print("Question", i + 1)
        print(questions[i])
        user_ans = input("Your answer: ")
        print("")

        if user_ans == answers[i]:
            score += 1
        i += 1

    print(f"Your Score Is: {score} / {total}")

def test_choice():
    """
    Asks the user to choose which test they want to run, and when one is selected, that chosen test will run.
    """
    premadeoptions = ["Geometry", "Polynomials", "Algebra", "Coordinate Planes",
                      "Quadratics", "Trigonometry", "Exit"]
    pre_made_test_options = promptinput("Which Pre-Made test would you like to pick?", premadeoptions)
    match pre_made_test_options:
        case "Geometry":
            geometry_test()
        case "Polynomials":
            polynomials_test()
        case "Algebra":
            algebra_tests()
        case "Coordinate Planes":
            coordinate_planes_test()
        case "Quadratics":
            quadratics_test()
        case "Trigonometry":
            trigonometry_test()
        case "Exit":
            return
    
def graph_calculator():
    """
    A graphing calculator which draws a graph based on user input
    """
    menu = promptinput("What kind of graph?",["Trig", "Polynomial", "Exit"])
    error = False

    while menu != "Exit":
        os.system('cls' if os.name == 'nt' else 'clear') # Clean terminal
        if menu == "Polynomial":
            menup = promptinput("How do you want to enter your graph?", ["Equation", "Enter each term", "Exit"])
            if menup == "Equation":
                with Graph('my graph') as G:
                    f, x = G.f, G.x # Setup the graph using f of x
                    try:
                        print("Use ^ to show exponents")
                        f[x] = input("f(x) = ") # Set graph as the input
                    except:
                        print("Enter valid numbers!")
            elif menup == "Exit":
                pass
            else:
                try:
                    coefficient = []
                    equation = ""
                    exponent = int(input("Enter graph degree: "))
                    for i in range(exponent+1):
                        coefficient.append(int(input(f"Enter coefficient of the the term with degree {i}: ")))
                    # Formats the coefficients to fit the proper form of the equation
                    for i in range(len(coefficient), 0, -1):
                        if i != 0:
                            equation += f"{coefficient[i-1]}*x^{i-1} + "
                    equation = equation[:len(equation)-3] # Inverts the equation
                    error = False
                except:
                    error = True
                    print("Enter valid numbers!")
                if not error:
                    try:
                        with Graph('my graph') as G:
                                f, x = G.f, G.x
                                f[x] = equation # Sets the formatted equation to the graph
                    except:
                        print("Couldn't graph!")
            menu = promptinput("What kind of graph?",["Trig", "Polynomial", "Exit"])
        elif menu == "Trig":
            trig_type = promptinput("Type of trig?",["Cos", "Sin", "Tan", "Exit"])
            if trig_type == "Exit":
                menu = promptinput("What kind of graph?",["Trig", "Polynomial", "Exit"])
            else:
                try:
                    a = int(input("Enter a value: "))
                    k = int(input("Enter k value: "))
                    d = int(input("Enter d value: "))
                    c = int(input("Enter c value: "))
                    error = False
                except:
                    error = True
                    print("Enter valid inputs!")
                if not error:
                    try:
                        match trig_type:
                            case "Cos":
                                with Graph('my graph') as G:
                                    f, x = G.f, G.x
                                    f[x] = a*sympy.cos(k*(x-d))+c
                            case "Sin":
                                with Graph('my graph') as G:
                                    f, x = G.f, G.x
                                    f[x] = a*sympy.sin(k*(x-d))+c
                            case "Tan":
                                with Graph('my graph') as G:
                                    f, x = G.f, G.x
                                    f[x] = a*sympy.tan(k*(x-d))+c
                    except:
                        print("Couldn't graph!")
                    menu = promptinput("What kind of graph?",["Trig", "Polynomial", "Exit"])
    os.system('cls' if os.name == 'nt' else 'clear') 
    return

def mental_math():
    """
    Displays and setup the math exercises
    """
    def menu():
        """
        Asks the user what kind of questions they want.

        Return
            (str): Type of question picked
        """
        return promptinput("What kind of math?", ["Everything","Dividing", "Multiplying", "Adding", "Subtracting", "Exit"])
    def get_random():
        """
        Generates a random number that is not zero, and that can be divided by each other and that are not the same.

        Return:
            (int): first number
            (int): second number
        """
        number1 = random.randrange(1,100)
        while number1 < 4:
            number1 = random.randrange(1,100)
        number2 = random.randrange(2,number1)
        while number1%number2 != 0:
            number1 = random.randrange(1,100)
            while number1 < 4:
                number1 = random.randrange(1,100)
            number2 = random.randrange(2,number1)
        return number1, number2

    def initialize():
        """
        Initializes the game by asking the user how many questions they want to answer.

        Returns:
            (int): starting score
            (int): number of questions on the quiz
        """
        tries = 0
        while tries < 1:
            try:
                tries = int(input("How many questions? "))
            except:
                print("Enter a valid number!")
        return 0, tries

    def check_answer(correct, corrects):
        """
        Checks if the user answered correctly and returns the total score.

        Args:
            correct(int): Number of the correct option in the alphabet -1. E.g: 2(c)
            corrects(int): Score of the user
        
        Return:
            (int): New score after the user answered
        """
        answer = input("Enter choice: ").lower().strip()
        if answer[0] == multiple[correct]:
            corrects = corrects + 1
        return corrects

    def dividing_system():
        """
        Generates random multiple choice questions based on division.

        Return:
            (int): Position in the alphabet of the correct option -1. E.g: 3(d)
        """
        pastanswers = []
        number1, number2 = get_random()
        print(f"Divide: {number1} by {number2}")
        correct = random.randrange(0,3)
        for i in range(4):
            if i != correct:
                new_answer = random.randrange(-2, 2) # Randomize the choices
                while (new_answer in pastanswers) or (new_answer == 0): # Make sure no option is repeated
                    new_answer = random.randrange(-2, 2)
                print(f"{multiple[i]}) {int(number1/number2+new_answer)}")
                pastanswers.append(new_answer)
            else:
                print(f"{multiple[i]}) {int(number1/number2)}")
        return correct

    def multiplying_system():
        """
        Generates random multiple choice questions based on multiplication.

        Return:
            (int): Position in the alphabet of the correct option -1. E.g: 3(d)
        """
        pastanswers = []
        number1 = random.randrange(2, 30)
        number2 = random.randrange(2, 25)
        print(f"Multiply: {number1} and {number2}")
        correct = random.randrange(0,3)
        for i in range(4):
            if i != correct:
                new_answer = random.randrange(-2, 2) # Randomize the choices
                while (new_answer in pastanswers) or (new_answer == 0): # Make sure no option is repeated
                    new_answer = random.randrange(-2, 2)
                print(f"{multiple[i]}) {int(number1*number2+new_answer)}")
                pastanswers.append(new_answer)
            else:
                print(f"{multiple[i]}) {int(number1*number2)}")
        return correct

    def adding_system():
        """
        Generates random multiple choice questions based on addition.

        Return:
            (int): Position in the alphabet of the correct option -1. E.g: 3(d)
        """
        pastanswers = []
        number1 = random.randrange(2, 30)
        number2 = random.randrange(2, 25)
        print(f"Add: {number1} and {number2}")
        correct = random.randrange(0, 3)
        for i in range(4):
            if i != correct:
                new_answer = random.randrange(-2, 2) # Randomize the choices
                while (new_answer in pastanswers) or (new_answer == 0): # Make sure no option is repeated
                    new_answer = random.randrange(-2, 2)
                print(f"{multiple[i]}) {int(number1+number2+new_answer)}")
                pastanswers.append(new_answer)
            else:
                print(f"{multiple[i]}) {int(number1+number2)}")
        return correct

    def subtract_system():
        """
        Generates random multiple choice questions based on subtraction.

        Return:
            (int): Position in the alphabet of the correct option -1. E.g: 3(d)
        """
        pastanswers = []
        number1, number2 = get_random()
        print(f"Subtract: {number1} and {number2}")
        correct = random.randrange(0,3)
        for i in range(4):
            if i != correct: 
                new_answer = random.randrange(-2, 2) # Randomize the choices
                while (new_answer in pastanswers) or (new_answer == 0): # Make sure no option is repeated
                    new_answer = random.randrange(-2, 2)
                print(f"{multiple[i]}) {int(number1-number2+new_answer)}")
                pastanswers.append(new_answer)
            else:
                print(f"{multiple[i]}) {int(number1-number2)}")
        return correct

    multiple = ["a","b","c","d"]
    cases = ["/", "+", "*", "-"]

    choice = menu()
    while choice != "Exit":
        match choice:
            case "Dividing" :
                corrects, tries = initialize()
                for k in range(tries):
                    os.system('cls' if os.name == 'nt' else 'clear') # Cleans terminal
                    correct = dividing_system()
                    corrects = check_answer(correct,corrects)
                    if k == tries-1:
                        print(f"Score: {corrects}/{tries}")
                        choice = menu()

            case "Multiplying":
                corrects, tries = initialize()
                for k in range(tries):
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    correct = multiplying_system()
                    corrects = check_answer(correct,corrects)
                    if k == tries-1:
                        print(f"Score: {corrects}/{tries}")
                        choice = menu()

            case "Adding":
                corrects, tries = initialize()
                for k in range(tries):
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    correct = adding_system()
                    corrects = check_answer(correct,corrects)
                    if k == tries-1:
                        print(f"Score: {corrects}/{tries}")
                        choice = menu()

            case "Subtracting":
                corrects, tries = initialize()
                for k in range(tries):
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    correct = subtract_system()
                    corrects = check_answer(correct,corrects)
                    if k == tries-1:
                        print(f"Score: {corrects}/{tries}")
                        choice = menu()
                        
            case "Everything":
                corrects, tries = initialize()
                for k in range(tries):
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    random.shuffle(cases)
                    match cases[0]:
                        case "/":
                            correct = dividing_system()
                            corrects = check_answer(correct,corrects)
                        case "*":
                            correct = multiplying_system()
                            corrects = check_answer(correct, corrects)
                        case "+":
                            correct = adding_system()
                            corrects = check_answer(correct, corrects)
                        case "-":
                            correct = subtract_system()
                            corrects = check_answer(correct, corrects)
                    if k == tries-1:
                            print(f"Score: {corrects}/{tries}")
                            choice = menu()


def simple_calculator():
    history = []

    class Calculation_history:
        def __init__(self, history: list[str]):
            self._history = history
        
        def get_history(self) -> None:
            spot_history = 1

            for equation in self._history:
                print(f"{spot_history}. {equation}")
                spot_history += 1

        def output_history_file(self) -> None:
            with open("Calculator history.txt", "w") as file:
                pass

    def menu() -> None:
        while True:
            option = promptinput(
                "-----------------------------------------------------",
                ["{ 1. Calculate }", "{ 2. Get calculator history }", "{ 3. Clear calculator history file }", "{ 4. Exit }"])
            match option:
                case "{ 1. Calculate }":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    calculate(history)

                case "{ 2. Get calculator history }":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    show_history = Calculation_history(history)
                    show_history.get_history()

                case "{ 3. Clear calculator history file }":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    output_history = Calculation_history(history)
                    output_history.output_history_file()

                case "{ 4. Exit }":
                    return


    def test_calculate() -> bool:
        return True
        
    def calculate(history: list[str]) -> None:
        option = promptinput(
            "Would you like to input a calculation/calculations",
            ["{ 1. Yes }", "{ 2. Go back to menu }"])
        os.system('cls' if os.name == 'nt' else 'clear')
        if option == "{ 1. Yes }":
            while True:
                equation = str(input("Equation(use: '+' '-' '/' '*' '**' 'sqrt(x)'): "))
                #if not true retry
                if test_calculate() == True:
                    #use alt to evaluate expression
                    result = sympify(equation)
                    result_text = f"| {equation} = {result} |"
                    print(result_text)
                    history.append(result_text)

                    with open("Calculator history.txt", "a+") as file:
                        file.writelines(result_text + "\n")

                    next_option = promptinput(
                    "Would you like to input a calculation again?",
                    choices= ["{ 1. Yes }", "{ 2. Go back to menu }"])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if next_option == "{ 2. Go back to menu }":
                        break

        elif option == "{ 2. Go back to menu }":   
            return None
    
    menu()

def geometry_calc():
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
            """
            Method for solving the diamter of a circle
            """
            cir_diameter = 2 * self._radius
            print(f"The diameter of the circle is {cir_diameter:.2f} units.")
        def circumference(self):
            """
            Method for solving the circumference of a circle
            """
            cir_circumference = 2 * self.pi * self._radius
            print(f"The circumference of the circle is {cir_circumference:.2f} units.")
        def radius(self):
            """
            Method for solving the radius of a circle
            """
            cir_radius = self._circumference / (2 * self.pi)
            print(f"The circumference of the circle is {cir_radius:.2f} units.")
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


    def menu():
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

    menu()

def shaper():

    #TUTORIALS VV
    #https://www.geeksforgeeks.org/python/how-to-draw-shapes-in-matplotlib-with-python/
    #https://matplotlib.org/stable/gallery/mplot3d/index.html
    while True:
        fig, ax = matplotlib.pyplot.subplots()
        shaper = promptinput("What shape?", ["Circle", "Rectangle/Square", "Exit"])
        if shaper == "Circle":
            radius = float(input("Enter radius: "))
            ax.add_patch(Circle((radius*4/2, radius*4/2), radius=radius, edgecolor="lightblue", facecolor="lightblue"))
            ax.set_xlim(0,radius*4)
            ax.set_ylim(0,radius*4)
            ax.set_aspect('equal')
            matplotlib.pyplot.grid(True)
            matplotlib.pyplot.title("Circle")
            ax.set_yticks(numpy.arange(0, radius*4+1, radius//2))
            ax.set_xticks(numpy.arange(0, radius*4+1, radius//2))
            shaper = promptinput("What shape?", ["Circle", "Rectangle/Square", "Exit"])
        elif shaper == "Rectangle/Square":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            ax.add_patch(Rectangle((width, height), width=width, height=height, edgecolor="lightblue", facecolor="lightblue"))
            ax.set_xlim(0, width*3)
            ax.set_ylim(0, height*3)
            ax.set_aspect('equal')
            matplotlib.pyplot.grid(True)
            matplotlib.pyplot.title("Rectangle/Square")
            ax.set_yticks(numpy.arange(0, height*3+1, height//2))
            ax.set_xticks(numpy.arange(0, width*3+1, width//2))
            shaper = promptinput("What shape?", ["Circle", "Rectangle/Square", "Exit"])
        else: 
            return
        matplotlib.pyplot.show()

def scientific_calc():
    history = []
    class Calculation_history:
        def __init__(self, history: list[str]):
            self._history = history
    
        def get_history(self) -> None:
            spot_history = 1

            for equation in self._history:
                print(f"{spot_history}. {equation}")
                spot_history += 1

        def reset_history(self) -> None:
            with open("Calculator history.txt", "w") as file:
                pass

    def menu() -> None:

        mode = "DEG" #rad/deg

        while True:
            option = promptinput(
                "-----------------------------------------------------",
                ["{ 1. Calculate }", "{ 2. Change mode: RAD/DEG}", "{ 3. How to use the calculator }", "{ 4. Get calculator history }",
                "{ 5. Clear calculator history file }", "{ 6. Exit }"])
            match option:
                case "{ 1. Calculate }":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    calculate(history, mode)

                case "{ 2. Change mode: RAD/DEG}":
                    if mode == "DEG":
                        mode = "RAD"
                    else:
                        mode = "DEG"
                    print(f"Mode: |{mode}|")

                case "{ 3. How to use the calculator }":
                    information()
            
                case "{ 4. Get calculator history }":
                    show_history = Calculation_history(history)
                    show_history.get_history()

                case "{ 5. Clear calculator history file }":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    output_history = Calculation_history(history)
                    output_history.reset_history()

                case "{ 6. Exit }":
                    return

    def information():
        # (use: '+' '-' '/' '*' '**' 'sqrt(x)')
        # how to use in rad and deg and log(x, base)
        pass


    def test_calculate() -> bool:
        return True #test
    
    def calculate(history: list[str], mode: str) -> None:
        while True:
            option = promptinput(
                "Would you like to input a calculation/calculations",
                ["{ 1. Calculate }", "{ 2. Go back to menu }"])
        
            os.system('cls' if os.name == 'nt' else 'clear')
            match option:
                case "{ 1. Calculate }":
                    while True:
                        original_eq = str(input("Equation: "))
                        equation = original_eq.split()
                        
                        #if not true retry
                        if test_calculate() == True:
                            #use alt to evaluate expression
                            if mode == "DEG":

                                for i in range(len(equation)):
                                    start = 0
                                    end = 0
                                    final = ""

                                    for j in range(len(equation[i])):
                                        if equation[i][j] == "(":
                                            start = j + 1

                                        elif equation[i][j] == ")":
                                            end = j
                                        
                                        num = equation[i][start:end]

                                    if "sin" in  equation[i]:
                                        equation[i] = f"{sympy.sin((int(num) * math.pi)/180)}"
                                        
                                    elif "cos" in  equation[i]:
                                        equation[i] = f"{sympy.cos((int(num) * math.pi)/180)}"

                                    elif "tan" in  equation[i]:
                                        equation[i] = f"{sympy.tan((int(num) * math.pi)/180)}"
                                        
                                for new in equation:
                                    final += new
                                result = sympify(final)

                                final_result= f"{round(result, 2):.2f}"
                                
                                result_text = f"| {original_eq} = {final_result} |"
                                print(result_text)
                                history.append(result_text)

                                with open("Calculator history.txt", "a+") as file:
                                    file.writelines(result_text + "\n")
                                            
                            else:
                                result = sympify(equation)
                                result_text = f"| {equation} = {result} |"
                                print(result_text)

                                history.append(result_text)

                                with open("Calculator history.txt", "a+") as file:
                                    file.writelines(result_text + "\n")

                            next_option = promptinput(
                            "Would you like to input a calculation again?",
                            choices= ["{ 1. Yes }", "{ 2. Go back }"])
                            os.system('cls' if os.name == 'nt' else 'clear')
                            if next_option == "{ 2. Go back }":
                                break
                case "{ 2. Go back to menu }":  
                    break
                        
    menu()

def algebra_formulas():
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
                        n = Pascals_Triangle(int(input("Enter the value of N: ")))
                        n.printing_triangle()
                    except:
                        print("Enter a valid value for N.")
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
    main()


def main():
    tests = {}
    menu_options = ["Create new test", "Load test from file", "Run a test",
                     "Study Guides", "Math Definitions", "Graph Calculator", "Mental Math",
                     "Simple Calculator", "Scientific Calculator", "Geometry Calculator",  
                     "Draw Shapes", "Algebra Calculator", "Exit"]
    
    choice = promptinput("What do you want?", menu_options)
    while choice != "Exit":
        os.system('cls' if os.name == 'nt' else 'clear')  # Clean terminal
        match choice:
            case "Create new test":
                new_tests = create_tests()
                tests.update(new_tests)
                choice = promptinput("What do you want?", menu_options)

            case "Load test from file":
                filename = input("Enter filename (Please include .txt): ")
                loaded = load_test(filename)
                tests.update(loaded)
                choice = promptinput("What do you want?", menu_options)

            case "Run a test":
                type_of_test = promptinput("Would you like to run a :", ["Custom test", "Pre-Made Test"])
                if type_of_test == "Custom test":
                    if tests == {}:
                        print("No tests were loaded.")
                    else:
                        run_test(tests)
                if type_of_test == "Pre-Made Test":
                    test_choice()
                choice = promptinput("What do you want?", menu_options)

            case "Study Guides":
                show_sources()
                choice = promptinput("What do you want?", menu_options)

            case "Math Definitions":
                math_definitions()
                choice = promptinput("What do you want?", menu_options)

            case "Graph Calculator":
                graph_calculator()
                choice = promptinput("What do you want?", menu_options)

            case "Mental Math":
                mental_math()
                choice = promptinput("What do you want?", menu_options)
            
            case "Simple Calculator":
                simple_calculator()
                choice = promptinput("What do you want?", menu_options)
            
            case "Scientific Calculator":
                scientific_calc()
                choice = promptinput("What do you want?", menu_options)

            case "Geometry Calculator":
                geometry_calc()
                choice = promptinput("What do you want?", menu_options)
            
            case "Algebra Calculator":
                algebra_formulas()
                choice = promptinput("What do you want?", menu_options)

            case "Draw Shapes":
                shaper()
                choice = promptinput("What do you want?", menu_options)
            

    print("Bye!")


if __name__ == '__main__':
    main()