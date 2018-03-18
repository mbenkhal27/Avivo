#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 09:29:48 2018

@author: mbenkhal
"""

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



Location = r'/Users/mbenkhal/Documents/Avivo/Treatment Hours by Year.xlsx'
data_2014_origin= pd.read_excel(Location, "2014")
years = ['2014','2015','2016','2017','2018']

data_2014_origin.loc[data_2014_origin.Code.isnull(), 'Code'] = ''
data_2014_origin.head(5)

def CleanAndRearrangeData(InputData,year,newDataFrame):

    new_client=True
    new_program=True
    index = 0
    Number_of_hours = 0
    temp = "new_data_" + str(year)
    while index < len(InputData):
        if(new_client == True):
            if(new_program == True):
                Number_of_hours = 0
                start_date_service = InputData.iloc[index][2]
                Client_Number = InputData.iloc[index][3]
                Program = InputData.iloc[index][1]
                code = InputData.iloc[index][4]
                dob = InputData.iloc[index][6]
                sex = InputData.iloc[index][7]
                Race = InputData.iloc[index][8]
                end_date_service = InputData.iloc[index][2]
                new_client = False
                new_program = False
        else:
            if(new_program == True):
                Number_of_hours = 0
                start_date_service = InputData.iloc[index][2]
                Client_Number = InputData.iloc[index][3]
                Program = InputData.iloc[index][1]
                code = InputData.iloc[index][4]
                end_date_service = InputData.iloc[index][2]
                new_program = False
        if(InputData.iloc[index][4] == '' and (index + 1) < len(InputData)):
            if(InputData.iloc[index + 1][4] == ''):
                new_client =True
                new_program =True
                end_date_service = InputData.iloc[index - 1][2]
                Number_of_hours = InputData.iloc[index][5]
                lst = pd.DataFrame([[Client_Number,Program,code,start_date_service,end_date_service,dob,sex,Race,Number_of_hours,year]],columns=cols)
                newDataFrame = newDataFrame.append(lst,ignore_index=True)
                index = index + 2
            else:
                end_date_service = InputData.iloc[index - 1][2]
                Number_of_hours = InputData.iloc[index][5]
                lst = pd.DataFrame([[Client_Number,Program,code,start_date_service,end_date_service,dob,sex,Race,Number_of_hours,year]],columns=cols)
                newDataFrame = newDataFrame.append(lst,ignore_index=True)
                index = index + 1
                new_program = True
                
        else:

            Number_of_hours += InputData.iloc[index][5].astype('int')
            index = index + 1
    return newDataFrame
print("starting...")
cols =['Client_number','Program','Code','start_service_data','end_service_data','data_birth','gender','race','number_hours','year']
temp = pd.DataFrame(columns=cols)
temporary = pd.DataFrame(columns=cols)
#temporary = CleanAndRearrangeData(data_2014_origin,2014,temp)
#print(temporary.head(5))

for var in years:
    data_name = "data_"+ var + "origin"
    print("reading data" + var)
    data_name = pd.read_excel(Location, var)
    print(data_name.head(5))
    print("Done reading data" + var)
    data_name.loc[data_name.Code.isnull(), 'Code'] = ''
    print("Rearraging data " + var)
    
    temp = CleanAndRearrangeData(data_name,var,temp)
    print(temp.head(5))
    print("Done Rearraging data " + var)
    
print(temp.head(5)) 
print(temp.tail(5))    
    
    

temp.to_excel(r'/Users/mbenkhal/Documents/Avivo/ArrangedData.xlsx')
