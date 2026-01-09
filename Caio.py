import sympy, random, os, matplotlib.pyplot, numpy
from InquirerPy import prompt
from PyDesmos import Graph
from matplotlib.patches import Circle, Rectangle

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
    def get_random() -> tuple[int]:
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

    def initialize() -> tuple[int]:
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

    def check_answer(correct: int, corrects: int) -> int:
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

    def dividing_system() -> int:
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

    def multiplying_system() -> int:
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

    def adding_system() -> int:
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

    def subtract_system() -> int:
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
            matplotlib.pyplot.show()
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
            matplotlib.pyplot.show()
            shaper = promptinput("What shape?", ["Circle", "Rectangle/Square", "Exit"])
        else: 
            return
        matplotlib.pyplot.show()