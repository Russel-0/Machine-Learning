n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
op = input("Enter operator: ")

if op == "+":
    print("Sum: " + str(n1 + n2))
elif op == "-":
    print("Difference: " + str(n1 - n2))
elif op == "*":
    print("Difference: " + str(n1 * n2))
elif op == "/":
    print("Difference: " + str(n1 / n2))
else:
    print("INVALID OPERATOR")