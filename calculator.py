import math
import questionary
from sympy import sympify

history = []

class Calculation_history:
    def __init__(self, history: list[str]):
        self._history = history
    
    def get_history(self) -> None:
        spot_history = 1

        for equation in self._history:
            print(f"{spot_history}. | {equation} |")
            spot_history += 1

    def output_history_file(self) -> None:
        with open("Calculator history.txt", "w") as file:
            for data in self._history:
                file.write(data)



def menu() -> None:

    option = questionary.select(
        "-----------------------------------------------------\n",
        choices= ["{ 1. Calculate }", "{ 2. Get calculator history }", "{ 3. Output calculator history as a '.txt' file } \n ------------------------------------------------------"]
    ).ask()

    if option == "{ 1. Calculate }":
        calculate(history)

    elif option == "{ 2. Get calculator history }":
        show_history = Calculation_history(history)
        show_history.get_history()
        menu()

    elif option == "{ 3. Output calculator history as a '.txt' file }":
        output_history = Calculation_history(history)
        output_history.output_history_file()
        menu()


def test_calculate() -> bool:
    return True
    
def calculate(history: list[str]) -> None:
    option = questionary.select(
        "Would you like to input a calculation/calculations",
        choices= ["{ 1. Yes }", "{ 2. Go back to menu }"]
    ).ask()

    if option == "{ 1. Yes }":
        while True:
            equation = str(input("Equation(use: '+' '-' '/' '*' '**' 'sqrt()'): "))
            #if not true retry
            if test_calculate() == True:
                #use alt to evaluate expression
                result = sympify(equation)
                result_text = f"{equation} = {result}"
                print("|", result_text,"|")
                history.append(result_text)

                next_option = questionary.select(
                "Would you like to input a calculation again?",
                choices= ["{ 1. Yes }", "{ 2. Go back to menu }"]
                ).ask()

                if next_option == "{ 1. Yes }":
                    print("")
                
                elif next_option == "{ 2. Go back to menu }":
                    break

        menu()

    elif option == "{ 2. Go back to menu }":   
        menu()
    
       
                   
def main():
    #make a quick claculation, so basically if you want to quick calculate, manually see history and calculate or polymorphism
    #then create objects here, but if you want menu for interactive history and new calculation, then put menu function
    #basically, quick calcluate is for calculate function and get history/and get equation and __str__ method
    # /normal is the menu function which gets new equation or get history or output history as  file
    menu()

if __name__ == "__main__":
    main()

