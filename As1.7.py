a = float(input(""))
operation = input("")
b = float(input(""))
if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif operation == "/" and b !=0:
    print(a/b)
elif operation =="/" and b == 0:
    print("error")
else:
    print("Invalid operation")

