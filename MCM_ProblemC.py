# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:59:14 2025

@author: Allen
"""
import pandas as pd

path = 'C://MCM 2025//2025_Problem_C_Data//'

athletes = pd.read_csv(path+'summerOly_athletes.csv')

hosts = pd.read_csv(path+'summerOly_hosts.csv')

medal_counts = pd.read_csv(path+'summerOly_medal_counts.csv')

programs = pd.read_csv(path+'summerOly_programs - Copy.csv')

"""
year_list = []
athletes_by_year = pd.DataFrame()

for i in range(len(athletes['Year'])):
    
    if athletes['Year'][i] not in year_list:
        year_list.append(athletes['Year'][i])

"""    

print(athletes)
    
    
