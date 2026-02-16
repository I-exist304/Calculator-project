#Let's first set this loop to work
while True:
#Now we ask for it to choose a number,
    x = input("Choose a number between 1-7, " + "1 is addition, 2 is subtraction, 3 is multiplication, 4 is division, 5 is exponentiation, 6 is square root, 7 is the average of 2-10 or 20 numbers: ")
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
        x = input("How many digits would you like the average of? (2-10, 20): ")
#We ask him how many numbers they would like the average of from 1 to 10 and lets also add 20 as a bonus option
        if x == '2':
            a = input("Enter the first number of this equation: ")
            b = input("Enter the second number of this equation: ")
            try:
                int(a)
                int(b)
                avg = (int(a)+int(b))/2
                print("The average of", a, "and", b, "is", avg)
            except ValueError:
                print("Please input valid numbers!")
                continue
        elif x == '3':
            a = input("Enter the first digit of this equation: ")
            b = input("Enter the second number of this equation: ")
            c = input("Enter the third number of this equation: ")
            try:
                a = int(a)
                b = int(b)
                c = int(c)
                avg = (a+b+c)/3
                print("The average of", a, b, "and", c, "is",avg)
            except ValueError:
                print("Please input valid numbers!")
                continue
        elif x == '4':
            a = input("Enter the first digit of this equation: ")
            b = input("Enter the second number of this equation: ")
            c = input("Enter the third number of this equation: ")
            d = input("Enter the fourth number of this equation: ")
            try:
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                avg = (a+b+c+d)/4
                print("The average of", a, b, c, "and", d, "is", avg)
            except ValueError:
                print("Please input valid numbers!")
                continue
        elif x == '5':
            a = input("Enter the first digit of this equation: ")
            b = input("Enter the second number of this equation: ")
            c = input("Enter the third number of this equation: ")
            d = input("Enter the fourth number of this equation: ")
            e = input("Enter the fifth number of this equation: ")
            try:
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                e = int(e)
                avg = (a+b+c+d+e)/5
                print("The average of", a, b, c, d, "and", e, "is", avg)
            except ValueError:
                print("Please input valid numbers!")
                continue
        elif x == '6':
            a = input("Enter the first digit of this equation: ")
            b = input("Enter the second number of this equation: ")
            c = input("Enter the third number of this equation: ")
            d = input("Enter the fourth number of this equation: ")
            e = input("Enter the fifth number of this equation: ")
            f = input("Enter the sixth number of this equation: ")
            try:
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                e = int(e)
                f = int(f)
                avg = (a+b+c+d+e+f)/6
                print("The average of", a, b, c, d, e, "and", f, "is", avg)
            except ValueError:
                print("Please input valid numbers!")
                continue
        elif x == '7':
            a = input("Enter the first digit of this equation: ")
            b = input("Enter the second number of this equation: ")
            c = input("Enter the third number of this equation: ")
            d = input("Enter the fourth number of this equation: ")
            e = input("Enter the fifth number of this equation: ")
            f = input("Enter the sixth number of this equation: ")
            g = input("Enter the seventh number of this equation: ")
            try:
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                e = int(e)
                f = int(f)
                g = int(g)
                avg = (a+b+c+d+e+f+g)/7
                print("The average of", a, b, c, d, e, f, "and", g, "is", avg)
            except ValueError:
                print("Please input valid numbers!")
                continue
        elif x == '8':
            a = input("Enter the first digit of this equation: ")
            b = input("Enter the second number of this equation: ")
            c = input("Enter the third number of this equation: ")
            d = input("Enter the fourth number of this equation: ")
            e = input("Enter the fifth number of this equation: ")
            f = input("Enter the sixth number of this equation: ")
            g = input("Enter the seventh number of this equation: ")
            h = input("Enter the eighth number of this equation: ")
            try:
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                e = int(e)
                f = int(f)
                g = int(g)
                h = int(h)
                avg = (a+b+c+d+e+f+g+h)/8
                print("The average of", a, b, c, d, e, f, g, "and", h, "is", avg)
            except ValueError:
                print("Please input valid numbers!")
                continue
        elif x == '9':
            a = input("Enter the first digit of this equation: ")
            b = input("Enter the second number of this equation: ")
            c = input("Enter the third number of this equation: ")
            d = input("Enter the fourth number of this equation: ")
            e = input("Enter the fifth number of this equation: ")
            f = input("Enter the sixth number of this equation: ")
            g = input("Enter the seventh number of this equation: ")
            h = input("Enter the eighth number of this equation: ")
            i = input("Enter the ninth number of this equation: ")
            try:
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                e = int(e)
                f = int(f)
                g = int(g)
                h = int(h)
                i = int(i)
                avg = (a+b+c+d+e+f+g+h+i)/9
                print("The average of", a, b, c, d, e, f, g, h, "and", i, "is", avg)
            except ValueError:
                print("Please input valid numbers!")
                continue
        elif x == '10':
            a = input("Enter the first digit of this equation: ")
            b = input("Enter the second number of this equation: ")
            c = input("Enter the third number of this equation: ")
            d = input("Enter the fourth number of this equation: ")
            e = input("Enter the fifth number of this equation: ")
            f = input("Enter the sixth number of this equation: ")
            g = input("Enter the seventh number of this equation: ")
            h = input("Enter the eighth number of this equation: ")
            i = input("Enter the ninth number of this equation: ")
            j = input("Enter the tenth number of this equation: ")
            try:
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                e = int(e)
                f = int(f)
                g = int(g)
                h = int(h)
                i = int(i)
                j = int(j)
                avg = (a+b+c+d+e+f+g+h+i+j)/10
                print("The average of", a, b, c, d, e, f, g, h, i, "and", j, "is", avg)
            except ValueError:
                print("Please input valid numbers!")
                continue
        elif x == '20':
            a = input("Enter the first digit of this equation: ")
            b = input("Enter the second number of this equation: ")
            c = input("Enter the third number of this equation: ")
            d = input("Enter the fourth number of this equation: ")
            e = input("Enter the fifth number of this equation: ")
            f = input("Enter the sixth number of this equation: ")
            g = input("Enter the seventh number of this equation: ")
            h = input("Enter the eighth number of this equation: ")
            i = input("Enter the ninth number of this equation: ")
            j = input("Enter the tenth number of this equation: ")
            k = input("Enter the eleventh digit of this equation: ")
            l = input("Enter the twelfth number of this equation: ")
            m = input("Enter the thirteenth number of this equation: ")
            n = input("Enter the fourteenth number of this equation: ")
            o = input("Enter the fifteenth number of this equation: ")
            p = input("Enter the sixteenth number of this equation: ")
            q = input("Enter the seventeenth number of this equation: ")
            r = input("Enter the eighteenth number of this equation: ")
            s = input("Enter the nineteenth number of this equation: ")
            t = input("Enter the twentieth number of this equation: ")
            try:
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                e = int(e)
                f = int(f)
                g = int(g)
                h = int(h)
                i = int(i)
                j = int(j)
                k = int(k)
                l = int(l)
                m = int(m)
                n = int(n)
                o = int(o)
                p = int(p)
                q = int(q)
                r = int(r)
                s = int(s)
                t = int(t)
                avg = (a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t)/20
                print("The average of", a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, "and", t, "is", avg)
            except ValueError:
                print("Please input valid numbers!")
                continue
        else:
#Yet another safelock to prevent the program from exploding
            print("Invalid response, restarting...")
            wait(10)
            continue
#Here is the restart code
    choice = input("Would you like to begin another calculation? (yes/no): ")
    if choice == 'yes':
        continue
    elif choice == 'no':
        break
    else:
        print("Invalid response, restarting...")
        continue