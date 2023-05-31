import pandas as pd
df = pd.read_csv(r'locations.csv')
print('all data-\n',df)
print('\n Top five rows-\n',df.head(5))
print('\n Top eight rows-\n',df.head(8))