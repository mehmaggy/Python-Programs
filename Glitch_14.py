import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv(r"Salary_Data.csv") 
x=df['YearsExperience']
y=df['Salary']
colors = ["red", "green", "blue", "yellow", "orange"]
plt.title('Salary',color='b',fontsize=16)
plt.pie(x,labels=y,colors=colors)
plt.show()