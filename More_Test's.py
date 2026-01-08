def quadratic_tests():
    print("== PRE MADE QUADRATIC'S TEST QUESTIONS!! ==")
    score = 0
    total = 10

    # 1
    print("#1: What is the vertex of: y = 5(x + 7)^2 + 2?")
    print("A) (–7, 2)   B) (7, 2)   C) (5, –2)   D) (–2, 7)")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1

    print("")

    #2
    print("#2: What is the axis of symmetry of: f(x) = 4(x + 3)^2 + 5?")
    print("A) x = 5   B) x = 4   C) x = -3   D) x = 3")
    ans = input("Your answer: ")
    if ans == "c":
        score += 1

    print("")
    
    #3
    print("#2: What are the domain and range of: y = −8(x − 9)^2 + 2?")
    print("A)  Domain: {x| x ≤ −8, x ∈ R} // Range: {y| y ∈ R}")   
    print("B)  Domain: {x| x ∈ R} // Range: {y| y ≤ 2, y ∈ R}")   
    print("C)  Domain: {x| x ∈ R} // Range: {y| y ≥ −9, y ∈ R}")
    print("D) Domain: {x| x ≥ −9,x ∈ R} // Range: {y| y ∈ R}")
    ans = input("Your answer: ")
    if ans == "b":
        score += 1

    print("")
    
    #4
    print("#4: Find the slope between (–3, 5) and (4, –2).")
    ans = input("Your answer: ")
    if ans in ["-1", "-1.0"]:
        score += 1

    print("")
    
    #5
    print("#5: Use the Law of Cosines:")
    print("Given sides a=7, b=9, and angle C=42*, solve for side c (nearest tenth).")
    ans = input("Your answer: ")
    if ans in ["6", "6.0", "6.1"]:
        score += 1

    print("")
    
    #6
    print("#6: A triangle is reflected over the y-axis. What happens to point (x, y)?")
    print("A) (-x, y)   B) (x, -y)   C) (-x, -y)   D) (y, x)")
    ans = input("Your answer: ")
    if ans == "a":
        score += 1

    print("")

    #7
    print("#7: Two similar triangles have scale factor 3:5.")
    print("If a side in the smaller triangle is 12, what is the corresponding larger side?")
    ans = input("Your answer: ")
    if ans == "20":
        score += 1

    print("")
    # 8
    print("#8: Find the distance between points (2, 3) and (11, 9).")
    ans = input("Your answer: ")
    if ans in ["10.8", "10.819", "11"]:
        score += 1

    print("")
    
    # 9
    print("#9: Find the area of a triangle with sides 8, 9, and 13.")
    ans = input("Your answer: ")
    if ans in ["36", "37"]:
        score += 1

    print("")
    
    # 10
    print("#10: What is the interior angle of a regular 12 sided polygon?")
    ans = input("Your answer: ")
    if ans in ["150", "150*", "150 degrees"]:
        score += 1

    print("")
    print("== GEOMETRY TEST WAS COMPLETED. ==")
    print(f"Your Score Is: {score} / {total}")
    return score