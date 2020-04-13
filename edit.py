import pandas as pd
import numpy as np
bd=pd.read_csv('Data_Train (2).csv')
bd

#code to divide the 'Name' column to 3 different columns 'Namen', 'Model', and 'Version'
import warnings
warnings.filterwarnings('ignore')
bd['Namen']=""
bd['Model']=""
bd['Version']=""
import re
pat=re.compile(' ')
for i in range(len(bd['Name'])):
    res=re.split(pat,bd['Name'].iloc[i])
    bd['Namen'].iloc[i]=res[0]
    bd['Model'].iloc[i]=res[1]
    bd['Version'].iloc[i]=res[2:]

#code to convert and join the the list of elements in the column 'Version' to an object with a space(' ') in between the words
for _ in range(len(bd.Version)):
    jv=' '
    temp=jv.join(bd.Version[_])
    bd.Version[_]=temp
print(bd.Version[0])      
        
#code to remove the column 'Name' and renaming the column 'Namen' as 'Name'
bd=bd.drop(columns='Name')
bd=bd.rename(columns={"Namen": "Name"})

#code to replace the null values in the column 'Seats' with the values from other rows that have the same 'Model' and 'version'
nu=list()
for k in range(len(bd['Seats'])):
    if(bd['Seats'].isnull().iloc[k]==True):
        nu.append(k) 
        
bd['Seats']=bd['Seats'].fillna('null')      

for i in nu:
    for j in range(len(bd)):
        if((bd['Model'][j]==bd['Model'][i])&(bd['Version'][j]==bd['Version'][i])&(bd['Seats'][j]!='null')):
            bd['Seats'][i]=bd['Seats'][j]
        
for k in nu:
    if(bd['Seats'][k]=='null'):
         bd['Seats'].iloc[k]=float('nan')         
        
        
#removing all the rows that have any of the values as null
bd=bd.dropna(how='any')
