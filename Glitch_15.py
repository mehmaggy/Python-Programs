import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv(r"Salary_Data.csv") 
x=df['YearsExperience']
y=df['Salary']
colors= ["red", "green", "blue", "yellow", "orange"]
plt.title('Salary',color='b',fontsize=16)
plt.xlabel('Year of experience')
plt.ylabel('Salary')
plt.bar(x,y,color=colors)
plt.show()