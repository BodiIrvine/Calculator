# This will import the math module
import math

def Quadratic_Formula_Calculator():
    # Collect values from the user
    A = int(input("What is the A value: "))
    B = int(input("What is the B value: "))
    C = int(input("What is the C value: "))

    # Calculate the discriminant
    D = B ** 2 - 4 * A * C

    # Check if the discriminant is non-negative
    if D >= 0:
        sqrt_D = math.sqrt(D)
        Z = (-B + sqrt_D) / (2 * A)
        Y = (-B - sqrt_D) / (2 * A)
        return Z, Y
    else:
        return "Imaginary roots"

result = Quadratic_Formula_Calculator()
print(result)
