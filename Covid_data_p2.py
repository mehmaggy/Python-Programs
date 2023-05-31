#Import required modules
import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv(r'data.csv')
df = df[df['status']=='confirmed']
plt.title("confirmed covid cases around the globe")
plt.xlabel("dates")
plt.ylabel("recovered cases")
plt.plot(df.Date,df.Recovered)
plt.show()
print("The maximum covid cases in a day are:",max(df.confirm))