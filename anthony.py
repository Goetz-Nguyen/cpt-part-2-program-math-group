from InquirerPy import prompt
from sympy import sympify, SympifyError
import os, math, sympy

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

def simple_calculator() -> None:


    history = [] #history of calculations

    class Calculation_history:
        """Records history of calculations

        Args:
            self._history(list[str]): (private) A list of all calculations done in the calculator
        """
        def __init__(self, history: list[str]) -> None:
            self._history = history
    
        def get_history(self) -> None:
            """Outputs the list of calculations in numeric order
            >>> { 2. Get calculator history }
            1. 12 + 5
            2. 3 / 2        
            """
            spot_history = 1 #Counter

            #Goes through the history and prints the spot of the calculation in order
            for equation in self._history:
                print(f"{spot_history}. {equation}")
                spot_history += 1

        def reset_history(self) -> None:
            """Clears the "Calculator history.txt" file that has the history of the calculations
            >>> { 3. Clear calculator history file }
            Clears the file
            """

            #pass clears the file inside when you write in it
            with open("Calculator history.txt", "w") as file:
                pass

    def menu() -> None:
        while True:
            option = promptinput(
                "-----------------------------------------------------",
                ["{ 1. Calculate }", "{ 2. Get calculator history }", "{ 3. Clear calculator history file }", "{ 4. Exit }"])
            match option:
                case "{ 1. Calculate }":
                    os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal 
                    calculate(history)

                case "{ 2. Get calculator history }":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    show_history = Calculation_history(history) #create a class object for the history class
                    show_history.get_history()

                case "{ 3. Clear calculator history file }":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    output_history = Calculation_history(history)
                    output_history.reset_history()

                case "{ 4. Exit }":
                    return
        
    def calculate(history: list[str]) -> None:
        """Calculator that calculates any user inputted equation
        args:
            history(list[str]): Will save the calculation inside
            mode(str): The current mode of the calculator
        >>> 12 + 5
        12 - 6 = 6
        12 / 2 = 6.0 
        """
                
        while True:
            #ask the user  wether they want to calculate or go back to the menu
            option = promptinput(
                "Would you like to input a calculation/calculations",
                ["{ 1. Yes }", "{ 2. Go back to menu }"])
            os.system('cls' if os.name == 'nt' else 'clear')
            if option == "{ 1. Yes }":
                
                while True:
                    try:
                        original_eq = str(input("Equation(use: '()' '+' '-' '/' '*' '**' 'sqrt()'): "))
                        equation = original_eq.split() #split version works for error checking
                        error_check = sympify(equation) #Uses the sympy library to check beforehand with the
                                                        #SympifyError library if there is incorrect syntax

                    except ZeroDivisionError: #Checks if devision by zero
                        print("")
                        print("Cannot divide by zero!")
                        print("")
                        continue

                    except SympifyError: #The library connected to sympy which checks for errors
                        print("")
                        print("Incorrect syntax")
                        print("")
                        continue

                    if original_eq == "" or original_eq == " ":
                        print("")
                        print("Cannot be empty")
                        print("")
                        continue
                    
                    else:
                        break     

                result = sympify(original_eq) #use the sympy library to evaluate the equation
                result_text = f"{original_eq} = {result}"
                print(result_text)

                history.append(result_text) #append to the history list

                with open("Calculator history.txt", "a+") as file: #append to the Calculator history.txt
                    file.writelines(result_text + "\n")

            else:
                return None
    menu()

