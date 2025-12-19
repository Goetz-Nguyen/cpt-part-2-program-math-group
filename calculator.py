from InquirerPy import prompt
from sympy import sympify
import os


# Trigonometric Functions: Sine, cosine, tangent, and their inverses for solving triangles and working with angles. 
# 1
# Logarithmic Functions: Natural logarithm (ln) and common logarithm (log) for working with exponential relationships and solving equations. 
# 1
# Exponential Functions: The exponential function (e^x) and its inverse for growth and decay problems. 
# 1
# Fractional Calculations: Performing operations with fractions, displaying results in either fractional or decimal form. 
# 1
# Scientific Notation: Working with very large or small numbers with scientific notation functionality. 
# 1

#percentage
#inverse

# Degrees, Radians, and Gradians: 


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
    return True #test
    
def calculate(history: list[str]) -> None:
    option = promptinput(
        "Would you like to input a calculation/calculations",
        ["{ 1. Yes }", "{ 2. Go back to menu }"])
    os.system('cls' if os.name == 'nt' else 'clear')
    if option == "{ 1. Yes }":
        while True:
            equation = str(input("Equation(use: '+' '-' '/' '*' '**' 'sqrt()'): "))
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
                     
def main():

    menu()

if __name__ == "__main__":
    main()

