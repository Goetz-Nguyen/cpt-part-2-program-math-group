import matplotlib.pyplot, numpy
from matplotlib.patches import Circle, Rectangle, Polygon
from InquirerPy import prompt
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


fig, ax = matplotlib.pyplot.subplots()
dimension = promptinput("2d or 3d?", ["2d", "3d"])
if dimension == "2d":
    shaper = promptinput("What shape?", ["Circle", "Triangle", "Rectangle/Square"])
    match shaper:
        case "Circle":
            radius = float(input("Enter radius: "))
            ax.add_patch(Circle((radius*4/2, radius*4/2), radius=radius, edgecolor="black",facecolor="blue"))
            ax.set_xlim(0,radius*4)
            ax.set_ylim(0,radius*4)
            ax.set_aspect('equal')
            matplotlib.pyplot.grid(True)
            matplotlib.pyplot.title("Circle")
            matplotlib.pyplot.show()