def scientific_calculator() -> None:

    history = [] #history of calculations

    class Calculation_history:
        """Records history of calculations

        Args:
            self._history(list[str]): (private) A list of all calculations done in the calculator
        """
        def __init__(self, history: list[str]) -> None:
            self._history = history
    
        def get_history(self) -> None:
            """Outputs the list of calculations in numeric order
            >>> { 3. Get calculator history }
            1. 12 + 5
            2. 3 / 2        
            """
            spot_history = 1 #Counter

            #Goes through the history and prints the spot of the calculation in order
            for equation in self._history:
                print(f"{spot_history}. {equation}")
                spot_history += 1

        def reset_history(self) -> None:
            """Clears the "Calculator history.txt" file that has the history of the calculations
            >>> { 5. Clear calculator history file }
            Clears the file
            """

            #pass clears the file inside when you write in it
            with open("Calculator history.txt", "w") as file:
                pass

    def menu() -> None:
        """An interactive menu to navigate through the calculator
        >>> "{ 1. Calculate }"
        asks if you want to confirm to calculate or back out
        """

        mode = "DEG" #RAD/DEG -> always starts in degree mode

        while True:
            print(f"Current mode: [{mode}]")
            option = promptinput(
                "-----------------------------------------------------",
                ["{ 1. Calculate }", "{ 2. Change mode: RAD/DEG}", "{ 3. How to use the calculator }", "{ 4. Get calculator history }",
                "{ 5. Clear calculator history file }", "{ 6. Exit }"])
            
            #Use the promptinput to choose between options by scrolling with the up and down arrow keys
            match option:

                case "{ 1. Calculate }": #Goes to the main caalculator
                    os.system('cls' if os.name == 'nt' else 'clear') #Clears previous text in the terminal
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
                    show_history = Calculation_history(history) #Create a class object with the current history
                    show_history.get_history() #Use the class object to access a function from the class

                case "{ 5. Clear calculator history file }":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    output_history = Calculation_history(history)
                    output_history.reset_history()

                case "{ 6. Exit }":
                    return

    def information() -> None:
        """Prints out a personal guide on the syntax of how to use the scientific calculator"""

        print("""
    |============================================================|
    | --BASIC--
    | +    addition
    | -    subtraction
    | *    multiplication
    | /    division
    | **   power
    |          
    | --Examples--
    | 2 + 5
    | 7 - 3
    | 4 * 6
    | 8 / 2
    | 2**3
    |
    | ------------------------------------------------------------
    | Paranthesees
    | ( )
    |
    | --Example--
    | (3 + 5) * 2
    |
    | ------------------------------------------------------------
    | --Roots & Powers--
    | sqrt(x)      square root
    | x**2         square
    | x**(1/3)     cube root
    |
    | --Examples--
    | sqrt(25)
    | 5**2
    | 27**(1/3)
    |
    | ------------------------------------------------------------
    | --Logarithm--
    | ln(x)        natural logarithm
    | log(x)       logarithm
    | log(x, base) base set logarithm
    |
    | --Examples--
    | ln(5)
    | log(100, 10)
    |
    | ------------------------------------------------------------
    | --Triganometric Ratios--
    | sin(x)
    | cos(x)
    | tan(x)
    |
    | --Examples--
    | sin(pi/6)
    | cos(pi/3)
    | tan(pi/4)
    |
    | ------------------------------------------------------------
    | --Inverse Triganometric Ratios--
    | asin(x)
    | acos(x)
    | atan(x)
    |
    | --Examples--
    | asin(1/2)
    | acos(0)
    | atan(1)
    |
    | ------------------------------------------------------------
    | --Degree Mode--
    | sin(30*pi/180)
    | cos(60*pi/180)
    | tan(45*pi/180)
    |
    | ------------------------------------------------------------
    | --Constants--
    | pi  π  3.14...  
    | e   2.718...
    |
    | ------------------------------------------------------------
    | --Scientific Notation--
    | 1e3    = 1000
    | 5e-2   = 0.05
    |
    | ------------------------------------------------------------
    | --Absolute Value--
    | abs(x)
    |
    | --Example--
    | abs(-7)
    |
    | ------------------------------------------------------------
    | --Fraction--
    | 1/2
    | 3/4
    | 5/8
    |
    | --Example--
    | 2/3 + 1/6
    |
    | ------------------------------------------------------------
    | --Rounding--
    | round(x, 2) round to 2 decimal placements
    |
    | --Example--
    | round(3.14159, 3)
    |
    | ------------------------------------------------------------
    | --Percentage--
    | x / 100
    |
    | --Example--
    | 20/100
    |
    |============================================================|""")
    
    def calculate(history: list[str], mode: str) -> None:
        """Calculator that calculates any user inputted equation
        args:
            history(list[str]): Will save the calculation inside
            mode(str): The current mode of the calculator
        >>> 12 + 5
        12 + 5 = 17
        13 / 2 = 6.5
        """
        while True:
            option = promptinput(
                "Would you like to input a calculation/calculations",
                ["{ 1. Calculate }", "{ 2. Go back to menu }"])
        
            os.system('cls' if os.name == 'nt' else 'clear')

            match option:
                case "{ 1. Calculate }":
                    while True:
                        try:
                            original_eq = str(input("Equation: "))
                            equation = original_eq.split() #Split the equation for the triganometry portion
                            error_check = sympify(equation) #Uses the sympy library to check beforehand with the
                                                            #SympifyError library if there is incorrect syntax

                        except ZeroDivisionError: #Checks if devision by zero
                            print("")
                            print("Cannot divide by zero!")
                            print("")
                            continue

                        except SympifyError: #The library connected to sympy which checks for errors
                            print("")
                            print("Incorrect syntax")
                            print("")
                            continue

                        if original_eq == "" or original_eq == " ":
                            print("")
                            print("Cannot be empty")
                            print("")
                            continue
                        
                        else:
                            break

                    if mode == "DEG": #If the mode is degree or rad, then change how triganometric ratios are evaluated

                        for i in range(len(equation)):
                            #Find where the paranthesees in a triganometric ratio is located and set the index
                            #cos(90) -> start = 3, end = 6
                            #final is an empty string for the final result to be shown
                            start = 0
                            end = 0
                            final = ""

                            for j in range(len(equation[i])):
                                if equation[i][j] == "(": #starting paranthesee
                                    start = j + 1 #add one for the splicing portion

                                elif equation[i][j] == ")": #ending paranthesee
                                    end = j
                                
                                num = equation[i][start:end] #get the number between the paranthesees

                            #replace the triganometric ratio with the sympy version
                            if "sin" in  equation[i]:
                                equation[i] = f"{sympy.sin((int(num) * math.pi)/180)}"
                                
                            elif "cos" in  equation[i]:
                                equation[i] = f"{sympy.cos((int(num) * math.pi)/180)}"

                            elif "tan" in  equation[i]:
                                equation[i] = f"{sympy.tan((int(num) * math.pi)/180)}"
                        
                        #get the final equation by iterating through the split and adding to the empty string 
                        for new in equation:
                            final += new
                        result = sympify(final) #evaluate the equation with the sympy library
                        
                        #print the final result to 2 decimals
                        final_result= f"{round(result, 2):.2f}"
                        
                        result_text = f"{original_eq} = {final_result}"
                        print(result_text)

                        #append to the history list
                        history.append(result_text)
                        
                        #append to the "Calculator history.txt file
                        with open("Calculator history.txt", "a+") as file:
                            file.writelines(result_text + "\n")
                                    
                    else:
                        result = sympify(equation)
                        result_text = f"{equation} = {result}"
                        print(result_text)

                        history.append(result_text)

                        with open("Calculator history.txt", "a+") as file:
                            file.writelines(result_text + "\n")
                        
                case "{ 2. Go back to menu }":  
                    return None
    menu()

