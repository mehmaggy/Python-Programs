#Call CSV Module
import csv 
#Declare a variable to enter the batch size
batchsize = int(input("Enter batch size: "))
#Open the CSV file in write mode
with open ("Names.csv","w") as csvfile:
    field_names = ['Name','Age','Height']
    writer = csv.DictWriter(csvfile,fieldnames = field_names)
    writer.writeheader()
    #Ask the user data
    for i in range(batchsize):
        writer.writerow({'Name':input("Enter the name: "),'Age':input("Enter your age: "), 'Height': input("Enter your height: ")})