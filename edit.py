import pandas as pd
import numpy as np

#for graphing purposes
import seaborn as sns
import matplotlib.pyplot as plt

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

#code to convert the the list of elements in the column 'Version' to string with an underscore('_') in between the words
str1=""
for i in range(len(bd['Version'])):
    bd['Version'].iloc[i]= [x + '_' for x in bd['Version'].iloc[i]]\
j=0
for i in bd['Version']:
        str1=""
        str1=str1.join(i)
        bd['Version'].iloc[j]=str1
        j=j+1    
        
bd['Version'].iloc[0]

#code to remove the underscore('_') after the last word
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


#code to remove the column 'Name' and renaming the column 'Namen' as 'Name'
bd=bd.drop(columns='Name')
bd=bd.rename(columns={"Namen": "Name"})

#code to replace the null values in the column 'Seats' with the values from other rows that have the same 'Model' and 'version'
bd['Seats']=bd['Seats'].fillna('null')
nu=list()
for i in range(len(bd['Seats'])):
    if(bd['Seats'].isnull().iloc[i]==True):
        nu.append(i)        
for i in nu:
    bd['Seats'].iloc[i]=bd[(bd['Model']=='City')&(bd['Version']=='1.5 GXI')&(bd['Seats']!='null')].iloc[0,10]
        
#removing all the rows that have any of the values as null
bd=bd.dropna(how='any')

#removed columns "Mileage", "Engine", "Power"
bd = bd.drop(["Mileage", "Engine", "Power"], axis = 1)

#cleaning up the owner data
bd["Owner_Type"] = bd["Owner_Type"].str.replace("First", "1")
bd["Owner_Type"] = bd["Owner_Type"].str.replace("Second", "2")
bd["Owner_Type"] = bd["Owner_Type"].str.replace("Third", "3")
bd["Owner_Type"] = bd["Owner_Type"].str.replace("Fourth & Above", "4")

#performing univariate analysis on the owner data
#basically we're just plotting a graph here
print("Number of cars sold according to type of owner: ")
owner_graph = sns.countplot(x = "Owner_Type", data = bd)

#similarly perform univariate analysis on the location data
loc_graph = sns.countplot(x = "Location", data = bd)
