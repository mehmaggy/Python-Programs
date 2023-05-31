#Call csv and numpy module
import csv 
import numpy as np
from scipy import stats
#Declare list
height = []
#Open the csv file in reader mode
with open('Names.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    #Read the contents of the file
    for row in reader:
        print(row)
        height.append(row['Height'])
#Convert height string to integer
for i in range(0,len(height)):
    height[i]=int(height[i])
#Create a numpy array of height
np_height = np.array(height)
print("Height: ",np_height)

#Calculating mean of the height
n = len(np_height)
mean = np.sum(np_height)/n
print("Mean is: ",mean)

#Calculating the median of the height/data
np_height.sort()
#Check if the length of the height/data is even or odd
if n%2 == 0:
    median1 = np_height[n//2] #Get first median and its index
    median2 = np_height[n//2-1] #Get second median and its index
    median = (median1 + median2)/2
else:
    median = np_height[n//2]
print("Median is: "+str(median))

#Calculating mode of the data
height_mode = stats.mode(np_height)
print("Mode is: ",height_mode)