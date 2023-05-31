terms = int(input("How many terms do you want printed out: "))
count = 0
num1 = 0
num2 = 1

if terms <= 0:
    print("Please try entering a positive number")
while count < terms:
    print(num1)
    sum = num1 + num2
    num1 = num2
    num2 = sum
    count += 1


