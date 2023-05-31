import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'data.csv')
#Making histogram for confirmed cases 
plt.title("Days required to increased cases by 10000")
bins = [0,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
plt.hist(df.Recovered,bins = bins)
plt.xlabel("Number of covid cases")
plt.ylabel("Number of days")
plt.show()

#Pie chart showing recovered and not recovered cases
#df_recovered = df[df['status']=='Recovered'] 
#confirmed = df['confirm'].sum()
#print("Number of people that have been infected= ",confirmed)
#recovered = df_recovered['confirm'].sum()
#print("Number of people that have been recovered= ",recovered)
#not_recovered = confirmed - recovered
#plt.title("pie chart showing percentage of recovered and not recovered patients")
#labels = ['Recovered','Not recovered']
#plt.pie([recovered,not_recovered],labels = labels)
#plt.show()