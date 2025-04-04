P = int(input("Enter the Principle:"))
R = float(input("Enter the Rate:"))
T = int(input("Enter the time:"))
N = int(input("Enter the number of times the compound interest is used per year"))
CI = P * ( 1 + R / N)**N*T
print ("Compound Interest:", CI)