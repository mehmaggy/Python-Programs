print("Enter the lengths of the sides of the triangle-")
a = int(input("1st side length:"))
b = int(input("2st side length: "))
c = int(input("3rd side length:"))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of triangle is", area)