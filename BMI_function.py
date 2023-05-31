def bmi(my_height,my_weight):
    my_bmi = round(my_weight/(my_height*my_height),2)
    print("Your bmi level is- ",my_bmi)
    return
my_weight = float(input("Please enter your weight in kg- "))   
my_height = float(input("Please enter your height in meters- "))
bmi(my_height,my_weight)
