# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:54:09 2021

@author: tim.dassen
"""
import pandas as pd

fileName = 'P:/Code_plus/moldflow/Data_generation/python/material_database/logtable_material_database.csv'


df = pd.read_csv(fileName)

df['Trade name'] = df['Trade name'].str[1:]

print(df)

df.to_csv('P:/Code_plus/moldflow/Data_generation/python/material_database/logtable_material_database_new.csv')
