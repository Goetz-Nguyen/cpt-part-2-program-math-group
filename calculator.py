import questionary
from sympy import sympify

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
        option = questionary.select(
            "-----------------------------------------------------\n",
            choices= ["{ 1. Calculate }", "{ 2. Get calculator history }", "{ 3. Clear calculator history file }", "------------------------------------------------------"]
        ).ask()
        match option:
            case "{ 1. Calculate }":
                calculate(history)

            case "{ 2. Get calculator history }":
                show_history = Calculation_history(history)
                show_history.get_history()

            case "{ 3. Clear calculator history file }":
                output_history = Calculation_history(history)
                output_history.output_history_file()


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
                result_text = f"| {equation} = {result} |"
                print(result_text)

                history.append(result_text)

                with open("Calculator history.txt", "a+") as file:
                    file.writelines(result_text + "\n")

                next_option = questionary.select(
                "Would you like to input a calculation again?",
                choices= ["{ 1. Yes }", "{ 2. Go back to menu }"]
                ).ask()

                if next_option == "{ 1. Yes }":
                    print("")
                
                elif next_option == "{ 2. Go back to menu }":
                    break

    elif option == "{ 2. Go back to menu }":   
        return None
                     
def main():

    menu()

if __name__ == "__main__":
    main()

