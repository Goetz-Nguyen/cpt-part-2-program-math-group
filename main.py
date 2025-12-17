import sympy, random, os
from InquirerPy import prompt
from PyDesmos import Graph

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
    print("== PRE MADE GEOMETRY TEST QUESTIONS!! ==")
    score = 0
    total = 10

    # 1
    print("#1: In a right triangle, the angle is 37*. The adjacent side is 12.")
    print("Find the hypotenuse. (Round to nearest tenth)")
    ans = input("Your answer: ")
    if ans in ["15.0", "15", "15.1"]:
        score += 1

    print("")

    #2
    print("#2:An arc measures 84*. What is the measure of the inscribed angle intercepting it?")
    print("A) 42*   B) 84*   C) 126*   D) 168*")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1

    print("")
    
    #3
    print("#3: A cylinder has a radius 4 and height 10. What is its volume? (Use pi)")
    ans = input("Your answer: ")
    if ans == "160":
        score += 1

    print("")
    
    #4
    print("#4: Find the slope between (–3, 5) and (4, –2).")
    ans = input("Your answer: ")
    if ans in ["-1", "-1.0"]:
        score += 1

    print("")
    
    #5
    print("#5: Use the Law of Cosines:")
    print("Given sides a=7, b=9, and angle C=42*, solve for side c (nearest tenth).")
    ans = input("Your answer: ")
    if ans in ["6", "6.0", "6.1"]:
        score += 1

    print("")
    
    #6
    print("#6: A triangle is reflected over the y-axis. What happens to point (x, y)?")
    print("A) (-x, y)   B) (x, -y)   C) (-x, -y)   D) (y, x)")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1

    print("")

    #7
    print("#7: Two similar triangles have scale factor 3:5.")
    print("If a side in the smaller triangle is 12, what is the corresponding larger side?")
    ans = input("Your answer: ")
    if ans == "20":
        score += 1

    print("")
    # 8
    print("#8: Find the distance between points (2, 3) and (11, 9).")
    ans = input("Your answer: ")
    if ans in ["10.8", "10.819", "11"]:
        score += 1

    print("")
    
    # 9
    print("#9: Find the area of a triangle with sides 8, 9, and 13.")
    ans = input("Your answer: ")
    if ans in ["36", "37"]:
        score += 1

    print("")
    
    # 10
    print("#10: What is the interior angle of a regular 12 sided polygon?")
    ans = input("Your answer: ")
    if ans in ["150", "150*", "150 degrees"]:
        score += 1

    print("")
    print("== GEOMETRY TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")
    return score

def polynomials_test():

    print("== PRE MADE POLYNOMIALS TEST QUESTIONS!! ==")
    score = 0
    total = 10

    # 1
    print("#1: Factor using the greatest common factor: 18x^5 + 36x^4")
    print("A) 18x^4(x + 2)   B) 18x^5(x + 2)   C) 6x^4(3x + 6)   D) x^4(18x + 36)")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1

    print("")

    # 2
    print("#2: Find the product: (x + 4)(x^2 − 3x − 5)")
    print("A) x^3 + x^2 − 17x − 20")
    print("B) x^3 + 4x^2 − 3x − 20")
    print("C) x^3 + x^2 − 11x − 20")
    print("D) x^3 + 4x^2 − 17x − 20")
    ans = input("Your answer: ")
    if ans == "d":
        score += 1

    print("")

    # 3
    print("#3: Factor completely: x^2 − 16")
    print("A) (x − 8)(x + 2)   B) (x − 4)(x + 4)   C) (x − 16)(x + 1)   D) Prime")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1

    print("")

    # 4
    print("#4: Simplify: (5x^3)(2x^2)")
    print("A) 10x^5   B) 7x^6   C) 10x^6   D) x^5")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1

    print("")

    # 5
    print("#5: Factor: x^2 + 9x + 20")
    print("A) (x + 10)(x + 2)   B) (x + 5)(x + 4)   C) (x − 5)(x − 4)   D) Prime")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1

    print("")

    # 6
    print("#6: What is the degree of the polynomial: 7x^3 − 4x + 6?")
    print("A) 1   B) 2   C) 3   D) 6")
    ans = input("Your answer: ")
    if ans == "c":
        score += 1

    print("")

    # 7
    print("#7: Simplify: (x^2 − 9) ÷ (x − 3)")
    print("A) x − 3   B) x + 3   C) x^2 − 3   D) Cannot be simplified")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1

    print("")

    # 8
    print("#8: Expand: (x + 5)^2")
    print("A) x^2 + 25   B) x^2 + 10x + 25   C) x^2 − 10x + 25   D) 2x + 10")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1

    print("")

    # 9
    print("#9: Factor by grouping: x^3 − x^2 − 6x + 6")
    print("A) (x − 1)(x^2 − 6)")
    print("B) (x + 1)(x^2 − 6)")
    print("C) (x − 3)(x^2 − 2)")
    print("D) Prime")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1

    print("")

    # 10
    print("#10: Evaluate when x = 3: 2x^2 − 5x + 4")
    print("A) 7   B) 10   C) 5   D) 1")
    ans = input("Your answer: ")
    if ans == "c":
        score += 1

    print("")
    print("== POLYNOMIAL TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")

    return score

