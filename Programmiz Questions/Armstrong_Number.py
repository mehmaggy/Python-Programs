num = int(input("Enter a number"))
sum = 0
exponent = num
while exponent > 0:
    digit = exponent % 10
    sum += digit ** 3
    exponent //= 10

if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
