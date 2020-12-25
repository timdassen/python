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

    # print(itemdigit1)
    # print(count)

# =============================================================================
# # create a new list called 'seatFiles'
# # define matches of strings in RAD file names
# # if their is a match, than append file to seatFiles list
# =============================================================================    
    
    seatFiles = []
    count1 =0
    matches = ["UP1805_include_03_seat","0000.rad"]
    for i in range(0, len(itemdigit1)):
        for file in os.listdir(itemdigit1[i]):
            # if os.path.isfile(os.path.join(path,file)) and 'UP1805_include_03_seat' in file:
            if all(x in file for x in matches):
                seatFiles.append(os.path.join(itemdigit1[i],file))
                count1+=1
            else:
                continue
    # print(seatFiles)
    # print(count1)

# =============================================================================
# opens seatFiles to readlines
# than opens again as write to write lines except for "/END"
# than opens as append to append "UP1805_include_03_seat_extra_card.txt"
# than writes the updated "UP1805_include_03_seat" rad file 
# =============================================================================

    for j in range(0, len(seatFiles)):
        with open(seatFiles[j], 'r') as f:
            lines = f.readlines()
        with open(seatFiles[j], "w") as f:
            for line in lines:
                if line.strip("\n") != "/END":
                    f.write(line)
        with open(seatFiles[j], "a+") as f:
            with open("UP1805_include_03_seat_extra_card.txt","r") as h:
                lines_new = h.readlines()
                for line in lines_new:
                    f.write(line)
                f.close()
get_filepaths()