def show_sources():
    print("== STUDY SOURCES ==")
    print("Which unit do you want sources for?")
    print("1) Geometry")
    print("2) Back")

    choice = input("Choose an option: ")

    if choice == "1":
        print("")
        print("== GEOMETRY SOURCES ==")

        print("Khan Academy High School Trigonometry & Geometry")
        print("https://www.khanacademy.org/math/geometry/hs-geo-trig")
        print("")

        print("Intro to Trigonometry (YouTube)")
        print("https://www.youtube.com/watch?v=gSGbYOzjynk")
        print("")

        print("Right Triangle Trigonometry")
        print("https://youtu.be/fxTsG4qkz1U")
        print("")

        print("Law of Sines & Cosines")
        print("https://youtu.be/bpRsuccb6dI")
        print("")

        print("Area of Triangles (Trig)")
        print("https://youtu.be/PXnAKcBipKM")
        print("")

        print("Distance Formula & Midpoint")
        print("https://youtu.be/qcb-mcREIi0")
        print("")

        print("Similar Triangles")
        print("https://youtu.be/P1f3sJpIYGI")
        print("")

        print("Transformations (Reflections, Rotations)")
        print("https://youtu.be/5NyuamsbLMo")
        print("")

        print("Circles & Arc Length")
        print("https://youtu.be/a1DXlvwnqUw")
        print("")

        print("Polygon Angles")
        print("https://youtu.be/E_-3ulbtcLk")
        print("")

        print("Volume of Solids")
        print("https://youtu.be/pvMuDPVOm7Y")
        print("")

        print("MathBits Geometry Notebook")
        print("https://mathbitsnotebook.com/Geometry/Geometry.html")
        print("")

        print("Coordinate Geometry Review")
        print("https://youtu.be/DerrI1FstO4")
        print("")

    else:
        return
def save_test(test_name, questions, answers):
    file = open(test_name + ".txt", "w")
    for i in range(len(questions)):
        file.write(questions[i] + "\n")
        file.write(answers[i] + "\n")
    file.close()


def load_test(filename):
    tests = {}
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
    except:
        print("File could not be loaded.")
        return tests

    questions = []
    answers = []

    i = 0
    while i < len(lines):
        questions.append(lines[i].strip())
        answers.append(lines[i + 1].strip())
        i += 2

    test_name = filename.replace(".txt", "")
    tests[test_name] = {"questions": questions, "answers": answers}
    return tests


def create_tests():
    tests = {}

    print("== CREATING A NEW TEST ==")
    test_name = input("Please enter a name for this test: ")

    num = int(input("How many questions do you want to make for this test? "))

    questions = []
    answers = []

    i = 0
    while i < num:
        print("Question", i + 1)
        question = input("Type your question: ")
        answer = input("Type the correct answer: ")
        questions.append(question)
        answers.append(answer)
        i += 1

    tests[test_name] = {"questions": questions, "answers": answers}
    save_test(test_name, questions, answers)

    print(f"The test '{test_name}' was created and saved.")
    return tests


def run_test(tests):
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
    print("Which Pre-Made test would you like to pick?")
    print("1. Geometry")
    print("2. Polynomials")
    print("3. Exit")
    pre_made_test_options = input("Choice: ")
    if pre_made_test_options == "1":
        geometry_test()
    if pre_made_test_options == "2":
        polynomials_test()
    else:
        return
    
