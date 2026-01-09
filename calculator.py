from InquirerPy import prompt
from sympy import sympify, SympifyError
import os

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
                        error_check = sympify(original_eq) #Uses the sympy library to check beforehand with the
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

