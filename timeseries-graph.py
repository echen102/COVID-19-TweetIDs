import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

file_list = []

folder_names = ['2020-01', '2020-02', '2020-03']

for folder in folder_names:
    for root, dirs, files in os.walk(folder):
        #print(root, dirs, files)
        for file in files:
            count = 0
            if file.endswith('.txt'):
                with open(os.path.join(root, file), 'r') as f:
                    for line in f:
                        count = count+1
                        #new_list.append(text)
            file_list.append((file[21:-7],count))

df = pd.DataFrame(file_list, columns=['Date', 'count']).sort_values(by=['Date'])
#print(df)

df2 = df.groupby(['Date'])['count'].sum().reset_index()
#print(df2)
fp = open("df-date-count.txt", "w+")
fp.write(df2.to_string())
fp.close()

df.set_index('Date').plot()
plt.show()