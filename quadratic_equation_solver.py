#quadratic_equation_solver.py
#Date: 30/September/2020
#by irving-rs

#Description:
#Quadratic Equation Solver: A simple program that solves the famous equation.

#Basics:
#The user must indicate the coefficient values.
#The quadratic equation has the form: a*x^2 + b*x + c = 0
#Computes: real roots and complex roots

#Functions:
def solve_quad(a , b, c): #Solves the quadratic equation.

    s = "" #String
    
    if (a==0 and b==0):
        s = "Invalid equation." #String
        return s #Returns the result in a string.
    elif (a==0 and c==0) or (b==0 and c==0):
        s = "x = 0" #String
        return s #Returns the result in a string.
    elif a==0:
        x = -c/b
        s = "x = " + str(x) #String
        return s #Returns the result in a string.
    else:
        D = b**2 - (4*a*c)
        if D==0:
            x = -b / (2*a)
            s = "x = " + str(x) #String
            return s
        elif D>0:
            x1 = (-b + D**0.5) / (2*a)
            x2 = (-b - D**0.5) / (2*a)
            s = "x1 = " + str(x1) + "      x2 = " + str(x2) #String
            return s
        else:
            x_real = -b / (2*a)
            x1_imag = (abs(D)**0.5) / (2*a)
            x2_imag = -(abs(D)**0.5) / (2*a)
            s = "x1 = " + str("{:.4f}".format(x_real)) + " + (" + str("{:.4f}".format(x1_imag)) + ") i" + "      x2 = " + str("{:.4f}".format(x_real)) + " + (" + str("{:.4f}".format(x2_imag)) + ") i" #String
            return s

#Presentation:
print("\nQuadratic Equation Solver:\n")

#Description:
print("Description:")
print("The quadratic equation has the form:")
print("a*x^2 + b*x + c = 0")

#Menu:
print("\nPlease, enter the coefficient values (a, b, c):\n")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print("\nEquation:")
print("(", "{:.4f}".format(a), ")*x^2 + (", "{:.3f}".format(b), ")*x + (", "{:.4f}".format(c), ") = 0", sep="")

print("\nResult:")
s = solve_quad(a, b, c)
print(s,"\n")
