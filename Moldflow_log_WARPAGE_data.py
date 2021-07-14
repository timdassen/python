## THIS SCRIPT GETS THE WARPAGE DEFLECTIONS OUT OF MOLDFLOW .TXT FILES ##
#FOR 'AUTOMATIC WARPAGE CALCULATIONS' THE RESULTS CAN BE SMALL AND/OR
# LARGE DEFLECTION SO THE SCRIPT NEEDS TO WORK FOR BOTH OPTIONS


import os
import glob
import pandas as pd
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
    
    # FIND LINE INDEX (number) CONTAINING THIS STRING
    try:
        alinel = LinesList.index("Reading input data...")
        #SPLIT AND STRIP THE NEXT LINE (this contains the file name)
        msplit = LinesList[alinel+1].strip().split(':')
        m = msplit[1]
        n = m.strip(' ')
    
    except ValueError:
        continue
    
    try:
        alinel2 = LinesList.index("Reading input data...")
        #SPLIT AND STRIP THE NEXT LINE (this contains the file name)
        m2split = LinesList[alinel2+1].strip().split(':')
        m1 = m2split[1]
        n1 = m1.strip(' ')
       
    except ValueError:
        continue

    # FIND LINE INDEX (number) CONTAINING THIS STRING        
    if 'Switching from buckling check to large deflection warpage...' in LinesList:
        
        #APPEND THE WARPAGE DEFLECTIONS X,Y,Z TO THEIR LISTS (defl)x_l,..)
        try:
            #APPEND FILE NAME TO LIST 'simulations1'
            simulations1.append(n1)
            aline_large_defl = LinesList.index('Switching from buckling check to large deflection warpage...')
            #APPEND THE WARPAGE DEFLECTIONS X,Y,Z TO THEIR LISTS (defl_x_l,defl_y_l,defl_z_l)
            for line in LinesList[((aline_large_defl)+1):((aline_large_defl)+200)]:
                if line[0:10].startswith('   Trans-X'):
                    defl_x_l.append(line.split('    ')[-1])
                else:  
                    continue
            for line in LinesList[((aline_large_defl)+1):((aline_large_defl)+200)]:
                if line[0:10].startswith('   Trans-Y'):
                    defl_y_l.append(line.split('    ')[-1])
                else:  
                    continue
            for line in LinesList[((aline_large_defl)+1):((aline_large_defl)+200)]:
                if line[0:10].startswith('   Trans-Z'):
                    defl_z_l.append(line.split('    ')[-1])
                else:  
                    continue
        except ValueError:
            print('foutje')         
    elif 'Minimum/maximum displacements at last step (unit: mm):' in LinesList:
        simulations.append(n)
        aline_defl_start = LinesList.index('Minimum/maximum displacements at last step (unit: mm):')
        for line in LinesList[((aline_defl_start)+1):((aline_defl_start)+6)]:
            if line[0:10].startswith('   Trans-X'):
                defl_x.append(line.split('    ')[-1])
            else:  
                continue
        for line in LinesList[((aline_defl_start)+1):((aline_defl_start)+6)]:
            if line[0:10].startswith('   Trans-Y'):
                defl_y.append(line.split('    ')[-1])
            else:  
                continue
        for line in LinesList[((aline_defl_start)+1):((aline_defl_start)+7)]:
            if line[0:10].startswith('   Trans-Z'):
                defl_z.append(line.split('    ')[-1])
            else:  
                continue    
    else:
        #COLLECT FILES WHICH ARE NOT CONTAINING THE ABOVE STRINGS 
        errorList.append(y)
            
                
    length = len(simulations)
    length1 = len(simulations1)
    
    # THE LENGTH OF ALL LISTS SHOULD BE THE SAME FOR A PANDAS DICTIONARY
    if all(len(lst) == length for lst in [defl_y,defl_x]):
        data = {
                'Simulation':       simulations,
                # 'Material ID' :     material_ids,
                # 'Material 11me' :   material_11mes,
                # 'Pressures' :       max_pressures,
                # 'max Clamp Force':  max_cf,
                'max Defl-X' :      defl_x,
                'max Defl-Y' :      defl_y,
                'max Defl-Z' :      defl_z,
                   
        }
        results = pd.DataFrame(data)
    else:
        continue
    
    if all(len(lst) == length1 for lst in [defl_y_l,defl_x_l]):
        data1 = {
                'Simulation':       simulations1,
                # 'Material ID' :     material_ids,
                # 'Material 11me' :   material_11mes,
                # 'Pressures' :       max_pressures,
                # 'max Clamp Force':  max_cf,
                'max Defl-X-Large' :      defl_x_l,
                'max Defl-Y-Large' :      defl_y_l,
                'max Defl-Z-Large' :      defl_z_l
        
        }
        results1 = pd.DataFrame(data1)
    else:
        print(errorList)
        break
    
    # SHOW RESULTS    
    display(results)
    display(results1)
    results.to_csv("TEMP.csv")
    results1.to_csv("TEMP1.csv")
    
