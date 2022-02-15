# THIS SCRIPT MAKES A PLOT OF THE CSV FILES OF THE SCI SENSOR
# IT ASKS FOR DIRECTORY WITH CSV FILES AND PLOTS THE DATA WITH ANNOTATION OF
# THE MAXIMUM X,Y AND Z VALUE

from __future__ import print_function
import os 
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, f
import numpy



from scipy.integrate import simps
from numpy import trapz

def get_filepaths():
    root = tk.Tk()
    root.withdraw()
    
        
    global path 
    path = filedialog.askdirectory()
    i=1
    # CREATE DICTIONARY 'data' AND DATABASE 'df_new' WITH COLUMNNAMES
    data = []        
    columns = ["NAME","AREA"]
    df_new = pd.DataFrame(columns = columns)

    # LOOP OVER ITEMS IN PATH AND SELECT ONLY .csv FILES    
    for item in os.listdir(path):
        item1 = os.path.join(path, item)
        name, extension = os.path.splitext(item1)
        if name[-3:] == 'XYZ':
            
            if extension == '.csv': 
                
                
                df = pd.read_csv(item1, header=0)
                df1 = df.iloc[0:88]

        
                y=df1['XYZ']
                area = trapz(y, dx=0.000625)
                print("area =", area)
      
        #       UPDATE DICTIONARY WITH APPENDING NAMES, MEAN AND STD VALUES
                
                values = [item, area]   
                zipped = zip(columns, values)
                a_dictionary = dict(zipped)
    
            
                data.append(a_dictionary)
                i=i+1
                
            else:
                print("no csv file")
        else:
            print('no correct name')
            
    #UPDATING DATABASE WITH APPENDING OF DICTIONARY
    df_new = df_new.append(data, True)
    df_new.to_csv(path + '/' + os.path.basename(path) + '_AREA' + '.csv')
       
get_filepaths()