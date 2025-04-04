P = int(input("Enter the Principle:"))
R = float(input("Enter the rate:"))
N = int(input("Enter the number of times the compound interest is used per year:"))
A = P * (1 -(1 + R ) ** -N) / R
print("Annuity:",A)