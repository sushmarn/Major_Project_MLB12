import pandas as pd
import numpy as np
bd=pd.read_csv('Data_Train (2).csv')
bd
#removing all the rows that have any of the values as null
bd=bd.dropna(how='any')
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

#code to convert the the list of elements in the column 'Version' to string with a space in between the words
str1=""
for i in range(len(bd['Version'])):
    bd['Version'].iloc[i]= [x + ' ' for x in bd['Version'].iloc[i]]\
j=0
for i in bd['Version']:
        str1=""
        str1=str1.join(i)
        bd['Version'].iloc[j]=str1
        j=j+1    
        
bd['Version'].iloc[0]

#code to remove the space after the last word
str2=''
for i in range(len(bd['Version'])):
    li=list(bd['Version'].iloc[i])
    del(li[-1])
    bd['Version'].iloc[i]=li
j=0
for i in bd['Version']:
        str1=""
        str1=str1.join(i)
        bd['Version'].iloc[j]=str1
        j=j+1    
        
 bd['Version'].iloc[0]       

        
