import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'Data7.csv')
x=df['ProgrammingLanguages']
y=df['Popularity']
plt.title("Popularity of Programming Languages",fontsize=16)
plt.xlabel("Popularity")
plt.ylabel("Programming Languages")
plt.bar(x,y)
plt.show()