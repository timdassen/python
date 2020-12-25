# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:34:40 2020

@author: tim.dassen
"""
"""
Created on Mon Dec 21 17:43:34 2020

@author: tim.dassen
"""
import os 
import tkinter as tk
from tkinter import filedialog


def get_filepaths():
    
# =============================================================================
# # Sets up and draws the "ask directory" popup
# # joins items and path as item
# # if that item is a directory than appends to list dirlist[]
# =============================================================================

    root = tk.Tk()
    root.withdraw()

    dirlist = []

    global path 
    path = filedialog.askdirectory()
    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isdir(item):
            dirlist.append(item)
        else:
            continue
            
    # print(dirlist)

# =============================================================================
# # takes last path (.basename(.normpath))
# # checks if first 4 indices are digits
# # if so, adds this ite to list itemdigit1[]
# =============================================================================

    itemdigit1 = []
    count =0
    for item in dirlist:
        itemdigit = os.path.basename(os.path.normpath(item))
        if itemdigit[0:4].isdigit():
            itemdigit1.append(item)
            # print(itemdigit)
            count+=1
        else:
            continue

#    print(itemdigit1)
#    print(count)

# =============================================================================
# # create a new list called 'xmlFiles'
# # define matches of strings in xml file names
# # if their is a match, than append file to xmlFiles list
# =============================================================================    
    
    xmlFiles = []
    count1 =0
    matches = ["usr.xml"]
    for i in range(0, len(itemdigit1)):
        for file in os.listdir(itemdigit1[i]):
            if all(x in file for x in matches):
                xmlFiles.append(os.path.join(itemdigit1[i],file))
                count1+=1
            else:
                continue
        print(xmlFiles)


# =============================================================================
# insert text "<OUTPUT_JOINT_DOF ..." into xmlFiles
# opens xmlFiles to readlines
# enumerates over lines to find index i of word matching '<OUTPUT_JOINT_DOF'
# than opens xmlFiles as write to insert the inserttext using 'slicing'method
# =============================================================================
     
    inserttext = ['      <OUTPUT_JOINT_DOF\n']
    inserttext2 = ['         ID="2"\n']
    inserttext3 = ['         SIGNAL_TYPE="VEL"\n']
    inserttext4 = ['         DESCRIPTION="Output_JointVel\n']
    inserttext5 = ['         JOINT_LIST="ALL"\n']
    inserttext6 = ['      />\n']

    k=0
    for j in range(0, len(xmlFiles)):
        with open(xmlFiles[j], 'r') as f:
            lines = f.readlines()
            for i, word in enumerate(lines):
                if '<OUTPUT_JOINT_DOF' in word:
                    k=i +6                
                else: continue
        f.close()
        with open(xmlFiles[j], 'w') as f:
            xmlFiles[j] = lines[0:k] + inserttext + inserttext2 +inserttext3 + inserttext4 + inserttext5 + inserttext6 + lines[k:]
            print(*lines[:], sep="\n")
            f.write(''.join(map(str,xmlFiles[j])))
            f.close()            
                  

            
      
get_filepaths()