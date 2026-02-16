x = input("Choose a number between 1-7: ")
if x == 1:
    a = int(input("Enter the first number of this equation: "))
    b = int(input("Enter the second number of this equation: "))
    ab = a+b
    print(a, "plus", b, "equals", ab)
elif x == 2:
    a = int(input("Enter the first number of this equation: "))
    b = int(input("Enter the second number of this equation: "))
    ab = a-b
    print(a, "minus", b, "equals", ab)
elif x == 3:
    a = int(input("Enter the first number of this equation: "))
    b = int(input("Enter the second number of this equation: "))
    ab = a*b
    print(a, "times", b, "equals", ab)
elif x == 4:
    a = int(input("Enter the first number of this equation: "))
    b = int(input("Enter the second number of this equation: "))
    ab = a/b
    print(a, "divided by", b, "equals", ab)
elif x == 5:
    a = int(input("Enter the first number of this equation: "))
    b = int(input("Enter the second number of this equation: "))
    ab = a**b
    print(a, "exponatiated by", b, "equals", ab)
elif x == 6:
    a = int(input("Enter the first number of this equation: "))
    asqr = a**0.5
    if asqr < 0:
        print("Invalid input")
    else:
        print("The square root of", a, "is", asqr)
elif x == 7:
    a = int(input("Enter the first number of this equation: "))
    b = int(input("Enter the second number of this equation: "))
    c = int(input("Enter the third number of this equation: "))
    abc = (a+b+c)/3
    print("The average of", a, b, "and", c, "is", abc)
else:
    print("Invalid Input")