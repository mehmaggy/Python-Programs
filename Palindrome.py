#Get the word as an input from user
my_string = input("Enter a string- ")
#Change the input string to lower case
string_lower = my_string.lower()
#Find the length of the string
length_string = len(string_lower)
#Set the index to check each letter of the string
i = 0
j = length_string - 1
#Check if the letters in the word are same or not
for i in range(length_string):
    #Set the flag to 1 if the first and last index is same
    if(string_lower[i] == string_lower[j]):
        i = i+1
        j = j-1
        flag = 1
    else:
        flag = 0
        break 
if(flag == 1):
    print("Its a palindrome")
if(flag == 0):
    print("Its not a palindrome")