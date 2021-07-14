## THIS SCRIPT GETS THE WARPAGE DEFLECTIONS OUT OF MOLDFLOW .TXT FILES ##
#FOR 'AUTOMATIC WARPAGE CALCULATIONS' THE RESULTS CAN BE SMALL AND/OR
# LARGE DEFLECTION SO THE SCRIPT NEEDS TO WORK FOR BOTH OPTIONS


import os
import glob
import pandas as pd
import re
from IPython.display import display


# SET PATH TO LOG FILES (.TXT)
path="P:/Code_plus/moldflow/Data_generation/test"
os.chdir(path)

# FILES ARE ALL FILL IN THE CHOSEN DIRECTORY PATH
files = os.listdir()

# ONLY LOOK FOR GLOBAL EXTENSIONS (*.OUT & *.TXT)
outfiles = glob.glob('*.out')
logfiles = glob.glob('*.txt')

#CREATE EMPTY LISTS FOR COLLECTION DATA
simulations = []
simulations1 = []
material_ids = []
material_11mes = []
pressures = []
max_pressures = []
cf_filling = []
cf_packing = []
max_cf = []
defl_x = []
defl_y = []
defl_z = []
defl_x_l = []
defl_y_l = []
defl_z_l = []
errorList = []





#READ EACH FILE
for y in logfiles:
    index = logfiles.index(y)
    # print(y)
    f = open(y, 'r')
    Lines = f.readlines()
    LinesList = [x.strip('\n') for x in Lines]
    
    # FIND LINE INDEX CONTAINING THIS STRING FOR COLLECTING MATERIAL DATA
    try:
        aline = LinesList.index('Material data : ')
        msplit = LinesList[aline+2].strip().split(':')
        m = msplit[1]
        if len(msplit)>2:
            c = msplit[2]
            manufacturer = c.strip(' ')
        
        material = m.strip(' ')
        
        material_ids.append(material)
        material_11mes.append(manufacturer)
    except ValueError:
            continue
    # FIND LINE INDEX CONTAINING THIS STRING FOR COLLECTING FILE NAME    
    try:
        alinel = LinesList.index("Reading input data...")
        msplit = LinesList[alinel+1].strip().split(':')
        m = msplit[1]
        n = m.strip(' ')
 
        simulations.append(n)
       
    except ValueError:
        continue

    # FIND LINE INDEX CONTAINING THIS STRING FOR COLLECTING PRESSURES
    try:
        aline_start = LinesList.index('  Filling phase:    Status: V  = Velocity control')
        aline_end = LinesList.index('  Packing phase:')
        
        for line in LinesList[((aline_start)+7):((aline_end)-9)]:
            if line[0].startswith('|'):
                pressures.append(line.strip().split('|')[3])

            else:  
                continue
         
    # FIND LINE INDEX CONTAINING THIS STRING FOR COLLECTING CLAMP FORCES   
        aline_cf_start = LinesList.index('End of filling phase results summary :')
        for line in LinesList[((aline_cf_start)+1):((aline_cf_start)+6)]:
            if line[0:22].startswith('   Maximum Clamp force'):
                line1 = re.split(r'[=N]', line)
                cf_filling.append(line1[1])
            else:  
                continue
        
        aline_cf_pack_start = LinesList.index('Packing phase results summary :')
        for line in LinesList[((aline_cf_pack_start)+1):((aline_cf_pack_start)+6)]:
            if line[0:24].startswith('   Clamp force - maximum'):
                line1 = re.split(r'[=N]', line)
                cf_packing.append(line1[1])
            else:  
                continue
        max_cf = [max(value) for value in zip(cf_filling, cf_packing)]
    
    except ValueError:
            continue
    
   
    # THE LENGTH OF ALL LISTS SHOULD BE THE SAME FOR A PANDAS DICTIONARY
    length = len(simulations)

    if all(len(lst) == length for lst in [max_cf]):
        data = {
                'Simulation':       simulations,
                'Material ID' :     material_ids,
                'Material 11me' :   material_11mes,
                # 'Pressures' :       pressures,
                'max Clamp Force':  max_cf,

        }
        
        results = pd.DataFrame(data)
    
        display(results)
        results.to_csv("logtable_filling.csv")

## TO ADD 'PRESSURES' TO THE DICTIONARY, THE SCRIPT 'Find_maximum_in_dictionary.py'
    # NEEDS TO BE RUN FIRST. FIRST CREATE 'Logtable_pressures.csv' BY SELECTION:
    ##
    #   data = {
    #         'Pressures' :       pressures }
    ##

## THAN USE 'Merge_2_CSV_files.py' TO MERGE ALL CSV FILES TOGETHER