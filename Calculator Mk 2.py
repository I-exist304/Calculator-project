#Let's first set this loop to work
while True:
#Now we ask for it to choose a number,
    x = input("Choose a number between 1-7, " + "1 is addition, 2 is subtraction, 3 is multiplication, 4 is division, 5 is exponentiation, 6 is square root, 7 is the average of 3 numbers: ")
#Now time for all the ifs and elifs
    if x == '1':
        a = input("Enter the first number of this equation: ")
        b = input("Enter the second number of this equation: ")
        try:
#Tries to turn them into ints, if it fails the program restarts.
            a = int(a)
            b = int(b)
            ab = a+b
            print(a, "plus", b, "equals", ab)
        except ValueError:
            print("Please input valid numbers!")
            continue
    elif x == '2':
        a = input("Enter the first number of this equation: ")
        b = input("Enter the second number of this equation: ")
        try:
            a = int(a)
            b = int(b)
            ab = a-b
            print(a, "minus", b, "equals", ab)
        except ValueError:
            print("Please input valid numbers!")
            continue
    elif x == '3':
        a = input("Enter the first number of this equation: ")
        b = input("Enter the second number of this equation: ")
        try:
            a = int(a)
            b = int(b)
            ab = a*b
            print(a, "times", b, "equals", ab)
        except ValueError:
            print("Please input valid numbers!")
            continue
    elif x == '4':
        a = input("Enter the first number of this equation: ")
        b = input("Enter the second number of this equation: ")
#This part detects if b is zero so it can stop it in time
        if b == '0':
            print("Cannot divide by zero.")
            continue
        else:
            try:
                a = int(a)
                b = int(b)
                ab = a/b
                print(a, "divided by", b, "equals", ab)
            except ValueError:
                print("Please input valid numbers!")
                continue
    elif x == '5':
        a = input("Enter the first number of this equation: ")
        b = input("Enter the second number of this equation: ")
#This part now tries to see if b is less than 0
        if b < 0:
            print("Please don't put negative powers.")
            continue
        else:
            try:
                a = int(a)
                b = int(b)
                ab = a**b
                print(a, "exponatiated by", b, "equals", ab)
            except ValueError:
                print("Please input valid numbers!")
                continue
    elif x == '6':
        a = input("Enter the number you would like the square root of: ")
#Same check to see if a is less than 0
        if a < 0:
            print("Error: Negative number detected, preparing system reboot...")
            continue
        else:
            try:
                a = int(a)
                asqr = a**0.5
                print("The square root of", a, "is", asqr)
            except ValueError:
                print("Please input valid numbers!")
                continue
    elif x == '7':
        a = input("Enter the first digit of this equation: ")
        b = input("Enter the second number of this equation: ")
        c = input("Enter the third number of this equation: ")
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            abc = (a+b+c)/2
            print("The average of", int(a), + ",", b, "and", c, "is", abc)
        except ValueError:
            print("Please input valid numbers!")
            continue
#Here is the restart code
    choice = input("Would you like to begin another calculation? (yes/no)")
    if choice == 'yes':
        continue
    elif choice == 'no':
        break
    else:
        print("Invalid response, restarting...")
        continue
