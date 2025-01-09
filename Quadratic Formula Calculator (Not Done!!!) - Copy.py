# this will import the math module
import math


import math

def Quadratic_Formula_Calculator():
    # Collect values from the user
    A = 1  # Assuming A, B, C are predefined
    B = 5
    C = 6

    # Calculate the discriminant
    D = B ** 2 - 4 * A * C
    X = math.sqrt(-(D))

    # Check if the discriminant is non-negative
    if D >= 0:
    #here is where i will return the two roots
        sqrt_D = math.sqrt(D)
        Z = (-B + sqrt_D) / (2 * A)
        Y = (-B - sqrt_D) / (2 * A)
        return Z, Y

    if D < 0 and :
        return


result = Quadratic_Formula_Calculator()
print(result)

