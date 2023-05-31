import pandas as pd
df = pd.read_csv(r'data.csv')
print("1. The top data of the file is: ","\n",df.head(5))
print("2. The bottom data of the file is: ","\n",df.tail(5))
print("3. The info about the type of data is: ","\n",df.info())