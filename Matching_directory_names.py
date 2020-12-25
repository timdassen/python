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
from itertools import islice

def get_filepaths():
    
# =============================================================================
# # Sets up and draws the "ask directory" popup
# # joins items and path as item
# # if that item is a directory than appends the list path to L[]
# =============================================================================

    root = tk.Tk()
    root.withdraw()
    
    K = []
    L=[]
    A = ['62','63','64','65','66','67','68','69','70','71','72','75','76','86','87','99','100',"106",'109','110','111','112','113','117','118','119','120','121','122','123','125','126','127','128','129','130','131','135','136','138','139','140','141','142','144','145','146','101rev01','102rev01','104rev01','104rev01','104rev02','114rev01','133rev01','134rev01','137rev01','143rev01']
    global path 
    path = filedialog.askdirectory()
    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isdir(item):
            item1 = os.path.basename(os.path.normpath(item))
            L.append(item1)
            
# loops over the length of list A[] 
# loops over the length of list L[]
# if an item in list A is matching the first 3 characters of a item in list [L] than append the item
# if an item in list A is matching the first 2 characters of a item in list [L] than append the item
           
    for x in range(len(A)):
        for y in range(len(L)):
            if (A[x]) == (L[y][:3]):
                K.append(L[y])
            if (A[x]) == (L[y][:2]):
                K.append(L[y])
    print(K)

get_filepaths()


