import sympy
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


menu = promptinput("What kind of graph?",["Trig", "Polynomial", "Exit"])
error = False
while menu != "Exit":
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
            menu = promptinput("What kind of graph?",["Trig", "Polynomial"])
    else:
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
            menu = promptinput("What kind of graph?",["Trig", "Polynomial"])
print("Bye!")