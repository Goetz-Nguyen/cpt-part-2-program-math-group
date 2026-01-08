import matplotlib.pyplot, numpy
from matplotlib.patches import Circle, Rectangle
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


def shaper():
    """
    Draw the desired shape in the cartestian plane
    """
    #TUTORIALS VV
    #https://www.geeksforgeeks.org/python/how-to-draw-shapes-in-matplotlib-with-python/
    #https://matplotlib.org/stable/gallery/mplot3d/index.html
    while True:
        fig, ax = matplotlib.pyplot.subplots() # Creates the plane
        shaper = promptinput("What shape?", ["Circle", "Rectangle/Square", "Exit"])
        if shaper == "Circle":
            radius = float(input("Enter radius: "))
            ax.add_patch(Circle((radius*4/2, radius*4/2), radius=radius, edgecolor="lightblue", facecolor="lightblue"))
            ax.set_aspect('equal')
            matplotlib.pyplot.grid(True)
            matplotlib.pyplot.title("Circle")
            ax.set_yticks(numpy.arange(0, radius*4+1, radius//2))
            ax.set_xticks(numpy.arange(0, radius*4+1, radius//2))
        elif shaper == "Rectangle/Square":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            ax.add_patch(Rectangle((width, height), width=width, height=height, edgecolor="lightblue", facecolor="lightblue"))
            ax.set_xlim(0, width*3)
            ax.set_ylim(0, height*3)
            ax.set_aspect('equal')
            matplotlib.pyplot.grid(True)
            matplotlib.pyplot.title("Rectangle/Square")
            ax.set_yticks(numpy.arange(0, height*3+1, height//2))
            ax.set_xticks(numpy.arange(0, width*3+1, width//2))
        else: 
            return
        matplotlib.pyplot.show()
        shaper = promptinput("What shape?", ["Circle", "Rectangle/Square", "Exit"])

shaper()