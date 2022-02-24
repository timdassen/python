# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 19:25:55 2022

@author: tim.dassen
"""
# THIS SCRIPT MAKES A PLOT OF THE XYZ.CSV FILES OF THE SCI SENSOR
# IT ASKS FOR DIRECTORY WITH XYZ.CSV FILES AND PLOTS THE DATA WITH ANNOTATION OF
# THE MAXIMUM X,Y,Z AND XYZ VALUE

import os 
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import trapz


    
def HICloop():
    """

    This function stores the HIC values and the time boundaries of the HIC 
    pulse 
    
    Parameters:
    ----------
        :param int    st : start of range of data points included in HIC 
                           time slot
        :param int    nd : end of range of data points included in HIC time 
                           slot
        :param int    id : id to indicate 15 or 36 ms HIC

    """   
    root = tk.Tk()
    root.withdraw()
    
        
    global path 
    path = filedialog.askdirectory()
    
    columns = ["AREA"]
    df_new = pd.DataFrame(columns = columns)
    
    for item in os.listdir(path):
        item1 = os.path.join(path, item)
        name, extension = os.path.splitext(item1)
        if name[-3:] == 'XYZ':
            
            if extension == '.csv': 
                
                      
                df1 = pd.read_csv(item1, header=0)
                df2 = df1.copy()
                    
                    
                AREAlist = []
                HIClist = []
                
                dt=0.000625
                HIClimit=80
                startID = 0 ; endID = len(df2['Time'])
                # endID = len(df2['Time'])
                # for m in range(startID,endID):
                #     g1 = df2.iloc[m-1]['XYZ']
                #     g2 = df2.iloc[m]['XYZ']
                #     area=(g1+g2)*0.5*dt
                #     AREAlist.append(area)
                #     print(AREAlist)
                for i1 in range(startID,endID):
                    for i2 in range(i1+1,endID):
                        t1=df2.iloc[i1]['Time']
                        t2=df2.iloc[i2]['Time']
                        if HIClimit>=t2-t1:
                            y=df2['XYZ'][i1:i2+1]
                            area = trapz(y, dx=dt)
                            HIC=(t2-t1)*(area/(t2-t1))**2.5
                            HIClist.append(HIC)
                
                maxHIC = max(HIClist)   
                print(maxHIC)
                print(HIClist.index(maxHIC))
                # max_index = HIClist.index(maxHIC)
                # print(max_index)
                df2.loc[0, 'maxHIC'] = maxHIC
               
                
                            
                        

                        

                df2.to_csv(path +  '/' + item[:-3] + 'HIC' + '.csv')
                

            else:
                print("no csv file")
        else:
            continue
        # df2.to_csv(path +  '/' + item[:-3] + 'HIC15' + '.csv')
HICloop ()