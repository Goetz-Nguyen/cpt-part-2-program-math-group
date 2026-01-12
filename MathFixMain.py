from InquirerPy import prompt
from Caio import mental_math, graph_calculator, shaper
from anthony import simple_calculator, scientific_calculator
import os
from Sebastian import create_tests, load_test, show_sources , test_choice, run_test, math_definitions
from Gabriel import geometry_calc, algebra_formulas
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

def main():
    tests = {}
    menu_options = ["Create new test", "Load test from file", "Run a test",
                     "Study Guides", "Math Definitions", "Graph Calculator", "Mental Math",
                     "Simple Calculator", "Scientific Calculator", "Geometry Calculator",  
                     "Draw Shapes", "Algebra Calculator", "Exit"]
    
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
                type_of_test = promptinput("Would you like to run a :", ["Custom test", "Pre-Made Test"])
                if type_of_test == "Custom test":
                    if tests == {}:
                        print("No tests were loaded.")
                    else:
                        run_test(tests)
                if type_of_test == "Pre-Made Test":
                    test_choice()
                choice = promptinput("What do you want?", menu_options)

            case "Study Guides":
                show_sources()
                choice = promptinput("What do you want?", menu_options)

            case "Math Definitions":
                math_definitions()
                choice = promptinput("What do you want?", menu_options)

            case "Graph Calculator":
                graph_calculator()
                choice = promptinput("What do you want?", menu_options)

            case "Mental Math":
                mental_math()
                choice = promptinput("What do you want?", menu_options)
            
            case "Simple Calculator":
                simple_calculator()
                choice = promptinput("What do you want?", menu_options)
            
            case "Scientific Calculator":
                scientific_calculator()
                choice = promptinput("What do you want?", menu_options)

            case "Geometry Calculator":
                geometry_calc()
                choice = promptinput("What do you want?", menu_options)
            
            case "Algebra Calculator":
                algebra_formulas()
                choice = promptinput("What do you want?", menu_options)

            case "Draw Shapes":
                shaper()
                choice = promptinput("What do you want?", menu_options)
            
    mental_math()
    print("Bye!")


if __name__ == '__main__':
    main()