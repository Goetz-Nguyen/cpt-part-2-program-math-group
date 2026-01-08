from InquirerPy import prompt
import random, os
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

mental_math()