print("Enter 3 numbers to find the one with the maximum value")
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if num1>num2 and num1>num3:
    print(num1, "2has the greatest value")
elif num2>num1 and num2>num3:
    print(num2, "has the greatest value")
elif num3>num1 and num3>num2:
    print(num3, "has the greatest value")
else:
    print("Please enter 3 different values that arent the same")

