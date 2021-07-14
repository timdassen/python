
import os
import pandas as pd


path="P:/Code_plus/moldflow/Data_generation/python/csv"

os.chdir(path)

# Merging of 2 CSV files

data3 = pd.read_csv("logtable1_total.csv") 

data1 = pd.read_csv("logtable_all_results_new.csv")

# Merge data3 on similar strings of column data1['Simulation] (left file)

data_new = pd.merge(data1, data3, on='Simulation', how='left')

print(data_new[0:4])
print(data_new.shape)

data_new.to_csv("logtable_all_results_new_new.csv")



