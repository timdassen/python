# THIS SCRIPT MAKES A PLOT OF THE CSV FILES OF THE SCI SENSOR
# IT ASKS FOR DIRECTORY WITH CSV FILES AND PLOTS THE DATA WITH ANNOTATION OF
# THE MAXIMUM X,Y AND Z VALUE

import os 
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, f
import numpy

def get_filepaths():
    root = tk.Tk()
    root.withdraw()
    
        
    global path 
    path = filedialog.askdirectory()
    i=1
    # CREATE DICTIONARY 'data' AND DATABASE 'df_new' WITH COLUMNNAMES
    data = []        
    columns = ["NAME","MEAN", "STD"]
    df_new = pd.DataFrame(columns = columns)

    # LOOP OVER ITEMS IN PATH AND SELECT ONLY .csv FILES    
    for item in os.listdir(path):
        item1 = os.path.join(path, item)
        name, extension = os.path.splitext(item1)
        if extension == '.csv':
            
            
            df = pd.read_csv(item1, header=6)
            df1 = df.iloc[0:88]
    
    # defining timing range min as 0.02s (iloc[32]) and max 0.033 s (iloc[33])
            df2=(df1.iloc[32:54])
    
            plot1=df2.hist(column='X')
            plt.savefig(path + '/' + item + '_histogram' + '.jpg', bbox_inches = 'tight')
            
    #       GET MEAN & STD OF X-VALUES
            mean = (df2['X'].mean())
            
            std = (df2['X'].std())
            plt.text(-5, 5, mean, fontsize = 12)
            plt.text(-5, 4.5, std, fontsize = 12)
            
         
    
    #       UPDATE DICTIONARY WITH APPENDING NAMES, MEAN AND STD VALUES
            
            values = [item, mean, std]   
            zipped = zip(columns, values)
            a_dictionary = dict(zipped)

        
            data.append(a_dictionary)
            i=i+1
            
        else:
            print("no csv file")
            
    #UPDATING DATABASE WITH APPENDING OF DICTIONARY
    df_new = df_new.append(data, True)
    df_new.to_csv(path + '/' + 'statistics' + '.csv')

       
get_filepaths()