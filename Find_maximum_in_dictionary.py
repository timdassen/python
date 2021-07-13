import pandas as pd

import numpy as np



#-------------------------------------------------------

#                  user input

#

#-------------------------------------------------------

# location of input file 

# fileName = 'P:/Code_plus/moldflow/Data_generation/test/logtable_pressure.csv'
fileName = 'C:/Users/timd/Desktop/Code_BI/JADS/Graduation_project/Autodesk_Moldflow_log'



#location of output

outFile = 'logtable_maximum_pressure.csv'







#-------------------------------------------------------

#                  read data

#

#-------------------------------------------------------

#read the csv file into a dataframe

df = pd.read_csv(fileName)

#get the simulation names

simNames = np.unique(df['Simulation'])





#-------------------------------------------------------

#                  process pressures

#

#-------------------------------------------------------



#variable to save maxima

maxVals = [] 

#loop trough all the sims

for sim in simNames:

    #create a data frame containing only the data from given sim.

    dfSim = df[df['Simulation']==sim] 



    #filter the pressure data for given simulation

    pressureValues =  dfSim['Pressures']



    #save maximum pressure (this will be in the same order as the sim names so should be easy to write after)

    maxVals.append(np.max(pressureValues))

  



#-------------------------------------------------------

#                  write data

#

#-------------------------------------------------------

#open output file

fw = open (outFile,'w')

# write header

fw.write("'index','Simulation','Pressures'\n")



#loop trough sims and write a line into csv format

for idx,sim in enumerate(simNames):

    fw.write('%d, %s, %f\n' % (idx,sim,maxVals[idx]))



fw.close()