def graph_calculator():
    menu = promptinput("What kind of graph?",["Trig", "Polynomial", "Exit"])
    error = False
    while menu != "Exit":
        os.system('cls' if os.name == 'nt' else 'clear') 
        if menu == "Polynomial":
            try:
                coefficient = []
                equation = ""
                exponent = int(input("Enter graph degree: "))
                for i in range(exponent+1):
                    coefficient.append(int(input(f"Enter coefficient of the the term with degree {i}: ")))
                for i in range(len(coefficient), 0, -1):
                    if i != 0:
                        equation += f"{coefficient[i-1]}*x^{i-1} + "
                equation = equation[:len(equation)-3]
                error = False
            except:
                error = True
                print("Enter valid numbers!")
            if not error:
                try:
                    with Graph('my graph') as G:
                            f, x = G.f, G.x
                            f[x] = equation
                except:
                    print("Couldn't graph!")
                menu = promptinput("What kind of graph?",["Trig", "Polynomial", "Exit"])
        elif menu == "Trig":
            trig_type = promptinput("Type of trig?",["Cos", "Sin", "Tan"])
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
    def menu():

        return promptinput("What kind of math?", ["Everything","Dividing", "Multiplying", "Adding", "Subtracting", "Exit"])
    def get_random():
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
        tries = 0
        while tries < 1:
            try:
                tries = int(input("How many questions? "))
            except:
                print("Enter a valid number!")
        return 0, tries

    def check_answer(correct, corrects):
        answer = input("Enter choice: ").lower().strip()
        if answer[0] == multiple[correct]:
            corrects = corrects + 1
            return corrects

    def dividing_system():
        pastanswers = []
        number1, number2 = get_random()
        print(f"Divide: {number1} by {number2}")
        correct = random.randrange(0,3)
        for i in range(4):
            if i != correct:
                new_answer = random.randrange(-2, 2)
                while (new_answer in pastanswers) or (new_answer == 0):
                    new_answer = random.randrange(-2, 2)
                print(f"{multiple[i]}) {int(number1/number2+new_answer)}")
                pastanswers.append(new_answer)
            else:
                print(f"{multiple[i]}) {int(number1/number2)}")
        return correct

    def multiplying_system():
        pastanswers = []
        number1 = random.randrange(2, 30)
        number2 = random.randrange(2, 25)
        print(f"Multiply: {number1} and {number2}")
        correct = random.randrange(0,3)
        for i in range(4):
            if i != correct:
                new_answer = random.randrange(-2, 2)
                while (new_answer in pastanswers) or (new_answer == 0):
                    new_answer = random.randrange(-2, 2)
                print(f"{multiple[i]}) {int(number1*number2+new_answer)}")
                pastanswers.append(new_answer)
            else:
                print(f"{multiple[i]}) {int(number1*number2)}")
        return correct

    def adding_system():
        pastanswers = []
        number1 = random.randrange(2, 30)
        number2 = random.randrange(2, 25)
        print(f"Add: {number1} and {number2}")
        correct = random.randrange(0, 3)
        for i in range(4):
            if i != correct:
                new_answer = random.randrange(-2, 2)
                while (new_answer in pastanswers) or (new_answer == 0):
                    new_answer = random.randrange(-2, 2)
                print(f"{multiple[i]}) {int(number1+number2+new_answer)}")
                pastanswers.append(new_answer)
            else:
                print(f"{multiple[i]}) {int(number1+number2)}")
        return correct

    def subtract_system():
        pastanswers = []
        number1, number2 = get_random()
        print(f"Subtract: {number1} and {number2}")
        correct = random.randrange(0,3)
        for i in range(4):
            if i != correct:
                new_answer = random.randrange(-2, 2)
                while (new_answer in pastanswers) or (new_answer == 0):
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
                    os.system('cls' if os.name == 'nt' else 'clear') 
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

def main():
    tests = {}
    menu_options = ["Create new test", "Load test from file", "Run a test",
                     "Study Guides", "Graph Calculator", "Mental Math", "Exit"]
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
                type_of_test = input("Would you like to run a custom test (1), or a Pre-Made Test? (2): ")
                if type_of_test == "1":
                    if tests == {}:
                        print("No tests were loaded.")
                    else:
                        run_test(tests)
                if type_of_test == "2":
                    test_choice()
                choice = promptinput("What do you want?", menu_options)

            case "Study Guides":
                show_sources()
                choice = promptinput("What do you want?", menu_options)

            case "Graph Calculator":
                graph_calculator()
                choice = promptinput("What do you want?", menu_options)

            case "Mental Math":
                mental_math()
                choice = promptinput("What do you want?", menu_options)

    print("Bye!")


if __name__ == '__main__':
    main()