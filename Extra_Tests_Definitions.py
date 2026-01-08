def algebra_tests():
    print("== PRE MADE ALGEBRA TEST QUESTIONS!! ==")
    score = 0
    total = 5


    # 1
    print("#1: Find all sides of a right triangle whose perimeter is equal to 60 cm and its area is equal to 150 square cm.")
    print("Enter the numbers via the example: '10 20 30'")
    ans = input("Your answer: ")
    if ans in ["25 15 20", "25 20 15", "15 25 20", "15 20 25", "20 15 25", "20 25 15"]:
        score += 1

    print("")

    #2
    print("#2: If 200 is added to a positive integer I, the result is a square number. If 276 is added to to the same integer I, another square number is obtained. Find I.")
    print("A) Make sure your answer is writtin in this exact format: 'I=x^z - _ = _'")
    ans = input("Your answer: ")
    if ans == "I=x^2 − 200 = 124":
        score += 1

    print("")
   
    #3
    print("#3: A rock is dropped into a water well and it travels approximately 16t^2 feet in t seconds. If the splash is heard")
    print("3.5 seconds later and the speed of sound is 1087 feet/second, what is the height of the well? (Round to the nearest unit)")
    ans = input("Your answer: ")
    if ans in ["178", "178 Feet", "178ft", "178Ft", "178FT", "178Feet", "178FEET", "178 FEET"]:
        score += 1

    print("")
   
    #4
    print("#4: It takes pump A 2 hours less time than pump B to empty a swimming pool.")
    print("Pump A is started at 8:00 a.m. and pump B is started at 10:00 a.m. At 12:00 p.m.")
    print("60 percent of the pool is empty when pump B broke down. How much time after 12:00 p.m. would it take pump A to empty the pool?")
    ans = input("Your answer: ")
    if ans in ["3.766", "3.7", "3.8","3.766h", "3.7h", "3.8h","3.766hours", "3.7hours", "3.8hhours",]:
        score += 1

    print("")

    #5
    print("#5: Two boats on opposite banks of a river start moving towards each other. They first pass each other")
    print("1400 meters from one bank. They each continue to the opposite bank, immediately turn around and start back to the other bank. When they pass each other a second time, they are")
    print("600 meters from the other bank. We assume that each boat travels at a constant speed all along the journey. Find the width of the river?")
    print("Given sides a=7, b=9, and angle C=42*, solve for side c (nearest tenth).")
    ans = input("Your answer: ")
    if ans in ["3600 meters", "3600 m", "3600m"]:
        score += 1

    print("")

    print("")
    print("== ALGEBRA TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")
    return score

def coordinate_planes_test():
    print("== PRE MADE COORDINATE PLANES TEST QUESTIONS!! ==")
    score = 0
    total = 10

    # 1
    print("#1: What quadrant is the point (4, -7) located in?")
    print("A) Quadrant I   B) Quadrant II   C) Quadrant III   D) Quadrant IV")
    ans = input("Your answer: ")
    if ans == "d":
        score += 1

    print("")

    # 2
    print("#2: What is the x-coordinate of the point (-3, 5)?")
    ans = input("Your answer: ")
    if ans == "-3":
        score += 1

    print("")

    # 3
    print("#3: Find the slope between the points (2, 4) and (6, 12).")
    ans = input("Your answer: ")
    if ans in ["2", "2.0"]:
        score += 1

    print("")

    # 4
    print("#4: Which point lies on the y-axis?")
    print("A) (5, 0)   B) (0, 6)   C) (3, 3)   D) (-4, 2)")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1

    print("")

    # 5
    print("#5: Find the distance between the points (1, 1) and (4, 5). (Round to nearest tenth)")
    ans = input("Your answer: ")
    if ans in ["5", "5.0", "5.1"]:
        score += 1

    print("")

    # 6
    print("#6: If a point is reflected over the x-axis, what happens to (x, y)?")
    print("A) (x, -y)   B) (-x, y)   C) (-x, -y)   D) (y, x)")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1

    print("")

    # 7
    print("#7: What is the midpoint between the points (2, 6) and (8, 10)?")
    ans = input("Your answer: ")
    if ans in ["5 8", "(5,8)", "(5, 8)", "5,8", "5, 8"]:
        score += 1

    print("")

    # 8
    print("#8: Which point is in Quadrant III?")
    print("A) (3, -4)   B) (-2, 5)   C) (-6, -1)   D) (4, 2)")
    ans = input("Your answer: ")
    if ans == "c":
        score += 1

    print("")

    # 9
    print("#9: What is the slope of a horizontal line?")
    ans = input("Your answer: ")
    if ans in ["0", "0.0"]:
        score += 1

    print("")

    # 10
    print("#10: What is the ordered pair of the origin?")
    ans = input("Your answer: ")
    if ans in ["0 0", "(0,0)", "(0, 0)", "0,0", "0, 0"]:
        score += 1

    print("")
    print("== COORDINATE PLANES TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")
    return score

