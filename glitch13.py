import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv(r"Salary_Data.csv") 
x=df['YearsExperience']
y=df['Salary']
plt.title('Salary',color='b',fontsize=16)
plt.xlabel('Year of experience',color='b',fontsize=14)
plt.ylabel('Salary',color='b',fontsize=14)
plt.plot(df.YearsExperience,df.Salary)
plt.show()