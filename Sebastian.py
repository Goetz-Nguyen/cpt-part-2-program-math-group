import sympy, random, os, matplotlib.pyplot, numpy
from InquirerPy import prompt

def promptinput(message: str,choices: list) -> str:
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


def geometry_test() -> int:
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

def polynomials_test() -> int:
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

def algebra_tests() -> int:
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

def coordinate_planes_test() -> int:
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

def trigonometry_test() -> int:
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

def quadratics_test() -> int:
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
            print("== TRIGONOMETRY SOURCES ==")


            print("Khan Academy Trigonometry")
            print("Full lessons and practice for trigonometry.")
            print("https://www.khanacademy.org/math/trigonometry")
            print("")


            print("Trigonometry Math Is Fun")
            print("Simple explanations and examples for trig.")
            print("https://www.mathsisfun.com/algebra/trigonometry.html")
            print("")


            print("Intro to Trig Ratios")
            print("Explains sine cosine and tangent.")
            print("https://www.khanacademy.org/math/trigonometry/trigonometry-right-triangles/intro-to-the-trig-ratios/v/basic-trigonometry-ii")
            print("")


            print("Solve Right Triangles Using Trig")
            print("Shows how to find missing sides and angles.")
            print("https://www.khanacademy.org/math/trigonometry/trigonometry-right-triangles/trig-solve-for-a-side/v/example-trig-to-solve-the-sides-and-angles-of-a-right-triangle")
            print("")


            print("SOH CAH TOA Explained")
            print("Teaches trig ratios using triangles.")
            print("https://www.youtube.com/watch?v=PUB0TaZ7bhA")
            print("")


            print("Finding Missing Sides Using Trigonometry")
            print("Shows step by step trig examples.")
            print("https://www.youtube.com/watch?v=bQLEVsfVQ_o")
            print("")


            print("Finding Missing Angles Using Trigonometry")
            print("Shows how to calculate angles with trig.")
            print("https://www.youtube.com/watch?v=fMIqJzt2sCk")
            print("")


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


def load_test(filename) -> dict:
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


def create_tests() -> dict:
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