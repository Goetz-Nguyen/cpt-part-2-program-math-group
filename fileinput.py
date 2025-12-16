try:
    questions = {}
    questionslst = []
    #
    with open("tests.txt", "r") as f_in:
        f_in = f_in.read().split("\n")
    for lines in f_in:
        if lines[0] != "1":
            if lines[0].isnumeric():
                questions[question] = questionslst
                question = lines
                questionslst = []
            else:
                questionslst.append(lines)
        else:
            question = lines
    questions[question] = questionslst
    question = lines
    questionslst = []
except:
    print("Couldn't find tests.txt!/File in wrong format")

# Showing questions
for question, options in questions.items():
    print(question)
    for option in options:
        if "âœ…" in option:
            print(option[:len(option)-3])
            correctanswer = option[0]
        else:
            print(option)
    answer = input("Enter your choice: ")
    print(answer == correctanswer)
    print()