def trigonometry_test():
    print("== PRE MADE TRIGONOMETRY TEST QUESTIONS!! ==")
    score = 0
    total = 10

    # 1
    print("#1: In a right triangle, sin(0) = opposite / ?")
    print("A) Adjacent   B) Hypotenuse   C) Tangent   D) Cosine")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1

    print("")

    # 2
    print("#2: cos(0) = ? / hypotenuse")
    print("A) Opposite   B) Adjacent   C) Tangent   D) Sine")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1

    print("")

    # 3
    print("#3: tan(0) =")
    print("A) Opposite / Hypotenuse   B) Adjacent / Hypotenuse")
    print("C) Opposite / Adjacent   D) Hypotenuse / Opposite")
    ans = input("Your answer: ")
    if ans == "c":
        score += 1

    print("")

    # 4
    print("#4: Find sin(30*)")
    ans = input("Your answer: ")
    if ans in ["0.5", "1/2"]:
        score += 1

    print("")

    # 5
    print("#5: Find cos(60*)")
    ans = input("Your answer: ")
    if ans in ["0.5", "1/2"]:
        score += 1

    print("")

    # 6
    print("#6: A ladder leans against a wall making a 60* angle with the ground.")
    print("If the ladder is 10m long, how high up the wall does it reach? (Nearest tenth)")
    ans = input("Your answer: ")
    if ans in ["8.7", "8.66", "8.7m"]:
        score += 1

    print("")

    # 7
    print("#7: Which trig ratio is used for Opposite and Adjacent?")
    print("A) Sine   B) Cosine   C) Tangent   D) Secant")
    ans = input("Your answer: ")
    if ans == "c":
        score += 1

    print("")

    # 8
    print("#8: Find tan(45*)")
    ans = input("Your answer: ")
    if ans in ["1", "1.0"]:
        score += 1

    print("")

    # 9
    print("#9: An angle of elevation is measured:")
    print("A) Below the horizontal   B) Above the horizontal")
    print("C) From the vertical   D) Inside the triangle")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1

    print("")

    # 10
    print("#10: What is the hypotenuse?")
    print("A) Shortest side   B) Longest side")
    print("C) Side opposite right angle   D) Both B and C")
    ans = input("Your answer: ")
    if ans == "d":
        score += 1

    print("")
    print("== TRIGONOMETRY TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")
    return score

def quadratics_test():
    print("== PRE MADE QUADRATICS TEST QUESTIONS!! ==")
    score = 0
    total = 10

    # 1
    print("#1: What is the standard form of a quadratic?")
    print("A) y = mx + b   B) y = ax^2 + bx + c")
    print("C) y = a(x + h)^2 + k   D) y = x^3")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1

    print("")

    # 2
    print("#2: Factor: x^2 + 5x + 6")
    ans = input("Your answer: ")
    if ans in ["(x+2)(x+3)", "(x + 2)(x + 3)"]:
        score += 1

    print("")

    # 3
    print("#3: Factor: x^2 − 9")
    ans = input("Your answer: ")
    if ans in ["(x-3)(x+3)", "(x + 3)(x - 3)"]:
        score += 1

    print("")

    # 4
    print("#4: What is the vertex of y = (x − 4)^2 + 1?")
    ans = input("Your answer: ")
    if ans in ["(4,1)", "(4, 1)"]:
        score += 1

    print("")

    # 5
    print("#5: How many zeros does a quadratic have?")
    print("A) 1   B) 2   C) 3   D) Depends")
    ans = input("Your answer: ")
    if ans == "d":
        score += 1

    print("")

    # 6
    print("#6: Find the axis of symmetry for y = x^2 − 6x + 2")
    ans = input("Your answer: ")
    if ans in ["x=3", "x = 3"]:
        score += 1

    print("")

    # 7
    print("#7: Expand: (x + 4)^2")
    ans = input("Your answer: ")
    if ans in ["x^2+8x+16", "x^2 + 8x + 16"]:
        score += 1

    print("")

    # 8
    print("#8: What is the shape of a quadratic graph?")
    ans = input("Your answer: ")
    if ans.lower() == "parabola":
        score += 1

    print("")

    # 9
    print("#9: Solve: x^2 − 4 = 0")
    ans = input("Your answer: ")
    if ans in ["x=2,-2", "2,-2", "-2,2"]:
        score += 1

    print("")

    # 10
    print("#10: If a > 0 in y = ax^2 + bx + c, the parabola opens:")
    print("A) Down   B) Up")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1

    print("")
    print("== QUADRATICS TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")
    return score

def math_definitions():
    print("== MATH DEFINITIONS & VOCABULARY ==")
    print("Choose a unit to view definitions for:")
    print("1) Geometry")
    print("2) Trigonometry")
    print("3) Algebra")
    print("4) Coordinate Planes")
    print("5) Quadratics")
    print("6) Polynomials.")

    choice = input("Enter a number: ")
    print("")

    if choice == "1":
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

    elif choice == "2":
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

    elif choice == "3":
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
        print("Greatest Common Factor: The largest number that divides into two temrs.")

    elif choice == "4":
        print("== COORDINATE PLANE VOCABULARY ==:")
        print("X-axis: The horizontal number line.")
        print("Y-axis: The vertical number line.")
        print("Origin: The point (0, 0).")
        print("Ordered Pair: Coordinates written as (x, y).")
        print("Quadrant: One of the four sections of the plane.")
        print("Slope: Rate of change between two points.")
        print("Coordinate Plane: The plane where a Horizontal line, and a vertical line intersect at their zero's.")
        print("Ordered Pair: (X,Y)")

    elif choice == "5":
        print("== QUADRATICS VOCABULARY == :")
        print("Quadratic Equation: An equation with x^2 as the highest power.")
        print("Parabola: The graph of a quadratic.")
        print("Vertex: The highest or lowest point of a parabola.")
        print("Axis of Symmetry: Vertical line through the vertex.")
        print("Zeros/Roots: X-values where the graph crosses the x-axis.")
        print("Standard Form: ax^2 + bx + c.")
        print("Quadratic Function: y = ax^2 + bx + c")

    elif choice == "6":
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

    else:
        return

def show_sources():
    print("== STUDY SOURCES ==")
    print("Which unit do you want sources for?")
    print("1) Geometry")
    print("2. Coordinate Planes")
    print("2) Back")

    choice = input("Choose an option: ")

    if choice == "1":
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


    elif choice == "2":
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
    else:
        return
    
algebra_tests()