import pandas as pd
  
# read CSV file
results = pd.read_csv('nameListUser.csv')
x = len(results)
print(x+1)