# THIS SCRIPT MAKES A PLOT OF THE CSV FILES OF THE SCI SENSOR
# IT ASKS FOR DIRECTORY WITH CSV FILES AND PLOTS THE DATA WITH ANNOTATION OF
# THE MAXIMUM X,Y AND Z VALUE

import os 
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

def get_filepaths():
    root = tk.Tk()
    root.withdraw()
    
        
    global path 
    path = filedialog.askdirectory()
    for item in os.listdir(path):
        item1 = os.path.join(path, item)

        
        df = pd.read_csv(item1, header=0)
        df1 = df.iloc[0:88]
        
        plot1=df1.plot(x='frequency', y=['X','Y','Z'])
        
        
# #       GET MAXIMUM ABSOLUTE X-VALUE
        maxXindex=(df1.abs().idxmax()['X'])
        maxX = df1.iloc[maxXindex]['frequency']
        maxXY = df1.iloc[maxXindex]['X']
        plot1.annotate((maxXY),xy=(maxX,maxXY))
        
#       GET MAXIMUM ABSOLUTE Y-VALUE
        maxXindex=(df1.abs().idxmax()['Y'])
        maxY = df1.iloc[maxXindex]['frequency']
        maxYY = df1.iloc[maxXindex]['Y']
        plot1.annotate(maxYY,xy=(maxY,maxYY))

#       GET MAXIMUM ABSOLUTE Z-VALUE
        maxXindex=(df1.abs().idxmax()['Z'])
        maxZ = df1.iloc[maxXindex]['frequency']
        maxZY = df1.iloc[maxXindex]['Z']
        plot1.annotate(maxZY,xy=(maxZ,maxZY))
        
        plt.savefig(path + '/' + item + '.png', bbox_inches = 'tight')

get_filepaths()