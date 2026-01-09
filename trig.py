from sympy import sympify
import sympy
import math

i = (input("Enter: "))
equation2 = "cos(90) + sin(90)"
equation = "cos(90)"
split_equation = i.split()


for i in range(len(split_equation)):
    start = 0
    end = 0
    final = ""
    for j in range(len(split_equation[i])):
        if split_equation[i][j] == "(":
            start = j + 1

        elif split_equation[i][j] == ")":
            end = j
        
        num = split_equation[i][start:end]

    if "sin" in  split_equation[i]:
        split_equation[i] = f"{sympy.sin((int(num) * math.pi)/180)}"
        
    elif "cos" in  split_equation[i]:
        split_equation[i] = f"{sympy.cos((int(num) * math.pi)/180)}"

    elif "tan" in  split_equation[i]:
        split_equation[i] = f"{sympy.tan((int(num) * math.pi)/180)}"
        
for new in split_equation:
    final += new
result = sympify(final)

print(f"{round(result, 2):.2f}")


