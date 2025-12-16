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


def poly_graph(a,b,c,d,e):
    with Graph('my graph') as G:
        f, x = G.f, G.x
        f[x] = a*x**4 + b*x**3 + c*x**2 + d*x + e
menu = promptinput("What kind of graph?",["Trig", "Polynomial"])
coefficient = []
if menu == "Polynomial":
    exponent = int(input("Enter graph degree(max of 4): "))
    for i in range(exponent+1):
        coefficient.append(int(input(f"Enter coefficient of the the term with degree {i}: ")))
    match exponent:
        case 0:
            poly_graph(0,0,0,0,coefficient[0])
        case 1:
            poly_graph(0,0,0,coefficient[1],coefficient[0])
        case 2:
            poly_graph(0,0,coefficient[2],coefficient[1],coefficient[0])
        case 3:
            poly_graph(0,coefficient[3],coefficient[2],coefficient[1],coefficient[0])
        case 4:
            poly_graph(coefficient[4],coefficient[3],coefficient[2],coefficient[1],coefficient[0])
else:
    trig_type = promptinput("Type of trig?",["Cos", "Sin", "Tan"])
    match trig_type:
        case "Cos":
            a = int(input("Enter a value"))
            with Graph('my graph') as G:
                f, x = G.f, G.x
                f[x] = a*sympy.cos()