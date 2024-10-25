import pandas as pd
#panda was not friendly to me
#Reminder:
#pip install pandas in command prompt, select interpreter for python in VS Code

d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

df = pd.DataFrame(data=d)

print(df)